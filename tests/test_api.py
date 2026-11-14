import logging
import requests


def test_obtener_publicacion():
    try:
        logging.info("Inicio de consulta API: GET /posts/1")
        respuesta = requests.get("https://jsonplaceholder.typicode.com/posts/1", timeout=15)
        logging.info("GET /posts/1 respondió con HTTP %s", respuesta.status_code)

        assert respuesta.status_code == 200
        assert "application/json" in respuesta.headers["Content-Type"]

        datos = respuesta.json()
        assert isinstance(datos, dict)
        assert datos["id"] == 1
        assert datos["userId"] == 1
        assert "title" in datos
        assert "body" in datos
        logging.info("Publicación comprobada. Código HTTP y datos JSON correctos")
    except Exception:
        logging.exception("Falló la consulta GET /posts/1")
        raise


def test_obtener_tarea():
    try:
        logging.info("Inicio de consulta API: GET /todos/1")
        respuesta = requests.get("https://jsonplaceholder.typicode.com/todos/1", timeout=15)
        logging.info("GET /todos/1 respondió con HTTP %s", respuesta.status_code)

        assert respuesta.status_code == 200
        assert "application/json" in respuesta.headers["Content-Type"]

        datos = respuesta.json()
        assert isinstance(datos, dict)
        assert datos["id"] == 1
        assert datos["userId"] == 1
        assert datos["title"] == "delectus aut autem"
        assert datos["completed"] is False
        logging.info("Tarea comprobada. Código HTTP y datos JSON correctos")
    except Exception:
        logging.exception("Falló la consulta GET /todos/1")
        raise


def test_publicacion_inexistente():
    try:
        logging.info("Inicio del caso negativo API: GET /posts/999999")
        respuesta = requests.get("https://jsonplaceholder.typicode.com/posts/999999", timeout=15)
        logging.info("GET /posts/999999 respondió con HTTP %s", respuesta.status_code)

        assert respuesta.status_code == 404
        logging.info("Recurso inexistente comprobado con el HTTP 404 esperado")
    except Exception:
        logging.exception("Falló la comprobación GET /posts/999999")
        raise


def test_crear_publicacion():
    try:
        logging.info("Inicio de creación API: POST /posts")
        publicacion = {
            "title": "Prueba del curso",
            "body": "Contenido de prueba",
            "userId": 1
        }
        respuesta = requests.post("https://jsonplaceholder.typicode.com/posts", json=publicacion, timeout=15)
        logging.info("POST /posts respondió con HTTP %s", respuesta.status_code)

        assert respuesta.status_code == 201
        assert "application/json" in respuesta.headers["Content-Type"]

        datos = respuesta.json()
        assert isinstance(datos, dict)
        assert datos["id"] == 101
        assert datos["title"] == publicacion["title"]
        assert datos["body"] == publicacion["body"]
        assert datos["userId"] == publicacion["userId"]
        logging.info("Creación comprobada. Los datos recibidos coinciden con los enviados")
    except Exception:
        logging.exception("Falló la solicitud POST /posts")
        raise


def test_eliminar_publicacion():
    try:
        logging.info("Inicio de eliminación API: DELETE /posts/1")
        respuesta = requests.delete("https://jsonplaceholder.typicode.com/posts/1", timeout=15)
        logging.info("DELETE /posts/1 respondió con HTTP %s", respuesta.status_code)

        assert respuesta.status_code == 200
        assert "application/json" in respuesta.headers["Content-Type"]

        datos = respuesta.json()
        assert isinstance(datos, dict)
        assert datos == {}
        logging.info("Eliminación comprobada. Se recibió el objeto JSON vacío esperado")
    except Exception:
        logging.exception("Falló la solicitud DELETE /posts/1")
        raise
