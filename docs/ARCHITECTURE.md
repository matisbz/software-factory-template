# Arquitectura reutilizable por proyecto

El repositorio central contiene prompts, payload versionado y un instalador local.
Cada aplicación recibe una copia independiente; ninguna modificación en la plantilla
cambia proyectos ya instalados hasta que se ejecuta una actualización.

El orquestador es la conversación principal de Codex guiada por AGENTS.md. Los seis
roles son configuraciones de subagentes que Codex puede elegir para tareas concretas.
No hay un daemon propio, cola de procesos, API ni sistema externo de facturación.
`docs/project/CONTEXT.md` define el producto; las reglas reutilizables definen el trabajo.

La concurrencia se limita a tres por defecto para que haya margen de coordinación.
Los seis roles se ejecutan en varias tandas cuando es útil. Es un límite de configuración,
no una promesa sobre los recursos o políticas de cada sesión.

Solo developer edita el código asignado. El orquestador también puede hacer cambios
locales cuando convenga. Todos comparten el entorno de trabajo, por lo que las tareas
con escritura requieren propiedad explícita de archivos o worktrees independientes.
Diseño, arquitectura, QA y revisión retornan evidencias al orquestador.

La instalación separa contenido upstream, huella previamente gestionada y estado local.
Eso permite actualizar lo intacto, proponer lo incompatible y preservar personalizaciones.
AGENTS.md se integra mediante un bloque delimitado; el contexto se inicializa una vez.
La configuración global y las autorizaciones de acciones externas quedan en manos del
usuario y de Codex.
