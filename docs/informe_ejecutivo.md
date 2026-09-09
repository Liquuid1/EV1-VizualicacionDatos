# Informe ejecutivo

## StreamView Analytics
### Solución de visualización para la adquisición y priorización de contenidos audiovisuales

**Asignatura:** ADY1104 Visualización de Datos  
**Integrantes:** Betsabe Spring y David Zúñiga  
**Profesor:** Oscar Oliva  
**Fecha:** 09/09/2026  

---

## 1. Descripción del problema de negocio

### 1.1 Contexto organizacional

StreamView Analytics es una plataforma internacional de streaming digital que administra un catálogo audiovisual compuesto por películas y series. Para gestionar este catálogo, la organización dispone de información sobre títulos, directores, reparto, países de producción, idiomas, géneros, fechas de estreno, popularidad, cantidad de votos, calificaciones y, en el caso de las películas, presupuesto e ingresos.

El crecimiento del catálogo y la diversidad de variables disponibles generan la necesidad de transformar los datos en información clara, comparable y accionable. La solución desarrollada en este proyecto busca apoyar decisiones relacionadas con la adquisición, priorización, promoción y posicionamiento de contenidos.

### 1.2 Problema de negocio

La información disponible se encontraba distribuida en fuentes independientes y no ofrecía una visión consolidada del catálogo. Esta situación dificultaba comparar películas y series, reconocer los géneros con mayor presencia o popularidad, identificar mercados relevantes y seleccionar contenidos para campañas promocionales.

Además, los reportes convencionales presentaban una cantidad importante de información, poca interacción y criterios de lectura no necesariamente homogéneos. Como consecuencia, las áreas responsables podían tomar decisiones utilizando una visión parcial del catálogo y sin contar con un mecanismo sencillo para explorar los datos según el tipo de contenido, el género, el país o el año de estreno.

El problema central se formula de la siguiente manera:

> **¿Cómo transformar la información integrada del catálogo de StreamView Analytics en una solución visual interactiva que permita identificar oportunidades de adquisición y priorizar contenidos para revisión editorial y promocional?**

La solución no pretende reemplazar la evaluación editorial, contractual ni financiera. Su propósito es facilitar una primera priorización basada en evidencia, dejando explícitas las limitaciones de las métricas utilizadas.

### 1.3 Decisiones que debe apoyar el análisis

La solución se diseñó para entregar evidencia que apoye las siguientes decisiones:

- Priorizar géneros y mercados para futuras adquisiciones.
- Comparar la composición del catálogo entre películas y series.
- Identificar contenidos y categorías con mayor visibilidad relativa.
- Reconocer contenidos con mejores calificaciones, considerando un mínimo de votos válidos.
- Seleccionar títulos candidatos para campañas promocionales.
- Orientar decisiones de posicionamiento, renovación y gestión del catálogo.
- Analizar el desempeño financiero observado de películas con presupuesto e ingresos disponibles.

En este contexto, la popularidad se interpreta como un índice relativo dentro de la fuente de datos y no como una medida directa de reproducciones. Del mismo modo, el análisis financiero se limita a las películas que cuentan con presupuesto e ingresos positivos y válidos.

### 1.4 Audiencia objetivo

La audiencia principal de la solución es la **Gerencia de Contenidos y Adquisición**, que necesita decidir qué contenidos adquirir, renovar, producir, posicionar o someter a una revisión más detallada.

Como audiencias secundarias se consideran:

- **Gerencia General y Directorio:** requieren indicadores consolidados, tendencias y síntesis para apoyar decisiones estratégicas.
- **Gerencia de Marketing:** necesita identificar contenidos, géneros y títulos con potencial para campañas promocionales.
- **Gerencia de Producto:** puede utilizar la información para comprender la composición del catálogo y mejorar su presentación o navegación.
- **Equipo de Data & Analytics:** requiere una solución reproducible, trazable y consistente para mantener el análisis y ampliar sus capacidades.

### 1.5 Propósito comunicacional

El propósito comunicacional es convertir un catálogo amplio y heterogéneo en una lectura visual ordenada, comprensible y orientada a la acción. Para ello, el dashboard presenta primero una visión general del segmento seleccionado, luego muestra su concentración por género, país e idioma, identifica oportunidades mediante métricas de popularidad típica y finalmente ofrece títulos y películas que conviene revisar.

La comunicación está organizada para reducir la carga cognitiva y permitir que la audiencia avance desde una pregunta general hacia una decisión más específica. Los indicadores, filtros, rankings y visualizaciones no se presentan como conclusiones automáticas, sino como evidencia para orientar la conversación entre las áreas de contenidos, marketing, producto y analítica.

### 1.6 Alcance de esta entrega

El proyecto utiliza los archivos de datos proporcionados para el caso StreamView Analytics y genera un catálogo integrado para el análisis exploratorio y el dashboard. La procedencia externa, autoría y licencia original de los archivos CSV no se encuentran documentadas dentro del proyecto, por lo que el informe los identifica como fuentes entregadas para el desarrollo del caso.

La solución se implementa mediante notebooks de análisis y una aplicación interactiva desarrollada con Streamlit y Plotly. La aplicación permite explorar el catálogo mediante filtros por tipo, género, país y año de estreno, además de consultar indicadores, rankings y métricas financieras cuando existe información suficiente.

---

## 2. Objetivos del proyecto

### 2.1 Objetivo general

Diseñar e implementar una solución de Visual Analytics que integre y explore el catálogo audiovisual de StreamView Analytics mediante visualizaciones claras y un dashboard interactivo, con el propósito de entregar evidencia para apoyar decisiones de adquisición, promoción, posicionamiento y gestión de contenidos.

### 2.2 Objetivos específicos

