# Software Factory: biblioteca de prompts

Este repositorio privado mantiene **prompts completos para copiar y pegar** en sesiones
de Codex Desktop dentro de cada proyecto. Versión actual: **2.5.0**.

## Uso

1. Abre el proyecto destino en Codex, sea nuevo o existente.
2. Copia TODO [01-bootstrap.md](prompts/01-bootstrap.md) mediante **Copy raw file** y
   pégalo en su sesión. Codex instala la fábrica con el desarrollo bloqueado hasta que
   apruebes explícitamente diseño y flujos. No necesitas clonar este repositorio.
3. Revisa pendientes y abre una conversación nueva en la raíz para cargar las reglas;
   confía en el proyecto mediante Codex si corresponde tras revisar los archivos.
4. Rellena y pega [02-project-context.md](prompts/02-project-context.md). Preparará el
   contexto y una primera tarea de diseño, sin implementar la aplicación.
5. Copia y pega [04-design-and-approval.md](prompts/04-design-and-approval.md). Codex
   prepara pantallas y recorridos revisables, presenta una versión y espera tu decisión.
6. Cuando lo decidas, aprueba explícitamente **diseño Y flujos**, identificando versión
   y alcance. Si ya encargaste desarrollar ese alcance, o lo encargas en ese mensaje,
   comienza la implementación sin pedir otra autorización. Si únicamente pediste diseño
   y no hay encargo de desarrollo, se registra la decisión y se espera ese encargo.

Para un proyecto que ya tenía instalada la fábrica, pega primero
[03-update-factory.md](prompts/03-update-factory.md) para aplicar también las reglas a
los siete roles, y después el prompt 04. El actualizador conserva personalizaciones y
aprobaciones vigentes; si hay conflictos que impidan persistir el límite, informa y deja
la implementación bloqueada en esa sesión. Comprueba esos pendientes antes de continuar.
Cada prompt es autónomo y contiene los documentos/configuraciones que requiere.

## Qué contiene este repositorio

