from game import ejecutar_juego
from palabras import obtener_palabra

# EJERCICIO 1
def generar_pista(palabra):
    """
    Dada una palabra, devolver un string con letras y guiones.
    Ejemplo:
    "python" -> "p _ t _ o _"
    """
    myLista = ["_"] * len(obtener_palabra)
    impares = [1,3,5,7,9,11,13,15]

    for i in range (len(obtener_palabra)):
        if i in impares:
            myLista[i] = obtener_palabra[i]
        
    pista = " ".join(myLista)

    return(pista)
    
    pass


# EJERCICIO 2
def verificar_palabra(palabra, intento):
    """
    Debe devolver True si el intento es correcto, False si no.
    """
    pass


def calcular_puntaje(tiempo_restante, intentos_restantes):
    pass

# Ejercicio Adicional
def actualizar_pista(pista: str, palabra):
    # Si me queda una letra por adivinar, no hago nada y devuelvo la misma pista que tenía
    pass


# ---------------- MAIN ----------------
palabra = obtener_palabra()

ejecutar_juego(
    palabra,
    generar_pista,
    verificar_palabra,
    actualizar_pista,
    calcular_puntaje
)