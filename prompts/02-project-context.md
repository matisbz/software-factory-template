# Inicializar o actualizar el contexto de este proyecto

Versión de prompt: **2.5.0**. Trabaja en el proyecto local de ESTA sesión de Codex.
Escribe o actualiza `docs/project/CONTEXT.md` usando la información que te doy aquí:

- Nombre y propósito: <rellenar o dejar pendiente>
- Usuarios y problema principal: <rellenar o dejar pendiente>
- Alcance inicial y exclusiones: <rellenar o dejar pendiente>
- Flujos y reglas de negocio: <rellenar o dejar pendiente>
- Stack confirmado o restricciones técnicas: <rellenar o dejar pendiente>
- Estado actual y fuentes de requisitos: <rellenar o dejar pendiente>
- Prioridades, plazos y presupuesto: <rellenar o dejar pendiente>
- Criterios de éxito: <rellenar o dejar pendiente>

Si dejo un campo vacío o con su marcador, trátalo como desconocido. Puedes inferir
tecnología y convenciones del código existente, citando las fuentes; no inventes
objetivos de negocio, usuarios, autorizaciones o restricciones a partir de carpetas.

## Diseño y flujos: desarrollo bloqueado hasta aprobación

Este proyecto exige aprobación explícita y verificable del usuario del diseño Y los flujos
UX/UI, de una versión concreta y su alcance. Inicializar contexto o solicitar construir la
web no concede esa aprobación. No implementes ni generes código de aplicación, tests de
implementación, scaffolding, dependencias, servicios o migraciones por este encargo.

Consulta docs/uxui/DESIGN_POLICY.md y docs/uxui/DESIGN_APPROVAL.md si existen. Su ausencia,
corrupción o falta de evidencia implica estado efectivo bloqueado, no excepción. No marques
approved, no copies una frase de ejemplo como evidencia y no reinicies una aprobación válida.
En un contexto existente añade la sección de aprobación que figura en la estructura inferior,
preservando las secciones de negocio. Si contradice una regla local que permite desarrollar
sin aprobación, conserva esa información como antecedente y registra el nuevo requisito del
usuario; no mantengas esa contradicción como permiso. No reduzcas design_approval_required.
Si falta la política o el registro persistente, indica el pendiente y conserva el bloqueo
para esta sesión; no simules que ya instalaste sus archivos.

Si la información nueva altera pantallas, navegación, estados, reglas o alcance aprobado,
señala que el cambio no está autorizado y debe pasar por una nueva versión y aprobación.
Conserva la evidencia histórica: no reescribas ese approved como aprobación del nuevo alcance.
Si solo documentas mejor el mismo alcance, conserva la aprobación verificable vigente.

## Flujo Git obligatorio por tarea

Cada tarea que modifique archivos del proyecto debe trabajar en una rama propia
`codex/<descripcion-de-la-tarea>` y terminar con una pull request hacia `main`, solo
cuando `pr_reviewer` haya revisado el cambio final y lo declare conforme. Se aplica
incluso a documentación, configuración de la fábrica y tareas pequeñas. Una consulta
sin cambios no requiere rama ni PR vacías. Las continuaciones de la misma tarea usan
su rama y PR existentes; una tarea distinta no reutiliza una rama de otro encargo.

El orquestador coordina este flujo:

1. Antes de editar, comprueba raíz real, estado de Git, remoto y rama. Actualiza la
   referencia remota de `main` y crea la rama desde ella; no trabajes ni hagas commits
   directamente en `main`. Conserva cambios ajenos y aísla el trabajo si el checkout
   está ocupado; no los arrastres a la rama ni uses reset, stash o force-push para limpiarlo.
2. Implementa únicamente el alcance autorizado y ejecuta las comprobaciones pertinentes.
   Esta regla no elimina el requisito de aprobación de diseño y flujos ni autoriza
   implementar por el mero hecho de crear una rama.
3. Prepara commits solo con los archivos de la tarea y solicita a `pr_reviewer` una
   revisión independiente, sin editar, del diff completo contra `main`. Identifica los
   SHA de base y HEAD y facilita alcance, criterios y resultados de validación.
