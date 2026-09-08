from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st


st.set_page_config(page_title="StreamView Analytics", page_icon="S", layout="wide")


@st.cache_data
def load_catalog():
	project_root = Path(__file__).resolve().parents[1]
	catalog = pd.read_csv(project_root / "data" / "streamview_catalogo_limpio.csv")
	for column in ["release_year", "popularity", "vote_count", "vote_average", "budget", "revenue", "roi"]:
		catalog[column] = pd.to_numeric(catalog[column], errors="coerce")
	catalog["has_rating"] = catalog["vote_average"].gt(0)
	catalog["has_financial_data"] = (
		catalog["type"].eq("Movie")
		& catalog["budget"].gt(0)
		& catalog["revenue"].gt(0)
	)
	return catalog


def explode_dimension(catalog, column, output_column):
	dimension = catalog[["show_id", "title", column]].copy()
	dimension[output_column] = dimension[column].fillna("Sin información").astype(str).str.split(",")
	dimension = dimension.explode(output_column)
	dimension[output_column] = dimension[output_column].str.strip()
	return dimension[~dimension[output_column].isin(["", "Sin información"])]


catalog = load_catalog()
genres = explode_dimension(catalog, "genres", "genre")
countries = explode_dimension(catalog, "country", "country_name")

st.title("StreamView Analytics")
st.subheader("Radar de adquisición de contenidos")
st.caption(
	"Explora volumen, popularidad típica y títulos prioritarios. "
	"La popularidad es un índice relativo, no reproducciones."
)

with st.sidebar:
	st.header("Segmento de análisis")
	selected_type = st.selectbox("Tipo", ["Todos", "Movie", "TV Show"])
	genre_options = ["Todos"] + sorted(genres["genre"].unique())
	selected_genre = st.selectbox("Género", genre_options)
	country_options = ["Todos"] + sorted(countries["country_name"].unique())
	selected_country = st.selectbox("País", country_options)
	min_year = int(catalog["release_year"].min())
	max_year = int(catalog["release_year"].max())
	selected_years = st.slider("Año de estreno", min_year, max_year, (min_year, max_year))
	selected_metric = st.selectbox(
		"Métrica del ranking",
		options=["popularity", "vote_average", "vote_count"],
		format_func=lambda value: value.replace("_", " ").title(),
	)
	top_n = st.slider("Títulos a mostrar", 5, 20, 10, step=5)

filtered = catalog[catalog["release_year"].between(*selected_years)].copy()
if selected_type != "Todos":
	filtered = filtered[filtered["type"] == selected_type]
if selected_genre != "Todos":
	filtered = filtered[filtered["show_id"].isin(genres.loc[genres["genre"] == selected_genre, "show_id"])]
if selected_country != "Todos":
	filtered = filtered[filtered["show_id"].isin(countries.loc[countries["country_name"] == selected_country, "show_id"])]

if filtered.empty:
	st.warning("No hay contenidos para la combinación de filtros seleccionada.")
	st.stop()

st.markdown("### Lectura ejecutiva")
kpi_columns = st.columns(5)
kpi_columns[0].metric("Contenidos", f"{len(filtered):,}")
kpi_columns[1].metric("Películas", f"{(filtered['type'] == 'Movie').sum():,}")
kpi_columns[2].metric("Series", f"{(filtered['type'] == 'TV Show').sum():,}")
kpi_columns[3].metric("Popularidad mediana", f"{filtered['popularity'].median():,.1f}")
rated = filtered.loc[filtered["has_rating"], "vote_average"]
kpi_columns[4].metric("Valoración válida", f"{rated.mean():,.2f} / 10" if not rated.empty else "Sin datos")

