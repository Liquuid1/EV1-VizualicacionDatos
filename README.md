# StreamView Analytics

Análisis del catálogo audiovisual para apoyar revisión editorial, adquisición y promoción. Python prepara los datos y genera evidencia estática; Power BI es la herramienta de construcción del informe interactivo.

## Estado de la entrega

Están preparados los datos, código reproducible, notebook de exploración, gráficos estáticos, indicadores DAX, guía de construcción e informe ejecutivo en Markdown. Quedan pendientes el archivo Power BI, sus comprobaciones y la evidencia que depende de su implementación. El informe es un borrador hasta completar esas partes.

Consultar **[PENDIENTES_DASHBOARD.md](PENDIENTES_DASHBOARD.md)** para localizar todas las correcciones de cierre. La presentación y su ensayo se preparan fuera de este repositorio; deben incluirse en el paquete final de entrega.

## Contenido del proyecto

| Carpeta o archivo | Contenido |
| --- | --- |
| `data/raw/` | Dos CSV originales entregados por el profesor. No se modifican. |
| `data/processed/` | Catálogo preparado, dimensiones, asociaciones, diagnósticos, excepciones, referencias de KPIs y resúmenes exploratorios. |
| `src/` | `main.py`: limpieza e integración. `referencias_kpis.py`: indicadores de control para once escenarios. `analisis_catalogo.py`: resúmenes y gráficos estáticos. |
| `notebooks/` | `analisis_catalogo.ipynb`: ejecución del proceso, inspección de calidad, exploración y visualización de resultados. |
| `dashboard/` | `medidas.dax`: 23 medidas para crear en Power BI. `tema_streamview.json`: tema visual. Aquí se guardará `StreamView.pbix`. |
| `images/` | Seis gráficos estáticos generados por Python. Aquí se añadirán capturas de Power BI. |
| `docs/` | Informe ejecutivo y documentación de limpieza, preparación, modelo e implementación. |
| `requirements.txt` | Dependencias para ejecutar código y notebook. |
| `PENDIENTES_DASHBOARD.md` | Lista de cierre y ubicación de los marcadores que debe completar el equipo. |

`.venv/` es un entorno de desarrollo local, no un entregable. También deben excluirse `.git/`, caches y checkpoints del paquete que se envíe al docente.

## Ejecución reproducible

Requiere Python 3.10 o superior. Desde la raíz del proyecto:

```bash
python -m venv .venv
```

Activar el entorno:

```bash
# Linux / macOS
source .venv/bin/activate
```

```powershell
# Windows PowerShell
.venv\Scripts\Activate.ps1
```

Instalar dependencias y generar todas las salidas:

```bash
python -m pip install -r requirements.txt
python src/main.py
python src/referencias_kpis.py
python src/analisis_catalogo.py
```

Los scripts encuentran el proyecto a partir de su ubicación, por lo que no requieren modificar rutas en el código. `main.py` permite `--data-dir` y `--output-dir` para una ejecución alternativa; los otros dos scripts utilizan las rutas estándar del proyecto. Las salidas derivadas se regeneran y los originales permanecen intactos.

Para explorar en Jupyter:

```bash
jupyter lab notebooks/analisis_catalogo.ipynb
```

Ejecutar las celdas en orden. El notebook utiliza los mismos scripts y datos que el informe; no contiene una aplicación de dashboard adicional.

## Construcción de Power BI

Los CSV ya están generados: la persona que construye el dashboard puede empezar sin ejecutar Python.

1. Seguir [la guía de construcción](docs/guia_construccion_powerbi.md).
2. Importar únicamente `catalogo.csv`, `dim_generos.csv`, `contenido_genero.csv`, `dim_paises.csv`, `contenido_pais.csv` y `dim_anio_estreno.csv` desde `data/processed/`.
3. Configurar las cinco relaciones de [modelo_indicadores.md](docs/modelo_indicadores.md) y crear las medidas de `dashboard/medidas.dax`.
4. Importar el tema y construir Resumen, Catálogo, Popularidad y valoración, y Finanzas de películas.
5. Guardar como `dashboard/StreamView.pbix` y comparar resultados con `referencia_kpis.csv` y las selecciones de `reference_cases.json`.

Los CSV usan UTF-8 con BOM, delimitador coma y punto decimal. Importar claves como texto y banderas como valores lógicos; convertir decimales con configuración regional Inglés (Estados Unidos). Registrar la ruta o parámetro de datos del equipo de construcción y comprobar actualización en el PC de entrega.

**Archivo PBIX y ruta de actualización:** pendientes de implementación. Sustituir esta línea por la ubicación final y los pasos para actualizar fuentes al trasladar el proyecto.

## Documentación

- [Informe ejecutivo](docs/informe_ejecutivo.md): diez secciones, análisis y recomendaciones, con marcadores `PB01`–`PB16` para la evidencia pendiente.
- [Criterios de limpieza](docs/criterios_limpieza.md): identidad, duplicados, nulos y restricciones semánticas.
- [Preparación de datos](docs/preparacion_datos.md): ejecución, tipos y descripción de derivados.
- [Modelo e indicadores](docs/modelo_indicadores.md): relaciones, medidas, filtros y reglas de interpretación.
- [Guía Power BI](docs/guia_construccion_powerbi.md): campos de cada visual, navegación, formato y comprobaciones.

Los diagnósticos, excepciones, resúmenes y referencias de KPIs sirven como respaldo; no se cargan como nuevas tablas de hechos de Power BI. Los archivos originales mantienen sus nombres para conservar trazabilidad.

## Resultados de control y alcance

La base contiene 31.991 contenidos: 16.000 películas y 15.991 series. La clave es `content_id`, que combina tipo e identificador. Las asociaciones multivaluadas no deben sumarse como si fueran títulos distintos. Hay 3.540 películas con presupuesto e ingresos positivos y 55 presupuestos marcados para revisión.

La popularidad es un índice relativo; no son reproducciones. Las valoraciones cero se excluyen del promedio válido. La razón ingresos/presupuesto no es rentabilidad de la plataforma. No hay clasificación etaria utilizable ni datos para medir retención o comportamiento individual de usuarios.

## Cierre y entrega

Una vez validado el dashboard, completar la lista de pendientes, incorporar capturas y convertir `docs/informe_ejecutivo.md` a `docs/exportaciones/informe_ejecutivo.pdf`. Exportar también un respaldo estático del dashboard, comprobando legibilidad. El PDF no reemplaza la interactividad del PBIX.

Incluir la presentación o resumen ejecutivo preparado por el equipo en `docs/exportaciones/`. La carpeta de exportaciones se crea cuando existan esos productos. Entregar datos, scripts, notebook, gráficos, documentación, PDF, PBIX y presentación. No incluir el entorno virtual ni archivos de control local.