```text
software-factory-template/
├── README.md
├── CHANGELOG.md
└── prompts/
    ├── 01-bootstrap.md
    ├── 02-project-context.md
    ├── 03-update-factory.md
    └── 04-design-and-approval.md
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
| developer | Aplicación, interfaz e integración con el backend |
| backend_engineer | APIs, datos, autenticación y migraciones; especialización en Supabase |
| qa_engineer | Validación y regresiones |
| pr_reviewer | Revisión del cambio final |

Cada definición completa aparece como bloque de contenido en 01-bootstrap.md y en el
actualizador. No depende de definiciones, scripts o plantillas en otro lugar del repo.
El límite de referencia es tres subagentes concurrentes; Codex usa los roles pertinentes
en varias tandas. La sesión o las políticas de la cuenta pueden imponer menos recursos.

## Una rama y una PR por tarea

Cada tarea con cambios, incluida documentación o configuración, usa una rama
`codex/<descripcion-de-la-tarea>` creada desde `main` actualizada. Tras implementar y
validar, `pr_reviewer` revisa el diff completo de los commits finales. Se corrigen los
hallazgos y se repite la revisión hasta obtener un dictamen **CONFORME**.

Solo entonces el orquestador sube la rama y abre la pull request con destino **`main`**,
sin pedir otra confirmación para esos pasos. Entrega el enlace, la validación y los SHA
revisados. Si cambia el contenido, los commits o la base, hay que volver a revisar.
Las continuaciones mantienen la misma rama y PR; las consultas sin cambios no generan PR.
No se fusiona automáticamente ni se hace push directo a `main`.

Los cuatro prompts aplican este flujo. Bootstrap y actualización lo instalan en el bloque
de `AGENTS.md` y en los siete roles, conservando personalizaciones. Si falta acceso, remoto,
`main` o revisión independiente, se informa del paso pendiente sin simular su cumplimiento.
Una carpeta sin Git puede recibir archivos locales, pero rama y PR quedan pendientes.
La conformidad técnica no sustituye la aprobación humana del diseño y los flujos.

## Backend y Supabase

`backend_engineer` es un rol incluido en la configuración y usado solo cuando hay trabajo
significativo de backend. `architect` define límites y contratos; el especialista implementa
APIs, persistencia, autenticación y migraciones; `developer` integra esos contratos en la
aplicación. QA y `pr_reviewer` mantienen la revisión independiente. No se añade un agente
por rutina ni se aumenta el límite de tres subagentes concurrentes.

Si el proyecto utiliza Supabase, el especialista usa las skills y herramientas disponibles
para Database, Auth, RLS, Storage, Realtime y Edge Functions. No elige Supabase por defecto
ni necesita un rol separado de data engineering para estas tareas. La instalación de la
fábrica no instala plugins, conecta servicios ni ejecuta operaciones de base de datos.

Los cambios de esquema quedan en migraciones versionadas antes de aplicarse en un entorno
compartido. Cada operación identifica proyecto, entorno y autorización; hay un único escritor
por base de datos/entorno. Las pruebas usan datos sintéticos fuera de producción y verifican
tanto accesos permitidos como denegados. Preparar una migración no implica haberla aplicado
ni autoriza su ejecución remota. Se respetan las autorizaciones existentes para su alcance.

El rol hereda las herramientas y permisos de la sesión: su nombre no crea aislamiento.
Supabase permite limitar una conexión MCP a un proyecto o a solo lectura; esa configuración
se gestiona en la conexión, no dentro del TOML del subagente.
Fuentes: [agentes de Codex](https://learn.chatgpt.com/docs/agent-configuration/subagents)
y [MCP de Supabase](https://supabase.com/docs/guides/ai-tools/mcp#configuration-options).

## Aprobación obligatoria antes de desarrollar

El requisito afecta al orquestador y a los siete agentes, sin excepción para tareas
pequeñas o para implementar backend, tests, scaffolding, dependencias o migraciones.
Antes de aprobar se permiten análisis, documentación, maquetas y prototipos visuales
en herramientas de diseño, sin crear código de la aplicación. Se conserva el código
ya existente. Instalar/configurar la propia fábrica está permitido por el prompt solicitado.

Cada versión de diseño contiene pantallas, estados, flujos, revisión y un manifiesto de
artefactos. El registro conserva el mensaje real del usuario, su fuente, la versión, el
alcance y la huella de lo aprobado. Un approved escrito en un documento no es suficiente
sin evidencia humana verificable. «Me gusta», silencio y ejemplos no conceden autorización.

Si cambia materialmente lo aprobado, se presenta una versión nueva y se espera su
aprobación. Una aprobación vigente no se pide otra vez para el mismo alcance; corregir
la implementación para ajustarse al diseño aprobado tampoco necesita aprobarlo de nuevo.
La actualización de la fábrica no aprueba diseños ni invalida una aprobación válida por sí sola.

La política y el registro se crean en docs/uxui/ del proyecto destino. Es un control de
proceso mediante instrucciones y evidencia, no un sandbox ni una opción nativa de permisos.
Si las reglas no se pudieron aplicar o faltan documentos/evidencia, debe indicarse el
bloqueo y sus pendientes, en vez de afirmar que ya está autorizado desarrollar.

## Limpieza de pruebas y propuestas aprobadas

Al terminar cada prueba se eliminan los scripts auxiliares y outputs generados para ella:
logs, capturas, vídeos, trazas, reportes, cobertura y datos desechables. Se aplica también
si falla o se cancela; se conserva un resultado y diagnóstico breve en la entrega.
Los tests permanentes de la suite, sus fixtures mantenidos y los archivos ajenos se conservan.
Cada agente limpia sus temporales y el orquestador comprueba e informa de cualquier residuo.

Tras aprobar diseño y flujos se eliminan las propuestas locales de esa versión, incluidas
maquetas, prototipos y exportaciones, aunque todavía no se haya encargado la implementación.
Se conserva una especificación textual ligera, los manifiestos y la evidencia de aprobación
en `docs/uxui/approved/<version>/` y `docs/uxui/DESIGN_APPROVAL.md`. La transición verifica
huellas antes de borrar y deja constancia de lo retirado; futuras sesiones validan lo
conservado sin exigir ni recrear los visuales eliminados. QA usa esa especificación y
comunica si una comprobación necesita el original visual ya retirado.

Las propuestas pendientes y los originales compartidos en herramientas externas se conservan.
No se guardan copias comprimidas de los desechables ni se borra por extensión o antigüedad.
Para aplicar estas reglas a una fábrica existente, usa el prompt 03; el prompt 04 gestiona
la limpieza de diseños aprobados tras verificar su evidencia. Editar esta biblioteca no
limpia otros proyectos automáticamente.

## Modelos asignados

| Rol | Modelo base | Razonamiento |
| --- | --- | --- |
| Orquestador (sesión principal) | gpt-6-astra | high |
| architect | gpt-6-astra | high |
| solution_designer | gpt-6.1-sol | high |
| uxui_designer | gpt-6-astra | high |
| developer | gpt-6.1-sol | high |
| backend_engineer | gpt-6.1-sol | high |
| qa_engineer | gpt-6.1-sol | high |
| pr_reviewer | gpt-6-astra | high |

Astra se utiliza para arquitectura, coordinación, diseño UX/UI y revisión crítica. Sol
se utiliza para diseño de la solución, implementación y validación. Esta distribución es una decisión de diseño
para la biblioteca, apoyada en la documentación oficial; no es una asignación oficial
de OpenAI por puesto. El razonamiento high es el punto de partida de esta versión.

Los siete TOML incluidos en bootstrap y actualización contienen `model` y
`model_reasoning_effort`. Para el orquestador, selecciona GPT-6 Astra y razonamiento
alto en Codex cuando estén disponibles: es la sesión principal, no un subagente adicional.
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

Se usa la sintaxis oficial revisada el **19 de octubre de 2026**: TOML independientes
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
la ausencia de dependencias externas y las reglas de conservación antes de publicar. Mantén sincronizada la política entre
bootstrap, actualización y diseño, y el contexto compartido con el segundo prompt.

Se revisaron los cuatro prompts, la sincronización de política y registros y los
dieciséis bloques TOML incluidos (siete roles y un config en cada prompt). Se comprobó
que todos los roles contienen el límite de aprobación y que los registros nuevos
empiezan pending sin evidencia inventada.
El catálogo local de Codex consultado el 2026-10-16 lista gpt-6-astra y gpt-6.1-sol,
ambos con high. No se realizó inferencia ni se asumió disponibilidad en otras cuentas. No se ha ejecutado
una instalación mediante inferencia para validar la versión 2.5; se comprueba en la sesión
destino. Las 31 pruebas automatizadas de la versión 1 pertenecen a su instalador anterior.
La release v1.0.0 queda como historial. Para incorporar esta versión a un proyecto ya
instalado, copia el prompt 03 en su sesión. Editar esta biblioteca no actualiza los proyectos.
