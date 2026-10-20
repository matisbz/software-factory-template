# Diseñar y obtener aprobación de los flujos UX/UI antes de desarrollar

Versión de prompt y política: **2.4.0**. Trabaja en el proyecto local de ESTA sesión.
Quiero revisar y aprobar explícitamente el diseño Y los flujos UX/UI antes de que se
implemente nada de la aplicación. Este prompt es autónomo: contiene las reglas y los
registros necesarios; no necesitas clonar ni consultar la biblioteca de prompts.

## Información del encargo

- Qué producto o parte quiero diseñar: <usar el contexto existente si lo dejo pendiente>
- Usuarios, objetivos y flujos prioritarios: <usar el contexto o dejar pendiente>
- Referencias visuales o sistema de diseño confirmado: <pendiente>
- Dispositivos y tamaños relevantes: <pendiente>
- Alcance y exclusiones de esta revisión: <pendiente>

Los marcadores no rellenados no son requisitos ni autorizaciones. Lee el contexto y
solo lo necesario para verificar el sistema existente. Pregunta por decisiones de
negocio que realmente bloqueen el diseño y avanza en las demás. Declara los supuestos.

## Activar y conservar el límite

Antes de aplicar cambios prepara y valida el plan completo con el estado de procedencia
y los documentos actuales. Si un estado o registro existente está corrupto, conserva su
contenido, informa y trabaja solo en análisis/artefactos independientes; no sobrescribas
los documentos de control ni afirmes que su persistencia está resuelta.

1. Identifica la raíz del proyecto y muestra la ruta. No escribas fuera de ella ni en
   la biblioteca central. Rechaza enlaces simbólicos y colisiones de tipos en las rutas
   afectadas. Conserva código, cambios ajenos y documentación de negocio.
2. Este mensaje impone el bloqueo inmediatamente en ESTA sesión, aun si faltan archivos
   o roles. No implementes aplicación, tests de implementación, scaffolding, frontend,
   backend, APIs, dependencias, servicios o migraciones. Si hay implementación ya iniciada,
   detén esas subtareas con las herramientas disponibles, informa y conserva los cambios.
3. Aplica la política y registro completos que se incluyen abajo:
   - Si DESIGN_POLICY.md falta, créalo. Si ya contiene exactamente esta política, no lo
     reescribas. Si coincide con su huella base gestionada, actualízalo a esta versión
     siguiendo el procedimiento de copias y estado de abajo. Si está personalizado o
     no hay base verificable, conserva, documenta el conflicto y prepara una
     propuesta de esta política; esta sesión sigue bloqueada hasta aprobación real.
   - Si DESIGN_APPROVAL.md falta y nunca estuvo registrado, créalo con status pending.
     Si existe, conserva historial y aprobaciones; valida evidencia, alcance y artefactos
     antes de interpretar approved como permiso. Si fue borrado después de registrarlo,
     respeta el borrado y comunica el pendiente; no inventes una aprobación para sustituirlo.
4. Haz que la regla persista en AGENTS.md sin alterar normas específicas: si el archivo
   ya tiene la sección completa «Aprobación obligatoria de diseño y flujos UX/UI» instalada
   con las reglas de retención y limpieza de esta versión, o un bloque design-gate con las
   mismas reglas, no añadas otro. Si hay una sección anterior que exige conservar todos los
   visuales, actualiza solo esa sección cuando su bloque coincida con la huella base gestionada;
   registra la nueva huella del bloque modificado. Sin base verificable, conserva y propone
   la actualización; no añadas una sección contradictoria. Si no había sección, añade al
   final el bloque AGENTS que se incluye abajo y guarda copia.
   Si un bloque previo está personalizado, conserva y propone; no lo reemplaces sin base
   reconocible. No dupliques marcadores ni declares activación persistente completa cuando
   un conflicto impida escribir la regla. La instrucción directa de este mensaje conserva
   el bloqueo de esta sesión aunque quede pendiente su persistencia.
