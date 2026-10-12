# Pendientes de cierre del dashboard y del informe

Este archivo reúne los lugares que se deben corregir cuando esté construido y validado Power BI. No declara tareas completadas. Marcar cada casilla únicamente después de verificar la evidencia.

## Informe ejecutivo

Archivo: `docs/informe_ejecutivo.md`. Buscar el código de cada marcador. Los gráficos estáticos de Python ya están incluidos como evidencia exploratoria; las capturas y pruebas de Power BI se agregan al completar la implementación.

- [ ] **PB01:** Completar este resumen con el estado real del dashboard: páginas efectivamente implementadas, resultado de la validación y una conclusión breve sobre su utilidad comprobada. Hasta entonces, conservar la expresión «el diseño propone».

- [ ] **PB02:** Una vez terminada y comprobada la solución, actualizar el objetivo y la descripción del alcance para reflejar su implementación efectiva.

- [ ] **PB03:** Insertar Figura 1: barras de películas y series con cantidades y alcance. Registrar archivo de imagen y pie: «Fuente: CSV del caso, preparación StreamView en Python y visualización en Power BI». Comprobar concordancia con la tabla anterior.

- [ ] **PB04:** Insertar Figura 2: comparación por género y país, y Figura 3: treemap de idiomas. Identificar Top N, nulos excluidos y filtros utilizados. Añadir pies que adviertan que las categorías de género y país no son aditivas.

- [ ] **PB05:** Insertar Figura 4: línea «Contenidos por año de estreno», con eje 2010–2025. Evitar interpretar la reducción de nueve registros como caída del negocio.

- [ ] **PB06:** Insertar Figura 5: popularidad mediana por género, con tamaño de muestra. Insertar Figura 6: dispersión de popularidad y valoración. Describir la relación solo después de revisar el gráfico final y su población; no afirmar causalidad ni una correlación estadística no calculada. Añadir ranking final de candidatos con filtros, criterio y votos visibles.

- [ ] **PB07:** Insertar Figura 7: dispersión de presupuesto e ingresos y tabla de razones por título, con alertas. Confirmar cobertura general de 22,1 % y que la página no filtre globalmente solo películas válidas, lo que falsearía el denominador de cobertura. Documentar la selección y la unidad sin agregar símbolo monetario.

- [ ] **PB08:** Actualizar esta tabla con los gráficos realmente utilizados. Justificar cualquier sustitución, agregar evidencia de legibilidad y confirmar que etiquetas, leyendas y colores se mantengan consistentes en el informe y exportaciones.

- [ ] **PB09:** Seleccionar un ejemplo real de exploración que conecte filtros, visualizaciones y una recomendación concreta. Registrar selección, cifras y título elegido. No escribir una acción comercial definitiva sin evidencia suficiente.

- [ ] **PB10:** Registrar nombre y versión del archivo PBIX, versión de Power BI utilizada, fecha de actualización y ruta o parámetro de fuentes. Insertar captura del modelo y confirmar cardinalidades, direcciones, tipos y ausencia de relaciones automáticas adicionales. Registrar ajustes reales respecto del diseño.

- [ ] **PB11:** Insertar capturas de las cuatro páginas implementadas. Describir qué filtros se sincronizan, qué interacción ocurre al seleccionar una barra, cómo se navega y cómo se restablece el estado. Confirmar que los segmentos vacíos muestran conteos cero y métricas sin datos, y que no existen filtros ocultos que alteren resultados.

- [ ] **PB12:** Comparar los once escenarios de `referencia_kpis.csv` con el PBIX. Añadir tabla de esperado/obtenido/resultado, evidencia de los filtros usados y explicación de diferencias. Registrar pruebas de navegación, filtros combinados, ausencia de datos y selección de series en Finanzas. Indicar quién verificó y en qué fecha.

- [ ] **PB13:** Registrar exportaciones finales, calidad de capturas, legibilidad del PDF y prueba de apertura y actualización del proyecto en el PC de entrega. Comprobar que los productos estén completos y documentados; no declarar publicación en línea si no se realizó.