left, right = st.columns(2)
with left:
	type_counts = filtered["type"].value_counts().rename_axis("type").reset_index(name="contents")
	st.plotly_chart(
		px.bar(
			type_counts,
			x="type",
			y="contents",
			color="type",
			color_discrete_map={"Movie": "#e05a47", "TV Show": "#1f8a70"},
			labels={"type": "Tipo", "contents": "Contenidos"},
			title="Composición del segmento",
		),
		use_container_width=True,
	)
with right:
	yearly = filtered.groupby("release_year", as_index=False).agg(contents=("show_id", "nunique"))
	st.plotly_chart(
		px.line(
			yearly,
			x="release_year",
			y="contents",
			markers=True,
			labels={"release_year": "Año de estreno", "contents": "Contenidos"},
			title="Evolución de los estrenos",
		),
		use_container_width=True,
	)

st.markdown("### Concentración del catálogo")
st.write(
	"Esta sección muestra dónde se concentra la oferta del segmento seleccionado. "
	"Géneros y países pueden repetirse en un mismo título, por lo que sus conteos "
	"representan asociaciones de contenido; los idiomas se cuentan por título y "
	"se muestran mediante su código ISO. "
	"La concentración describe disponibilidad, no necesariamente desempeño."
)

composition_columns = st.columns(3)
filtered_genres = genres[genres["show_id"].isin(filtered["show_id"])]
genre_counts = (
	filtered_genres.groupby("genre", as_index=False)
	.agg(contents=("show_id", "nunique"))
	.sort_values("contents", ascending=False)
	.head(10)
)
with composition_columns[0]:
	st.plotly_chart(
		px.bar(
			genre_counts.sort_values("contents"),
			x="contents",
			y="genre",
			orientation="h",
			color="contents",
			color_continuous_scale=["#f4f1ea", "#e05a47"],
			labels={"contents": "Contenidos", "genre": "Género"},
			title="Top 10 géneros",
		),
		use_container_width=True,
	)

filtered_countries = countries[countries["show_id"].isin(filtered["show_id"])]
country_counts = (
	filtered_countries.groupby("country_name", as_index=False)
	.agg(contents=("show_id", "nunique"))
	.sort_values("contents", ascending=False)
	.head(10)
)
with composition_columns[1]:
	st.plotly_chart(
		px.bar(
			country_counts.sort_values("contents"),
			x="contents",
			y="country_name",
			orientation="h",
			color="contents",
			color_continuous_scale=["#e8f0ed", "#1f8a70"],
			labels={"contents": "Contenidos", "country_name": "País"},
			title="Top 10 países",
		),
		use_container_width=True,
	)

language_counts = (
	filtered.loc[~filtered["language"].isin(["Sin información", "", "nan"]), "language"]
	.value_counts()
	.rename_axis("language")
	.reset_index(name="contents")
	.head(10)
)
with composition_columns[2]:
	st.plotly_chart(
		px.bar(
			language_counts.sort_values("contents"),
			x="contents",
			y="language",
			orientation="h",
			color="contents",
			color_continuous_scale=["#fff1df", "#d97706"],
			labels={"contents": "Contenidos", "language": "Idioma (código ISO)"},
			title="Top 10 idiomas (código ISO)",
		),
		use_container_width=True,
	)

top_genre = genre_counts.iloc[0] if not genre_counts.empty else None
top_country = country_counts.iloc[0] if not country_counts.empty else None
top_language = language_counts.iloc[0] if not language_counts.empty else None
concentration_summary = []
if top_genre is not None:
	concentration_summary.append(f"**{top_genre['genre']}** concentra {int(top_genre['contents']):,} contenidos asociados")
if top_country is not None:
	concentration_summary.append(f"**{top_country['country_name']}** concentra {int(top_country['contents']):,} contenidos asociados")
if top_language is not None:
	concentration_summary.append(f"**{top_language['language']}** es el idioma de {int(top_language['contents']):,} títulos")
if concentration_summary:
	st.info(" | ".join(concentration_summary))

