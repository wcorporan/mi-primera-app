# Mi día · Tareas diarias

Aplicación en español para agregar, completar, volver a marcar como pendiente y eliminar tareas. Incluye filtros y una barra de progreso. Se adapta a computadoras y celulares.

Está hecha con HTML, CSS y JavaScript: no necesitas instalar paquetes ni crear una cuenta. Funciona sin Internet.

## Descargar esta versión desde GitHub

Esta versión está preparada en la rama `mi-dia-corregida-20261103`. En GitHub selecciona esa rama y pulsa **Code → Download ZIP**. Extrae el ZIP y abre `index.html` con Edge o Chrome. Al pie debe decir **Versión 1.1 · Lista para usar**. La descarga de `main` no incluirá estos cambios hasta que se combine la rama.

## Verla en tu laptop ASUS (Windows)

Si los archivos todavía están solo en Codex, primero guárdalos en GitHub con los pasos de la siguiente sección.

1. Abre `wcorporan/mi-primera-app` en GitHub y selecciona la rama donde guardaste la aplicación.
2. Pulsa **Code** (Código) → **Download ZIP** (Descargar ZIP).
3. Busca el ZIP en **Descargas**, haz clic derecho y elige **Extraer todo**.
4. Abre la carpeta extraída y haz doble clic en **index.html**. Si Windows pregunta con qué abrirlo, elige Edge o Chrome.
5. Escribe una tarea y pulsa **Agregar tarea** o Enter. Marca su casilla para completarla y pulsa la papelera para eliminarla.

Usa siempre la misma carpeta y el mismo navegador/perfil para volver a tu lista. Las tareas se guardan con `localStorage` en ese navegador; no se envían a GitHub ni se sincronizan entre dispositivos. Al borrar datos del navegador o usar el modo privado puedes perderlas. El almacenamiento de archivos locales depende del navegador: si aparece un aviso de guardado, usa el servidor local descrito más abajo.

## Guardar los cambios en GitHub

### Sin usar comandos

Si descargaste el ZIP preparado por Codex, extráelo y abre tu repositorio en GitHub. Selecciona **Add file** → **Upload files** y arrastra los dos archivos de la aplicación (`index.html` y `README.md`), sin la carpeta contenedora. Escribe un mensaje como «Crear aplicación de tareas diarias» y pulsa **Commit changes**. Esto también actualiza el README existente. Si GitHub te pide crear una rama o solicitud de cambios, sigue ese flujo y combina la solicitud para incorporarla a `main`.

### Desde Codex

Si la interfaz muestra una opción para crear una solicitud de cambios (**Create PR**), úsala después de revisar los archivos. Abre la solicitud en GitHub y pulsa **Merge pull request** para incorporar la aplicación a `main`. Las opciones exactas dependen de la interfaz.

### Con Git desde una terminal

Ejecuta estos comandos dentro de la copia que contiene los archivos nuevos, por ejemplo, en la terminal del entorno de Codex. Una copia antigua descargada desde GitHub no contiene estos cambios.

```bash
cd /workspace/mi-primera-app
git status
git switch -c app-tareas-diarias
git add -A
git commit -m "Crear aplicación de tareas diarias en español"
git push -u origin app-tareas-diarias
```

Si la rama ya existe, usa `git switch app-tareas-diarias` en lugar de crearla de nuevo. Si Git pide tu identidad para el primer commit, configura tu propio nombre y correo con `git config user.name "Tu nombre"` y `git config user.email "tu-correo"`. Para subir cambios necesitas permiso de escritura.

Después abre GitHub, selecciona **Compare & pull request**, crea la solicitud y pulsa **Merge pull request**. Una vez incorporada a `main`, puedes descargar el ZIP de esa rama en tu ASUS. Guardar archivos en Codex por sí solo no los sube a GitHub.

## Servidor local opcional

Si tienes Python 3, abre una terminal en la carpeta del proyecto y ejecuta:

```bash
python -m http.server 8000 --bind 127.0.0.1
```

En Windows también puedes usar `py -m http.server 8000 --bind 127.0.0.1`. En el navegador escribe la dirección local `http://127.0.0.1:8000`. Detén el servidor con **Ctrl+C**. Conserva el mismo puerto para acceder a la misma lista: las tareas de este modo son independientes de las guardadas al abrir el archivo directamente.

## Archivos

- `index.html`: aplicación completa; incluye el diseño y el JavaScript. Puedes abrir este único archivo sin dependencias.
- `README.md`: instrucciones.

## Comprobación manual

Agrega dos tareas, completa una, prueba los tres filtros, recarga y comprueba que se conservan. Elimina una y vuelve a recargar para confirmar que sigue eliminada. Comprueba también que no se admiten tareas vacías y que la página se adapta al estrechar la ventana.


## Corrección de carga de JavaScript

La versión inicial cargaba el diseño y el comportamiento desde archivos separados. Si `app.js` no se cargaba, el diseño aparecía pero los controles quedaban sin activar. Ese escenario se reprodujo bloqueando la petición del archivo; no confirma por sí solo la causa en una laptop concreta.

Ahora todo está integrado en `index.html`, con el JavaScript al final del documento, después de los controles. No se necesita `app.js` ni `estilos.css`. El formulario permanece desactivado hasta que termine la inicialización y muestra un aviso si JavaScript no se ejecuta, en lugar de aparentar que está listo.

Para actualizar, cierra la versión anterior y reemplaza su `index.html` por el nuevo en la misma carpeta. Después vuelve a abrirlo con el mismo navegador y perfil. La clave de almacenamiento se mantiene para conservar las tareas existentes. No borres los datos del navegador. Los archivos antiguos `app.js` y `estilos.css`, si aún están en tu laptop, ya no se utilizan.

Las vistas previas de archivos pueden bloquear JavaScript. Descarga el archivo y ábrelo en una pestaña normal de Edge o Chrome. Si el aviso de inicio sigue visible, comprueba que JavaScript esté permitido. Si el navegador bloquea el almacenamiento local, se mostrará un aviso y los cambios solo durarán durante la sesión.


## Identificar la descarga actual

La versión actual muestra **Versión 1.1 · Lista para usar** al pie de la página una vez que el formulario está conectado. Al agregar una tarea aparece una confirmación debajo del campo. Si no ves la versión 1.1, estás abriendo una copia anterior.

Ambas descargas (`mi-dia.zip` y `mi-dia-corregida.zip`) se actualizan con la misma aplicación. Extrae el ZIP antes de abrirlo y sustituye el `index.html` anterior en la misma carpeta para mantener su ubicación de almacenamiento.

## Prueba automatizada para desarrollo

`pruebas/comprobar_app.py` usa Python, Playwright y Chromium. Con esas herramientas instaladas, ejecútalo desde el proyecto:

```bash
python3 pruebas/comprobar_app.py
```

La prueba usa un servidor local temporal y un perfil de navegador de prueba. Comprueba clic y Enter, completar/desmarcar, filtros, eliminar, persistencia tras cerrar y reabrir Chromium, almacenamiento bloqueado, JavaScript deshabilitado y tamaños de pantalla. No usa las tareas personales del navegador. No necesitas estas herramientas para utilizar la aplicación.
