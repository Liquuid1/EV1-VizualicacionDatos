# Preparación reproducible de datos

## Ejecución

Requisitos: Python 3.10 o superior y pandas. Desde la raíz del proyecto:

```bash
python -m pip install -r requirements.txt
python src/main.py
```

Opcionalmente se pueden indicar carpetas distintas:

```bash
python src/main.py --data-dir /ruta/datos --output-dir /ruta/salidas
```

Las fuentes se encuentran en `data/raw/` y deben mantener los nombres originales. El script valida tipos, claves, fechas, métricas, conflictos en duplicados y referencias antes de exportar. Una condición inválida detiene la ejecución con un error. Ante un fallo no se deben usar derivados antiguos como si se hubieran actualizado.

No se modifican las fuentes originales de `data/raw/`. Cada ejecución correcta regenera las salidas de StreamView. Las huellas SHA-256 en el resumen permiten identificar exactamente qué fuentes se utilizaron.

## Archivos generados en `data/processed/`

| Archivo | Contenido y uso |
| --- | --- |
| `catalogo.csv` | Una fila por contenido. Tabla principal de Power BI. |
| `dim_generos.csv` | Identificador entero y nombre de cada género. |
| `contenido_genero.csv` | Pares únicos de contenido y género. |
| `dim_paises.csv` | Identificador entero y nombre de cada país. |
| `contenido_pais.csv` | Pares únicos de contenido y país. |
| `dim_anio_estreno.csv` | Años presentes en los datos; no es un calendario diario. |
| `calidad_columnas.csv` | Tipo, cantidad y porcentaje de nulos por columna del catálogo. |
| `duplicados_series.csv` | Las 18 filas de los 9 grupos repetidos; `selected` indica qué fila se conservó. |
| `ids_compartidos_entre_tipos.csv` | Evidencia de identificadores compartidos, que se conservan como contenidos distintos. |
| `presupuestos_revision.csv` | Películas con presupuesto positivo menor a 1.000, para revisión y transparencia. |
| `resumen_calidad.json` | Conteos de control, parámetros y huellas de las fuentes. |

Los archivos de diagnóstico no deben sumarse a la tabla principal. El catálogo ya incluye los registros seleccionados y las banderas de revisión.

## Columnas principales y derivadas

| Columna | Tipo de importación | Significado |
| --- | --- | --- |
| `content_id` | Texto | Clave única, prefijo `movie:` o `tv:` seguido del identificador original. |
| `show_id` | Texto | Identificador original, no único entre tipos. No usar como clave de relación. |
| `type`, `title` y atributos descriptivos | Texto | Metadatos del contenido. Los nulos se conservan. |
| `source_file`, `source_row` | Texto / entero | Archivo y número de línea lógica, contando cabecera como fila 1, para trazabilidad. |
| `release_year`, `date_added_year`, `vote_count` | Entero | Año de estreno, año de fecha declarada y votos. |
| `date_added` | Fecha | Fecha declarada en fuente, con semántica pendiente de verificar. |
| `popularity`, `vote_average` | Decimal | Índice relativo y calificación en escala 0–10. |
| `budget`, `revenue` | Decimal | Valores positivos de películas, en unidad monetaria no documentada. |
| `has_valid_rating` | Lógico | Calificación mayor que cero. |
| `rating_rank_eligible` | Lógico | Calificación válida y al menos 100 votos. |
| `has_valid_financials` | Lógico | Película con presupuesto e ingresos positivos. |
| `budget_review_required` | Lógico | Presupuesto positivo menor a 1.000; alerta provisional, no exclusión automática. |
| `revenue_budget_ratio` | Decimal | Ingresos divididos por presupuesto, solo con ambas métricas válidas. |

`rating` se excluye del catálogo derivado porque replica `vote_average`; permanece en las fuentes y en la evidencia de duplicados. La ausencia de clasificación etaria no se sustituye con calificaciones.

## Importación en Power BI

1. Importar las seis tablas analíticas mediante Texto/CSV desde `data/processed/`.
2. Seleccionar UTF-8 y delimitador coma. Los archivos incluyen BOM para facilitar lectura de caracteres acentuados.
3. Confirmar las claves como texto y las banderas como valores lógicos. Los identificadores de dimensiones y años son enteros.
4. Convertir decimales usando configuración regional **Inglés (Estados Unidos)**, ya que el separador decimal exportado es punto. Las fechas utilizan `AAAA-MM-DD`.
5. Mantener campos vacíos como nulos. Las dimensiones representan categorías ausentes mediante «Sin información».
6. Configurar una ruta de datos en el equipo donde se construya el dashboard y documentarla. No asumir que las rutas locales del equipo original existirán en otro PC.

Consultar `docs/modelo_indicadores.md` para relaciones y medidas DAX. No unir simultáneamente las tablas de asociación de países y géneros al catálogo como una tabla plana: multiplicaría filas y métricas. Los conteos generales deben utilizar claves distintas de contenido.

## Resultado verificado con las fuentes actuales

- 32.000 filas originales y 31.991 contenidos finales.
- 16.000 películas y 15.991 series.
- 9 filas repetidas descartadas dentro de series; 397 identificadores compartidos conservados entre tipos.
- 66.967 asociaciones de género y 39.889 de país, incluyendo «Sin información».
- 27.427 contenidos con valoración mayor que cero.
- 3.540 películas con presupuesto e ingresos positivos.
- 55 películas con alerta de presupuesto.
- Años de estreno: 2010–2025.

Las asociaciones incluyen ausencias etiquetadas y no se deben comparar directamente con conteos que excluyan esas ausencias.
