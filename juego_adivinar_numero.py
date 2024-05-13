import random

def juego_adivinar_numero():
    numero_secreto = random.randint(1, 100)
    intentos_maximos = 5
    intentos_realizados = 0

    print("¡Bienvenido al juego de adivinar el número!")
    print("Tienes que adivinar un número entre 1 y 100.")
    print(f"Tienes un máximo de {intentos_maximos} intentos.")

    while intentos_realizados < intentos_maximos:
        try:
            intento = int(input(f"Intento {intentos_realizados + 1}/{intentos_maximos} - Ingresa un número entre 1 y 100: "))
            if intento < 1 or intento > 100:
                print("Por favor, ingresa un número dentro del rango especificado.")
                continue
            
            intentos_realizados += 1

            if intento == numero_secreto:
                print(f"¡Felicidades! Adivinaste el número en {intentos_realizados} intentos.")
                break
            elif intento < numero_secreto:
                print("El número es mayor.")
            else:
                print("El número es menor.")

        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número entero.")

    if intentos_realizados == intentos_maximos and intento != numero_secreto:
        print(f"Lo siento, has perdido. El número secreto era {numero_secreto}.")

if __name__ == "__main__":
    juego_adivinar_numero()
