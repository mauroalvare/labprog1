from game import ejecutar_juego
from palabras import obtener_palabra


# EJERCICIO 1
def generar_pista(palabra):
    """
    Dada una palabra, devolver un string con letras y guiones.
    Ejemplo:
    "python" -> "p _ t _ o _"

    Criterio: Se muestran las letras en posiciones pares (0, 2, 4, ...)
    y se ocultan las de posiciones impares (1, 3, 5, ...)
    """
    pista = ""
    for i in range(len(palabra)):
        if i % 2 == 0:
            # Posición par: mostrar la letra
            pista += palabra[i]
        else:
            # Posición impar: ocultar con guión
            pista += "_"
        # Agregar espacio entre letras/guiones para mejor legibilidad
        if i < len(palabra) - 1:
            pista += " "
    return pista


# EJERCICIO 2
def verificar_palabra(palabra, intento):
    """
    Debe devolver True si el intento es correcto, False si no.
    Se utiliza lower() para evitar errores por mayúsculas/minúsculas.
    """
    return palabra.lower() == intento.lower()


def calcular_puntaje(tiempo_restante, intentos_restantes):
    """
    Calcula el puntaje según la fórmula:
    puntaje = tiempo_restante * 10 + intentos_restantes * 20

    Esto recompensa terminar rápido y con menos errores.
    """
    puntaje = int(tiempo_restante * 10) + intentos_restantes * 20
    return puntaje


# Ejercicio Adicional
def actualizar_pista(pista: str, palabra):
    """
    Revela una letra oculta en la pista cada vez que el jugador falla.

    Algoritmo:
    1. Buscar todas las posiciones donde hay un guión bajo (_)
    2. Elegir la primera posición con guión bajo
    3. Reemplazarla por la letra correspondiente en la palabra original
    4. Devolver la pista actualizada

    Si no quedan letras por adivinar, devuelve la misma pista.
    """
    # Convertir la pista a lista para poder modificarla
    pista_lista = list(pista)

    # Buscar la primera posición con guión bajo
    for i in range(len(pista_lista)):
        if pista_lista[i] == "_":
            # Encontramos un guión. Ahora necesitamos calcular la posición real en la palabra
            # La pista tiene espacios entre caracteres, así que la posición real es (i // 2)
            posicion_palabra = i // 2

            if posicion_palabra < len(palabra):
                # Reemplazar el guión por la letra de la palabra original
                pista_lista[i] = palabra[posicion_palabra]
            break

    # Convertir la lista de vuelta a string
    pista_actualizada = "".join(pista_lista)
    return pista_actualizada


# ---------------- MAIN ----------------
palabra = obtener_palabra()

ejecutar_juego(
    palabra, generar_pista, verificar_palabra, actualizar_pista, calcular_puntaje
)
