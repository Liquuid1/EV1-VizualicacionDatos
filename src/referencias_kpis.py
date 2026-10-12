"""Genera controles independientes para comparar las medidas de Power BI."""

import json
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "processed"


def metrics(c, genre_pairs, country_pairs):
    financial = c[c.has_valid_financials]
    rated = c[c.has_valid_rating]
    movies = int(c.type.eq("Movie").sum())
    ids = set(c.content_id)
    ratio = lambda a, b: a / b if b else None
    return {
        "Total contenidos": len(c), "Peliculas": movies,
        "Series": int(c.type.eq("TV Show").sum()),
        "Porcentaje peliculas": ratio(movies, len(c)),
        "Popularidad mediana": c.popularity.median() if len(c) else None,
        "Contenidos con valoracion": len(rated),
        "Valoracion promedio valida": rated.vote_average.mean() if len(rated) else None,
        "Cobertura valoracion": ratio(len(rated), len(c)),
        "Votos registrados": int(c.vote_count.sum()) if len(c) else None,
        "Contenidos elegibles ranking": int(c.rating_rank_eligible.sum()),
        "Peliculas con datos financieros": len(financial),
        "Cobertura financiera peliculas": ratio(len(financial), movies),
        "Ingresos poblacion valida": float(financial.revenue.sum()) if len(financial) else None,
        "Presupuesto poblacion valida": float(financial.budget.sum()) if len(financial) else None,
        "Presupuesto promedio valido": financial.budget.mean() if len(financial) else None,
        "Ingresos presupuesto veces": ratio(financial.revenue.sum(), financial.budget.sum()),
        "Peliculas presupuesto en revision": int(c.budget_review_required.sum()),
        "Peliculas financieras en revision": int(financial.budget_review_required.sum()),
        "Generos presentes": genre_pairs.loc[genre_pairs.content_id.isin(ids) & genre_pairs.genre.ne("Sin información"), "genre_id"].nunique(),
        "Paises presentes": country_pairs.loc[country_pairs.content_id.isin(ids) & country_pairs.country.ne("Sin información"), "country_id"].nunique(),
        "Idiomas presentes": c.language.dropna().loc[lambda s: s.ne("Sin información")].nunique(),
    }


def main():
    c = pd.read_csv(DATA / "catalogo.csv", dtype={"content_id": "string"})
    gp = pd.read_csv(DATA / "contenido_genero.csv").merge(pd.read_csv(DATA / "dim_generos.csv"), on="genre_id", validate="many_to_one")
    cp = pd.read_csv(DATA / "contenido_pais.csv").merge(pd.read_csv(DATA / "dim_paises.csv"), on="country_id", validate="many_to_one")
    cases = {
        "catalogo_completo": {}, "peliculas": {"type": "Movie"}, "series": {"type": "TV Show"},
        "drama": {"genres": ["Drama"]}, "japon": {"countries": ["Japan"]},
        "drama_japon": {"genres": ["Drama"], "countries": ["Japan"]},
        "drama_comedy_japon": {"genres": ["Drama", "Comedy"], "countries": ["Japan"]},
        "estrenos_2020_2025": {"years": [2020, 2025]},
        "presupuesto_en_revision": {"review": True},
        "peliculas_ingles": {"type": "Movie", "language": "en"},
        "segmento_vacio": {"years": [1900, 1901]},
    }
    rows = []
    for case, filters in cases.items():
        selected = c.copy()
        if "type" in filters:
            selected = selected[selected.type.eq(filters["type"])]
        if "genres" in filters:
            selected = selected[selected.content_id.isin(gp.loc[gp.genre.isin(filters["genres"]), "content_id"])]
        if "countries" in filters:
            selected = selected[selected.content_id.isin(cp.loc[cp.country.isin(filters["countries"]), "content_id"])]
        if "years" in filters:
            selected = selected[selected.release_year.between(*filters["years"])]
        if "review" in filters:
            selected = selected[selected.budget_review_required.eq(filters["review"])]
        if "language" in filters:
            selected = selected[selected.language.eq(filters["language"])]
        # La selección de dimensión también restringe los valores presentes
        # en su propia asociación, aunque un contenido tenga otras categorías.
        context_gp = gp[gp.genre.isin(filters["genres"])] if "genres" in filters else gp
        context_cp = cp[cp.country.isin(filters["countries"])] if "countries" in filters else cp
        values = metrics(selected, context_gp, context_cp)
        assert values["Total contenidos"] == values["Peliculas"] + values["Series"]
        assert values["Peliculas con datos financieros"] <= values["Peliculas"]
        rows.append({"case": case, **values})
    result = pd.DataFrame(rows)
    baseline = result.set_index("case")
    assert baseline.loc["catalogo_completo", "Total contenidos"] == 31991
    assert baseline.loc["catalogo_completo", "Peliculas con datos financieros"] == 3540
    assert baseline.loc["series", "Peliculas"] == 0
    assert pd.isna(baseline.loc["series", "Ingresos presupuesto veces"])
    assert baseline.loc["segmento_vacio", "Total contenidos"] == 0
    assert baseline.loc["drama_japon", "Total contenidos"] <= baseline.loc["japon", "Total contenidos"]
    assert baseline.loc["drama_comedy_japon", "Total contenidos"] >= baseline.loc["drama_japon", "Total contenidos"]
    assert baseline.loc["drama_japon", "Generos presentes"] == 1
    assert baseline.loc["drama_japon", "Paises presentes"] == 1
    result.to_csv(DATA / "referencia_kpis.csv", index=False, encoding="utf-8-sig", float_format="%.12g")
    (DATA / "reference_cases.json").write_text(json.dumps(cases, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(result[["case", "Total contenidos", "Peliculas con datos financieros", "Popularidad mediana"]].to_string(index=False))


if __name__ == "__main__":
    main()
