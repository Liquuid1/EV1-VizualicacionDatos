# Guía de construcción del dashboard en Power BI

## Alcance de la implementación
El proyecto cuenta con un dashboard interactivo de cuatro páginas, desarrollado en Power BI y guardado como `dashboard/StreamView.pbix`. No se requiere su publicación en línea para utilizarlo.

Este documento conserva las instrucciones técnicas de construcción y las recomendaciones de diseño originales. Algunas funcionalidades complementarias, como determinados botones de navegación o limpieza de filtros, pueden no formar parte de la implementación final.

## 1. Preparación y reproducción del proyecto
Los siguientes pasos documentan el procedimiento utilizado como referencia para construir el modelo y permiten reproducirlo en otro equipo. El dashboard final se encuentra disponible en `dashboard/StreamView.pbix`, por lo que no es necesario crearlo nuevamente para consultar sus resultados.

1. Copiar la carpeta del proyecto al PC. Usar los CSV ya preparados en `data/processed/`; no es necesario ejecutar Python para comenzar a construir. Para regenerarlos, consultar `docs/preparacion_datos.md`.
2. Abrir Power BI Desktop y crear un informe vacío. Importar **solo** `catalogo`, `dim_generos`, `contenido_genero`, `dim_paises`, `contenido_pais` y `dim_anio_estreno`.
3. Revisar tipos y configuración regional según la guía de preparación. `content_id` y `show_id` son texto; banderas son lógicas; números usan punto decimal.
4. Crear las cinco relaciones de `docs/modelo_indicadores.md`. Comprobar que no haya relaciones automáticas adicionales. No fusionar tablas de asociaciones.
5. Crear las 23 medidas de `dashboard/medidas.dax`, una por una, mediante Nueva medida. Si una fórmula falla, revisar nombres de tablas, tipos y separador regional.
6. Crear una página temporal de control con `[Total contenidos]`, `[Peliculas]`, `[Series]`, `[Peliculas con datos financieros]` y `[Popularidad mediana]`. Deben mostrar 31.991, 16.000, 15.991, 3.540 y 22,071 respectivamente, sin filtros.
7. Guardar el archivo con el nombre previsto y después de completar cada página.

### Clave visible para rankings

Crear esta columna calculada en `catalogo` para diferenciar obras con títulos iguales:

```dax
Etiqueta contenido =
catalogo[title] & " · " & catalogo[type] & " · " & catalogo[content_id]
```

Utilizarla como fila de los rankings y como campo de categoría del filtro Top N. Así el visual mantiene una fila por contenido. No aplicar Top N únicamente sobre `title`. En las tablas de detalle incluir también `release_year`, votos y métricas para interpretar el resultado.

## 2. Diseño común

Esta sección reúne los criterios de diseño utilizados como referencia durante la construcción del dashboard. La distribución y los elementos descritos corresponden a la propuesta original y pueden presentar diferencias respecto de la versión final implementada en Power BI.

Lienzo 16:9, fondo claro y texto oscuro. Usar Segoe UI, títulos de página de 24–28 puntos, valores de tarjetas de 26–32, títulos de visuales de 14–16 y etiquetas de 11–12. Estas medidas son una base; comprobar legibilidad en el equipo de exposición.

Se incluye `dashboard/tema_streamview.json`, que puede importarse desde los temas del informe. Paleta: azul oscuro para encabezados, azul para películas, verde para series y naranja para alertas. Mantener los colores por tipo en todas las páginas y acompañar las alertas con texto.

| Zona | Contenido |
| --- | --- |
| Franja superior | Nombre de página y subtítulo con pregunta de negocio. |
| Debajo del título | Navegador de páginas, siempre en la misma posición. |
| Franja de filtros | Tipo, género, país, idioma y año, visibles y compactos. |
| Franja de indicadores | Cuatro o cinco tarjetas prioritarias por página. |
| Área principal | Dos visuales comparativos o de tendencias. |
| Área inferior | Ranking o tabla de detalle cuando corresponda. |
| Pie | Alcance, advertencia breve y mensaje «Sin datos para esta selección» cuando aplique. |

