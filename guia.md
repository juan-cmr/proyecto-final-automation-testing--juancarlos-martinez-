# Guía rápida de uso

1. Tener Python y Firefox instalados y conexión a internet. Abrir una terminal en la carpeta principal del proyecto, donde están `pytest.ini` y `requirements.txt`.

2. Instalar las dependencias.

   ```powershell
   python -m pip install -r requirements.txt
   ```

3. Ejecutar las pruebas.

   ```powershell
   python -B -m pytest tests/ -v
   ```

4. Abrir `reports/reporte.html` en el navegdor. Revisar el resultado y desplegar las filas para consultar los mensajes y la información de los fallos

5. Si alla una prueba UI, consultar la captura integrada al reporte y el PNG guardado en `reports/screenshots/` con el nombre de la prueba y la fecha y la hora.

El README explica los casos automatizados y los comandos para ejecutar UI o API por separado.