- Integrar los datasets de películas y series en una estructura común, conservando las variables relevantes para el análisis.
- Revisar y mejorar la calidad de los datos mediante la estandarización de tipos, textos, fechas, valores faltantes y registros duplicados.
- Describir la composición del catálogo según tipo de contenido, género, país, idioma y año de estreno.
- Identificar patrones y oportunidades mediante el análisis conjunto de popularidad, calificación, cantidad de votos y disponibilidad de información financiera.
- Diseñar visualizaciones adecuadas a la naturaleza de cada variable, priorizando la comparación, la lectura temporal y la identificación de relaciones.
- Construir un dashboard interactivo con filtros, KPIs, rankings y mecanismos de exploración orientados a preguntas de adquisición y promoción.
- Comunicar los principales hallazgos mediante una narrativa visual que avance desde la visión general del catálogo hacia la priorización de categorías y títulos.
- Proponer recomendaciones para la revisión editorial, la planificación de campañas y la toma de decisiones basada en datos.

### 2.3 Preguntas de negocio

El análisis exploratorio y el dashboard se organizan en torno a las siguientes preguntas:

1. ¿Cómo se distribuye el catálogo entre películas y series?
2. ¿Qué géneros, países e idiomas concentran la mayor cantidad de contenidos?
3. ¿Cómo ha evolucionado la incorporación y el estreno de contenidos a través del tiempo?
4. ¿Qué contenidos presentan mayor popularidad relativa y cuáles tienen mejores calificaciones?
5. ¿Existe una relación observable entre popularidad, calificación y cantidad de votos?
6. ¿Qué países o categorías pueden representar oportunidades para futuras adquisiciones?
7. ¿Qué películas presentan mayores ingresos o retorno observado sobre el presupuesto?
8. ¿Qué contenidos y categorías deberían priorizarse para una revisión de campañas promocionales?

Estas preguntas delimitan el alcance del proyecto. La solución permite identificar señales y patrones dentro de los datos disponibles, pero no estima directamente retención, reproducciones, satisfacción de usuarios ni rentabilidad completa de una decisión de negocio.

### 2.4 Indicadores clave de desempeño

Los KPIs se agrupan según la decisión que ayudan a informar:

| Dimensión | Indicador | Uso en el análisis |
| --- | --- | --- |
| Volumen | Total de contenidos | Dimensionar el catálogo seleccionado por los filtros. |
| Volumen | Cantidad de películas y series | Comparar la composición del catálogo. |
| Cobertura | Cantidad de géneros, países e idiomas | Medir la diversidad y concentración de la oferta. |
| Popularidad | Popularidad mediana | Comparar la visibilidad relativa de categorías y segmentos reduciendo el efecto de valores extremos. |
| Valoración | Calificación promedio válida | Identificar la percepción registrada para contenidos con calificación mayor que cero. |
| Participación | Cantidad de votos | Aportar contexto sobre el respaldo disponible para una calificación. |
| Evolución | Contenidos por año de estreno | Observar la composición temporal del catálogo. |
| Finanzas | Presupuesto e ingresos | Comparar el desempeño financiero observado de películas con datos válidos. |
| Finanzas | ROI aproximado | Calcular la razón `revenue / budget` como señal exploratoria de retorno observado. |

Los indicadores de popularidad y valoración se interpretan de manera complementaria. Un contenido puede presentar alta popularidad sin tener la mejor calificación, por lo que ambos criterios se combinan para construir prioridades de revisión. En el caso de las campañas, el dashboard utiliza un puntaje relativo que combina en partes iguales la posición de popularidad y la posición de calificación; este resultado sirve para ordenar candidatos y no constituye una recomendación automática.

El análisis financiero se realiza únicamente para películas con presupuesto e ingresos positivos. Las series se excluyen de esta comparación porque la fuente no dispone de las mismas variables financieras para ese tipo de contenido.

---

## 3. Fuentes e integración de datos

### 3.1 Fuentes utilizadas

El proyecto utiliza dos archivos CSV proporcionados para el caso StreamView Analytics. Ambos contienen información de contenidos audiovisuales y fueron integrados para construir una vista común del catálogo.

| Fuente | Tipo de contenido | Registros iniciales | Características principales |
| --- | --- | ---: | --- |
| `data/netflix_movies_detailed_up_to_2025.csv` | Películas | 16.000 | Identificación, título, director, reparto, país, fecha de incorporación, año de estreno, clasificación, duración, géneros, idioma, popularidad, votos, calificación, presupuesto e ingresos. |
| `data/netflix_tv_shows_detailed_up_to_2025.csv` | Series | 16.000 | Identificación, título, director, reparto, país, fecha de incorporación, año de estreno, clasificación, duración, géneros, idioma, popularidad, votos y calificación. |

La autoría, procedencia externa y licencia original de estos archivos no se encuentran documentadas en el repositorio. Por esta razón, el informe los considera fuentes de datos entregadas para el desarrollo del caso y no atribuye su origen a una organización externa específica.

### 3.2 Variables relevantes

Las variables se seleccionaron según su utilidad para describir el catálogo, comparar el desempeño observado y apoyar las decisiones definidas en la sección anterior.

| Grupo | Variables | Uso |
| --- | --- | --- |
| Identificación | `show_id`, `type`, `title` | Identificar cada contenido y distinguir películas de series. |
| Caracterización | `director`, `cast`, `rating`, `duration` | Describir atributos editoriales y de clasificación. |
| Cobertura | `country`, `language`, `genres` | Analizar diversidad y concentración por país, idioma y género. |
| Tiempo | `date_added`, `release_year`, `date_added_year` | Estudiar estrenos e incorporación de contenidos. |
| Desempeño | `popularity`, `vote_count`, `vote_average` | Comparar visibilidad relativa, valoración y respaldo de las calificaciones. |
| Finanzas | `budget`, `revenue`, `roi` | Analizar películas con información financiera positiva y disponible. |

