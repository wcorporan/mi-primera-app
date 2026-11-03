# Publicar Mi Día y compartirla por WhatsApp

La rama `mi-dia-corregida-20261103` está preparada para GitHub Pages. `index.html` contiene la aplicación completa y `.nojekyll` indica que se sirvan los archivos estáticos directamente. No requiere compilación ni paquetes.

## Activar el sitio en GitHub

Estos pasos los realiza una persona con permiso para cambiar la configuración del repositorio. La preparación de archivos y su subida no activan Pages por sí solas.

1. Abre [la configuración de Pages](https://github.com/wcorporan/mi-primera-app/settings/pages) e inicia sesión si te lo pide.
2. Busca **Build and deployment** (Compilación e implementación).
3. En **Source** (Origen), selecciona **Deploy from a branch** (Implementar desde una rama).
4. En **Branch** (Rama), elige **mi-dia-corregida-20261103**. No selecciones `main`: la aplicación está en la rama corregida.
5. En la carpeta, selecciona **/ (root)** (raíz).
6. Pulsa **Save** (Guardar).
7. Espera a que termine la publicación. Puedes revisar su estado en la pestaña **Actions** (Acciones). No es necesario crear otro archivo de flujo de trabajo.
8. Regresa a **Settings → Pages**. Cuando GitHub muestre el sitio publicado, pulsa **Visit site** (Visitar sitio). Usa el enlace que muestre GitHub.

La dirección prevista, después de una publicación correcta y sin un dominio personalizado, es:

https://wcorporan.github.io/mi-primera-app/

Esta dirección prevista no demuestra que el sitio esté activo. Confírmalo con **Visit site** y las pruebas de abajo.

Si no aparece la opción de publicar, comprueba tu permiso de administración y la disponibilidad de Pages para la visibilidad del repositorio y el plan de GitHub. No hace falta cambiar la visibilidad a público sin revisar esa decisión. Si GitHub muestra un error, conserva el mensaje para diagnosticarlo.

## Comprobar el sitio publicado

1. Abre **Visit site** y comprueba **Versión 1.1 · Lista para usar** al pie.
2. Agrega una tarea con el botón y otra con Enter.
3. Completa una y elimina la otra.
4. Cierra y vuelve a abrir el enlace en el mismo navegador y perfil. La tarea restante debe seguir guardada con su estado.
5. Abre el enlace en tu celular y comprueba el diseño y los botones.

Si aparece un error 404, comprueba que la publicación terminó y que seleccionaste la rama corregida con la carpeta raíz. La dirección necesita el tramo `/mi-primera-app/`; no basta con abrir el dominio del usuario.

## Enviar por WhatsApp

Desde el celular, abre el sitio publicado y usa **Compartir → WhatsApp**, o copia la dirección y pégala en una conversación. También puedes pegarla en WhatsApp Web desde tu laptop. Envía el enlace del sitio publicado, no una dirección que empiece por `file:`, la ruta de tu laptop ni el enlace al código en GitHub.

Ejemplo de mensaje, una vez comprobada la publicación:

> Te comparto Mi Día, una aplicación sencilla para organizar tareas. Ábrela aquí: https://wcorporan.github.io/mi-primera-app/

Cada persona tendrá su propia lista guardada en su navegador. No se comparten tus tareas ni se sincronizan listas entre usuarios. En el celular, abrir el enlace en Edge, Chrome o Safari de forma habitual ayuda a volver al mismo almacenamiento; la vista interna de WhatsApp puede usar un contexto diferente.

## Tus tareas anteriores y las actualizaciones

Las tareas guardadas al abrir el archivo de tu laptop no aparecen automáticamente en el sitio web. Son ubicaciones de almacenamiento distintas. Para utilizar el sitio con las tareas anteriores, tendrás que agregarlas de nuevo; la versión actual no incluye importación.

Después de activar Pages con esta rama, los cambios que se suban a ella podrán publicarse automáticamente. El código del sitio y los archivos publicados serán accesibles conforme a la configuración de Pages; las tareas personales permanecen en el navegador.

## Estado de la preparación

- Preparado: aplicación estática sin dependencias externas, archivo `.nojekyll` e instrucciones.
- Comprobación local: el flujo de tareas se valida también bajo la ruta `/mi-primera-app/`.
- Pendiente: activar Pages en GitHub y comprobar el sitio real con **Visit site**. La API de GitHub no fue accesible desde el entorno de trabajo, por lo que no se confirmó la configuración ni la publicación remota.
