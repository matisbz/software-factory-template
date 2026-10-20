# Historial de versiones

## Sin publicar

## 2.6.0 — 2026-10-20

- Procedimiento completo de diseño y aprobación integrado en la política que instalan
  bootstrap y actualización; se elimina el prompt separado 04-design-and-approval.md.
- El orquestador inicia o retoma el diseño al recibir contexto o un encargo de producto,
  conservando versiones pendientes y aprobaciones vigentes. Instalar o actualizar la
  fábrica no inicia por sí solo trabajo de producto.
- El prompt de contexto continúa con pantallas y recorridos revisables sin exigir otro
  prompt. Aprobar mantiene la exigencia de un encargo de desarrollo para implementar.
- Se conservan presentación, evidencia verificable, revisión, limpieza y límites de alcance.

## 2.5.0 — 2026-10-20

- Rama propia por tarea con cambios y pull request hacia main únicamente después de
  revisión independiente conforme de pr_reviewer sobre el diff final.
- Corrección y nueva revisión de hallazgos; dictamen ligado a SHA de base y HEAD,
  invalidado si cambia la versión revisada. Sin autorrevisión como sustituto.
- Autorización de rama, commits, push y PR para el orquestador; sin fusión automática,
  push directo a main ni despliegue. Continuaciones reutilizan rama y PR de su tarea.
- Flujo sincronizado en los cuatro prompts, AGENTS y siete roles; faltas de Git, remoto,
  main, acceso o revisor se comunican como pendientes sin fingir una PR completada.

## 2.4.0 — 2026-10-20

- Limpieza de scripts auxiliares y outputs temporales al terminar cada prueba, también
  con fallo o cancelación; se conservan tests permanentes y archivos ajenos.
- Retirada de propuestas de diseño tras aprobar diseño y flujos, conservando solo
  especificación textual ligera, manifiestos y evidencia humana verificable.
- Transición de retención registrada antes de borrar, reanudación de limpiezas pendientes
  y comprobación de vigencia sin exigir ni recrear los visuales retirados.
- Reglas sincronizadas en los cuatro prompts, orquestador y siete roles; la actualización
  conserva aprobaciones existentes y el prompt de diseño gestiona su limpieza.
- uxui_designer pasa a GPT-6 Astra/high en los prompts de instalación y actualización
  y en la documentación de modelos asignados.

## 2.3.0 — 2026-10-19

- Séptimo rol backend_engineer, con GPT-6.1 Sol/high y especialización en Supabase
  cuando lo utiliza el proyecto; se conserva el máximo de tres subagentes concurrentes.
- Reparto explícito entre arquitectura, backend y aplicación, con contratos compartidos
  y un único escritor por archivo y base de datos/entorno.
- Migraciones versionadas, identificación de destino y alcance autorizado antes de operar,
  y comprobación de permisos con identidades representativas y datos sintéticos.
- Contexto y fase de diseño incorporan análisis de backend. Los siete roles conservan
  el bloqueo de implementación hasta aprobación verificable de diseño y flujos.
- Bootstrap y actualización incluyen la definición completa; se conservan personalizaciones,
  borrados y aprobaciones existentes. La biblioteca no instala ni conecta servicios reales.
- Validados dieciséis bloques TOML, sincronización de contenidos y conservación del bloqueo;
  no se ha ejecutado una instalación en un proyecto destino ni probado operaciones remotas.

## 2.2.0 — 2026-10-16

- Nuevo prompt autónomo 04-design-and-approval.md para preparar diseños y recorridos
  revisables, presentar una versión y registrar exclusivamente la decisión auténtica del usuario.
- Bootstrap y actualización incluyen política persistente y registro inicial pending;
  el contexto exige aprobación y propone trabajo de diseño antes de implementación.
- Orquestador y seis roles bloquean aplicación, tests de implementación, scaffolding,
  dependencias, servicios y migraciones hasta aprobación explícita de diseño Y flujos.
- Aprobación vinculada a versión, alcance, evidencia humana y huella de artefactos congelados;
  cambios materiales requieren revisión nueva. No hay aprobación automática por instalar.
- Conservación de personalizaciones y aprobaciones válidas; conflictos o datos ausentes
  mantienen el desarrollo bloqueado y se comunican, sin afirmar activación completa.
- Revisión estática de contenidos, registros pendientes, sincronización y catorce TOML.
  El repositorio central conserva únicamente cuatro prompts, README y CHANGELOG.

## 2.1.0 — 2026-10-16

- Modelos y razonamiento explícitos por rol en bootstrap y actualización: Astra/high
  para architect y pr_reviewer; GPT-6.1 Sol/high para solution_designer, uxui_designer,
  developer y qa_engineer.
- Orquestador: recomendación Astra/high en el selector de Codex, conservando el modelo
  actual de la sesión y la configuración principal del proyecto.
- Verificación de disponibilidad por cuenta antes de escribir; alternativas confirmadas
  y herencia comunicada solo como último recurso.
- Contexto y reglas del orquestador respetan el modelo configurado en cada subagente.
- Conservación de modelos personalizados y comparación de huellas de los contenidos
  resueltos. Catálogo local y catorce bloques TOML comprobados, sin inferencia.

## 2.0.0 — 2026-10-16

- Repositorio central convertido en una biblioteca de prompts y documentación mínima.
- Eliminados de main scripts, tests, template/, configuración de agentes y documentación
  del instalador: no hay que clonar ni descargar la biblioteca para instalar la fábrica.
- Bootstrap autónomo con definiciones completas de los seis agentes, AGENTS.md, config
  y plantilla de contexto, para pegar en una sesión del proyecto destino.
- Prompt independiente de actualización con todo el contenido y reglas para preservar
  personalizaciones, borrados, contexto y configuración global.
- Prompt de contexto autónomo, con información específica aportada por el usuario.
- Versiones y reglas de procedencia incluidas en el texto; migración del manifiesto v1.
- Sintaxis TOML revisada y comprobación estática de los prompts. No se atribuyen a esta
  versión las pruebas del instalador anterior. v1.0.0 permanece disponible como historial.

## 1.0.0 — 2026-10-16

Primera implementación con archivos de plantilla, seis agentes standalone e instalador
local con 31 pruebas. Este método se sustituyó por el flujo de copiar y pegar prompts.