st.markdown("### Dónde buscar oportunidades")
opportunity_columns = st.columns(2)
genre_summary = (
	filtered_genres.merge(filtered[["show_id", "popularity"]], on="show_id")
	.groupby("genre", as_index=False)
	.agg(contents=("show_id", "nunique"), median_popularity=("popularity", "median"))
	.query("contents >= 25")
	.nlargest(10, "median_popularity")
)
with opportunity_columns[0]:
	st.plotly_chart(
		px.bar(
			genre_summary.sort_values("median_popularity"),
			x="median_popularity",
			y="genre",
			orientation="h",
			color="contents",
			labels={"median_popularity": "Popularidad mediana", "genre": "Género"},
			title="Géneros con mayor popularidad típica",
		),
		use_container_width=True,
	)

country_summary = (
	filtered_countries.merge(filtered[["show_id", "popularity"]], on="show_id")
	.groupby("country_name", as_index=False)
	.agg(contents=("show_id", "nunique"), median_popularity=("popularity", "median"))
	.query("contents >= 25")
	.nlargest(10, "median_popularity")
)
with opportunity_columns[1]:
	st.plotly_chart(
		px.bar(
			country_summary.sort_values("median_popularity"),
			x="median_popularity",
			y="country_name",
			orientation="h",
			color="contents",
			labels={"median_popularity": "Popularidad mediana", "country_name": "País"},
			title="Mercados con mayor popularidad típica",
		),
		use_container_width=True,
	)

st.markdown("### Popularidad y calificaciones")
st.write(
	"Estas métricas responden preguntas distintas: la popularidad identifica los "
	"contenidos con mayor visibilidad relativa, mientras que la calificación refleja "
	"la valoración promedio de quienes votaron. Un contenido puede destacar en una "
	"dimensión y no en la otra."
)

popularity_columns = st.columns(2)
popular_titles = filtered.nlargest(top_n, "popularity")[
	["title", "type", "release_year", "popularity", "vote_average", "vote_count"]
]
with popularity_columns[0]:
	st.markdown("#### Contenidos más populares")
	st.caption("Ordenados por el índice relativo `popularity`.")
	st.dataframe(popular_titles, use_container_width=True, hide_index=True)

minimum_votes_for_rating = 100
best_rated_titles = (
	filtered[
		filtered["has_rating"]
		& filtered["vote_count"].ge(minimum_votes_for_rating)
	]
	.nlargest(top_n, "vote_average")[
		["title", "type", "release_year", "vote_average", "vote_count", "popularity"]
	]
)
with popularity_columns[1]:
	st.markdown("#### Contenidos mejor calificados")
	st.caption(
		f"Solo incluye valoraciones mayores que cero y al menos {minimum_votes_for_rating} votos."
	)
	if best_rated_titles.empty:
		st.info("No hay suficientes contenidos calificados para este segmento.")
	else:
		st.dataframe(best_rated_titles, use_container_width=True, hide_index=True)

st.markdown("#### Lectura de la comparación")
st.info(
		"La popularidad no equivale a reproducciones y la calificación no mide alcance. "
		"Para priorizar una adquisición conviene revisar ambas señales junto con el número "
		"de votos, el género, el país y la disponibilidad de datos financieros."
)

st.markdown("### Características de los contenidos destacados")
popular_ids = set(filtered.nlargest(top_n, "popularity")["show_id"])
rated_ids = set(
	filtered[
		filtered["has_rating"]
		& filtered["vote_count"].ge(minimum_votes_for_rating)
	].nlargest(top_n, "vote_average")["show_id"]
)
shared_ids = popular_ids.intersection(rated_ids)
featured_ids = popular_ids.union(rated_ids)
profile_ids = shared_ids if len(shared_ids) >= 3 else featured_ids
profile_contents = filtered[filtered["show_id"].isin(profile_ids)].copy()

