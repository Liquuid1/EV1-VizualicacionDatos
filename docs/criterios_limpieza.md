# Diagnóstico y criterios de limpieza

Auditoría realizada el 12/10/2026 sobre los dos CSV originales entregados por el profesor. Los archivos fuente se conservan sin modificaciones.

## Alcance

El proyecto estudia composición, popularidad, valoración y señales financieras del catálogo. No hay datos de usuarios, reproducciones, suscripciones ni costos de licencias. No se calcularán retención, engagement de usuarios ni rentabilidad de StreamView. Popularidad y votos no sustituyen métricas de consumo.

## Identificación y duplicados

| Comprobación | Resultado |
| --- | ---: |
| Filas originales de películas | 16.000 |
| Filas originales de series | 16.000 |
| Identificadores repetidos dentro de películas | 0 |
| Filas excedentes por identificador dentro de series | 9 |
| Identificadores presentes en ambas fuentes | 397 |
| Duplicados exactos en cada fuente | 0 |
| Identificadores ausentes | 0 |

Deduplicar únicamente por `show_id` después de concatenar las fuentes descartaría 397 series cuyos identificadores coinciden con películas distintas, además de las 9 repeticiones internas. Por ejemplo, el identificador 38234 corresponde a la película «Undisputed III: Redemption» y a la serie «Lives of Omission».

**Decisión:** preservar `show_id` y crear `content_id` combinando `type` y `show_id`. Usar esta clave en todas las relaciones y conteos distintos de StreamView. El catálogo esperado tendrá **31.991 títulos: 16.000 películas y 15.991 series**, tras resolver las repeticiones internas.

Los 9 grupos repetidos de series solo difieren en `popularity`. No existe fecha de actualización que permita determinar qué observación es más reciente. Se conservará la primera fila según el orden del archivo fuente, como regla determinista de selección, sin afirmar que sea la más reciente. Se exportarán todas las filas de esos grupos como evidencia. No se sumará ni promediará su popularidad.

## Semántica y disponibilidad

| Variable | Evidencia en fuentes originales | Decisión StreamView |
| --- | --- | --- |
| `rating` | Coincide numéricamente con `vote_average` en las 32.000 filas. | Conservar en origen; excluir como clasificación etaria y evitar duplicarla en el modelo analítico. No hay clasificación etaria utilizable. |
| `date_added` | Su año coincide con `release_year` en las 32.000 filas. | Conservar y señalar la ambigüedad. Priorizar tendencias por año de estreno; no concluir crecimiento real de la plataforma a partir de esta fecha. |
| `duration` de películas | Ausente en las 16.000 películas. | No estimar minutos ni comparar duración con temporadas de series. |
| `vote_average` | Valores entre 0 y 10. | Promedio válido solo con valores mayores que cero; mostrar cobertura. Rankings de valoración con mínimo de 100 votos, criterio analítico del equipo. |
| `popularity` | Valores entre 2,323 y 6.421,923. | Índice relativo; usar mediana para comparar categorías. No representa reproducciones. |
| `release_year` | Rango 2010–2025. | Mostrar ese alcance temporal en los productos. |
| `budget`, `revenue` | Solo películas; 3.540 tienen ambas métricas positivas. | Valores no positivos pasan a nulo en derivados. No imputar ni aplicar a series. |

## Anomalías financieras

Hay **55 películas con presupuesto positivo inferior a 1.000**, incluyendo valores de 1, 3 y 5. No se puede confirmar su unidad o corregirlos con los datos disponibles.

**Decisión:** conservar los valores positivos y crear una bandera de revisión para presupuestos menores a 1.000. El umbral es una alerta analítica provisional, no prueba de error ni regla del profesor. Exportar los registros señalados y permitir distinguirlos en el dashboard. Mostrar cobertura y explicar el efecto de estos registros sobre los rankings. No presentar los retornos extremos como recomendaciones de inversión.

La razón `revenue / budget` se nombrará **«Ingresos / presupuesto (veces)»**. Puede mencionarse como ROI aproximado del caso, pero no equivale a utilidad ni rentabilidad de la plataforma. Los agregados se calcularán sobre una misma población válida. La razón agregada será suma de ingresos dividida por suma de presupuestos; no se confundirá con el promedio de razones individuales. La moneda no se asumirá sin documentación.

## Valores faltantes y categorías

Conservar nulos reales en métricas y fechas. En categorías se puede usar «Sin información» para visualización, conservando trazabilidad. No imputar directores, reparto, países ni géneros. Los códigos de idioma permanecen disponibles y cualquier etiqueta será una transformación documentada.

Separar géneros y países en tablas de asociación, con pares únicos `content_id`–categoría. Un título puede aparecer en varias categorías, por lo que la suma de categorías puede superar el total de títulos. No crear una expansión conjunta de países y géneros que multiplique métricas financieras.

## Criterios de aceptación de la preparación

- Fuentes originales intactas y salidas separadas en `data/processed/`.
- 31.991 claves compuestas únicas y no nulas, con selección de duplicados documentada.
- Tablas auxiliares con claves existentes y asociaciones sin duplicados.
- Métricas financieras disponibles exclusivamente para películas con valores positivos.
- Reporte de calidad y archivos de excepciones generados por Python.
- Cifras del informe calculadas sobre el catálogo preparado.

## Implementación

El script `src/main.py` aplica estos criterios y exporta catálogo, dimensiones, asociaciones, diagnóstico y excepciones para Power BI. El informe utiliza las cifras de esa base.