Las variables financieras no tienen el mismo alcance para ambos tipos de contenido. Por ello, `budget`, `revenue` y `roi` se mantienen como valores faltantes para las series y no se utilizan para compararlas directamente con las películas.

### 3.3 Proceso de integración

La integración se realizó mediante las siguientes etapas:

1. **Carga de fuentes:** se leyeron los dos archivos CSV desde la carpeta `data/`.
2. **Alineación de estructura:** se agregaron las columnas financieras a la tabla de series como valores faltantes y se concatenaron ambas fuentes en una tabla común.
3. **Normalización de nombres y textos:** los nombres de columnas se convirtieron a minúsculas y se eliminaron espacios innecesarios. Las variables de texto fueron convertidas a un formato consistente y los valores categóricos ausentes se representaron como `Sin información`.
4. **Conversión de tipos:** las fechas se transformaron a formato de fecha y las variables numéricas se convirtieron mediante coerción para detectar valores no interpretables.
5. **Tratamiento de métricas financieras:** los valores de presupuesto e ingresos menores o iguales a cero se trataron como información no disponible. Luego se calculó `roi` como `revenue / budget` cuando ambas variables eran válidas.
6. **Eliminación de duplicados:** se utilizó `show_id` como identificador de contenido y se eliminaron 406 registros duplicados de series.
7. **Creación de variables derivadas:** se creó `date_added_year` a partir de la fecha de incorporación y `roi` para las películas con información financiera válida.
8. **Exportación:** el resultado se guardó como `data/streamview_catalogo_limpio.csv` para reutilizarlo en el análisis exploratorio y en el dashboard.

El catálogo integrado quedó compuesto por **31.594 registros y 20 columnas**, sin duplicados restantes por `show_id`. La distribución final corresponde a **16.000 películas y 15.594 series**.

### 3.4 Tablas auxiliares para dimensiones multivaluadas

Las columnas `genres` y `country` pueden contener más de un valor separado por comas para un mismo contenido. Para evitar perder información o contar una fila completa como si perteneciera a una sola categoría, se crearon tablas auxiliares mediante una operación de separación y expansión (`explode`).

Estas tablas conservan el identificador del contenido y una fila por asociación de género o país. De esta forma, un título asociado a tres géneros puede contabilizarse en los tres géneros sin duplicar el contenido en la tabla principal. El mismo criterio se aplica a los países de producción.

Las tablas auxiliares se utilizan para:

- Construir rankings de géneros y países.
- Calcular la cantidad de contenidos asociados a cada categoría.
- Obtener la popularidad mediana por género o país.
- Aplicar correctamente los filtros del dashboard.
- Evitar interpretaciones incorrectas producidas por conteos sobre cadenas de texto completas.

### 3.5 Diagnóstico de calidad y criterios de uso

El diagnóstico mostró que las variables financieras presentan disponibilidad parcial: `budget` tiene aproximadamente 84,66 % de valores faltantes, `revenue` 82,13 % y `roi` 88,80 %. Esta ausencia se explica principalmente porque las variables financieras no aplican a las series y porque algunos registros de películas no contienen información válida.

La descripción textual presenta aproximadamente 10,34 % de valores faltantes, mientras que variables estructurales como `show_id`, `title` y `type` no presentan nulos en el catálogo preparado. Estas diferencias se consideran al seleccionar los indicadores y al construir las visualizaciones.

En consecuencia, se adoptaron los siguientes criterios:

- No utilizar los campos financieros para comparar películas y series.
- No interpretar un valor de popularidad como cantidad de reproducciones.
- Excluir las calificaciones iguales a cero del promedio válido.
- Exigir un volumen mínimo de contenidos en los rankings de categorías para reducir resultados inestables.
- Mantener trazabilidad entre el contenido original y las tablas auxiliares mediante `show_id`.

El archivo limpio constituye la fuente común utilizada por el análisis exploratorio y la aplicación interactiva, lo que permite reproducir las visualizaciones a partir de una misma base preparada.

---

## 4. Análisis exploratorio

### 4.1 Enfoque del análisis

El análisis exploratorio se orientó a identificar patrones, tendencias y oportunidades que fueran relevantes para la Gerencia de Contenidos y Adquisición. La lectura se organizó desde la descripción general del catálogo hacia el análisis de desempeño y la priorización de categorías y títulos.

Se estudiaron cinco dimensiones principales:

- Composición del catálogo por tipo de contenido.
- Concentración por género, país e idioma.
- Evolución de los contenidos según año de estreno.
- Relación entre popularidad, valoración y cantidad de votos.
- Desempeño financiero observado de las películas con información válida.

Para las variables que pueden contener varios valores por contenido, como género y país, los conteos se calcularon sobre las asociaciones normalizadas. Esto permite reconocer la presencia de una categoría sin confundir el número de asociaciones con el número total de títulos.

### 4.2 Composición del catálogo

El catálogo preparado contiene **31.594 contenidos**, distribuidos en **16.000 películas** y **15.594 series**. Esta composición es relativamente equilibrada y permite analizar ambos tipos de contenido sin que uno de ellos elimine completamente la lectura del otro.

La comparación entre películas y series debe realizarse considerando la naturaleza de cada formato. Ambas comparten variables de identificación, caracterización, popularidad y valoración, pero las variables de presupuesto e ingresos solo están disponibles para películas. Por este motivo, el análisis financiero se presenta como un bloque independiente.

Este resultado confirma la necesidad de incluir un filtro por tipo de contenido. La audiencia puede estudiar el catálogo completo o concentrarse en películas o series según la decisión que deba tomar.

### 4.3 Géneros y concentración temática

Los géneros con mayor presencia en el catálogo son **Drama**, **Comedy** y **Animation**. En los conteos observados, Drama reúne aproximadamente 14.571 asociaciones de contenido, Comedy 8.983 y Animation 4.000.

