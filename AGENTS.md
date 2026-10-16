# Mantenimiento de Software Factory

Este repositorio distribuye una plantilla, no es una aplicación de negocio.
Mantén separados scripts, prompts reutilizables y payload de `template/`.
No fijes modelos ni esfuerzo, credenciales, proveedores, MCP, permisos o herramientas de pago.
No cambies personalizaciones de proyectos instalados. Para cambios en el instalador,
verifica conflictos, borrados, idempotencia, enlaces simbólicos y fallos de integridad.
Después de editar el payload, ejecuta `python3 scripts/build_manifest.py` y
`python3 scripts/factory.py validate`, seguido de `python3 -m unittest discover -s tests -v`.
La documentación oficial vigente prevalece para la sintaxis de Codex.
Actualiza VERSION, CHANGELOG.md y el manifiesto juntos al publicar una versión.
