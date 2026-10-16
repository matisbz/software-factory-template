# Validación de 1.0.0

Realizada el 2026-10-16 en macOS, con Python 3.12.14 y el ejecutable incluido en la
aplicación: `codex-cli 0.162.0-alpha.17.2`.

## Resultado

- 31 pruebas locales del instalador: aprobadas.
- 18 archivos de payload: integridad SHA-256 y manifiesto coherentes con VERSION.
- TOML parseado; seis nombres únicos y los tres campos standalone requeridos.
- Claves, tipos y límite de concurrencia del config contrastados con el
  [JSON Schema oficial](https://developers.openai.com/codex/config-schema.json).
- Lectura local con `codex app-server --strict-config`: config del proyecto aceptado,
  `agents.enabled = true` y límite de concurrencia 3.
- Inspección local del prompt de Codex: el bloque de AGENTS.md aparece cargado.

El fixture usado para esa lectura recibió confianza solo mediante una opción del
proceso de diagnóstico. No se modificó la configuración global del usuario.
No se ejecutó una llamada a un modelo ni una tarea de subagente para estas pruebas;
la lectura de config no prueba por sí sola una delegación completa. La comprobación
opcional de activación real está en COMPATIBILITY.md y usa el acceso de tu cuenta.

## Cobertura del instalador

Instalación en carpeta nueva, proyecto existente, rutas con espacios, repetición sin
reescrituras, dry-run/status sin escrituras, actualización de archivos intactos,
copias y permisos, cambios locales, borrados, contexto de inicialización, bloques de
AGENTS.md, propuestas repetidas y alteradas, adopción de cambios upstream, archivos
nuevos y retirados, cambios de política, TOML inválido, corrupción de manifiestos,
integridad, rutas peligrosas, enlaces simbólicos, colisiones de tipos, bloqueo concurrente,
cambios durante la operación y recuperación tras un fallo parcial simulado.

## Repetir comprobaciones locales

Desde el checkout de la plantilla, con Python 3.11+:

```sh
python3 scripts/factory.py validate
python3 -m unittest discover -s tests -v
```

Después de un cambio intencional en template/ o VERSION, regenera el manifiesto con
`python3 scripts/build_manifest.py` antes de esas comprobaciones. No lo regeneres
para ocultar una divergencia inesperada en una plantilla descargada.

Las pruebas crean proyectos desechables en carpetas temporales. No usan GitHub,
OpenAI API, bases de datos ni servicios de producción.
