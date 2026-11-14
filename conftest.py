import base64
from datetime import datetime
from pathlib import Path
import re
import warnings

import pytest
import pytest_html
from selenium.common.exceptions import WebDriverException


@pytest.fixture
def capturar_fallo(request):
    def guardar_captura(driver):
        try:
            carpeta = Path(__file__).parent / "reports" / "screenshots"
            carpeta.mkdir(parents=True, exist_ok=True)
            nombre = re.sub(r"[^a-zA-Z0-9_-]", "_", request.node.name)
            fecha = datetime.now().astimezone().strftime("%Y-%m-%d_%H-%M-%S_%f")
            archivo = carpeta / f"{nombre}_{fecha}.png"

            imagen = driver.get_screenshot_as_png()
            archivo.write_bytes(imagen)
            request.node.captura_base64 = base64.b64encode(imagen).decode("ascii")
        except (WebDriverException, OSError) as error:
            warnings.warn(f"No se pudo guardar la captura: {error}", RuntimeWarning)

    return guardar_captura


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    resultado = yield
    reporte = resultado.get_result()
    imagen = getattr(item, "captura_base64", None)

    if reporte.when == "call" and reporte.failed and imagen:
        extras = getattr(reporte, "extras", [])
        extras.append(pytest_html.extras.png(imagen, name="Captura del fallo"))
        reporte.extras = extras