5. Añade o actualiza SOLO la sección de aprobación del contexto con
   design_approval_required: true y las rutas de política/registro. Conserva las demás
   secciones; no reduzcas esa regla a false ni interpretes una aprobación de requisitos
   como aprobación de diseño y flujos. No fijes un estado inicial pending sobre evidencia
   de una aprobación previa que siga siendo válida.
6. Usa el estado de procedencia ya existente para no pisar archivos gestionados; no
   inventes una instalación completa de la fábrica si faltan agentes. Guarda copias de
   los documentos antes de cambios reales en .software-factory/backups/<operacion>/,
   con archivos 600 y carpetas nuevas 700. Si el resultado es igual, no reescribas ni hagas
   una copia. Para colisiones usa .software-factory/proposals/<sha256>/<ruta> sin reemplazar
   propuestas editadas. Calcula las huellas reales; compara otra vez los bytes antes de
   sustituir mediante un temporal en el mismo directorio y conserva permisos.
   Excluye backups/propuestas con .software-factory/.gitignore, conservando reglas ajenas.
7. Si existe prompt-state válido, conserva sus campos, versión y entradas: actualiza la
   huella base de DESIGN_POLICY.md solo si era gestionado e intacto o lo acabas de crear;
   registra DESIGN_APPROVAL.md como seed. Si añades un bloque fuera del bloque factory de
   AGENTS, no cambies la huella de factory: registra solo esa adición por separado si hace
   falta, conservando los contenidos anteriores. No reclames propiedad sobre personalizaciones.
   No cambies la versión instalada de la fábrica por haber ejecutado únicamente este prompt.
   Si el estado está corrupto, no lo ignores; prepara diseño sin sobrescribirlo, informa
   y deja pendiente la persistencia. No declares que futuros chats cargarán una regla no aplicada.

## Preparar una versión revisable

Coordina los roles disponibles con sus modelos configurados, sin forzar otros modelos:

- solution_designer: objetivos, alcance, pantallas y recorridos, reglas y aceptación.
- uxui_designer: diseño visual y estados responsive/accesibles; artefactos revisables.
- architect: viabilidad, dependencias y restricciones, solo análisis técnico.
- backend_engineer: viabilidad de datos, contratos, acceso y servicios; solo análisis,
  sin crear esquemas, migraciones ni ejecutar escrituras remotas.
- qa_engineer: revisión de coherencia de recorridos, estados y accesibilidad, sin tests
  de implementación ni comandos que generen código o cambien la aplicación.
- pr_reviewer: revisión del paquete de diseño y sus pendientes cuando aporte valor.

No asignes implementación a developer, backend_engineer ni a ningún otro rol durante esta
fase, ni la hagas tú. Delega únicamente análisis o artefactos de diseño con propiedad
exclusiva de sus archivos. Si no aparecen roles/herramientas, informa y realiza tú el
trabajo de diseño posible, conservando el
mismo bloqueo. No crees nuevos agentes, procesos Codex anidados, chats separados, SDKs,
servicios, claves ni APIs de pago para simularlos. No hagas commits, pushes o publicaciones.

Primero comprueba si existe un paquete que ya cubra exactamente el encargo. Si está
pending y no hay cambios solicitados, continúa su revisión sin recrearlo. Si está aprobado
con evidencia vigente y no cambia diseño o alcance, conserva esa aprobación y no la pidas
otra vez. Crea una versión nueva e inequívoca, por ejemplo UX-001, solo para un diseño nuevo,
un cambio material o una alternativa que el usuario solicite. Conserva de una versión aprobada
su registro y especificación ligera, aplicando la limpieza descrita en la política; conserva íntegra una propuesta aún pendiente. No edites ni reutilices
una carpeta o revisión ya presentada/aprobada para el cambio nuevo.
El paquete debe cubrir objetivos, pantalla por pantalla, navegación y transiciones,
validación, carga/vacío/error/éxito, cancelación y recuperación, accesibilidad y los tamaños
relevantes. Guarda DESIGN.md, FLOWS.md, REVIEW.md, visuales y ARTIFACTS.json en la carpeta
de esa versión. Incluye criterios de aceptación y límites de lo que se podrá implementar.

