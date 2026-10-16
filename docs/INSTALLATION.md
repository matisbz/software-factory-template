# Instalación y actualizaciones seguras

Requisitos: Python 3.11+, Codex Desktop con soporte para agentes standalone y una
cuenta con acceso a Codex. El instalador usa solo biblioteca estándar, archivos locales
y el destino explícito. No necesita red, permisos administrativos, Git ni un SDK.
Si `python3` es antiguo o macOS pide una licencia pendiente de Xcode, usa el Python
ya disponible en Codex. No aceptes licencias ni instales herramientas por la fábrica.

## Política de propiedad

| Situación | Resultado |
| --- | --- |
| Archivo ausente, nunca instalado | Crear |
| Contenido igual al de la plantilla | Reconocer como gestionado |
| Gestionado, sin cambios locales | Actualizar, con copia previa |
| Personalizado y upstream sin novedades | Conservar como customized |
| Personalizado con novedades o colisión inicial | Conservar; guardar propuesta upstream |
| Archivo borrado tras instalar | Respetar el borrado; no recrear automáticamente |
| Contexto existente o personalizado | Conservar siempre |
| Archivo retirado de una versión futura | Conservar; marcar como retirado |
| AGENTS.md existente sin bloque | Añadir bloque; guardar original |
| AGENTS.md con bloque personalizado | Conservar bloque y resto; proponer nueva versión |

`docs/project/CONTEXT.md` es un archivo de inicialización (`seed`). Nunca se actualiza,
aunque todavía coincida con el ejemplo. AGENTS.md usa propiedad por bloque y otros
archivos usan huellas SHA-256 completas. Conserva el manifiesto de instalación en Git.
No contiene secretos ni rutas absolutas del usuario.

## Revisar conflictos

La salida 2 indica que se conservó alguna personalización o borrado y que existe una
propuesta en `.software-factory/proposals/<sha256>/<ruta>`. Cada propuesta se identifica
por contenido: repetir la operación no crea duplicados. No está activada en Codex.

Compara la propuesta con tu archivo y fusiona solo lo que necesites en tu editor.
Si decides adoptar exactamente la propuesta, vuelve a ejecutar update para reconocer
su nueva huella. Si fusionas parcialmente, el archivo continúa siendo personalizado y
se preservará en futuras actualizaciones; no hace falta adoptar todo el contenido.
Para config.toml, mantén modelo, permisos, proveedores, comentarios y ajustes existentes.
En versiones actuales los agentes se descubren por sus propios TOML, no por incluir
seis declaraciones manuales en el config. Revisa cualquier ajuste que los desactive.

## Recuperación

Cada reemplazo y ampliación guarda el contenido anterior bajo
`.software-factory/backups/<identificador>/`. Localiza la copia correspondiente y
restaura solo el archivo o bloque necesario, preservando ediciones posteriores.
No hay una orden automática de rollback que pueda pisar trabajo nuevo.
También se guarda el manifiesto anterior antes de actualizarlo.
Los archivos de copia y propuesta se crean con permisos 600 y sus carpetas nuevas
con permisos 700 para limitar su lectura a tu usuario local.

La operación es atómica **por archivo**, no una transacción de todo el proyecto.
Si el proceso se interrumpe, puede haber cambios parciales. Revisa el informe y copias;
repetir install/update reconocerá contenido ya aplicado y preservará lo que no coincida.
Un cierre abrupto puede dejar `.software-factory/.install.lock`. Comprueba que no haya
un instalador activo (el archivo owner indica su PID) antes de retirar ese bloqueo.
El programa no lo elimina automáticamente.

## Garantías y límites

Se valida el payload completo y su integridad antes de instalar. Se rechazan rutas
que escapen del destino, enlaces simbólicos dentro de rutas usadas, archivos donde
se esperan directorios y manifiestos inválidos. El bloqueo impide dos instaladores
a la vez; se comprueba el contenido antes de cada sustitución.

No modifiques archivos afectados mientras se instala. No protege contra un proceso
malicioso con acceso al mismo sistema de archivos, ni contra la edición deliberada
de las huellas del manifiesto. SHA-256 detecta divergencias; no firma ni autentica un
checkout descargado. Obtén la plantilla del repositorio privado y una versión conocida.
No ofrece soporte para destinos en redes con semánticas de bloqueo distintas de las
carpetas locales de macOS. No borra archivos de usuario ni gestiona su repositorio Git.

Dry-run y status solo leen. Las carpetas creadas vacías o el directorio interno pueden
permanecer después de un error de instalación; no se limpia contenido ajeno.
