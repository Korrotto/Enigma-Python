from encryption import Rotor, buildPlugboard, encryptMessage
import msvcrt


def getNumber(message: str, minValue: int, maxValue: int) -> int:
    while True:
        value = input(message).strip()

        if not value.isdigit():
            print("Entez un nombre.")
            continue

        number = int(value)

        if minValue <= number <= maxValue:
            return number

        print(f"Entrez un nombre entre {minValue} et {maxValue}.")

def getLetter(message: str) -> str:
    while True:
        letter = input(message).strip().upper()

        if len(letter) == 1 and 'A' <= letter <= 'Z':
            return letter

        print("Entrez une lettre (A-Z).")

def getMessage() -> str:
    while True:
        message = input("Entrez un texte: ").strip()

        if message:
            return message

        print("Le texte ne peut pas être vide.")

def chooseRotor(positionName: str, usedRotors: set[int]) -> Rotor:
    print(f"\n--- Rotor {positionName} ---")

    while True:
        rotorNumber = getNumber("Choix rotor (1-5): ", 1, 5)
        rotorId = rotorNumber - 1

        if rotorId in usedRotors:
            print("Rotor déjà utilisé.")
            continue

        usedRotors.add(rotorId)
        break

    rotorPosition = getNumber("Position rotor (1-26): ", 1, 26) - 1
    ringLetter = getLetter("Lettre anneau (A-Z): ")
    ringPosition = ord(ringLetter) - ord("A")

    return Rotor(rotorId, rotorPosition, ringPosition)

def setupPlugboard() -> dict[str, str]:
    print("\n--- Configuration tableau de connexion ---")

    pairCount = getNumber("Nombre de paires (0-10): ", 0, 10)

    pairs: list[tuple[str, str]] = []
    usedLetters: set[str] = set()

    for i in range(pairCount):
        while True:
            entry = input(f"Paire {i + 1} (A-B): ").strip().upper()

            if len(entry) != 3 or entry[1] != '-':
                print("Format incorrect.")
                continue

            left, right = entry[0], entry[2]

            if left == right:
                print("Ne pas utiliser deux fois la même lettre.")
                continue

            if left in usedLetters or right in usedLetters:
                print("Lettre déjà utilisé.")
                continue

            usedLetters.update([left, right])
            pairs.append((left, right))
            break

    return buildPlugboard(pairs)

def setupMachine():
    print("\n=== Configuration Machine ===")

    usedRotors: set[int] = set()

    leftRotor = chooseRotor("gauche", usedRotors)
    middleRotor = chooseRotor("centre", usedRotors)
    rightRotor = chooseRotor("droite", usedRotors)

    plugboard = setupPlugboard()

    rotors = [rightRotor, middleRotor, leftRotor]

    return rotors, plugboard

def showTitle():
    print(r'''
███████╗███╗   ██╗██╗ ██████╗ ███╗   ███╗ █████╗ 
██╔════╝████╗  ██║██║██╔════╝ ████╗ ████║██╔══██╗
█████╗  ██╔██╗ ██║██║██║  ███╗██╔████╔██║███████║
██╔══╝  ██║╚██╗██║██║██║   ██║██║╚██╔╝██║██╔══██║
███████╗██║ ╚████║██║╚██████╔╝██║ ╚═╝ ██║██║  ██║
╚══════╝╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝                                                                                               
''')

def main():
    showTitle()

    message = getMessage()
    rotors, plugboard = setupMachine()

    encryptedMessage = encryptMessage(message, rotors, plugboard)

    print("\n--- Résultat ---")
    print(encryptedMessage)
    
    print("\nAppuyez sur une touche pour quitter...")
    msvcrt.getch()

if __name__ == "__main__":
    main()