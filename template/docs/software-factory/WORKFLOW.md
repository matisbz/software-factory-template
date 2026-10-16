# Trabajo con la fábrica

Pide un resultado concreto al orquestador. Ejemplo:

> Añade recuperación de contraseña con los criterios del contexto. Usa
> solution_designer para concretar los casos límite y uxui_designer para revisar
> los estados. Asigna la implementación a developer y pide QA y revisión del
> diff final cuando estén listos los cambios. No uses servicios reales para pruebas.

Secuencia habitual: necesidad → solución → implementación → QA → revisión → entrega.
Architect interviene en decisiones de arquitectura y UX cuando hay interfaz.
La secuencia se reduce para cambios pequeños y respeta las dependencias reales.

Antes de cada delegación define objetivo, alcance, evidencias de entrada, archivos
asignados, criterio de terminado y salida esperada. Los agentes de diseño y revisión
no editan. Developer recibe propiedad exclusiva del conjunto asignado. El orquestador
comprueba el resultado conjunto y las limitaciones antes de entregar.

Un test propuesto o inspeccionado no cuenta como ejecutado. Una revisión sin hallazgos
no elimina el riesgo. No des por verificadas integraciones que requieren credenciales
inexistentes. Informa con claridad de qué se pudo comprobar y qué queda pendiente.

Usa las plantillas cuando ayuden a conservar decisiones o coordinar trabajo grande.
No generes documentos para cada cambio menor.