No mostrar las 23 medidas a la vez. Las medidas auxiliares se utilizan en tooltips, controles y tablas. Los títulos deben describir exactamente la métrica y el universo.

## 3. Página «Resumen»

**Audiencia:** Directorio y Gerencia General. **Pregunta:** ¿cómo se compone el catálogo seleccionado y qué señales de desempeño presenta?

| Elemento | Visual y configuración |
| --- | --- |
| Tarjetas | `[Total contenidos]`, `[Peliculas]`, `[Series]`, `[Popularidad mediana]`, `[Valoracion promedio valida]`. |
| Composición | Barras: eje `catalogo[type]`, valor `[Total contenidos]`. Mostrar etiquetas de cantidad; películas azul y series verde. |
| Estrenos | Líneas: eje `dim_anio_estreno[release_year]`, valor `[Total contenidos]`, orden cronológico, eje sin agregación de años. Título «Contenidos por año de estreno». |
| Géneros predominantes | Barras horizontales: eje `dim_generos[genre]`, valor `[Total contenidos]`. Top 5 por esa medida, excluir «Sin información». |
| Contexto | Tooltip de valoración con `[Contenidos con valoracion]` y `[Cobertura valoracion]`. |

Pie: «Catálogo entregado para el caso · Estrenos 2010–2025 · Popularidad: índice relativo · Valoración: escala 0–10, excluye cero». Aclarar que los filtros pueden acotar el período.

Seleccionar una barra de tipo debe filtrar los demás gráficos y tarjetas. Las selecciones sobre gráficos son propias de la página; los segmentadores son los que se conservarán entre páginas.

## 4. Página «Catálogo»

**Audiencia:** Contenidos y Adquisición. **Pregunta:** ¿en qué categorías, países e idiomas se concentra la oferta?

| Elemento | Visual y configuración |
| --- | --- |
| Tarjetas | `[Total contenidos]`, `[Generos presentes]`, `[Paises presentes]`, `[Idiomas presentes]`. |
| Géneros | Barras horizontales: `dim_generos[genre]` y `[Total contenidos]`. Top 10, sin «Sin información». |
| Países | Barras horizontales: `dim_paises[country]` y `[Total contenidos]`. Top 10, sin «Sin información». |
| Idiomas | Treemap: grupo `catalogo[language]`, valor `[Total contenidos]`. Top 10, sin nulos. Título «Idiomas más representados (códigos de fuente)». |
| Detalle | Tabla: `content_id`, `title`, `type`, `release_year`, `language`, `genres`, `country`. Aplicar `[Mostrar contenido] = 1`; ocultar totales de columnas descriptivas. |

Pie: «Un contenido puede pertenecer a varios géneros y países. Las categorías no son aditivas. Los Top 10 no representan el catálogo completo». Los códigos de idioma se conservan como aparecen en fuente.

Seleccionar un país debe actualizar tarjetas, géneros, idiomas y detalle. Seleccionar un género debe actualizar países y detalle. No hacer que los gráficos modifiquen las selecciones visibles de los segmentadores.

## 5. Página «Popularidad y valoración»

**Audiencia:** Contenidos y Marketing. **Pregunta:** ¿qué géneros y títulos conviene revisar por popularidad y valoración?

| Elemento | Visual y configuración |
| --- | --- |
| Tarjetas | `[Popularidad mediana]`, `[Valoracion promedio valida]`, `[Cobertura valoracion]`, `[Contenidos elegibles ranking]`. |
| Géneros con popularidad típica | Barras: `dim_generos[genre]`, `[Popularidad genero con muestra suficiente]`. Top 10 por esa medida; filtrar medida no vacía. Tooltip `[Total contenidos]`. |
| Relación de métricas | Dispersión: X popularidad, Y calificación, categoría/detalle `content_id`, leyenda `type`. Usar `[Popularidad mediana]` y `[Valoracion promedio valida]` como valores a nivel de contenido; filtrar visual `has_valid_rating = TRUE`. Votos y título en tooltip. Escala logarítmica X si está disponible; popularidad es positiva. |
| Más populares | Tabla: `Etiqueta contenido`, `release_year`, `[Popularidad mediana]`, `[Valoracion promedio valida]`, `[Votos registrados]`. Top 10 sobre etiqueta por `[Popularidad mediana]`, orden descendente. |
| Mejor valorados | Tabla con los mismos campos. Filtro **solo de visual** `rating_rank_eligible = TRUE`. Top 10 sobre etiqueta por `[Valoracion promedio valida]`. Ordenar por valoración y después votos; documentar si el corte incluye empates. |

