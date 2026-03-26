REFLECTOR_TABLE: str = 'YRUHQSLDPXNGOKMIEBFZCWVJAT'

ROTOR_TABLE: tuple[str,str,str,str,str] = (
    'EKMFLGDQVZNTOWYHXUSPAIBRCJ',
    'AJDKSIRUXBLHWTMCQGZNPYFVOE',
    'BDFHJLCPRTXVZNYEIWGAKMUSQO',
    'ESOVPZJAYQUIRHXLNFTGKDCMWB',
    'VZBRGITYUPSDNHLXAWMJQOFECK')

ROTOR_TABLE_REVERSE: tuple[str,str,str,str,str] = (
    'UWYGADFPVZBECKMTHXSLRINQOJ',
    'AJPCZWRLFBDKOTYUQGENHXMIVS',
    'TAGBPCSDQEUFVNZHYIXJWLRKOM',
    'HZWVARTNLGUPXQCEJMBSKDYOIF',
    'QCYLXWENFTZOSMVJUDKGIARPHB')

NOTCH: tuple[int,int,int,int,int] = (16,4,21,9,25)

class Rotor:
    def __init__(self, id: int, rotorPosition: int, ringPosition: int) -> None:
        self.id: int = id
        self.rotorTable: str = ROTOR_TABLE[id]
        self.rotorTableReverse: str = ROTOR_TABLE_REVERSE[id]
        self.notch: int = NOTCH[id]
        self.rotorPosition: int = rotorPosition % 26
        self.ringPosition: int = ringPosition % 26
    
    def step(self) -> None:
        self.rotorPosition = (self.rotorPosition + 1) % 26

    def atNotch(self) -> bool:
        return self.rotorPosition == self.notch
    
    def translate(self, letter: str, reverse: bool) -> str:
        offset: int = (self.rotorPosition - self.ringPosition) % 26
        inputIndex: int = (letterToInt(letter) + offset) % 26

        if reverse:
            mappedLetter: str = self.rotorTableReverse[inputIndex]
        else:
            mappedLetter: str = self.rotorTable[inputIndex]
            
        outputIndex: int = (letterToInt(mappedLetter) - offset) % 26
        return intToLetter(outputIndex)

def letterToInt(letter: str) -> int:
    return ord(letter.upper()) - ord("A")

def intToLetter(number: int) -> str:
    return chr(number + ord("A"))

def stepRotors(rotors: list[Rotor]) -> None:
    rotorsToStep: list[bool] = [False] * len(rotors)
    rotorsToStep[0] = True

    for i in range(len(rotors) - 1):
        if rotors[i].atNotch():
            rotorsToStep[i] = True
            rotorsToStep[i + 1] = True

    for rotor, rotate in zip(rotors, rotorsToStep):
        if rotate:
            rotor.step()

def reflectorTranslation(letter: str) -> str:
    return REFLECTOR_TABLE[letterToInt(letter)]

def buildPlugboard(letterPairs: list[tuple[str, str]]) -> dict[str, str]:
    plugboard: dict[str, str] = {}

    for left, right in letterPairs:
        left = left.upper()
        right = right.upper()

        if left == right:
            raise ValueError("Une paire ne peut pas contenir deux fois la même lettre.")

        if left in plugboard or right in plugboard:
            raise ValueError("Une lettre est déjà utilisée dans une autre paire.")

        plugboard[left] = right
        plugboard[right] = left

    return plugboard

def plugboardTranslation(letter: str, plugboard: dict[str, str]) -> str:
    return plugboard.get(letter, letter)

def rotorsTranslation(letter: str, rotors: list[Rotor], reverse: bool) -> str:
    rotorPath = reversed(rotors) if reverse else rotors

    for rotor in rotorPath:
        letter = rotor.translate(letter, reverse)

    return letter

def encryptLetter(letter: str, rotors: list[Rotor], plugboard: dict[str, str]) -> str:
    stepRotors(rotors)
    letter = plugboardTranslation(letter, plugboard)
    letter = rotorsTranslation(letter, rotors, False)
    letter = reflectorTranslation(letter)
    letter = rotorsTranslation(letter, rotors, True)
    letter = plugboardTranslation(letter, plugboard)

    return letter

def encryptMessage(message: str, rotors: list[Rotor], plugboard: dict[str, str]) -> str:
    result: list[str] = []

    for char in message.upper():
        if 'A' <= char <= 'Z':
            result.append(encryptLetter(char, rotors, plugboard))
        else:
            result.append(char)

    return ''.join(result)