La concentración por volumen permite reconocer las categorías que tienen mayor representación y que, por lo tanto, pueden ser relevantes para la planificación de contenido y la navegación del catálogo. Sin embargo, la cantidad de títulos no equivale necesariamente a un mejor desempeño. Una categoría puede tener muchos contenidos y una popularidad mediana menor que otra categoría con menos títulos.

Por esta razón, el análisis incorpora una segunda lectura basada en la **popularidad mediana por género**. La mediana permite reducir la influencia de títulos excepcionales y aproximarse al desempeño típico de cada categoría. Para evitar conclusiones basadas en grupos demasiado pequeños, las oportunidades se filtran considerando un mínimo de 25 contenidos.

### 4.4 Países e idiomas

La dimensión de país muestra una concentración importante en **United States of America**, con 10.874 asociaciones de contenido. Le siguen Japón, con 2.822, y Reino Unido, con 2.583. También aparecen China, Corea del Sur, Francia, Canadá, Alemania, India y España entre los países con mayor cantidad de asociaciones.

Este patrón muestra que el catálogo tiene una fuerte presencia de contenidos asociados a Estados Unidos, mientras que otros mercados aportan volúmenes menores pero potencialmente relevantes para diversificación y adquisición. El volumen de contenidos por país debe interpretarse como disponibilidad dentro del catálogo y no como una medida directa de popularidad o rentabilidad.

El idioma se utiliza como una dimensión complementaria para comprender la composición de la oferta. En el dashboard se presenta mediante códigos ISO y se cuenta por título, mientras que géneros y países pueden generar más de una asociación por contenido.

### 4.5 Evolución temporal

La distribución por año de estreno evidencia una mayor presencia de contenidos estrenados en años recientes, especialmente entre **2020 y 2024**. Esto indica que el catálogo combina títulos históricos con una concentración relevante de producciones o incorporaciones de periodos más cercanos al momento de análisis.

La evolución temporal ayuda a responder dos preguntas distintas:

- ¿Qué años concentran una mayor cantidad de títulos estrenados?
- ¿Cómo cambia la composición del catálogo cuando se selecciona un intervalo temporal?

El gráfico de líneas resulta adecuado para observar la tendencia y detectar periodos de mayor concentración. No obstante, la cantidad de títulos por año no permite concluir por sí sola que los contenidos más recientes tengan mejor desempeño, ya que esa afirmación requeriría comparar popularidad, valoración y otras métricas controlando por tipo de contenido y disponibilidad de votos.

### 4.6 Popularidad, valoración e interacción

El análisis diferencia tres señales que no deben confundirse:

- **Popularidad:** índice relativo de visibilidad dentro de la fuente.
- **Valoración:** promedio registrado por los usuarios o evaluadores de la fuente.
- **Cantidad de votos:** volumen de observaciones que entrega contexto a una valoración.

Los contenidos más populares observados incluyen títulos como *Shrek Forever After*, *Inception*, *Harry Potter and the Deathly Hallows: Part I*, *Tangled* y *How to Train Your Dragon*. Estos casos muestran que la popularidad puede concentrarse en títulos reconocibles y con alta cantidad de votos, pero no permiten afirmar que exista una equivalencia entre popularidad y reproducciones reales.

La solución compara popularidad y valoración porque ambas dimensiones responden a preguntas diferentes. La popularidad ayuda a identificar visibilidad relativa, mientras que la valoración permite reconocer la recepción registrada. Cuando un título aparece bien posicionado en ambas dimensiones, se convierte en un candidato más sólido para revisión promocional; aun así, debe verificarse el segmento objetivo, los derechos disponibles, el presupuesto y el propósito de la campaña.

Las calificaciones iguales a cero se excluyen del promedio válido. Además, el dashboard exige un mínimo de votos para priorizar títulos, reduciendo el riesgo de destacar contenidos con una valoración basada en evidencia insuficiente.

### 4.7 Desempeño financiero de películas

El análisis financiero se limita a películas con presupuesto e ingresos positivos. Para estos registros se calcula un retorno observado mediante la razón:

$$
ROI\ aproximado = \\frac{ingresos}{presupuesto}
$$

Este indicador permite ordenar películas y observar diferencias relativas, pero no corresponde a una rentabilidad completa. No incluye costos de marketing, distribución, licencias, operación ni otros componentes financieros. Por este motivo, los resultados se presentan como una señal exploratoria para revisión y no como una recomendación automática de inversión.

La escala logarítmica utilizada en la visualización financiera permite mostrar valores con diferencias muy amplias sin ocultar completamente las películas con retornos menores. Las series no se incluyen en este bloque porque no cuentan con presupuesto e ingresos comparables dentro de la fuente utilizada.

### 4.8 Hallazgos principales

El análisis exploratorio permite sintetizar los siguientes hallazgos:

1. El catálogo tiene una composición equilibrada entre películas y series, por lo que el dashboard debe permitir separar ambos tipos.
2. Drama, Comedy y Animation concentran una parte importante de las asociaciones de género, aunque el volumen no equivale necesariamente a desempeño.
3. Estados Unidos concentra la mayor cantidad de contenidos asociados, mientras Japón y Reino Unido destacan entre los siguientes mercados.
4. Los años recientes, especialmente entre 2020 y 2024, tienen una presencia importante en la distribución de estrenos.
5. Popularidad, valoración y cantidad de votos entregan señales complementarias y deben analizarse conjuntamente.
6. La priorización de campañas debe combinar desempeño relativo con un volumen mínimo de evidencia y revisión humana.
7. El análisis financiero es útil para ordenar películas con datos válidos, pero su cobertura y definición impiden interpretarlo como rentabilidad completa.

