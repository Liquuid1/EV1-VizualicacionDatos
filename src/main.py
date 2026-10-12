"""Prepara las fuentes del caso para StreamView. Ejecutar: python src/main.py."""

import argparse
import hashlib
import json
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
SOURCES = {
    "Movie": "netflix_movies_detailed_up_to_2025.csv",
    "TV Show": "netflix_tv_shows_detailed_up_to_2025.csv",
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def dimension(catalog, column, name):
    pairs = catalog[["content_id", column]].copy()
    pairs[column] = pairs[column].fillna("Sin información").str.split(",")
    pairs = pairs.explode(column)
    pairs[column] = pairs[column].str.strip().replace("", "Sin información")
    pairs = pairs.drop_duplicates().sort_values(["content_id", column])
    values = sorted(pairs[column].unique())
    dim = pd.DataFrame({f"{name}_id": range(1, len(values) + 1), name: values})
    bridge = pairs.rename(columns={column: name}).merge(dim, on=name, validate="many_to_one")
    return dim, bridge[["content_id", f"{name}_id"]]


def prepare(data_dir, output_dir):
    frames, manifest = [], []
    for kind, filename in SOURCES.items():
        path = data_dir / filename
        frame = pd.read_csv(path, dtype={"show_id": "string"})
        require(frame["type"].eq(kind).all(), f"Tipo inesperado en {filename}")
        frame["source_file"] = filename
        frame["source_row"] = range(2, len(frame) + 2)
        manifest.append({"file": filename, "sha256": sha256(path), "rows": len(frame)})
        frames.append(frame)
    raw = pd.concat(frames, ignore_index=True)
    require(raw.show_id.notna().all(), "Identificadores ausentes")
    raw["show_id"] = raw.show_id.str.strip()
    require(raw.show_id.str.fullmatch(r"\d+").all(), "Identificadores no enteros")
    raw["content_id"] = raw.type.map({"Movie": "movie:", "TV Show": "tv:"}) + raw.show_id

    repeated = raw[raw.content_id.duplicated(keep=False)].copy()
    repeated["selected"] = ~repeated.content_id.duplicated(keep="first")
    # Fallar ante conflictos nuevos para evitar descartarlos silenciosamente.
    comparison = [c for c in raw.columns if c not in {"source_row", "popularity"}]
    for key, group in repeated.groupby("content_id"):
        require(len(group[comparison].drop_duplicates()) == 1,
                f"Conflicto adicional en duplicado {key}; revisar antes de continuar")
    common_ids = set(frames[0].show_id) & set(frames[1].show_id)
    collisions = raw.loc[raw.show_id.isin(common_ids)].copy()
    catalog = raw.drop_duplicates("content_id", keep="first").copy()
    numeric = ["release_year", "popularity", "vote_count", "vote_average", "budget", "revenue"]
    for col in numeric:
        original = catalog[col]
        catalog[col] = pd.to_numeric(original, errors="coerce")
        require(not (original.notna() & catalog[col].isna()).any(), f"Número inválido en {col}")
    for col in ["release_year", "vote_count"]:
        require(catalog[col].notna().all() and catalog[col].mod(1).eq(0).all(), f"Entero inválido en {col}")
        catalog[col] = catalog[col].astype("Int64")
    dates = pd.to_datetime(catalog.date_added, errors="coerce", format="%Y-%m-%d")
    require(dates.notna().all(), "Fecha inválida")
    catalog["date_added"] = dates.dt.strftime("%Y-%m-%d")
    require(catalog.vote_average.between(0, 10).all(), "Calificaciones fuera de escala")
    require(catalog.popularity.ge(0).all() and catalog.vote_count.ge(0).all(), "Métricas negativas")
    text = ["title", "director", "cast", "country", "duration", "genres", "language", "description"]
    for col in text:
        catalog[col] = catalog[col].astype("string").str.strip().replace("", pd.NA)
    # Nulos reales en catálogo; etiquetas de ausencia solo en dimensiones.
    for col in ["budget", "revenue"]:
        catalog.loc[catalog[col].le(0) | catalog.type.ne("Movie"), col] = float("nan")
    catalog["has_valid_rating"] = catalog.vote_average.gt(0)
    catalog["rating_rank_eligible"] = catalog.has_valid_rating & catalog.vote_count.ge(100)
    catalog["has_valid_financials"] = catalog.type.eq("Movie") & catalog.budget.gt(0) & catalog.revenue.gt(0)
    catalog["budget_review_required"] = catalog.budget.gt(0) & catalog.budget.lt(1000)
    catalog["revenue_budget_ratio"] = (catalog.revenue / catalog.budget).where(catalog.has_valid_financials)
    catalog["date_added_year"] = dates.dt.year.astype("Int64")
    # No publicar rating como clasificación etaria.
    catalog = catalog.drop(columns="rating").reset_index(drop=True)
    genres, content_genres = dimension(catalog, "genres", "genre")
    countries, content_countries = dimension(catalog, "country", "country")
    years = sorted(catalog.release_year.unique())
    release_years = pd.DataFrame({"release_year": years})

    require(catalog.content_id.is_unique, "Clave compuesta duplicada")
    require(len(catalog) == raw.content_id.nunique(), "Pérdida de contenidos")
    for bridge, dim, key in [(content_genres, genres, "genre_id"), (content_countries, countries, "country_id")]:
        require(not bridge.duplicated().any(), "Asociaciones duplicadas")
        require(bridge.content_id.isin(catalog.content_id).all(), "Referencia inexistente a contenido")
        require(bridge[key].isin(dim[key]).all(), "Referencia inexistente a dimensión")
    require(catalog.loc[catalog.revenue_budget_ratio.notna(), "has_valid_financials"].all(), "Razón financiera inválida")

    quality = pd.DataFrame({"column": catalog.columns, "dtype": [str(t) for t in catalog.dtypes],
                            "missing": catalog.isna().sum().values})
    quality["missing_pct"] = (quality.missing / len(catalog) * 100).round(2)
    summary = {
        "source_rows": len(raw), "contents": len(catalog),
        "movies": int(catalog.type.eq("Movie").sum()), "series": int(catalog.type.eq("TV Show").sum()),
        "removed_duplicate_rows": len(raw) - len(catalog), "duplicate_groups": repeated.content_id.nunique(),
        "cross_type_shared_ids": len(common_ids), "genre_associations": len(content_genres),
        "country_associations": len(content_countries), "valid_ratings": int(catalog.has_valid_rating.sum()),
        "valid_financials": int(catalog.has_valid_financials.sum()),
        "budget_review_required": int(catalog.budget_review_required.sum()),
        "rating_equals_vote_average_source_rows": int(pd.to_numeric(raw.rating).eq(raw.vote_average).sum()),
        "date_year_equals_release_year_source_rows": int(pd.to_datetime(raw.date_added).dt.year.eq(raw.release_year).sum()),
        "release_year_min": int(min(years)), "release_year_max": int(max(years)),
        "budget_review_threshold": 1000, "minimum_votes_for_rating_rank": 100,
        "sources": manifest,
    }
    # Comprobar integridad de fuentes antes de escribir derivados.
    require(all(sha256(data_dir / s["file"]) == s["sha256"] for s in manifest), "Fuentes modificadas")
    output_dir.mkdir(parents=True, exist_ok=True)
    tables = {"catalogo": catalog, "dim_generos": genres, "contenido_genero": content_genres,
              "dim_paises": countries, "contenido_pais": content_countries, "dim_anio_estreno": release_years,
              "calidad_columnas": quality, "duplicados_series": repeated,
              "ids_compartidos_entre_tipos": collisions,
              "presupuestos_revision": catalog.loc[catalog.budget_review_required]}
    for name, frame in tables.items():
        frame.to_csv(output_dir / f"{name}.csv", index=False, encoding="utf-8-sig", date_format="%Y-%m-%d")
    (output_dir / "resumen_calidad.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in summary.items() if k != "sources"}, indent=2, ensure_ascii=False))
    print(f"Salidas: {output_dir}")
    return summary


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-dir", type=Path, default=ROOT / "data" / "raw")
    parser.add_argument("--output-dir", type=Path, default=ROOT / "data" / "processed")
    args = parser.parse_args()
    prepare(args.data_dir.resolve(), args.output_dir.resolve())