Si el visual de dispersión limita o reduce puntos, indicar esa limitación en el informe y en el tooltip. No afirmar que muestra todos los títulos sin comprobarlo. No convertir una observación visual en causalidad.

Pie: «Popularidad no equivale a reproducciones. Rankings de valoración: mínimo 100 votos. Comparación de géneros: mínimo 25 títulos». Esos umbrales son criterios analíticos del equipo.

## 6. Página «Finanzas de películas»

**Audiencia:** Directorio y Contenidos. **Pregunta:** ¿qué muestran las películas con información financiera y qué limitaciones afectan la interpretación?

Mantener el segmentador Tipo sincronizado y visible, sin fijar un filtro de página Movie. Si el usuario llega con series seleccionadas, mostrar cero películas válidas y métricas sin datos; no cambiar silenciosamente la selección. Indicar «Selecciona películas o todos los tipos para consultar finanzas».

| Elemento | Visual y configuración |
| --- | --- |
| Tarjetas | `[Peliculas con datos financieros]`, `[Cobertura financiera peliculas]`, `[Ingresos poblacion valida]`, `[Ingresos presupuesto veces]`, `[Peliculas financieras en revision]`. |
| Presupuesto e ingresos | Dispersión: X presupuesto, Y ingresos, detalle `content_id`. Filtro **del visual** `has_valid_financials = TRUE`. Usar suma para ambos valores al nivel de clave única; título y bandera de revisión en tooltip. Escalas logarítmicas cuando estén disponibles. |
| Ingresos por título | Barras horizontales: eje `Etiqueta contenido`, valor `[Ingresos poblacion valida]`. Top 10 por esa medida. |
| Razón por título | Tabla: etiqueta, presupuesto, ingresos, `revenue_budget_ratio`, `budget_review_required`. Filtro `has_valid_financials = TRUE` **del visual**. Top 10 sobre etiqueta por `[Ingresos presupuesto veces]`, orden descendente. |
| Filtro adicional | Segmentador `budget_review_required`: todos, True y False. Etiqueta «Presupuesto marcado para revisión». Solo en esta página, sin sincronizar. |

No aplicar `has_valid_financials = TRUE` a toda la página: reduciría el denominador de cobertura y podría hacerla aparecer como 100 %. Las medidas financieras ya aplican su propia condición; los visuales que usan columnas necesitan el filtro individual.

Pie: «Solo películas con presupuesto e ingresos positivos. Unidad monetaria no documentada. Ingresos/presupuesto es una razón, no utilidad ni rentabilidad de StreamView. Las alertas señalan presupuestos menores a 1.000; no prueban un error».

Mostrar siempre la cobertura. El botón o segmentador de revisión permite examinar las anomalías; por defecto mantener todos los registros, con las banderas visibles.

## 7. Navegación, filtros y estados

Las siguientes instrucciones corresponden a la propuesta original de navegación y manejo de filtros. Algunas funcionalidades complementarias, como el navegador de páginas y el botón «Limpiar filtros», se mantienen documentadas como recomendaciones de implementación y no necesariamente forman parte del dashboard final.