Estos hallazgos orientan la narrativa del dashboard: primero se dimensiona el catálogo, luego se muestran las concentraciones y oportunidades, después se revisan títulos prioritarios y finalmente se presenta el bloque financiero.

---

## 5. Justificación de las visualizaciones

### 5.1 Criterio general de selección

Las visualizaciones se seleccionaron según la pregunta de negocio, el tipo de variable y la tarea cognitiva que debe realizar la audiencia. Se priorizaron gráficos que facilitan comparar magnitudes, ordenar categorías, observar tendencias y reconocer relaciones, evitando representaciones que agregaran complejidad sin aportar información relevante.

La selección sigue cuatro criterios:

- **Pertinencia:** el gráfico debe responder una pregunta concreta del análisis.
- **Comparabilidad:** las categorías deben poder ordenarse y compararse con facilidad.
- **Legibilidad:** los títulos, ejes, etiquetas y leyendas deben permitir una lectura rápida.
- **Accionabilidad:** el resultado debe ayudar a identificar una categoría, mercado o título que requiera revisión.

### 5.2 Tipos de gráficos utilizados

| Pregunta o necesidad | Representación seleccionada | Justificación |
| --- | --- | --- |
| ¿Cómo se distribuye el catálogo entre películas y series? | Gráfico de barras verticales | Permite comparar directamente cantidades discretas entre dos tipos de contenido. |
| ¿Cómo evolucionan los estrenos por año? | Gráfico de líneas con marcadores | Muestra el orden temporal y facilita detectar concentraciones o cambios entre años. |
| ¿Qué géneros concentran más contenidos? | Barras horizontales ordenadas | Los nombres de los géneros se leen mejor en horizontal y el orden facilita el ranking. |
| ¿Qué países concentran más títulos? | Barras horizontales ordenadas | Permite comparar países y mantener visibles nombres extensos sin rotar etiquetas. |
| ¿Qué idiomas tienen mayor presencia? | Barras horizontales | Facilita ordenar códigos y cantidades sin recurrir a una leyenda compleja. |
| ¿Qué géneros o países presentan mayor popularidad típica? | Barras horizontales con popularidad mediana | Permite comparar el desempeño típico de categorías con volumen mínimo suficiente. |
| ¿Qué títulos deben revisarse primero? | Ranking tabular o barras horizontales | Combina orden, nombre del título y métricas complementarias para apoyar la revisión. |
| ¿Cómo se relacionan popularidad y valoración? | Gráfico de dispersión | Permite observar simultáneamente dos variables cuantitativas y reconocer grupos o valores extremos. |
| ¿Qué películas tienen mayor retorno observado? | Barras horizontales con escala logarítmica | Ordena el retorno y reduce el efecto visual de diferencias extremas entre películas. |

No se utilizaron gráficos circulares como representación principal porque dificultan la comparación precisa entre muchas categorías. Tampoco se utilizaron mapas como recurso central, ya que el análisis disponible describe asociaciones de país, pero no incorpora una necesidad geográfica que requiera representar superficies o distancias espaciales.

### 5.3 Atributos visuales y percepción

La posición se utiliza como atributo principal para representar cantidades y valores comparables. En barras, la longitud sobre un eje común facilita identificar diferencias entre categorías. En líneas, la posición de los puntos permite seguir la evolución temporal. En dispersión, la posición horizontal y vertical representa simultáneamente dos métricas.

El color se utiliza como apoyo semántico y no como único mecanismo de codificación:

- Se emplean colores diferenciados para distinguir películas y series.
- Se utiliza una escala continua para reforzar valores bajos y altos de cantidad o desempeño.
- Se conserva una paleta coherente entre gráficos relacionados para facilitar la asociación visual.
- Los colores no reemplazan las etiquetas ni los ejes, de modo que la lectura no dependa exclusivamente de la percepción cromática.

El contraste se concentra en los elementos relevantes. Los títulos de las visualizaciones, los KPIs y los resultados priorizados reciben mayor jerarquía que los elementos secundarios. Las etiquetas y unidades se mantienen visibles para evitar que la audiencia tenga que inferir el significado de una escala.

### 5.4 Jerarquía y organización de la información

La interfaz organiza la información desde lo general hacia lo específico:

1. Los KPIs muestran el tamaño y la composición del segmento seleccionado.
2. Los gráficos de composición muestran dónde se concentra la oferta.
3. Las visualizaciones de oportunidades comparan popularidad típica por género y país.
4. Los rankings permiten revisar títulos concretos.
5. El bloque financiero se presenta al final y solo cuando existe información válida.

Esta jerarquía reduce la carga cognitiva porque evita presentar todos los análisis con el mismo nivel de importancia. La audiencia primero comprende qué está observando, luego identifica patrones y finalmente revisa posibles acciones.

### 5.5 Decisiones analíticas que mejoran la lectura

Se adoptaron decisiones específicas para aumentar la estabilidad y claridad de las representaciones:

- Se utiliza la mediana de popularidad en categorías para reducir la influencia de valores extremos.
- Los rankings de oportunidades exigen un mínimo de 25 contenidos por categoría.
- Los títulos priorizados para campañas deben contar con al menos 100 votos válidos.
- Las calificaciones iguales a cero no participan en el promedio válido.
- La información financiera se restringe a películas con presupuesto e ingresos positivos.
- El ROI se muestra en escala logarítmica para evitar que unos pocos valores extremos oculten el resto de la distribución.
- Los filtros actualizan de manera conjunta KPIs, gráficos, rankings y resultados financieros.

Estas decisiones conectan el diseño visual con la calidad de la evidencia. No se trata únicamente de mostrar gráficos atractivos, sino de evitar que la forma de representación exagere diferencias, oculte la falta de datos o presente como concluyente una señal que solo sirve para priorizar una revisión.

