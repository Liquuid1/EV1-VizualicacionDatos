"""Exporta resúmenes y gráficos estáticos del catálogo para el informe y notebook."""

import os
import tempfile
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", str(Path(tempfile.gettempdir()) / "streamview-matplotlib"))
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "processed"
IMAGES = ROOT / "images"


def main():
    catalog = pd.read_csv(DATA / "catalogo.csv")
    IMAGES.mkdir(exist_ok=True)
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False})
    summaries = {}
    summaries["tipos"] = catalog.groupby("type").size().rename("contents").reset_index()
    summaries["estrenos"] = catalog.groupby("release_year").size().rename("contents").reset_index()
    summaries["idiomas"] = catalog.groupby("language").size().rename("contents").reset_index().sort_values("contents", ascending=False)
    for plural, singular in [("generos", "genre"), ("paises", "country")]:
        bridge = pd.read_csv(DATA / f"contenido_{'genero' if plural == 'generos' else 'pais'}.csv")
        dim = pd.read_csv(DATA / f"dim_{plural}.csv")
        rows = bridge.merge(dim, on=f"{singular}_id", validate="many_to_one").merge(
            catalog[["content_id", "popularity"]], on="content_id", validate="many_to_one")
        summaries[plural] = rows.groupby(singular).agg(contents=("content_id", "nunique"), median_popularity=("popularity", "median")).reset_index().sort_values("contents", ascending=False)
    for name, table in summaries.items():
        table.to_csv(DATA / f"resumen_{name}.csv", index=False, encoding="utf-8-sig")

    def save(fig, name, note):
        fig.text(.02, .015, "Fuente: CSV del caso StreamView Analytics. " + note, fontsize=8)
        fig.tight_layout(rect=(0, .06, 1, 1))
        fig.savefig(IMAGES / f"{name}.png", dpi=180)
        plt.close(fig)

    fig, ax = plt.subplots(figsize=(8, 4.5))
    table = summaries["tipos"]
    bars = ax.bar(table.type, table.contents, color=["#2563EB", "#047857"])
    ax.bar_label(bars, labels=[f"{v:,}".replace(",", ".") for v in table.contents], padding=3)
    ax.set(title="Composición del catálogo", ylabel="Contenidos")
    ax.set_ylim(0, 18500)
    save(fig, "composicion_catalogo", "31.991 claves únicas; sin filtros.")
    for name, col, title in [("generos", "genre", "Géneros con más contenidos"), ("paises", "country", "Países con más contenidos"), ("idiomas", "language", "Idiomas más representados (códigos de fuente)")]:
        table = summaries[name]
        table = table[table[col].ne("Sin información")].head(10).sort_values("contents")
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.barh(table[col], table.contents, color="#2563EB")
        ax.set(title=title, xlabel="Contenidos")
        save(fig, f"{name}_catalogo", "Top 10. Géneros y países no son aditivos; ausencias excluidas.")
    fig, ax = plt.subplots(figsize=(9, 4.5))
    table = summaries["estrenos"]
    ax.plot(table.release_year, table.contents, marker="o", color="#2563EB")
    ax.set(title="Contenidos por año de estreno", xlabel="Año", ylabel="Contenidos")
    ax.set_ylim(0, 2200)
    ax.set_xticks(range(2010, 2026, 2))
    save(fig, "estrenos_catalogo", "Distribución de la muestra; no representa crecimiento operativo.")
    table = summaries["generos"].query('contents >= 25 and genre != "Sin información"').nlargest(10, "median_popularity").sort_values("median_popularity")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(table.genre, table.median_popularity, color="#047857")
    ax.set(title="Géneros con mayor popularidad típica", xlabel="Popularidad mediana (índice relativo)")
    save(fig, "popularidad_generos", "Mínimo 25 títulos por género; sin filtros.")
    print(f"Generados {len(summaries)} resúmenes y 6 gráficos en {IMAGES}")


if __name__ == "__main__":
    main()
