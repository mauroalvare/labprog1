from game import ejecutar_juego
from palabras import obtener_palabra

# EJERCICIO 1
def generar_pista(palabra):
    """
    Dada una palabra, devolver un string con letras y guiones.
    Ejemplo:
    "python" -> "p _ t _ o _"
    """
    
    pista = ""

    for i in range(len(palabra)):

        if i % 2 == 0:
            pista += palabra[i]
        else:
            pista += "_"

        if i != len(palabra) - 1:
            pista += " "

    return pista


# EJERCICIO 2
def verificar_palabra(palabra, intento):
    """
    Debe devolver True si el intento es correcto, False si no.
    """
    return palabra.lower() == intento.lower()

# Ejercicio 3
def calcular_puntaje(tiempo_restante, intentos_restantes):
    
    return tiempo_restante * 10 + intentos_restantes * 20

# Ejercicio Adicional
def actualizar_pista(pista: str, palabra):
   def actualizar_pista(pista, palabra):

    nueva_pista = ""

    indice_letra = 0
    reemplazado = False

    for i in range(len(pista)):

        if pista[i] == "_" and reemplazado == False:
            nueva_pista += palabra[indice_letra]
            reemplazado = True

        else:
            nueva_pista += pista[i]

        if pista[i] != " ":
            indice_letra += 1

    return nueva_pista


# ---------------- MAIN ----------------
palabra = obtener_palabra()

ejecutar_juego(
    palabra,
    generar_pista,
    verificar_palabra,
    actualizar_pista,
    calcular_puntaje
)