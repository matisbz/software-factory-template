# Historial de versiones

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