profile_columns = st.columns(4)
profile_columns[0].metric("Más populares", f"{len(popular_ids):,}")
profile_columns[1].metric("Mejor calificados", f"{len(rated_ids):,}")
profile_columns[2].metric("En ambos grupos", f"{len(shared_ids):,}")
profile_columns[3].metric(
	"Año mediano de estreno",
	f"{profile_contents['release_year'].median():.0f}" if not profile_contents.empty else "Sin datos",
)

if len(shared_ids) >= 3:
	st.success(
		f"Se analizaron los {len(shared_ids)} contenidos que aparecen simultáneamente "
		"entre los más populares y los mejor calificados."
	)
elif featured_ids:
	st.warning(
		"Hay menos de 3 contenidos presentes en ambos rankings. El perfil se construye "
		"con la combinación de ambos grupos y debe interpretarse como una señal exploratoria."
	)

profile_genres = (
	genres[genres["show_id"].isin(profile_ids)]
	.groupby("genre", as_index=False)
	.agg(contents=("show_id", "nunique"))
	.nlargest(5, "contents")
)
profile_countries = (
	countries[countries["show_id"].isin(profile_ids)]
	.groupby("country_name", as_index=False)
	.agg(contents=("show_id", "nunique"))
	.nlargest(5, "contents")
)
profile_languages = (
	profile_contents.loc[
		~profile_contents["language"].isin(["Sin información", "", "nan"]),
		"language",
	]
	.value_counts()
	.rename_axis("language")
	.reset_index(name="contents")
	.head(5)
)

characteristic_columns = st.columns(3)
with characteristic_columns[0]:
	st.markdown("#### Géneros frecuentes")
	st.dataframe(
		profile_genres.rename(columns={"genre": "Género", "contents": "Títulos"}),
		use_container_width=True,
		hide_index=True,
	)
with characteristic_columns[1]:
	st.markdown("#### Países frecuentes")
	st.dataframe(
		profile_countries.rename(columns={"country_name": "País", "contents": "Títulos"}),
		use_container_width=True,
		hide_index=True,
	)
with characteristic_columns[2]:
	st.markdown("#### Idiomas frecuentes")
	st.dataframe(
		profile_languages.rename(columns={"language": "Idioma (ISO)", "contents": "Títulos"}),
		use_container_width=True,
		hide_index=True,
	)

if not profile_contents.empty:
	type_profile = profile_contents["type"].value_counts()
	dominant_type = type_profile.index[0]
	dominant_genre = profile_genres.iloc[0]["genre"] if not profile_genres.empty else "sin género informado"
	dominant_language = profile_languages.iloc[0]["language"] if not profile_languages.empty else "sin idioma informado"
	st.info(
		f"**Patrón observable:** los contenidos destacados se concentran principalmente en "
		f"**{dominant_type}**, con predominio de **{dominant_genre}** "
		f"como género y **{dominant_language}** como idioma entre los "
		"registros informados. Estas características describen el grupo filtrado; no "
		"implican que todo contenido de esa categoría tendrá el mismo desempeño."
	)

st.markdown("### Prioridades para campañas promocionales")
st.write(
	"Esta recomendación combina dos señales: visibilidad relativa y valoración del público. "
	"Las categorías exigen al menos 25 contenidos y los títulos al menos 100 votos válidos, "
	"para que una campaña no se defina por casos aislados. El resultado es una lista de "
	"candidatos para marketing, no una decisión automática de inversión."
)

def add_campaign_score(dataframe, popularity_column="median_popularity", rating_column="average_rating"):
	result = dataframe.dropna(subset=[popularity_column, rating_column]).copy()
	if result.empty:
		return result
	result["campaign_score"] = (
		result[popularity_column].rank(pct=True) * 0.5
		+ result[rating_column].rank(pct=True) * 0.5
	)
	return result.sort_values("campaign_score", ascending=False)


