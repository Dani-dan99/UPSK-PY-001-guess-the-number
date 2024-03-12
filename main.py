import random

def guessTheNumber():
    return random.randint(1, 100)

def guess(playerNumber, secretNumber):
    if playerNumber == secretNumber:
        return '¡Yay! Es el número, lograste adivinarlo', True
    elif playerNumber > secretNumber:
        return 'El número ingresado es más alto de lo esperado, prueba de nuevo', False
    else:
        return 'El número ingresado es más bajo de lo esperado, prueba de nuevo', False

def playerTurn():
    playerInput = input("Bienvenido¡Es tu turno! Adivina el número que hay entre 1 y 100, ingresa tu número, por favor: ")
    try:
        playerNumber = int(playerInput)
        return playerNumber
    except ValueError:
        print("Por favor, ingresa un número válido.")
        return playerTurn()

def computerTurn(secretNumber):
    computerNumber = random.randint(1, 100)
    print(f'El ordenador elige el número {computerNumber}')
    result, correct = guess(computerNumber, secretNumber)
    print(result)
    return correct

def playAgain():
    while True:
        play_again = input("¿Quieres jugar de nuevo? (s/n): ").lower()
        if play_again == 's':
            return True
        elif play_again == 'n':
            return False
        else:
            print("Por favor, responde 's' para sí o 'n' para no.")

def main():
    while True:
        secretNumber = guessTheNumber()
        attempts = 0
        
        while True:
            playerNumber = playerTurn()
            attempts += 1
            result, correct = guess(playerNumber, secretNumber)
            print(result)

            if correct:
                print(f'¡Felicidades! Lograste adivinar el número en {attempts} intentos.')
                break

            computerCorrect = computerTurn(secretNumber)
            attempts += 1

            if computerCorrect:
                print(f'¡El ordenador logró adivinar el número en {attempts} intentos!')
                break
        
        if not playAgain():
            break


if __name__ == "__main__":
    main()