4. Corrige todos los hallazgos pendientes y repite la revisión hasta recibir un dictamen
   explícito de CONFORME, sin hallazgos abiertos ni comprobaciones necesarias pendientes.
   Un resultado incompleto, la falta de revisor o la autorrevisión del implementador no
   sustituyen ese dictamen. Si cambia el contenido, los commits o la base revisados,
   vuelve a validar lo afectado y solicita revisión de la versión final.
5. Con revisión conforme, verifica que los SHA siguen vigentes, que no quedan cambios
   de la tarea sin incluir y que el diff no contiene archivos ajenos, secretos ni temporales.
   Sube la rama y crea la PR con base `main`; si ya existe para esta tarea, actualízala.
   Incluye resumen, validación y dictamen con los SHA revisados. Comprueba base y HEAD
   remotos y entrega el enlace real; no declares una PR creada si la operación falló.

Este encargo autoriza al orquestador a crear la rama, hacer commits, subirla y abrir o
actualizar la PR de la tarea en el remoto del proyecto sin pedir otra confirmación.
No autoriza fusionar la PR, activar auto-merge, hacer push directo a `main` ni desplegar.
La revisión del agente es un requisito previo a crear la PR y no equivale a un APPROVE
publicado en GitHub. Los subagentes no gestionan ramas ni publican por iniciativa propia.

Si faltan Git, `main`, un remoto inequívoco, acceso de escritura o un revisor independiente,
explica el impedimento y deja pendiente el paso afectado; no inventes revisiones ni eludas
el flujo publicando sin conformidad. En una carpeta sin Git se permite preparar los archivos
locales del encargo, comunicando que rama y PR quedan pendientes; no crees un repositorio
remoto ni cambies su configuración para resolverlo por tu cuenta.

## Cómo trabajar

1. Identifica la raíz del proyecto de esta sesión y lee las instrucciones aplicables,
   el contexto existente y solo los archivos necesarios para verificar el estado real.
   No necesitas clonar, descargar o acceder a la biblioteca central de prompts.
2. Si el contexto existe, conserva información válida y cualquier sección adicional útil.
   Si detectas contradicciones, explica evidencia y cambios. Separa hechos confirmados,
   supuestos y preguntas abiertas. Haz solo preguntas que bloqueen una decisión importante
   y avanza en el resto; escribe «pendiente» en lo que no puedas determinar.
3. Te autorizo a usar los roles ya cargados cuando aporten valor: solution_designer para
   concretar alcance, architect para restricciones técnicas, uxui_designer si hay interfaz
   y backend_engineer para analizar datos, contratos y entornos si el proyecto lo necesita.
   Dales subtareas de análisis sin editar; tú integras y escribes el contexto. No necesitas
   ejecutarlos todos. Usa el modelo y esfuerzo que tenga configurado cada rol; no los
   reemplaces por los de la sesión ni edites sus TOML. Si los roles no están disponibles,
   comunica la limitación y realiza tú ese análisis, sin simular ejecuciones ni lanzar
   procesos, chats nuevos o APIs para sustituirlos. No reinstales agentes en este encargo.
4. Registra fecha, fuentes verificadas, decisiones confirmadas y pendientes. No guardes
   secretos, contraseñas, tokens, datos reales de clientes ni datos personales sensibles.
   Puedes mencionar nombres de variables de entorno sin incluir sus valores.
5. Antes de modificar un contexto existente guarda su copia en
   `.software-factory/backups/<identificador>/docs/project/CONTEXT.md`, con permisos 600
   y carpetas nuevas 700. Si el contenido resultante es idéntico, no reescribas ni crees
   una copia. Rechaza enlaces simbólicos/rutas fuera del proyecto y vuelve a comprobar
   los bytes antes de reemplazar mediante un archivo temporal en el mismo directorio.
   Conserva permisos y cambios ajenos. No reemplaces secciones de negocio por el ejemplo.
