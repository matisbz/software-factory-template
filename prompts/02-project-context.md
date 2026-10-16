# Prompt maestro 2: contexto específico del proyecto

Úsalo en una conversación nueva del proyecto una vez instalada la fábrica.
Rellena los campos que conozcas; puedes dejar el resto como «pendiente».

---

Inicializa o actualiza `docs/project/CONTEXT.md` para este proyecto:

- Nombre y propósito: <...>
- Usuarios y problema principal: <...>
- Alcance inicial y exclusiones: <...>
- Flujos y reglas de negocio: <...>
- Stack o restricciones técnicas: <...>
- Estado actual y fuentes de requisitos: <...>
- Plazos, presupuesto y prioridades: <...>
- Criterios de éxito: <...>

Lee el contexto existente y solo los archivos necesarios para comprobar tecnología,
comandos y convenciones. Usa el código actual como evidencia; no deduzcas decisiones
de negocio a partir de carpetas o ejemplos. Conserva información válida y registra
fuentes, fecha y cambios. No pongas secretos ni datos de clientes en la documentación.

Te autorizo a delegar subtareas independientes en los roles disponibles de la fábrica:
solution_designer para concretar alcance, architect para revisar restricciones técnicas
y uxui_designer si existe interfaz. No es necesario ejecutarlos todos; hereda el modelo
y esfuerzo de esta sesión. Si no aparecen roles personalizados, comunica la limitación
y continúa tú mismo; no simules ejecuciones ni uses APIs o procesos adicionales.

Escribe el contexto con hechos, supuestos y pendientes claramente distinguidos. Haz
solo las preguntas cuyo resultado bloquee una decisión importante y avanza en el resto.
No implementes funcionalidades ni añadas un stack, proveedor, dependencia o servicio
por iniciativa propia. Entrega el contexto actualizado, fuentes verificadas, decisiones
abiertas y una primera tarea pequeña con criterios de aceptación para comenzar.
