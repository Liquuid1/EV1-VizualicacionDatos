# StreamView Analytics

Análisis del catálogo audiovisual para apoyar revisión editorial, adquisición y promoción. Python prepara los datos y genera evidencia estática; Power BI es la herramienta de construcción del informe interactivo.

## Estado de la entrega

El proyecto cuenta con datos preparados, código reproducible en Python, notebook de exploración, gráficos estáticos, medidas DAX y un dashboard interactivo implementado en Power BI con cuatro páginas: Resumen del catálogo, Exploración del catálogo, Popularidad y valoración, y Finanzas de películas.

Se realizaron pruebas de funcionamiento de filtros individuales y combinados, actualización de indicadores y navegación entre páginas. El informe ejecutivo se encuentra finalizado y exportado a PDF, incorporando capturas del dashboard, análisis, conclusiones y recomendaciones. La presentación y su preparación se realizan fuera del repositorio y deben incorporarse al paquete final de entrega.

## Contenido del proyecto

| Carpeta o archivo | Contenido |
| --- | --- |
| `data/raw/` | Dos CSV originales entregados por el profesor. No se modifican. |
| `data/processed/` | Catálogo preparado, dimensiones, asociaciones, diagnósticos, excepciones, referencias de KPIs y resúmenes exploratorios. |
| `src/` | `main.py`: limpieza e integración. `referencias_kpis.py`: indicadores de control para once escenarios. `analisis_catalogo.py`: resúmenes y gráficos estáticos. |
| `notebooks/` | `analisis_catalogo.ipynb`: ejecución del proceso, inspección de calidad, exploración y visualización de resultados. |
| `dashboard/` | `medidas.dax`: 23 medidas DAX. `tema_streamview.json`: tema visual. `StreamView.pbix`:dashboard interactivo implementado en Power BI.. |
| `images/` | Gráficos estáticos generados en Python y capturas de las visualizaciones y páginas implementadas en Power BI. |
| `docs/` | Informe ejecutivo finalizado, documentación de limpieza, preparación, modelo e implementación, y archivos de respaldo. |
| `requirements.txt` | Dependencias para ejecutar código y notebook. |


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

## Implementación y reproducción de Power BI

El dashboard fue implementado en Power BI utilizando los seis archivos CSV preparados en Python. Las siguientes instrucciones permiten reproducir su configuración o actualizar el proyecto en otro equipo.

1. Seguir [la guía de construcción](docs/guia_construccion_powerbi.md).
2. Importar únicamente `catalogo.csv`, `dim_generos.csv`, `contenido_genero.csv`, `dim_paises.csv`, `contenido_pais.csv` y `dim_anio_estreno.csv` desde `data/processed/`.
3. Configurar las cinco relaciones de [modelo_indicadores.md](docs/modelo_indicadores.md) y crear las medidas de `dashboard/medidas.dax`.
4. Importar el tema y construir Resumen, Catálogo, Popularidad y valoración, y Finanzas de películas.
5. Guardar como `dashboard/StreamView.pbix` y comparar resultados con `referencia_kpis.csv` y las selecciones de `reference_cases.json`.

Los CSV usan UTF-8 con BOM, delimitador coma y punto decimal. Importar claves como texto y banderas como valores lógicos; convertir decimales con configuración regional Inglés (Estados Unidos). Registrar la ruta o parámetro de datos del equipo de construcción y comprobar actualización en el PC de entrega.

**Archivo PBIX y ruta de actualización:** El dashboard se guarda en `dashboard/StreamView.pbix`. Para actualizar los datos en otro equipo, se deben comprobar las rutas de origen de los seis archivos CSV ubicados en `data/processed/`, ajustar sus conexiones en Power BI si corresponde y ejecutar la actualización de datos.

## Documentación

- [Informe ejecutivo](docs/informe_ejecutivo.md): documento final de diez secciones que incluye análisis exploratorio, evidencias del dashboard implementado en Power BI, evaluación crítica, conclusiones y recomendaciones. 
- [Informe ejecutivo en PDF](docs\informe_ejecutivo_stream_view.pdf)
- [Informe ejecutivo en PDF](docs\StreamView_Dashboard.pdf): versión estática de las cuatro páginas del dashboard implementado en Power BI.
- [Criterios de limpieza](docs/criterios_limpieza.md): identidad, duplicados, nulos y restricciones semánticas.
- [Preparación de datos](docs/preparacion_datos.md): ejecución, tipos y descripción de derivados.
- [Modelo e indicadores](docs/modelo_indicadores.md): relaciones, medidas, filtros y reglas de interpretación.
- [Guía Power BI](docs/guia_construccion_powerbi.md): campos de cada visual, navegación, formato y comprobaciones.

Los diagnósticos, excepciones, resúmenes y referencias de KPIs sirven como respaldo; no se cargan como nuevas tablas de hechos de Power BI. Los archivos originales mantienen sus nombres para conservar trazabilidad.

## Resultados de control y alcance

La base contiene 31.991 contenidos: 16.000 películas y 15.991 series. La clave es `content_id`, que combina tipo e identificador. Las asociaciones multivaluadas no deben sumarse como si fueran títulos distintos. Hay 3.540 películas con presupuesto e ingresos positivos y 55 presupuestos marcados para revisión.

La popularidad es un índice relativo; no son reproducciones. Las valoraciones cero se excluyen del promedio válido. La razón ingresos/presupuesto no es rentabilidad de la plataforma. No hay clasificación etaria utilizable ni datos para medir retención o comportamiento individual de usuarios.

## Cierre y entrega

El proyecto cuenta con un dashboard interactivo implementado en Power BI y un informe ejecutivo finalizado, con análisis, visualizaciones, evidencias y conclusiones. Se realizaron pruebas de navegación, filtros individuales y combinados, y actualización de indicadores.

El paquete de entrega debe incluir los datos originales y procesados, scripts de Python, notebook de exploración, archivo `dashboard/StreamView.pbix`, medidas DAX, gráficos, documentación y el informe ejecutivo en PDF.

La presentación correspondiente a EP4 se prepara por separado y debe incorporarse cuando esté finalizada. El PDF del informe permite revisar los resultados, pero no reemplaza la interactividad del archivo PBIX.

Antes de entregar, se debe comprobar que los archivos puedan abrirse correctamente y excluir carpetas de desarrollo local como `.venv/`, `.git/`, cachés y checkpoints.