En conjunto, las decisiones de diseño buscan que la audiencia pueda pasar de una lectura descriptiva a una decisión de revisión sin perder el contexto metodológico de los datos.

---

## 6. Desarrollo de la narrativa visual

### 6.1 Propósito de la narrativa

La narrativa visual organiza los resultados para que la audiencia avance desde una pregunta amplia sobre el catálogo hacia decisiones concretas de adquisición y promoción. En lugar de presentar los gráficos como elementos aislados, la solución propone un recorrido progresivo: comprender el tamaño y la composición del catálogo, reconocer dónde se concentran los contenidos, identificar oportunidades y finalmente revisar títulos específicos.

El relato está dirigido principalmente a la Gerencia de Contenidos y Adquisición. Por ello, cada etapa combina una lectura descriptiva con una posible acción de negocio, manteniendo visibles las limitaciones de las métricas para evitar interpretaciones excesivas.

### 6.2 Secuencia narrativa

La historia se estructura en cuatro momentos:

#### Momento 1: ¿Qué contiene el catálogo?

La narrativa comienza dimensionando el catálogo seleccionado. Los KPIs muestran la cantidad total de contenidos, la distribución entre películas y series, la popularidad mediana y la valoración válida. Esta apertura establece el contexto antes de analizar categorías o títulos.

La audiencia puede modificar el segmento mediante filtros y observar cómo cambian los indicadores. De esta forma, la primera pregunta no es únicamente cuánto contenido existe, sino qué composición tiene el segmento que se desea analizar.

#### Momento 2: ¿Dónde se concentra la oferta?

La segunda etapa presenta la distribución por género, país e idioma. El objetivo es reconocer la estructura de la oferta y detectar concentraciones relevantes. Drama, Comedy y Animation aparecen como categorías con alta presencia, mientras que Estados Unidos concentra la mayor cantidad de asociaciones por país.

Esta etapa responde a una necesidad de planificación: identificar qué categorías y mercados ya tienen una presencia importante antes de proponer nuevas adquisiciones o estrategias de posicionamiento.

#### Momento 3: ¿Dónde existen oportunidades?

Después de describir el volumen, la narrativa incorpora la popularidad mediana por género y país. Esta comparación permite diferenciar las categorías con mayor presencia de aquellas que, aun teniendo menos contenidos, muestran una mayor popularidad típica.

El uso de un mínimo de contenidos por categoría evita que un grupo muy pequeño domine el resultado por unos pocos casos excepcionales. La lectura recomendada es identificar oportunidades para revisión, no declarar automáticamente que una categoría debe adquirirse o promocionarse.

#### Momento 4: ¿Qué títulos conviene revisar?

La última etapa baja desde las categorías hacia los contenidos concretos. Los rankings permiten ordenar títulos según popularidad, valoración o cantidad de votos. Para campañas promocionales se combinan popularidad y valoración, exigiendo un mínimo de votos válidos para aportar mayor estabilidad.

El bloque financiero se presenta como una lectura complementaria para películas con presupuesto e ingresos disponibles. El retorno observado ayuda a ordenar casos para revisión editorial o contractual, pero no sustituye un análisis financiero completo.

### 6.3 Mensaje central

El mensaje central de la narrativa es que StreamView puede pasar de una visión fragmentada del catálogo a una priorización informada mediante tres niveles de lectura:

1. **Volumen:** qué existe y cómo se distribuye.
2. **Desempeño relativo:** qué categorías y mercados muestran señales de visibilidad o valoración.
3. **Acción de revisión:** qué títulos conviene analizar con mayor detalle para adquisición, promoción o posicionamiento.

La narrativa evita presentar un único indicador como respuesta definitiva. La popularidad aporta una señal de visibilidad, la valoración aporta una señal de recepción y la cantidad de votos aporta contexto. La decisión final requiere complementar estas señales con objetivos de campaña, audiencia, derechos, presupuesto y evaluación editorial.

### 6.4 Recursos de comunicación

La solución utiliza los siguientes recursos para reforzar el storytelling:

- Encabezados que formulan preguntas de negocio.
- KPIs para entregar una síntesis inmediata.
- Gráficos ordenados para facilitar comparaciones.
- Mensajes de interpretación junto a los resultados principales.
- Filtros que permiten adaptar la historia a un tipo de contenido, género, país o periodo.
- Rankings que conectan las tendencias generales con títulos concretos.
- Advertencias metodológicas sobre popularidad, votos y disponibilidad financiera.

Estos recursos permiten que la audiencia explore el análisis sin perder el hilo conductor. La interacción no se utiliza como un fin en sí mismo, sino como una forma de responder preguntas específicas dentro de la misma historia.

### 6.5 Adaptación a la audiencia

Para la Gerencia de Contenidos y Adquisición, la narrativa prioriza categorías, mercados y títulos que requieren revisión. Para Marketing, el foco se desplaza hacia contenidos con una combinación favorable de popularidad y valoración. Para la Gerencia General, los KPIs y los hallazgos resumidos permiten obtener una lectura ejecutiva del catálogo. Para Producto y Data & Analytics, los filtros y la trazabilidad de las métricas permiten profundizar en segmentos particulares.

Así, una misma solución puede servir a distintos públicos sin perder coherencia: la estructura general permanece estable, mientras que cada área profundiza en las visualizaciones relacionadas con sus decisiones.

---

## 7. Diseño e implementación del dashboard interactivo

### 7.1 Descripción general

El producto principal es un dashboard interactivo desarrollado con Streamlit y Plotly, denominado **StreamView Analytics: Radar de adquisición de contenidos**. Su objetivo es permitir que la audiencia explore el catálogo integrado y priorice categorías o títulos para una revisión posterior.

La interfaz organiza la información según la narrativa definida: comienza con una lectura ejecutiva, continúa con la composición y las oportunidades del catálogo, y termina con rankings, campañas y finanzas. Todos los resultados se actualizan a partir del segmento seleccionado.