- [ ] **PB14:** Realizar una revisión de uso con ambos integrantes: localizar un segmento, comparar métricas, identificar una alerta y restablecer filtros. Registrar dificultades observadas, claridad de títulos, legibilidad, consistencia y comportamiento de navegación. Describir fortalezas y limitaciones reales del dashboard, evitando calificativos sin evidencia.

- [ ] **PB15:** Documentar al menos las mejoras que resulten necesarias, el problema que resuelven y su estado. Si se aplicó un cambio, incluir antes/después cuando aporte evidencia. Si no se implementó, identificarlo como mejora futura, no como funcionalidad existente.

- [ ] **PB16:** Añadir la conclusión final sobre el dashboard efectivamente construido, su utilidad demostrada y recomendaciones específicas derivadas del recorrido validado. Actualizar el resumen ejecutivo y retirar todos los marcadores de edición al finalizar.

## Otros archivos y productos que deben completarse

- [ ] **`dashboard/StreamView.pbix`:** crear, guardar y verificar el informe de cuatro páginas con modelo, medidas, navegación y segmentadores.
- [ ] **`docs/modelo_indicadores.md`:** registrar diferencias respecto del modelo propuesto y resultado real de validación; retirar la frase de ejecución pendiente solo después de ejecutar las medidas.
- [ ] **`dashboard/medidas.dax`:** reflejar cualquier ajuste realizado en Power BI para que fórmulas y archivo entregado coincidan.
- [ ] **`docs/guia_construccion_powerbi.md`:** actualizar nombres de páginas, visuales, campos, interacciones y exportaciones si la implementación difiere de la guía. Retirar la advertencia de que no existe PBIX solo cuando exista.
- [ ] **`README.md`, Estado de la entrega:** sustituir el estado de borrador por el estado validado y enlazar el PBIX y el PDF.
- [ ] **`README.md`, Archivo PBIX y ruta de actualización:** registrar ubicación o parámetro de datos y pasos para trasladar y actualizar el informe en otro PC.
- [ ] **`images/`:** agregar capturas con nombres descriptivos; comprobar que las rutas de imágenes del informe sean válidas.
- [ ] **`docs/exportaciones/informe_ejecutivo.pdf`:** convertir el informe completo a PDF y revisar imágenes, tablas, cortes de página y legibilidad.
- [ ] **`docs/exportaciones/dashboard.pdf`:** exportar las páginas finales como respaldo estático y registrar filtros utilizados.
- [ ] **`docs/exportaciones/`:** incorporar la presentación/resumen ejecutivo que el equipo prepara fuera del repositorio y comprobar coherencia con las cifras finales.

## Comprobaciones finales

- [ ] Comparar los once escenarios de `data/processed/referencia_kpis.csv` usando las selecciones de `reference_cases.json`. Registrar evidencia y diferencias en el informe.
- [ ] Confirmar que seleccionar series no devuelve métricas financieras, y que cobertura general de películas es 22,1 %.
- [ ] Comprobar filtros de género y país por intersección, multiselección por alternativas y conteos distintos de `content_id`.
- [ ] Probar sincronización, navegación, limpieza y estados vacíos. Revisar legibilidad y consistencia visual.
- [ ] Actualizar conclusiones y resumen ejecutivo con resultados comprobados; conservar limitaciones de los datos.
- [ ] Retirar del informe los dieciséis bloques de edición, la instrucción inicial y el anexo de edición cuando sus tareas estén resueltas.
- [ ] Confirmar nombres de integrantes y fecha final. No inventar fecha de entrega ni declarar publicación en línea si no ocurrió.
- [ ] Revisar que no queden rutas personales, marcadores o afirmaciones de pruebas no realizadas en los productos finales.
- [ ] Crear el paquete de entrega excluyendo `.git/`, `.venv/`, caches y checkpoints. Este archivo puede conservarse como registro interno o retirarse del paquete si ya no hay pendientes.