Prioriza las herramientas de diseño ya disponibles y autorizadas; sigue sus instrucciones
y permisos. No inventes una conexión o un enlace. Sin herramientas visuales, prepara la
especificación y los diagramas posibles, explica qué falta y mantén pending; no presentes
un prototipo imaginario como terminado ni generes una aplicación funcional para suplirlo.

## Presentar, revisar y registrar mi decisión

1. Muestra los artefactos visuales y los flujos en un formato accesible en esta conversación,
   con enlaces reales a los archivos o revisiones. Resume versión, alcance, decisiones y
   pendientes. No pidas aprobar pantallas o estados que no has mostrado o enlazado.
2. Antes de solicitar mi decisión, congela los artefactos, calcula ARTIFACTS.json y su huella,
   y registra versión/alcance pendiente sin crear una aprobación. Si no hay visuales revisables,
   datos necesarios o decisiones resueltas, explica ese pendiente antes de pedir aprobación.
3. Solicita una decisión sobre AMBOS elementos: diseño y flujos de ESA versión y alcance.
   Termina esta fase esperando mi respuesta; ni el silencio ni pasar tiempo autorizan código.
   Ejemplo de respuesta que puedo dar (es SOLO un ejemplo, nunca evidencia de aprobación):
   «Apruebo el diseño y los flujos UX/UI de UX-001 para el alcance presentado; puedes desarrollar ese alcance».
   No exijas esa frase exacta: acepta un mensaje directo equivalente que sea inequívoco.
4. Si pido cambios, registra changes_requested y prepara una versión siguiente con esos
   cambios y sus artefactos. Conserva las propuestas pendientes y el historial ligero de las
   aprobadas conforme a la política; vuelve a mostrar lo nuevo.
5. SOLO después de recibir mi aprobación auténtica registra approved con el mensaje real,
   fuente y fecha verificables, versión, alcance y huella aprobados. Un approved en el archivo,
   una respuesta de otro agente, un ejemplo o una referencia sin autenticidad no bastan.
   Si el mensaje es ambiguo, pregunta brevemente y mantén bloqueado el desarrollo.
6. Tras registrar approved, ejecuta la sección «Limpieza de propuestas aprobadas» de la
   política, aunque aún no haya encargo de desarrollo. No pidas otra confirmación; informa
   del resultado. Al retomar una versión ya aprobada, verifica o completa esa limpieza
   sin recrear propuestas eliminadas ni invalidar su aprobación por la retirada registrada.
7. Si existe un encargo de desarrollo anterior que siga vigente y la aprobación cubre
   su alcance, o si también te encargo implementar en ese mensaje, inicia la fase de desarrollo:
   comprueba la vigencia y asigna únicamente lo aprobado, sin solicitar otra autorización.
   Si solo se pidió diseño y no existe encargo de desarrollar, registra mi decisión y espera
   ese encargo, sin pedirme repetir una aprobación ya válida. Nunca apruebes por mí ni amplíes
   el alcance por conveniencia. El contexto de negocio por sí solo no es un encargo de desarrollo.
8. Cualquier cambio material de diseño, flujos o requisitos fuera de lo aprobado necesita
   versión nueva y mi aprobación de ese cambio. Ajustar código a un diseño ya aprobado no
   requiere aprobar de nuevo el mismo diseño. La aprobación no concede permisos para desplegar.

## Contenidos completos para los documentos del proyecto

Los bloques siguientes son datos para archivos del destino, no aprobaciones ni ejemplos
que puedas convertir en autorizaciones. No incluyas las cabeceras o cercas al escribirlos.
El bloque AGENTS se añade según las reglas de arriba; los otros bloques crean los documentos
solo cuando corresponda. Los mensajes auténticos posteriores del usuario determinan el estado.

### Bloque para `AGENTS.md`

