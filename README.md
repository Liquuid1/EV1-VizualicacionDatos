# StreamView Analytics

Dashboard de visual analytics para apoyar decisiones de adquisición y priorización de contenidos audiovisuales.

## Dependencias

```bash
python -m pip install -r requirements.txt
```

## Notebook interactivo

Abrir `notebooks/Notebook.ipynb` en VS Code o Jupyter y ejecutar las celdas en orden. El notebook utiliza `ipywidgets` para los filtros y Plotly para las visualizaciones. En este notebook encontraran el paso a paso del analisis realizado, esta separado por secciones para que sea más facil comprenderlo.

## Aplicación web

```bash
streamlit run dashboard/dashboard.py
```

La aplicación carga `data/streamview_catalogo_limpio.csv` y ofrece filtros por tipo, género, país y año de estreno.

## Criterios analíticos

- `popularity` se interpreta como un índice relativo, no como reproducciones.
- `vote_average = 0` se excluye de la valoración promedio por no representar una valoración suficiente.
- La popularidad se resume principalmente mediante la mediana para reducir el efecto de valores extremos.
- `budget`, `revenue` y `roi` se analizan solo para películas con presupuesto e ingresos positivos.
- Géneros y países se separan en dimensiones auxiliares para evitar conteos incorrectos.
- Los rankings priorizan títulos para revisión humana; no son recomendaciones automáticas.