1. Insertar un navegador de páginas con los cuatro nombres definitivos y copiarlo a todas las páginas. Comprobar estado activo y legibilidad. En modo edición de Desktop se prueba con Ctrl + clic.
2. Crear los cinco segmentadores comunes en Resumen. Copiarlos y activar sincronización y visibilidad en las cuatro páginas. Género, país e idioma en listas desplegables con búsqueda y multiselección; año como rango; tipo con todos / Movie / TV Show.
3. Revisar Editar interacciones: segmentadores filtran todos los visuales analíticos. Entre gráficos seleccionar **Filtrar**, cuando esté disponible, para una lectura consistente. No usar un resaltado parcial como si fuera el total filtrado.
4. Añadir un botón «Limpiar filtros» mediante la acción de limpiar segmentadores. Probar que restablezca las selecciones sincronizadas y el filtro local de revisión en la página financiera. Esta acción no limpia selecciones hechas sobre gráficos: deseleccionarlas haciendo clic en el espacio del visual.
5. No sincronizar el segmentador de revisión fuera de Finanzas. No crear filtros ocultos a nivel de informe ni filtros de elegibilidad a nivel de página.
6. Para tarjetas sin datos, utilizar texto alternativo o una medida de presentación basada en `ISBLANK` si la tarjeta muestra «(En blanco)». Conservar las medidas numéricas originales para gráficos y comprobaciones.
7. Si `[Total contenidos] = 0`, mostrar un mensaje visible de segmento vacío. Nunca mostrar promedios cero para un universo sin observaciones.

## 8. Etapas de implementación

La siguiente tabla presenta las etapas definidas para desarrollar el dashboard. Se conserva como referencia del proceso de implementación, incluyendo actividades de configuración, validación y acabado que pueden diferir del alcance final.

| Bloque | Finalización comprobable |
| --- | --- |
| A. Modelo | Datos importados, cinco relaciones, 23 medidas y tarjetas de control correctas. |
| B. Resumen | Página usable, filtros funcionando y tendencia temporal legible. |
| C. Catálogo | Filtros de género y país comprobados, detalle sin duplicación. |
| D. Popularidad | Dos rankings diferenciados, umbrales visibles y dispersión interpretable. |
| E. Finanzas | Cobertura correcta, exclusión de series, anomalías visibles. |
| F. Acabado | Navegador, sincronización, limpieza, colores y textos consistentes. |
| G. Entrega de construcción | PBIX guardado, rutas registradas, capturas de cuatro páginas y controles básicos. |

Completar A y B antes de invertir tiempo en formato avanzado. Añadir después las otras páginas. Los mapas y recursos decorativos quedan fuera de esta primera construcción; países se comparan mediante barras. No hay un número de páginas obligatorio en las pautas: las cuatro páginas son una decisión de diseño del equipo.

## 9. Comprobaciones de implementación

| Selección | Total esperado | Películas financieras válidas |
| --- | ---: | ---: |
| Sin filtros | 31.991 | 3.540 |
| Movie | 16.000 | 3.540 |
| TV Show | 15.991 | 0 |
| Drama | 14.769 | 1.662 |
| Japan | 2.869 | 83 |
| Drama + Japan | 1.084 | 27 |
| Drama o Comedy + Japan | 1.872 | 47 |
| Estrenos 2020–2025 | 11.991 | 862 |
| Presupuesto en revisión | 55 | 10 |

Usar `referencia_kpis.csv` para todos los indicadores y `reference_cases.json` para las selecciones exactas. Las selecciones de gráficos deben estar limpias al comparar. La cobertura financiera general es 3.540 / 16.000 = **22,125 %**; con formato de un decimal se muestra **22,1 %**.

El dashboard interactivo se encuentra guardado en `dashboard/StreamView.pbix` y se incorporaron capturas de sus visualizaciones al informe ejecutivo. El informe ejecutivo también fue exportado a PDF como respaldo documental. Este PDF no reemplaza la interactividad del archivo PBIX. La exportación adicional de las cuatro páginas de Power BI a PDF se mantiene como una recomendación opcional.

La ubicación del archivo PBIX y las instrucciones generales para actualizar las fuentes de datos se encuentran documentadas en el README. Al trasladar el proyecto a otro equipo, se recomienda comprobar las conexiones de los archivos CSV y verificar que la actualización funcione correctamente. Evitar el uso de rutas absolutas específicas de un computador como requisito permanente.

## Documentación oficial consultada

- [Navegadores de páginas](https://learn.microsoft.com/en-us/power-bi/create-reports/button-navigators).
- [Segmentadores y sincronización](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-slicers).
- [Botones y acción de limpiar segmentadores](https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-buttons).
