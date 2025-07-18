from palabras_ahorcado import palabras
import random

def palabra_valida(lista):
    palabra = random.choice(lista)
    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(lista)
    
    return palabra.upper()


def ahorcado():
    print("JUEGO DEL AHORCADO")
    palabra = palabra_valida(palabras)

    


    word_try = input("ingresa una letra:")
    if len(word_try) >= 2  and len(word_try) == 0:
        print("intento no valido pierdes una vida")