6. No implementes funcionalidades, cambies configuración, elijas un stack nuevo, añadas
   dependencias, ejecutes migraciones ni conectes proveedores por tu cuenta. Aplica el flujo
   Git obligatorio al cambio de contexto; no despliegues ni envíes mensajes por este encargo.
7. Entrega el contexto actualizado, fuentes y comprobaciones reales, decisiones abiertas
   y una primera tarea de DISEÑO con criterios de aceptación. No propongas la implementación
   como siguiente paso hasta la aprobación. Indica que el prompt de diseño debe preparar
   pantallas y recorridos revisables para que el usuario decida; no ejecutes esa tarea aún.

## Estructura para un contexto nuevo

Esta estructura es una guía para crear un contexto si no existe. En uno existente,
conserva su organización y añade únicamente la información que falte.

```markdown
# Contexto del proyecto

Estado: pendiente de inicializar. Última revisión: pendiente.
Este archivo pertenece al proyecto; el prompt de actualización no lo reemplaza.
Escribe «pendiente» para lo desconocido y separa hechos, hipótesis y decisiones.
No incluyas contraseñas, tokens, datos personales reales ni valores de secretos.

## Aprobación obligatoria de diseño y flujos UX/UI

- design_approval_required: true
- Política: docs/uxui/DESIGN_POLICY.md
- Registro: docs/uxui/DESIGN_APPROVAL.md
- Estado efectivo inicial: pending; si existe un registro previo, verificarlo según la política.
- Antes de aprobar: únicamente análisis, documentación y artefactos de diseño.
- Desarrollo de aplicación, tests de implementación, scaffolding, dependencias y migraciones:
  bloqueados hasta aprobación explícita del usuario de diseño Y flujos, versión y alcance.
- La planificación de negocio no constituye aprobación. El registro conserva la evidencia real.
- Una revisión del contexto que altere lo aprobado requiere diseño actualizado y nueva aprobación.
- Tras aprobar, retirar propuestas según DESIGN_POLICY.md y conservar especificación ligera,
  manifiestos y evidencia; verificar esa retención sin exigir los visuales eliminados.
- Eliminar scripts y outputs temporales al terminar cada prueba, incluso con fallo o cancelación;
  conservar tests permanentes y archivos ajenos e informar de residuos pendientes.

Estos campos documentan una regla del proyecto; no son opciones de configuración de Codex.

## Producto y negocio

- Nombre y propósito:
- Problema que resuelve y usuarios:
- Objetivos y métricas:
- Alcance inicial y exclusiones:
- Flujos principales y reglas de negocio:

## Estado y fuentes

- Etapa actual, repositorio y rama base:
- Funcionalidades existentes y deuda conocida:
- Fuentes autoritativas (documentos, código, personas):
- Decisiones confirmadas y supuestos por validar:

## Tecnología y arquitectura

- Lenguajes, frameworks, versiones y fuentes de versión:
- Módulos, responsabilidades y contratos:
- Datos, persistencia, migraciones e integraciones:
- Backend/proveedor confirmado y responsabilidades de aplicación/backend:
- Referencias de proyecto por entorno y conexiones autorizadas (sin credenciales):
- Ubicación de migraciones, historial y procedimiento de aplicación/verificación:
- Sistema de UI, accesibilidad y dispositivos:
- Entornos y límites entre desarrollo, pruebas y producción:

## Trabajo y validación

- Preparación local y gestores de dependencias:
- Comandos reales de ejecución, pruebas, formato y compilación:
- Datos de prueba y servicios requeridos:
- Criterios de aceptación y definición de terminado:
- Convenciones de ramas, commits y revisión: una rama codex/<tarea> por tarea con cambios;
  revisión independiente conforme de pr_reviewer sobre base y HEAD finales antes de abrir
  o actualizar una PR hacia main. Sin push directo a main ni fusión automática.

## Restricciones y decisiones abiertas

- Seguridad y privacidad aplicables:
- Presupuesto, plazos y límites técnicos:
- Acciones externas ya autorizadas (operación, proyecto y entorno; incluidas escrituras de backend):
- Preguntas abiertas con impacto y responsable:
```
