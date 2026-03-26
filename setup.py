from cx_Freeze import setup, Executable

setup(
    name="Enigma",
    version="1.0",
    description="Reproduction du chiffrement de la machine Enigma",
    executables=[Executable("userInterface.py")]
)