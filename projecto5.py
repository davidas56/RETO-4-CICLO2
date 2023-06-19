import random

def jugar_ahorcado():
    palabras = ['gato', 'perro', 'raton', 'elefante', 'tigre']
    palabra_secreta = random.choice(palabras)
    intentos = 6
    letras_adivinadas = []
    
    print("¡Bienvenido al juego de ahorcado!")
    
    while intentos > 0:
        print("\n")
        for letra in palabra_secreta:
            if letra in letras_adivinadas:
                print(letra, end=" ")
            else:
                print("_", end=" ")
        
        letra_usuario = input("\n\nIngrese una letra: ")
        
        if letra_usuario in letras_adivinadas:
            print("Ya has adivinado esa letra. ¡Intenta con otra!")
            continue
        
        letras_adivinadas.append(letra_usuario)
        
        if letra_usuario not in palabra_secreta:
            intentos -= 1
            print("Letra incorrecta. Te quedan", intentos, "intentos.")
        
        if all(letra in letras_adivinadas for letra in palabra_secreta):
            print("\n¡Felicidades! ¡Has adivinado la palabra!")
            break
    
    if intentos == 0:
        print("\n¡Oh no! Has perdido. La palabra secreta era", palabra_secreta)

# Ejecutar el juego
jugar_ahorcado()
