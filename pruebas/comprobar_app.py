from pathlib import Path
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from functools import partial
from threading import Thread
from tempfile import TemporaryDirectory
from playwright.sync_api import sync_playwright, expect

servidor = ThreadingHTTPServer(('127.0.0.1', 0), partial(SimpleHTTPRequestHandler, directory=str(Path(__file__).resolve().parents[1])))
Thread(target=servidor.serve_forever, daemon=True).start()
URL = f'http://127.0.0.1:{servidor.server_port}/'
with sync_playwright() as p, TemporaryDirectory(prefix='mi-dia-prueba-') as perfil:
    def abrir():
        return p.chromium.launch_persistent_context(perfil, executable_path='/usr/bin/chromium', headless=True, args=['--no-sandbox'], viewport={'width':1280,'height':1000}, locale='es-ES')
    contexto = abrir()
    page = contexto.pages[0]
    errores=[]
    page.on('pageerror', lambda e: errores.append(str(e)))
    page.route('**/*.js', lambda route: route.abort())
    page.goto(URL)
    expect(page.locator('script[src]')).to_have_count(0)
    expect(page.locator('#inicio-aviso')).to_be_hidden()
    expect(page.locator('#estado-inicio')).to_have_text('Lista para usar')
    expect(page.locator('html')).to_have_attribute('lang','es')
    expect(page.locator('#vacio')).to_be_visible()
    campo=page.get_by_label('¿Qué quieres hacer hoy?')
    campo.fill('   ')
    page.get_by_role('button', name='Agregar tarea').click()
    expect(page.locator('.tarea')).to_have_count(0)
    assert campo.evaluate('(e) => e.validationMessage') == 'Escribe una tarea antes de agregarla.'
    for texto in ['Salir a caminar', '<img src=x onerror=alert(1)>']:
        campo.fill(texto)
        if texto == 'Salir a caminar':
            page.get_by_role('button', name='Agregar tarea').click()
        else:
            campo.press('Enter')
    expect(page.locator('#confirmacion')).to_have_text('Tarea agregada: <img src=x onerror=alert(1)>')
    expect(page.locator('.tarea')).to_have_count(2)
    expect(page.locator('#lista img')).to_have_count(0)
    page.get_by_role('checkbox',name='Salir a caminar').check()
    expect(page.locator('#resumen')).to_have_text('1 pendiente')
    expect(page.locator('#progreso-texto')).to_have_text('1 de 2 completadas')
    page.get_by_role('button',name='Pendientes',exact=True).click()
    expect(page.locator('.tarea')).to_have_count(1)
    page.get_by_role('button',name='Completadas',exact=True).click()
    expect(page.get_by_role('checkbox',name='Salir a caminar')).to_be_checked()
    page.get_by_role('checkbox',name='Salir a caminar').click()
    expect(page.locator('.tarea')).to_have_count(0)
    expect(page.locator('#vacio')).to_be_visible()
    page.get_by_role('button',name='Todas',exact=True).click()
    page.get_by_role('checkbox',name='Salir a caminar').check()
    page.reload()
    expect(page.locator('.tarea')).to_have_count(2)
    expect(page.get_by_role('checkbox',name='Salir a caminar')).to_be_checked()
    contexto.close()
    contexto=abrir()
    page=contexto.pages[0]
    page.goto(URL)
    expect(page.locator('.tarea')).to_have_count(2)
    expect(page.get_by_role('checkbox',name='Salir a caminar')).to_be_checked()
    page.get_by_role('button',name='Eliminar tarea: <img src=x onerror=alert(1)>',exact=True).click()
    page.reload()
    expect(page.locator('.tarea')).to_have_count(1)
    for width in [1280,390,320]:
        page.set_viewport_size({'width':width,'height':900})
        assert page.evaluate('document.documentElement.scrollWidth <= window.innerWidth'), f'Desbordamiento a {width}'
        expect(page.get_by_role('button', name='Agregar tarea')).to_be_visible()
    page.screenshot(path='/tmp/mi-dia-celular.png',full_page=True)
    page.set_viewport_size({'width':1280,'height':1000})
    page.screenshot(path='/tmp/mi-dia-escritorio.png',full_page=True)
    page.get_by_role('button',name='Eliminar tarea: Salir a caminar',exact=True).click()
    expect(page.locator('#confirmacion')).to_have_text('Tarea eliminada: Salir a caminar')
    expect(page.locator('#vacio')).to_be_visible()
    expect(page.locator('#nueva-tarea')).to_be_focused()
    page.evaluate("localStorage.setItem('mi-dia.tareas.v1', '{roto')")
    page.reload()
    expect(page.locator('#aviso')).to_contain_text('No pudimos recuperar')
    page.evaluate("() => { Storage.prototype.setItem = () => { throw new Error('Bloqueado') }; }")
    page.locator('#nueva-tarea').fill('Tarea temporal')
    page.locator('#nueva-tarea').press('Enter')
    expect(page.locator('.tarea')).to_have_count(1)
    expect(page.locator('#aviso')).to_contain_text('El navegador no permite guardar')
    assert not errores, errores
    contexto.close()
    sin_js = p.chromium.launch(executable_path='/usr/bin/chromium', headless=True, args=['--no-sandbox'])
    pagina_sin_js = sin_js.new_page(java_script_enabled=False)
    pagina_sin_js.goto(URL)
    expect(pagina_sin_js.locator('#inicio-aviso')).to_be_visible()
    expect(pagina_sin_js.locator('#nueva-tarea')).to_be_disabled()
    expect(pagina_sin_js.get_by_role('button', name='Agregar tarea')).to_be_disabled()
    sin_js.close()
    print('CORRECTO: versión integrada sin peticiones JS externas, alta con clic y Enter, aviso si JavaScript está deshabilitado; agregar, rechazar espacios, completar/desmarcar, filtros, progreso, recarga, cierre y reapertura, eliminación persistente, texto seguro, datos corruptos, almacenamiento bloqueado, foco y diseños de 1280/390/320 px.')
