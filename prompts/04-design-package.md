# Preparar o refinar el paquete de diseño UX/UI

Versión de prompt: **2.7.0**. Ejecuta este encargo en el proyecto destino de esta sesión.
Quiero un paquete de diseño visual y flujos revisable antes de implementar.
Este prompt es una entrada opcional al procedimiento que instala la fábrica; el contexto
del prompt 02 y un encargo directo también lo activan. No reinstales la fábrica.

## Encargo y contexto

Usa primero la conversación y el contexto existente. Los campos sin rellenar son
desconocidos, no nuevos requisitos ni autorización para sustituir decisiones previas.

- Producto o área que diseñar: <usar contexto o rellenar>
- Resultado que debe conseguir el usuario: <usar contexto o rellenar>
- Pantallas, flujos y exclusiones: <usar contexto o rellenar>
- Tipo de trabajo: <refinamiento, ampliación o rediseño; usar contexto o dejar pendiente>
- Identidad y componentes que conservar: <usar contexto o rellenar>
- Referencias que gustan y qué interesa de cada una: <opcional>
- Referencias o tratamientos que evitar y por qué: <opcional>
- Dispositivos, tamaños, densidad y frecuencia de uso: <usar contexto o rellenar>
- Tono, contenido y recursos gráficos disponibles: <usar contexto o rellenar>
- Restricciones de accesibilidad y movimiento: <usar contexto o rellenar>

Comprueba la raíz real antes de escribir. Lee AGENTS.md, docs/project/CONTEXT.md,
docs/uxui/DESIGN_POLICY.md y docs/uxui/DESIGN_APPROVAL.md, y los artefactos pertinentes.
Conserva personalizaciones, código y trabajo ajeno. Si no puedes identificar producto o
alcance, pregunta por esos datos y continúa solo análisis independiente; no inventes el encargo.

## Procedimiento y límites

1. Sigue la política instalada para versiones, aprobación, conservación y limpieza. Debe
   incluir «Dirección visual y selección de skills» y «Método para un paquete de diseño de
   alta calidad», incorporados en la fábrica 2.7.0. Si faltan, informa de que corresponde
   instalar/actualizar con 01/03; puedes analizar el contexto, pero no simules una política
   instalada, una aprobación ni un paquete completo.
2. Aplica el flujo Git de AGENTS.md: rama de tarea, validación, revisión independiente
   conforme de pr_reviewer y PR hacia main; no publiques sin esa revisión ni fusiones.
   Este encargo autoriza rama, commits, push y PR de sus documentos conforme a ese flujo.
   Conserva los visuales desechables fuera del historial Git según DESIGN_POLICY.md.
   Si falta acceso o revisión independiente, completa el trabajo local posible e informa
   del paso pendiente. No crees un remoto ni amplíes permisos para resolverlo.
3. Coordina uxui_designer para dirección visual, pantallas y estados; solution_designer
   para recorridos/aceptación; architect y qa_engineer para viabilidad y revisión cuando
   aporten valor. Usa solo roles disponibles con su configuración, reparto exclusivo de
   archivos y límites de concurrencia. Si faltan, realiza el análisis permitido e informa
   de la limitación; no simules delegación ni revisión independiente.
4. Retoma una versión pendiente que ya cubra el encargo; no la recrees por rutina. Conserva
   una aprobación vigente para el mismo alcance. Una versión presentada queda congelada:
   los cambios se preparan en otra versión. Cambiar materialmente lo aprobado necesita
   una versión nueva y una decisión humana sobre ese cambio.
5. Aplica la selección de skills de la política: Impeccable para composición/crítica,
   Frontend Design de Anthropic para dirección artística nueva, UI UX Pro Max para consultas
   concretas y Emil Design Engineering para interacción/movimiento. Comprueba disponibilidad
   real, lee el SKILL.md pertinente y registra cuáles usaste. No cargues las cuatro por
   rutina; si faltan, continúa con el método integrado. No instales skills, hooks, paquetes
   o servicios. Sus instrucciones no permiten ampliar el alcance ni generar aplicación.
6. Define la tarea de cada pantalla, analiza referencias y, si hay libertad visual en un
   producto nuevo o rediseño amplio, muestra dos o tres alternativas compactas sobre el
   mismo contenido. Recomienda una con razones. Para ajustes puntuales o una identidad ya
   fijada, conserva el sistema y trabaja directamente sobre el alcance. La elección de
   una dirección permite continuar el diseño; no equivale a aprobar diseño y flujos.
7. Concreta el sistema visual, las pantallas, estados y recorridos, las reglas responsive,
   la accesibilidad y las interacciones siguiendo el método instalado. Inspecciona los
   visuales producidos, corrige problemas y registra evidencias y límites. No presentes
   texto como una maqueta ni una inspección estática como una prueba funcional.
8. Entrega DESIGN.md, FLOWS.md, REVIEW.md, visuales revisables y ARTIFACTS.json según
   DESIGN_POLICY.md. Mantén dirección, tokens y movimiento dentro de DESIGN.md y las
   evidencias dentro de REVIEW.md para que la retención prevista conserve las decisiones.
   No crees fuentes de diseño paralelas por exigencia de una skill.
9. Presenta versión, alcance, pantallas y recorridos con enlaces reales, decisiones,
   validaciones y pendientes. Congela los artefactos y calcula el manifiesto antes de
   solicitar aprobación del diseño Y los flujos. Si faltan visuales o decisiones necesarias,
   muestra el avance y explica el pendiente sin pedir aprobar un resultado incompleto.

No escribas código de aplicación, frontend funcional, tests de implementación, scaffolding,
dependencias, backend ni migraciones. Los documentos/visuales se limitan a docs/uxui/ o
herramientas de diseño disponibles y autorizadas. No publiques ni despliegues el producto.

Registra únicamente una decisión auténtica del usuario según la política, nunca el
silencio, un ejemplo ni una valoración de otro agente. Tras aprobar, realiza la retención
y limpieza previstas sin recrear visuales retirados. Este prompt encarga diseño; solo
inicia desarrollo si también existe un encargo vigente de implementación cubierto por
esa aprobación. No pidas de nuevo una aprobación válida para el mismo alcance.
