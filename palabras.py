import requests
import random

PALABRAS_FALLBACK = [
    "python",
    "computadora",
    "teclado",
    "pantalla",
    "programacion",
    "variable",
    "funcion",
    "bucle",
    "condicion",
    "archivo",
    "servidor",
    "cliente",
    "red",
    "datos",
    "algoritmo",
    "memoria",
    "proceso",
    "sistema",
    "software",
    "hardware"
]


def _palabra_valida(palabra):
    return len(palabra) > 5 and " " not in palabra


def obtener_palabra():
    try:
        for _ in range(20):
            response = requests.get("https://random-word-api.herokuapp.com/word?lang=es", timeout=5)
            palabra = response.json()[0].lower()
            if _palabra_valida(palabra):
                return palabra
    except:
        pass
    fallback = [p for p in PALABRAS_FALLBACK if _palabra_valida(p)]
    return random.choice(fallback)