category_metrics = (
	filtered_genres.merge(filtered[["show_id", "popularity", "vote_average", "has_rating"]], on="show_id")
	.groupby("genre", as_index=False)
	.agg(
		contents=("show_id", "nunique"),
		median_popularity=("popularity", "median"),
		average_rating=("vote_average", lambda values: values[values.gt(0)].mean()),
		rated_contents=("has_rating", "sum"),
	)
	.query("contents >= 25 and rated_contents >= 25")
)
category_metrics = add_campaign_score(category_metrics)

campaign_columns = st.columns(2)
with campaign_columns[0]:
	st.markdown("#### Categorías recomendadas")
	if category_metrics.empty:
		st.info("No hay categorías con suficiente información para priorizar campañas.")
	else:
		category_display = category_metrics.head(8).rename(
			columns={
				"genre": "Categoría",
				"contents": "Contenidos",
				"median_popularity": "Popularidad mediana",
				"average_rating": "Calificación promedio",
				"campaign_score": "Prioridad",
			}
		)[
			["Categoría", "Contenidos", "Popularidad mediana", "Calificación promedio", "Prioridad"]
		]
		st.dataframe(
			category_display.style.format(
				{
					"Popularidad mediana": "{:.1f}",
					"Calificación promedio": "{:.2f}",
					"Prioridad": "{:.2f}",
				}
			),
			use_container_width=True,
			hide_index=True,
		)

campaign_titles = filtered[
	filtered["has_rating"] & filtered["vote_count"].ge(minimum_votes_for_rating)
].copy()
if not campaign_titles.empty:
	campaign_titles["campaign_score"] = (
		campaign_titles["popularity"].rank(pct=True) * 0.5
		+ campaign_titles["vote_average"].rank(pct=True) * 0.5
	)
	campaign_titles = campaign_titles.nlargest(top_n, "campaign_score")

with campaign_columns[1]:
	st.markdown("#### Contenidos candidatos para promoción")
	if campaign_titles.empty:
		st.info("No hay títulos con suficientes votos para priorizar campañas.")
	else:
		st.dataframe(
			campaign_titles[
				["title", "type", "popularity", "vote_average", "vote_count", "campaign_score"]
			].rename(
				columns={
					"title": "Título",
					"type": "Tipo",
					"popularity": "Popularidad",
					"vote_average": "Calificación",
					"vote_count": "Votos",
					"campaign_score": "Prioridad",
				}
			).style.format(
				{
					"Popularidad": "{:.1f}",
					"Calificación": "{:.2f}",
					"Prioridad": "{:.2f}",
				}
			),
			use_container_width=True,
			hide_index=True,
		)

st.caption(
	"La prioridad combina en partes iguales el ranking relativo de popularidad y calificación. "
	"Debe complementarse con objetivos de campaña, segmento objetivo, derechos de uso y presupuesto."
)

st.markdown("### Finanzas de películas")
financial = filtered[filtered["has_financial_data"]]
if financial.empty:
	st.info("Este segmento no contiene películas con presupuesto e ingresos válidos.")
else:
	financial_top = financial.nlargest(min(top_n, 10), "roi")
	st.caption(
		"El ROI se calcula como ingresos / presupuesto y no se aplica a series. "
		"Se utiliza una escala logarítmica para que los valores extremos no oculten "
		"las diferencias del resto de las películas."
	)
	financial_figure = px.bar(
		financial_top.sort_values("roi"),
		x="roi",
		y="title",
		orientation="h",
		color="roi",
		hover_data={"roi": ":.2f"},
		labels={"roi": "ROI (escala logarítmica)", "title": "Película"},
		title="Películas con mayor retorno observado (escala logarítmica)",
	)
	financial_figure.update_xaxes(type="log")
	st.plotly_chart(financial_figure, use_container_width=True)

st.caption(
	"Las categorías pequeñas pueden tener resultados inestables. Los rankings sirven "
	"para priorizar revisión editorial y contractual, no constituyen recomendaciones automáticas."
)
