# Inicializar o actualizar el contexto de este proyecto

Versión de prompt: **2.0.0**. Trabaja en el proyecto local de ESTA sesión de Codex.
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

## Cómo trabajar

1. Identifica la raíz del proyecto de esta sesión y lee las instrucciones aplicables,
   el contexto existente y solo los archivos necesarios para verificar el estado real.
   No necesitas clonar, descargar o acceder a la biblioteca central de prompts.
2. Si el contexto existe, conserva información válida y cualquier sección adicional útil.
   Si detectas contradicciones, explica evidencia y cambios. Separa hechos confirmados,
   supuestos y preguntas abiertas. Haz solo preguntas que bloqueen una decisión importante
   y avanza en el resto; escribe «pendiente» en lo que no puedas determinar.
3. Te autorizo a usar los roles ya cargados cuando aporten valor: solution_designer para
   concretar alcance, architect para restricciones técnicas y uxui_designer si hay interfaz.
   Dales subtareas de análisis sin editar; tú integras y escribes el contexto. No necesitas
   ejecutarlos todos. Hereda el modelo y esfuerzo de esta sesión. Si no están disponibles,
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
   dependencias, ejecutes migraciones ni conectes proveedores por tu cuenta. No hagas
   commits, publicaciones, despliegues o envíos de mensajes por este encargo.
7. Entrega el contexto actualizado, fuentes y comprobaciones reales, decisiones abiertas
   y una primera tarea pequeña con criterios de aceptación. No ejecutes esa tarea aún.

## Estructura para un contexto nuevo

Esta estructura es una guía para crear un contexto si no existe. En uno existente,
conserva su organización y añade únicamente la información que falte.

```markdown
# Contexto del proyecto

Estado: pendiente de inicializar. Última revisión: pendiente.
Este archivo pertenece al proyecto; el prompt de actualización no lo reemplaza.
Escribe «pendiente» para lo desconocido y separa hechos, hipótesis y decisiones.
No incluyas contraseñas, tokens, datos personales reales ni valores de secretos.

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
- Sistema de UI, accesibilidad y dispositivos:
- Entornos y límites entre desarrollo, pruebas y producción:

## Trabajo y validación

- Preparación local y gestores de dependencias:
- Comandos reales de ejecución, pruebas, formato y compilación:
- Datos de prueba y servicios requeridos:
- Criterios de aceptación y definición de terminado:
- Convenciones de ramas, commits y revisión:

## Restricciones y decisiones abiertas

- Seguridad y privacidad aplicables:
- Presupuesto, plazos y límites técnicos:
- Acciones externas ya autorizadas:
- Preguntas abiertas con impacto y responsable:
```
