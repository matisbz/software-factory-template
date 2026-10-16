# Software Factory Template

Plantilla privada reutilizable para **Codex Desktop en macOS**. Cada proyecto obtiene
su propia fábrica: un orquestador y seis subagentes especializados. La plantilla no
incluye un producto, no añade servicios y no necesita claves de API.

## Empezar en Codex

1. Descarga o clona este repositorio en una carpeta independiente de tu aplicación.
   Abre la carpeta de tu aplicación como proyecto local de Codex. También puede ser
   una carpeta nueva y vacía; el instalador no exige Git ni inicializa un repositorio.
2. Copia [01-bootstrap.md](prompts/01-bootstrap.md), sustituye las dos rutas y envíalo
   en una conversación del proyecto. Codex puede usar su Python disponible; requiere 3.11+.
3. Revisa las instrucciones y confía en el proyecto mediante la interfaz de Codex
   si tu versión lo requiere. Abre una conversación **nueva** en su raíz.
4. Copia [02-project-context.md](prompts/02-project-context.md) y rellena lo que sepas.
   El contexto se guarda en `docs/project/CONTEXT.md` y pertenece a ese proyecto.
5. Pide una tarea concreta. La fábrica utiliza solo los roles pertinentes y hereda
   el modelo disponible que hayas elegido en la sesión de Codex.

## Instalación manual

Desde la carpeta de esta plantilla, con Python 3.11 o superior:

```sh
python3 scripts/factory.py validate
python3 scripts/factory.py install --target "/ruta/Mi proyecto" --dry-run
python3 scripts/factory.py install --target "/ruta/Mi proyecto"
python3 scripts/factory.py status --target "/ruta/Mi proyecto"
```

Usa una ruta distinta de la carpeta de la plantilla. Para actualizar, descarga una
nueva versión de la plantilla y ejecuta:

```sh
python3 scripts/factory.py update --target "/ruta/Mi proyecto" --dry-run
python3 scripts/factory.py update --target "/ruta/Mi proyecto"
```

`install` se puede repetir. `update` exige una instalación registrada. Salida **0**:
operación sin conflictos; **2**: personalizaciones preservadas con propuestas pendientes;
**1**: error. El modo dry-run y status no escriben ni crean carpetas.

## Núcleo de agentes

| Rol | Responsabilidad |
| --- | --- |
| architect | Arquitectura, dependencias y decisiones duraderas |
| solution_designer | Alcance, solución y criterios de aceptación |
| uxui_designer | Flujos, estados y accesibilidad de la interfaz |
| developer | Implementación delimitada y comprobaciones |
| qa_engineer | Validación independiente y regresiones |
| pr_reviewer | Revisión del diff final y hallazgos reproducibles |

Son **seis roles configurados**, no seis procesos permanentes ni seis chats que
se crean al instalar. Se coordina por subtareas y dependencias. El config base limita
a tres subagentes concurrentes, además del orquestador; la sesión puede imponer menos.

## Qué se instala

```text
proyecto/
├── AGENTS.md                         # bloque del orquestador
├── .codex/
│   ├── config.toml                   # solo si no colisiona con el existente
│   └── agents/                       # seis TOML standalone
├── .software-factory/
│   ├── manifest.json                 # versión, huellas y propiedad
│   ├── backups/                      # copias antes de cada reemplazo
│   └── proposals/                    # upstream separado ante conflictos
└── docs/
    ├── project/CONTEXT.md             # creado una vez; siempre preservado
    └── software-factory/
        ├── README.md, WORKFLOW.md
        ├── prompts/                   # los dos prompts maestros
        └── templates/                 # tarea, handoff, ADR y revisión
```

En un AGENTS.md existente se añade un bloque delimitado y se guarda el original.
Solo se actualiza ese bloque si no ha sido personalizado; el resto permanece igual.
Los archivos gestionados se actualizan únicamente si coinciden con su huella previa.
Los cambios locales y borrados se respetan. El contexto nunca se reemplaza. No hay
opción `--force`, borrados automáticos ni modificaciones de `~/.codex`.

La plantilla no fija modelos ni esfuerzo ni cambia permisos. Usa la sesión iniciada
en Codex y consume sus límites de uso. No incluye llamadas a APIs de pago, Agents SDK,
MCP de terceros ni trabajos de GitHub Actions habilitados automáticamente.

- [Instalación, actualización y recuperación](docs/INSTALLATION.md)
- [Sintaxis oficial y compatibilidad](docs/COMPATIBILITY.md)
- [Arquitectura y límites](docs/ARCHITECTURE.md)
- [Comprobaciones de la versión inicial](docs/VALIDATION.md)
- [Historial de versiones](CHANGELOG.md)

Versión inicial: **1.0.0**. Documentación oficial contrastada el **16 de octubre de 2026**.