### 7.2 Filtros, segmentación y KPIs

La barra lateral permite seleccionar tipo de contenido, género, país, rango de años, métrica de ranking y cantidad de títulos a mostrar. Los filtros se aplican conjuntamente, de modo que la audiencia puede analizar, por ejemplo, series de un género y país específicos dentro de un periodo determinado. Si no existen registros para la combinación elegida, el sistema informa la situación en lugar de mostrar resultados ambiguos.

| Control | Opciones o función | Decisión que apoya |
| --- | --- | --- |
| Tipo | Todos, Movie o TV Show | Comparar el catálogo completo o separar películas y series. |
| Género | Lista de géneros disponibles | Analizar una categoría temática específica. |
| País | Lista de países asociados a los contenidos | Explorar mercados y procedencias concretas. |
| Año de estreno | Rango ajustable entre el año mínimo y máximo disponible | Concentrar el análisis en un periodo determinado. |
| Métrica del ranking | Popularidad, valoración o cantidad de votos | Cambiar el criterio de ordenamiento de los títulos. |
| Títulos a mostrar | Entre 5 y 20 resultados | Ajustar el nivel de detalle de los rankings. |

Para la lectura ejecutiva se presentan cinco KPIs:

- Total de contenidos filtrados.
- Cantidad de películas.
- Cantidad de series.
- Popularidad mediana.
- Valoración promedio válida.

La popularidad se resume mediante la mediana para reducir el efecto de valores extremos. La valoración promedio excluye valores iguales a cero y se presenta como no disponible cuando el segmento no contiene calificaciones válidas.

### 7.3 Composición y concentración del catálogo

El bloque inicial combina un gráfico de barras sobre la distribución entre películas y series con un gráfico de líneas sobre la evolución de los estrenos por año. Luego, tres rankings de barras horizontales muestran los principales géneros, países e idiomas.

Los conteos de género y país representan asociaciones, ya que un título puede pertenecer a varias categorías o tener más de un país asociado. Los idiomas se cuentan por título. Esta diferencia se informa en la interfaz para evitar comparaciones incorrectas entre magnitudes construidas de distinta forma.

### 7.4 Oportunidades, rankings y contenidos destacados

El dashboard compara la popularidad mediana por género y país para identificar oportunidades. Solo se incluyen categorías con al menos 25 contenidos, evitando que grupos pequeños dominen los resultados por unos pocos casos. El color de las barras representa el volumen asociado y la posición horizontal representa la popularidad típica.

También se presentan dos rankings de títulos: contenidos más populares y contenidos mejor calificados. El segundo exige una calificación mayor que cero y al menos 100 votos. La intersección entre ambos rankings permite construir un perfil de contenidos que destacan simultáneamente por visibilidad y valoración, mostrando sus géneros, países, idiomas, tipo dominante y año mediano de estreno.

### 7.5 Campañas promocionales y análisis financiero

El bloque de campañas entrega categorías y títulos candidatos para promoción. El puntaje combina en partes iguales el ranking relativo de popularidad y el ranking relativo de valoración:

$$
Prioridad = 0{,}5 \times ranking\ de\ popularidad + 0{,}5 \times ranking\ de\ valoración
$$

El resultado es una lista de candidatos para marketing, no una decisión automática de inversión. El bloque financiero se limita a películas con presupuesto e ingresos positivos, calcula `roi` como ingresos divididos por presupuesto y utiliza una escala logarítmica para representar diferencias amplias. Las series quedan excluidas por no contar con variables comparables.

### 7.6 Reproducibilidad y controles de interpretación

La aplicación carga el catálogo integrado, convierte las variables numéricas antes de calcular indicadores y distingue contenidos con valoración válida de películas con información financiera completa. También informa cuando un segmento no posee datos suficientes.

Las notas metodológicas recuerdan que:

- La popularidad es relativa y no representa reproducciones.
- Las categorías pequeñas pueden producir resultados inestables.
- El ROI no representa rentabilidad completa.
- Los rankings sirven para priorizar revisión editorial, contractual o promocional.
- Las decisiones finales requieren información adicional y criterio experto.

Así, la interacción facilita la exploración y la priorización informada sin presentar el dashboard como un sistema automático de decisión.

---

## 8. Evaluación crítica de la solución

### 8.1 Fortalezas

La solución desarrollada presenta las siguientes fortalezas:

- Integra películas y series en una estructura común, manteniendo las diferencias relevantes entre ambos tipos.
- Utiliza un catálogo limpio y dimensiones auxiliares para reducir errores de conteo en géneros y países.
- Organiza la información mediante una narrativa progresiva, desde los KPIs generales hasta los títulos prioritarios.
- Ofrece filtros que permiten adaptar el análisis a distintos segmentos y preguntas de negocio.
- Combina volumen, popularidad, valoración y votos en lugar de depender de una sola métrica.
- Incorpora umbrales y advertencias para reducir interpretaciones basadas en muestras pequeñas.
- Presenta el análisis financiero de forma separada y evita comparar directamente películas con series en variables que no son equivalentes.
- Mantiene una orientación práctica: los rankings sirven para iniciar una revisión editorial, contractual o promocional.

### 8.2 Limitaciones

La principal limitación es que las fuentes disponibles describen el catálogo, pero no contienen métricas directas de consumo o comportamiento de usuarios. Por lo tanto, la popularidad no puede interpretarse como reproducciones, retención, engagement ni conversión.

Además, la cobertura financiera es parcial y se concentra en películas con presupuesto e ingresos válidos. El `roi` utilizado corresponde a la razón entre ingresos y presupuesto, por lo que no representa rentabilidad completa al no considerar marketing, distribución, licencias u otros costos.

