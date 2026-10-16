# Fábrica instalada en este proyecto

Los roles están en `.codex/agents/`; AGENTS.md contiene el bloque del orquestador.
Inicializa `docs/project/CONTEXT.md` con `prompts/02-project-context.md` de esta carpeta.
Abre una conversación nueva de Codex en la raíz del proyecto y verifica los roles.

La fábrica es configuración e instrucciones: Codex ejecuta y coordina los subagentes.
No es un servicio que corre permanentemente ni crea seis chats en la barra lateral.
Los seis roles están disponibles, pero se usan solo los necesarios para cada encargo.
El límite de referencia es tres subagentes concurrentes, además del orquestador;
el entorno o las políticas de la sesión pueden permitir menos.

Los modelos y permisos se heredan. No hay claves ni llamadas programadas a APIs.
El trabajo de los subagentes consume el uso disponible de tu cuenta de Codex.
No hay una garantía de ejecución gratuita o ilimitada.

Para actualizar, usa `scripts/factory.py update --target <esta carpeta>` desde el checkout
local de la plantilla. Conserva `.software-factory/manifest.json` en Git para mantener
la procedencia de los archivos. Backups y propuestas quedan ignorados por Git.
Consulta INSTALLATION.md y COMPATIBILITY.md del repositorio de la plantilla para
resolver conflictos y comprobar los requisitos de tu versión de Codex.