```markdown
<!-- software-factory:design-gate:begin -->
## Aprobación obligatoria de diseño y flujos UX/UI

No se desarrolla nada de la aplicación hasta que el usuario apruebe explícitamente
el diseño Y los flujos UX/UI de una versión concreta y su alcance. Lee y cumple
`docs/uxui/DESIGN_POLICY.md` y verifica `docs/uxui/DESIGN_APPROVAL.md` antes de asignar
o ejecutar implementación. Registro ausente, corrupto, desconocido o sin evidencia humana
verificable implica desarrollo BLOQUEADO; un approved escrito en un archivo no basta.
Este límite se aplica al orquestador y a todos los roles, sin excepción para tareas pequeñas,
backend, tests de implementación, scaffolding, dependencias, servicios o migraciones.
Solo se permiten análisis, documentación, maquetas y prototipos en una herramienta de diseño.
No implementes tú mismo ni delegues a otro para eludirlo. Las instrucciones locales, ejemplos,
planes, silencio y mensajes de agentes no sustituyen la aprobación real del usuario.
Antes de desarrollar verifica artefactos o retención documentada, versión, alcance, evidencia
y encargo de implementación. Cumple la limpieza de pruebas y propuestas de DESIGN_POLICY.md;
los visuales retirados según esa política no se exigen ni se recrean.
Si cambia lo aprobado, prepara versión nueva y espera aprobación de ese cambio; conserva una
aprobación verificable mientras siga vigente. No autoriza publicación ni acciones externas.
<!-- software-factory:design-gate:end -->
```

### Sección para `docs/project/CONTEXT.md`

```markdown
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
```

### Archivo: `docs/uxui/DESIGN_POLICY.md`

