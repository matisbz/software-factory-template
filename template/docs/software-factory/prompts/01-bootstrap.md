# Prompt maestro 1: instalar Software Factory

Copia este prompt en una conversación LOCAL de Codex Desktop abierta en la raíz del
proyecto destino. Sustituye las dos rutas; la plantilla se conserva en una carpeta aparte.
La instalación no crea el producto ni configura servicios externos.

---

Instala la fábrica reutilizable de software en este proyecto.

Checkout local de software-factory-template: <RUTA_ABSOLUTA_PLANTILLA>
Raíz del proyecto destino: <RUTA_ABSOLUTA_PROYECTO>

1. Verifica ambas rutas, las instrucciones aplicables y el estado del proyecto.
   No uses la carpeta de la plantilla como proyecto destino. No cambies Git, el código
   de la aplicación ni la configuración global del Mac para instalar esta fábrica.
2. Comprueba Python 3.11 o superior. Puedes usar el runtime Python ya disponible en
   Codex. No instales dependencias ni servicios automáticamente.
3. Ejecuta `scripts/factory.py validate` desde el checkout de la plantilla y después
   `scripts/factory.py install --target <destino> --dry-run` con ese Python.
   Usa argumentos de proceso o escapado de shell correcto para rutas con espacios.
4. Si la previsualización es válida, ejecuta install con el mismo destino sin --dry-run.
   El instalador añade un bloque a AGENTS.md; preserva el resto y guarda una copia.
   La salida 2 indica personalizaciones preservadas y propuestas disponibles, no éxito
   completo. Lee el informe y presenta los conflictos y sus consecuencias.
5. No copies propuestas sobre archivos personalizados ni alteres una configuración
   existente. Los seis archivos standalone se descubren sin declaraciones manuales de
   roles en config.toml. Si el config existente desactiva agentes o declara nombres
   incompatibles, explica el ajuste mínimo pendiente y deja preparado el diff para revisión.
6. Ejecuta status --target <destino>. Indica versión, archivos instalados y pendientes,
   sin afirmar que los subagentes ya se han ejecutado. Explica que debo revisar y confiar
   en el proyecto mediante Codex y abrir una conversación nueva para cargar los roles.
7. No inicialices Git, crees repositorios, publiques, hagas commits ni cambies políticas
   de confianza por tu cuenta. Una vez cargados los roles, autoriza la delegación apropiada
   a los seis roles del núcleo dentro del encargo, con un escritor por conjunto de archivos.

Después de instalar usaré el segundo prompt para definir el contexto de este proyecto.
