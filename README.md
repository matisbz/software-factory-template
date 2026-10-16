# Software Factory: biblioteca de prompts

Este repositorio privado mantiene **prompts completos para copiar y pegar** en sesiones
de Codex Desktop dentro de cada proyecto. Versión actual: **2.1.0**.

## Uso

1. Abre tu proyecto destino en Codex, sea una carpeta nueva o una aplicación existente.
2. Abre [01-bootstrap.md](prompts/01-bootstrap.md) en GitHub, pulsa **Copy raw file** y
   pega TODO su contenido como mensaje en la sesión de ese proyecto. No necesitas clonar
   este repositorio, indicar su ruta, descargar archivos ni ejecutar un instalador aparte.
3. Codex crea los seis agentes y las reglas dentro del proyecto destino, preservando
   personalizaciones. Revisa los pendientes que encuentre. Abre una conversación nueva
   en la raíz del proyecto para cargar los archivos; confía en el proyecto mediante la
   interfaz de Codex si es necesario tras revisarlos.
4. Copia [02-project-context.md](prompts/02-project-context.md), rellena los campos que
   conozcas y pégalo en esa nueva sesión. Codex documenta el contexto de ese producto.
5. Para aplicar una versión posterior de la fábrica, copia el
   [prompt de actualización](prompts/03-update-factory.md) vigente en una sesión del
   proyecto destino. También incluye todos los contenidos: no necesita consultar otro archivo.

## Qué contiene este repositorio

```text
software-factory-template/
├── README.md
├── CHANGELOG.md
└── prompts/
    ├── 01-bootstrap.md
    ├── 02-project-context.md
    └── 03-update-factory.md
```

La configuración de agentes está **dentro del texto de los prompts**. Los archivos TOML,
AGENTS.md, contexto y estado de actualización se crean en cada proyecto cuando pegas el
prompt. La biblioteca central no instala ni ejecuta agentes por sí misma.

## Agentes incluidos en el bootstrap

| Agente | Función |
| --- | --- |
| architect | Arquitectura y decisiones técnicas |
| solution_designer | Requisitos y diseño de la solución |
| uxui_designer | Experiencia de usuario, interfaz y accesibilidad |
| developer | Implementación delimitada |
| qa_engineer | Validación y regresiones |
| pr_reviewer | Revisión del cambio final |

Cada definición completa aparece como bloque de contenido en 01-bootstrap.md y en el
actualizador. No depende de definiciones, scripts o plantillas en otro lugar del repo.
El límite de referencia es tres subagentes concurrentes; Codex usa los roles pertinentes
en varias tandas. La sesión o las políticas de la cuenta pueden imponer menos recursos.

## Modelos asignados

| Rol | Modelo base | Razonamiento |
| --- | --- | --- |
| Orquestador (sesión principal) | gpt-6-astra | high |
| architect | gpt-6-astra | high |
| solution_designer | gpt-6.1-sol | high |
| uxui_designer | gpt-6.1-sol | high |
| developer | gpt-6.1-sol | high |
| qa_engineer | gpt-6.1-sol | high |
| pr_reviewer | gpt-6-astra | high |

Astra se reserva para arquitectura, coordinación y revisión crítica. Sol se utiliza
para diseño, implementación y validación. Esta distribución es una decisión de diseño
para la biblioteca, apoyada en la documentación oficial; no es una asignación oficial
de OpenAI por puesto. El razonamiento high es el punto de partida de esta versión.

Los seis TOML incluidos en bootstrap y actualización contienen `model` y
`model_reasoning_effort`. Para el orquestador, selecciona GPT-6 Astra y razonamiento
alto en Codex cuando estén disponibles: es la sesión principal, no un séptimo subagente.
El prompt conserva el modelo actual de esa sesión y los ajustes principales del proyecto.

La disponibilidad se comprueba antes de instalar. Si falta el modelo deseado, se usa
Sol/high cuando esté confirmado; como último recurso, los valores compatibles de la
sesión actual. Si no se pueden identificar con certeza, se omiten ambos campos para
heredarlos, comunicando esa excepción por rol. No se inventan modelos ni se hacen llamadas
de prueba a una API. Los modelos personalizados existentes se conservan.

## Repetición, personalizaciones y actualización

Los prompts indican a Codex conservar los cambios locales, usar huellas de procedencia,
añadir las reglas del orquestador por bloque y crear copias antes de cambios gestionados.
El contexto pertenece al proyecto y se conserva al actualizar la fábrica. Los conflictos
se guardan como propuestas separadas y se comunican; no se activan silenciosamente.

La versión 2 puede reconocer el manifiesto de la instalación anterior de la versión 1.
No borra archivos de proyectos que ya usaban aquella versión. Aquí no hay scripts,
instaladores, tests, plantillas desplegables ni agentes que se carguen en esta biblioteca.

La idempotencia y conservación son instrucciones que Codex debe ejecutar y verificar
en la sesión. Su resultado depende de esa ejecución; un prompt no sustituye las garantías
de un programa determinista. Cada ejecución debe informar de lo aplicado y lo pendiente.

## Compatibilidad y modelos

Se usa la sintaxis oficial revisada el **16 de octubre de 2026**: TOML independientes
con `name`, `description` y `developer_instructions` en `.codex/agents/` del destino.
El config base usa `agents.enabled` y `agents.max_concurrent_threads_per_session`.
Cada TOML de subagente incluye `model` y `model_reasoning_effort`. Los permisos y
proveedor se heredan de la sesión. No se requieren claves ni llamadas a APIs de pago;
los subagentes usan los límites disponibles de tu cuenta Codex. La disponibilidad se
comprueba de nuevo en cada cuenta o espacio de destino; no se garantiza por el nombre.

Fuentes oficiales:

- [Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents)
- [Config Basics](https://learn.chatgpt.com/docs/config-file/config-basic)
- [Configuration Reference](https://learn.chatgpt.com/docs/config-file/config-reference)
- [AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
- [Selección de modelos](https://developers.openai.com/api/docs/guides/model-selection)
- [Modelos de ChatGPT y Codex](https://learn.chatgpt.com/docs/models)

Para comprobar la activación en una conversación nueva del destino, puedes pedir:

> Comprueba qué roles de la fábrica tienes disponibles. Si pr_reviewer aparece cargado,
> úsalo para revisar AGENTS.md sin editar y devuélveme su resultado. Si no puedes delegar,
> informa del motivo comprobable; no simules una ejecución.

## Mantenimiento de los prompts

Edita el texto en esta biblioteca y versiona las mejoras. Mantén idéntico el contenido
literal de la fábrica en bootstrap y actualizador para una misma versión. Actualiza
las versiones dentro de los prompts y CHANGELOG.md. Comprueba la sintaxis de los bloques,
la ausencia de dependencias externas y las reglas de conservación antes de publicar.

Se revisaron los tres prompts y se parsearon los catorce bloques TOML incluidos.
El catálogo local de Codex consultado el 2026-10-16 lista gpt-6-astra y gpt-6.1-sol,
ambos con high. No se realizó inferencia ni se asumió disponibilidad en otras cuentas. No se ha ejecutado
una instalación mediante inferencia para validar la versión 2.1; se comprueba en la sesión
destino. Las 31 pruebas automatizadas de la versión 1 pertenecen a su instalador anterior.
La release v1.0.0 queda como historial: para copiar los prompts actuales usa main o v2.1.0.
