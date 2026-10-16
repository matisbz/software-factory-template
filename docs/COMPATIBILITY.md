# Compatibilidad y sintaxis oficial

Revisado el 2026-10-16. Referencias oficiales de OpenAI:

- [Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents)
- [Configuration Reference](https://learn.chatgpt.com/docs/config-file/config-reference)
- [Config Basics](https://learn.chatgpt.com/docs/config-file/config-basic)
- [AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md)

Esta versión usa archivos standalone en `.codex/agents/*.toml`, cada uno con
`name`, `description` y `developer_instructions`. El nombre interno identifica el rol.
En `.codex/config.toml` usa `agents.enabled` y `agents.max_concurrent_threads_per_session`.
No requiere el antiguo interruptor experimental ni declaraciones por rol `config_file`.

No se fijan `model`, `model_reasoning_effort`, modelos por defecto o proveedores:
se heredan de la sesión y de los ajustes existentes del usuario. El repositorio no
puede comprobar la disponibilidad de todos los modelos de todas las cuentas.
Cualquier personalización futura debe usar un modelo disponible en el selector
actual de tu cuenta y un esfuerzo compatible.

Los agentes heredan los permisos de la sesión. Los roles de diseño, QA y revisión
reciben instrucciones de no editar; esto no establece un sandbox propio.
La plantilla no modifica permisos, políticas de aprobación o configuración global.

La configuración local requiere que el proyecto sea de confianza según Codex.
Comprueba y selecciona esa confianza en la interfaz tras revisar los archivos.
El instalador no la concede ni modifica la configuración del usuario. Abre una
conversación nueva en la raíz para recoger los agentes y AGENTS.md actualizados.
Revisa también AGENTS.override.md y configuraciones de subcarpetas que puedan prevalecer.

## Verificar activación

En una conversación nueva del proyecto pide:

> Comprueba qué roles personalizados tienes disponibles. Si aparecen architect,
> solution_designer, uxui_designer, developer, qa_engineer y pr_reviewer, usa
> pr_reviewer para revisar AGENTS.md sin editar archivos y devuelve su resultado.
> Si falta alguno, indica el motivo comprobable; no simules una delegación.

Esta comprobación usa tu cuenta de Codex y sus límites. Es opcional y distinta de
las pruebas locales del instalador, que no hacen inferencia ni llaman a servicios.
Si tu versión carece de soporte para agentes standalone, actualiza Codex por su
mecanismo habitual o trabaja con el orquestador siguiendo las responsabilidades.
No hay una versión mínima histórica garantizada; consulta las fuentes para tu release.

## Proyectos existentes

Los TOML del mismo nombre se preservan ante una colisión. También se conserva config.toml.
Los roles standalone pueden descubrirse sin reemplazar ese config, salvo que sus ajustes
los desactiven, exista un conflicto de nombre o una política superior impida cargarlos.
No dupliques nombres con declaraciones heredadas `agents.<nombre>` sin revisar su precedencia.
Personaliza después de instalar, y revisa las propuestas al actualizar.