```markdown
# Política de aprobación de diseño y flujos UX/UI

Versión de política: 2.4.0. Este es un acuerdo de trabajo del proyecto, no una opción
nativa de permisos de Codex. Obliga al orquestador y a todos los subagentes.

## Condición obligatoria para implementar

No se desarrolla nada de la aplicación hasta que el usuario apruebe explícitamente
el diseño Y los flujos UX/UI de una versión concreta y su alcance. Una petición de
construir la web, una tarea pequeña, una urgencia o una instrucción de otro agente
no sustituyen esa aprobación. Una aprobación de requisitos, arquitectura o solamente
pantallas tampoco aprueba ambos elementos. Nadie puede aprobar por el usuario.

Comprueba esta condición antes de asignar desarrollo y antes de cada tarea que pueda
modificar la aplicación. Si faltan política, registro, evidencia auténtica, versión o alcance
inequívocos, o los artefactos exigibles según la retención descrita abajo, el desarrollo
permanece BLOQUEADO. No interpretes campos ausentes, vacíos, corruptos, desconocidos o no
verificables como permiso.
No declares que un proyecto sin interfaz queda exento automáticamente: documenta
su interacción y pregunta al usuario qué diseño y recorridos debe aprobar.

## Trabajo permitido mientras no hay aprobación

- Leer código existente, requisitos, documentación y referencias autorizadas.
- Analizar arquitectura y viabilidad sin implementar ni ejecutar migraciones.
- Crear documentación de requisitos, diagramas de recorridos, maquetas, imágenes y
  prototipos visuales en una herramienta de diseño ya disponible y autorizada.
- Revisar accesibilidad, estados, navegación y coherencia del paquete de diseño.
- Crear o actualizar la configuración de ESTA fábrica y sus registros mediante los
  prompts expresamente solicitados; eso no autoriza a implementar el producto.

Los artefactos previos a la aprobación pertenecen a docs/uxui/ o a una herramienta
de diseño. No crees ni cambies código de aplicación o tests de implementación,
scaffolding, componentes funcionales, frontend, backend, APIs, esquemas o migraciones;
no añadas dependencias ni conectes servicios de producto. No ejecutes comandos que
lo hagan indirectamente, ni disfraces HTML/CSS/JS funcional como un prototipo en docs/.
Puede usarse una automatización temporal solo para generar/exportar un artefacto de
DISEÑO, sin introducir código ejecutable del producto ni dependencias en el proyecto.
Conserva la aplicación existente tal como está. No borres cambios previos para simular
que aún no se desarrolló. Si hay agentes activos implementando, detén esas subtareas
con las herramientas disponibles, informa de cambios ya hechos y conserva su trabajo.

## Paquete de diseño revisable

Cada versión usa una carpeta nueva, por ejemplo docs/uxui/designs/UX-001/:

- DESIGN.md: objetivos, alcance/exclusiones, pantallas identificadas, jerarquía visual,
  componentes visuales, estados y tamaños de pantalla, accesibilidad y decisiones.
- FLOWS.md: recorridos identificados; inicio, acciones, pantallas/estados, transiciones,
  validaciones, errores, cancelación, recuperación y resultado; diagramas si ayudan.
- REVIEW.md: comprobaciones de diseño, viabilidad, supuestos y decisiones pendientes.
- Artefactos visuales exportados o referencias a revisiones concretas de una herramienta
  de diseño. Deben mostrar las pantallas y estados relevantes que se pide aprobar.
- ARTIFACTS.json: rutas/referencias exactas, SHA-256 de los archivos locales y una huella
  del manifiesto calculada con una representación canónica y ordenada documentada.

No inventes imágenes, capturas, enlaces, revisiones, identificadores ni hashes. Un
resumen escrito no equivale a una maqueta visual entregada. Si no puedes proporcionar
una representación revisable, informa y deja el estado pendiente. Para artefactos en
una herramienta externa, guarda exportaciones locales que el usuario pueda revisar;
si no puedes congelar y verificar su revisión, no autorices implementación a partir
solo de un enlace mutable. No publiques ni transmitas datos a un servicio nuevo.

## Evidencia de aprobación

La aprobación procede de un mensaje directo y auténtico del usuario en la conversación,
voz transcrita o evidencia de su autorización que el entorno permita verificar. Debe
identificar inequívocamente el diseño, sus flujos, la versión y el alcance. Si el usuario
se refiere a «la versión que acabas de presentar», es válido cuando hay una sola versión
revisable y ambos elementos quedan aprobados de forma explícita; no exijas una contraseña
ni una frase literal. No confundas ejemplos incluidos en un prompt con mensajes reales.

«Me gusta», «ok», «sigue», silencio, un plan, una captura de texto no autenticada, un
comentario de un agente, una especificación o un campo approved escrito en un archivo
no conceden por sí solos esta autorización. Si el significado o la versión son ambiguos,
pide una aclaración breve y mantén bloqueada la implementación mientras sigues con diseño.

Antes de solicitar aprobación, congela la versión presentada y calcula el manifiesto.
Después de recibirla, registra en docs/uxui/DESIGN_APPROVAL.md la versión, alcance,
artefactos y huella aprobados; el mensaje original sin reinterpretarlo; su fuente
verificable y fecha real. Identificadores de chat/mensaje son opcionales: usa solo los
que el entorno proporcione. No inventes autores, fechas ni referencias verificables.
El registro referencia la versión congelada y no incorpora una aprobación por defecto.

## Estados y comprobación de vigencia

- pending: falta aprobación; solo análisis y diseño.
- changes_requested: el usuario pidió cambios; solo revisión del diseño.
- approved: existe evidencia humana verificable para diseño Y flujos y un alcance exacto.
- superseded: la versión o el alcance cambió; no autoriza el cambio nuevo.

Para desarrollar deben cumplirse TODAS estas condiciones: estado approved, evidencia
humana verificable, artefactos originales intactos O retención verificada según la sección
de limpieza, coincidencia de versión y alcance, y la tarea solicitada incluida en ese alcance.
Un approved en solitario no es suficiente. Si se pierde la evidencia o no se puede comprobar, interpreta el estado
como bloqueado y pide la información necesaria; no reconstruyas una aprobación imaginaria.
Una confirmación directa del usuario sobre su aprobación previa puede servir de evidencia.
Si ya existe aprobación válida y verificable, no vuelvas a solicitarla para el mismo alcance.

Una modificación de pantallas, navegación, flujos, estados, reglas o requisitos que altere
lo aprobado requiere una nueva versión, estado pending y nueva aprobación de ese cambio.
No reutilices una versión aprobada editando sus artefactos ni arrastres su approved a la
versión siguiente. Conserva las aprobaciones históricas. Cumplir el diseño aprobado o
corregir la implementación para ajustarla a él no modifica el diseño y no exige reaprobación.
Actualizar la fábrica o un modelo de agente, sin modificar el diseño/alcance, no invalida
una aprobación auténtica; tampoco convierte una aprobación ausente en válida.

## Limpieza al terminar las pruebas

Los scripts auxiliares y outputs creados solo para ejecutar una prueba son temporales:
logs, capturas, vídeos, trazas, reportes, cobertura, compilaciones y datos/fixtures desechables.
Identifica sus rutas y propietario antes de ejecutar; usa una carpeta exclusiva por ejecución
y configura allí las salidas cuando sea posible. No uses una carpeta compartida como temporal.
Al terminar cada prueba, tanto si pasa como si falla o se cancela, registra en la entrega
comando, resultado y diagnóstico breve, detén los procesos propios y elimina esos archivos.
Usa finally/trap o el mecanismo equivalente disponible; tras una interrupción, completa la
limpieza de esa ejecución al retomar. No esperes al final del proyecto ni guardes copias ZIP.
Los auxiliares temporales de instalación, validación o exportación siguen la misma regla.

Conserva los tests permanentes de la suite, fixtures mantenidos, código del producto y archivos
previos o ajenos. No conviertas un auxiliar de una comprobación puntual en test permanente
para evitar la limpieza. Si se encargan tests de regresión mantenidos, son parte del producto.
No borres por extensión, antigüedad o con comandos globales como git clean. Comprueba las rutas
reales, rechaza enlaces simbólicos y borra solo lo identificado como propio y temporal.
Cada agente limpia sus salidas; en roles de solo lectura esta es la única excepción para
eliminar sus propios temporales, sin modificar fuentes. El orquestador verifica que no quedan
residuos, informa cualquier fallo de limpieza con su ruta y no declara completado lo pendiente.

## Limpieza de propuestas aprobadas

Tras registrar la aprobación auténtica, elimina las propuestas locales de ESA versión sin
pedir otra confirmación, aunque la implementación se vaya a encargar más tarde. Conserva
únicamente una especificación textual ligera, el manifiesto original y la evidencia humana;
no conserves maquetas, exportaciones, capturas, prototipos ni copias comprimidas por historial.
Las propuestas pending o changes_requested no se eliminan por esta regla. Tampoco se borran
archivos ajenos, recursos del producto ni originales compartidos en herramientas externas.

Antes de presentar el diseño, DESIGN.md y FLOWS.md deben describir suficientemente todas
las decisiones visuales y de comportamiento para implementar y revisar sin las maquetas.
Los documentos textuales no deben contener imágenes ni binarios embebidos; ARTIFACTS.json
incluye sus huellas además de las de los visuales. No añadas desechables a Git: evita que
permanezcan en su historial. Si ya estaban versionados, retíralos del árbol de trabajo
sin reescribir el historial ni atribuir a la limpieza una reducción del historial existente.
Después de aprobar, sigue este orden, con un único responsable y sin lectores/escritores activos:

1. Verifica la evidencia y TODAS las huellas originales antes de borrar. Prepara
   docs/uxui/approved/<version>/ con los bytes exactos de DESIGN.md, FLOWS.md, REVIEW.md y
   ARTIFACTS.json ya aprobados. No resumas ni cambies decisiones después de aprobar. Si falta
   detalle indispensable, resuélvelo antes de retirar la propuesta; comunica el pendiente.
2. Guarda allí RETENTION.json con versión, huella del manifiesto original, correspondencia
   entre rutas originales y conservadas, sus SHA-256 y lista exacta de archivos a eliminar.
   Usa la misma representación canónica documentada para calcular su huella. No incluyas
   binarios ni imágenes embebidas en los textos conservados. Comprueba los bytes guardados.
3. Actualiza las rutas de design_document, flows_document y artifact_manifest del registro
   a los documentos conservados; mantén approved_artifact_fingerprint y evidencia originales.
   Añade retention_manifest, retention_fingerprint y cleanup_status: pending. Guarda y relee
   este registro ANTES del primer borrado. No sustituyas ni simules una aprobación.
4. Elimina solo los archivos de la propuesta identificados y verificados, incluidas las
   copias de los textos ya conservados; quita su carpeta cuando quede vacía. Rechaza rutas
   fuera del proyecto, enlaces simbólicos y archivos modificados desde la comprobación.
   No hagas backups de los archivos desechables. Si falla o se interrumpe, conserva el registro
   y reanuda solo los borrados pendientes; no borres archivos nuevos ni reclames éxito parcial.
5. Verifica las ausencias y lo conservado; registra cleanup_status: completed y cleaned_at
   con la fecha real. En la entrega informa de la limpieza y de cualquier ruta pendiente.

Tras esta transición, la vigencia se verifica con la evidencia original, el manifiesto
original intacto (verificado contra approved_artifact_fingerprint) y los textos conservados
cuyas huellas deben coincidir tanto con ARTIFACTS.json como con RETENTION.json. Comprueba
además la huella del registro de retención y su vínculo con la misma versión aprobada.
Los archivos retirados expresamente en ese registro no se exigen ni se recrean; su ausencia
no invalida la aprobación. Esto también permite reanudar una limpieza pending ya registrada.
Cualquier ausencia no registrada, discrepancia o evidencia perdida mantiene el bloqueo.
Un hash de una maqueta eliminada no permite inspeccionarla: QA valida la especificación
textual conservada y declara ese límite si necesita una comparación visual del original.

Los registros antiguos sin campos de retención siguen siendo válidos con sus artefactos
originales intactos. Migra solo tras verificarlos, nunca deduciendo que un archivo ausente
fue limpiado. Instalar o actualizar la fábrica no borra propuestas ni migra aprobaciones
por su cuenta: el prompt de diseño gestiona esta transición. Una versión nueva conserva
el registro ligero anterior, sin recrear sus archivos de propuesta ni pedir reaprobación.

## Después de aprobar

El orquestador puede iniciar implementación SOLO con un encargo de desarrollo dentro
del alcance aprobado. Ese encargo puede ser una petición de desarrollo anterior que siga
vigente o estar en el mensaje de aprobación: «puedes desarrollar ese alcance» lo constituye.
Si ya existe un encargo vigente y la aprobación lo cubre, continúa sin pedir otra autorización.
Si se pidió únicamente diseño y no existe encargo de desarrollar, registra la aprobación y
espera ese encargo sin preguntar otra vez por lo ya aprobado. No existe autorización automática
para despliegues, publicaciones, envíos, cambios destructivos o servicios de pago.

Asigna a developer o backend_engineer la parte correspondiente, la versión y evidencia
de aprobación, los archivos exclusivos y criterios de aceptación. Cada implementador
verifica la condición por sí mismo; QA y revisión comprueban conformidad con la versión
aprobada. Si falta aprobación, ningún agente ni el orquestador implementa como sustitución
o delega a otro para eludirla.
```

### Archivo: `docs/uxui/DESIGN_APPROVAL.md`

```markdown
# Registro de aprobación de diseño y flujos UX/UI

- schema: 1
- status: pending
- design_version: pendiente
- approved_scope: pendiente
- design_document: pendiente
- flows_document: pendiente
- artifact_manifest: pendiente
- approved_artifact_fingerprint: pendiente
- approval_message: null
- approval_source: null
- approved_at: null
- retention_manifest: null
- retention_fingerprint: null
- cleanup_status: not_started
- cleaned_at: null

No hay aprobación registrada. El desarrollo está bloqueado.
Este documento pertenece al proyecto: bootstrap y actualización solo lo crean una vez,
nunca reemplazan una aprobación existente ni cambian su estado a approved.
El prompt de diseño registra evidencia real del usuario y conserva el historial ligero.
Los campos de retención se completan solo al verificar y retirar propuestas aprobadas;
null o not_started no justifican artefactos ausentes. Los registros antiguos sin estos
campos se verifican con sus artefactos originales, sin reiniciar su aprobación.
Los campos anteriores son un registro documental, no una configuración nativa de Codex.
```

