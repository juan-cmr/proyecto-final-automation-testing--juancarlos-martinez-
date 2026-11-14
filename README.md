# Automatización QA - SauceDemo

Este proyecto es parte del trabajo final de automatización de pruebas con Python y Pytest. Uso [SauceDemo](https://www.saucedemo.com/) para comprobar el inicio de sesión, los productos y el carrito. También realizo pruebas API sobre [JSONPlaceholder](https://jsonplaceholder.typicode.com/).

El proyecto ejecuta once casos: seis de interfaz web y cinco de API. Organicé las accciones de cada página en clases usando Page Object Model (POM).


## Herramients utilizadaas

- Pyton para escribir el código.
- Selenium WebDriver y Firefox para interactuar con la página.
- Pytest para ejecutar las pruebas y parametrizar los casos de login.
- Requests para las peticiones API.
- pytest-html para crear el reporte HTML y mostrar las capturas cuando falla una prueba.
- CSV para guardar los datos de login.
- La biblioteca estandar `logging` para registrar los pasos importantes.
- Git para guardar el historial de cambios y GitHub para subir el proyecto.







## Archivos del proyecto

| Archivo o carpeta | Descripción |
| --- | --- |
| `pages/` | Contiene `login_page.py`, `inventory_page.py` y `cart_page.py`, con las acciones de cada página. |
| `tests/` | Contiene `test_login.py`, `test_inventory.py`, `test_cart.py` y `test_api.py`. |
| `data/users.csv` | Guarda los tres conjuntos de datos para el login. |
| `utils/reader.py` | Lee el CSV y devuelve los datos para las pruebas. |
| `conftest.py` | Guarda las capturas cuando falla una prueba UI y las agrega al reporte. |
| `pytest.ini` | Configura qué pruebas se buscan, el reporte y los mensajes de logging. |
| `requirements.txt` | Lista las bibliotecas externas y sus versiones. |
| `reports/` | Guarda `reporte.html` y los PNG en `screenshots/`. |
| `README.md` | Presentación del proyecto. |
| `guia.md` | Instrucciones para preparar y ejecutar el proyecto. |



## Instalación

Primero hay que tener Python y Firefox instalados, además de conexión a internet. Probé el proyecto con Python 3.14.3. Selenium Manager se encarga del controlador de Firefox y puede necesitar descargarlo la primera vez.

Para instalar las bibliotecas de `requirements.txt`, abrir una termnal en la carpeta principal del proyecto y ejecutar:

```powershell
python -m pip install -r requirements.txt
```

Las versiones que usé son Selenium 4.43.0, Pytest 9.1.1, Requests 2.33.1 y pytest-html 4.2.0.

## Ejecución

Dsde la carpeta principal, donde está `pytest.ini`, ejecutar todos los casos.

```powershell
python -B -m pytest tests/ -v
```

Para ejecutar solamente las pruebas UI, usar estos tres archivos.

```powershell
python -B -m pytest tests/test_login.py tests/test_inventory.py tests/test_cart.py -v
```

Para ejecutar solamente las pruebas API, usar este comando.

```powershell
python -B -m pytest tests/test_api.py -v
```

Estos comandos utilizan la configuración de `pytest.ini` y actualizan `reports/reporte.html` con los casos ejecutados.

## Casos de prueba

### Inicio de sesión

En `tests/test_login.py` el login se ejecuta una vez por cada fila de `data/users.csv`. La fila de `standard_user` comprueba el acceso correcto. Después se verifica lo siguiente.

- La dirección contiene `/inventory.html`.
- El logotipo muestra `Swag Labs`.
- El título de la sección muestra `Products`.

Las filas de `admin` y `jose` comprueba que el mensaje de credenciales incorrectas sea visible y tenga el texto que se espera. La prueba usa una espera de 10 segundos y `LoginPage` utiliza esperas explícitas para el formulatio.

### Página de productps

En `tests/test_inventory.py` se inicia sesión y se comprueba lo siguiente.

- El título del navegador es `Swag Labs`.
- La lista tiene al menos un producto.
- El primer producto es `Sauce Labs Backpack` y su precio es `$29.99`.
- El botón del menú y el filtro están visibles.

La segunda prueba selecciona `Price (low to high)`, convierte los precios a numeros y comprueba que estén ordenados de menor a mayor.

### Carrito

En `tests/test_cart.py` se inicia sesión, se guarda el nombre del primer producto y se agrega al carrito. Después se comprueba que el nombre del producto dentro del caito coincida con el que se agregó.

Los tres conjuntos de login, las dos pruebas de inventario y el carrito suman seis ejecuciones UI. Cada ejecución abre Firefox y lo cierra mediante `try/finally`.

### Pruebas API

`tests/test_api.py` contiene cinco pruebas independientes de JSONPlaceholder.

- GET de `/posts/1`, con HTTP 200 y comprobaciones de los datos de la publicación.
- GET de `/todos/1`, con HTTP 200 y comprobaciones del título y estado de la tarea.
- GET de `/posts/999999`, con HTTP 404 para un recurso inexistente.
- POST de `/posts`, con HTTP 201 y comprobación de los datos enviados y del identificador recibido.
- DELETE de `/posts/1`, con HTTP 200 y un objeto JSON vacío, según la respuesta de este servicio.

En las respuestas exitosas, las pruebas leen el JSON y comprueban los datos con `assert`. JSONPlaceholder simula POST y DELETE: devuelve una respuesta, pero no guarda ni elimina realmente las publicaciones.

## Reportes, capturas y logging

Al terminar las pruebas, abrir `reports/reporte.html` con doble clic o desde Firefox. La tabla muestra qué casos se ejecutaron, el resultado y cuánto tardaron. `Passed` significa que las comprobaciones pasaron y `Failed` que hubo un fallo. Al desplegar una fila se pueden ver los mensajes de logging y los detalles del error, si lo hubo.

Cuando falla una prueba UI y el navegador sigue disponible, se guarda un PNG en `reports/screenshots/`. El nombre incluye la prueba, la fecha y la hora. La captura se toma antes de cerrar Firefox y también queda guardada dentro del HTML en base64. Así se puede ver qué mostraba la página cuando ocurrio el fallo.

Los pasos importantes se registran con `logging` y Pytest, como el acceso, los productos y las solicitudes HTTP. Los mensajes quedan en el detalle del reporte.