Las calificaciones dependen de la cantidad de votos y de la cobertura de la fuente. Aunque se exige un mínimo de votos para priorizar títulos, este criterio no elimina completamente los posibles sesgos de participación. Del mismo modo, las categorías con pocos contenidos pueden producir medianas inestables, incluso cuando cumplen el umbral mínimo.

Finalmente, la solución no incorpora todavía una evaluación formal con usuarios. No se cuenta con pruebas de tareas, encuestas de comprensión ni métricas de tiempo o error que permitan medir objetivamente la usabilidad del dashboard.

### 8.3 Oportunidades de mejora

Para fortalecer la solución se proponen las siguientes mejoras:

- Integrar datos de reproducciones, horas visualizadas, usuarios activos, retención y abandono.
- Incorporar costos de adquisición, marketing y distribución para reemplazar el retorno observado por una medida financiera más completa.
- Definir umbrales estadísticos o intervalos de confianza que complementen los mínimos de volumen y votos.
- Incorporar segmentación por mercado, perfil de usuario y periodo de consumo cuando existan esas variables.
- Agregar un registro de decisiones o comentarios para documentar por qué un título fue seleccionado para revisión.
- Realizar pruebas con usuarios de las áreas de Contenidos, Marketing y Dirección para evaluar comprensión, navegación y utilidad.
- Establecer un proceso periódico de actualización y control de calidad del catálogo.

En síntesis, el dashboard cumple su función como herramienta exploratoria y de priorización inicial. Su mayor valor está en consolidar información dispersa y convertirla en una conversación visual orientada al negocio. Para transformarlo en una herramienta de decisión operativa, será necesario complementar el catálogo con datos de uso, costos, objetivos comerciales y validación con sus usuarios finales.

---

## 9. Conclusiones y recomendaciones

### 9.1 Conclusiones

El proyecto permitió transformar dos fuentes independientes en una vista integrada del catálogo de StreamView Analytics, con una estructura común para películas y series. La preparación eliminó duplicados, normalizó variables y separó correctamente las dimensiones de género y país para evitar conteos incorrectos.

El análisis mostró que el catálogo contiene una cantidad equilibrada de películas y series, con una concentración importante en géneros como Drama, Comedy y Animation. También se observó una fuerte presencia de contenidos asociados a Estados Unidos y una participación relevante de estrenos recientes, especialmente entre 2020 y 2024.

La exploración confirmó que popularidad, valoración y cantidad de votos representan señales diferentes. Por esta razón, la priorización combina más de una métrica y aplica condiciones mínimas de volumen y votos. Esto permite orientar la revisión de categorías y títulos sin afirmar que una sola variable explique el desempeño completo de un contenido.

El dashboard responde al problema de negocio al reunir KPIs, filtros, comparaciones, rankings y análisis financiero en un recorrido visual único. La solución facilita pasar desde una visión general del catálogo hacia oportunidades específicas para adquisición, posicionamiento y promoción.

Sin embargo, los resultados deben interpretarse como una primera aproximación analítica. La ausencia de datos directos de consumo, retención, costos y comportamiento de usuarios impide estimar por completo el impacto comercial de una decisión. El dashboard entrega evidencia para priorizar conversaciones y revisiones, pero no reemplaza el criterio experto de las áreas responsables.

### 9.2 Recomendaciones para la organización

#### Adquisición y gestión de contenidos

- Utilizar los rankings de género y país como punto de partida para identificar categorías y mercados que requieran una revisión más profunda.
- Comparar siempre volumen de contenidos con popularidad mediana y valoración, evitando priorizar una categoría solo por tener muchos títulos.
- Revisar los contenidos destacados considerando derechos, costos, disponibilidad territorial, audiencia objetivo y coherencia con la estrategia de catálogo.
- Utilizar el análisis financiero únicamente como señal inicial para películas con datos válidos, complementándolo con costos y condiciones contractuales reales.

#### Marketing y posicionamiento

- Priorizar para revisión los títulos que combinan visibilidad relativa, valoración y una cantidad suficiente de votos.
- Utilizar los filtros para construir segmentos específicos por tipo, género, país y periodo antes de diseñar una campaña.
- Complementar los candidatos generados por el dashboard con objetivos de comunicación, público objetivo, presupuesto y derechos de uso.
- Medir posteriormente el resultado de las campañas mediante reproducciones, horas visualizadas, interacción y conversión.

#### Datos y gestión analítica

- Integrar métricas de consumo, usuarios activos, retención, abandono y horas visualizadas.
- Mantener un proceso periódico de actualización, validación de tipos, control de duplicados y revisión de valores faltantes.
- Documentar la procedencia, fecha de actualización y licencia de cada fuente de datos.
- Incorporar controles de calidad que alerten cuando cambie la cobertura de variables críticas o disminuya la cantidad de registros válidos.

#### Evolución de la solución

- Realizar pruebas de usabilidad con representantes de Contenidos, Marketing y Dirección.
- Registrar las decisiones tomadas a partir de cada análisis para evaluar si las prioridades visualizadas se convierten en acciones efectivas.
- Incorporar segmentación por mercado y perfil de usuario cuando se disponga de esa información.
- Reemplazar progresivamente el retorno observado por indicadores financieros que incluyan costos relevantes.

### 9.3 Cierre ejecutivo

La solución propuesta entrega a StreamView Analytics una base visual para comprender la composición de su catálogo y orientar la priorización de contenidos. Su principal aporte es convertir información dispersa en una lectura clara, interactiva y conectada con decisiones de negocio.

El siguiente paso recomendado es utilizar el dashboard como instrumento de exploración dentro de un proceso de decisión más amplio, integrando datos de consumo, costos, objetivos comerciales y validación de usuarios. De esta manera, la herramienta podrá evolucionar desde una priorización inicial hacia un sistema de apoyo continuo para la adquisición, promoción y gestión estratégica del catálogo.
