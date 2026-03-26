# Enigma Python

Petit projet Python qui simule le fonctionnement de la machine Enigma.  
Le programme permet de chiffrer un message avec des rotors, un réflecteur et un plugboard.

## Utilisation

Lancer le programme :

``` bash
python userInterface.py
```


Ensuite :

Entrer un message  
Choisir les rotors  
Définir leur position et leur anneau  
Configurer la table de connexion (optionnel)

Le message chiffré s’affiche à la fin.

## Fichiers
encryption.py : logique du chiffrement  
userInterface.py : interface en console  
setup.py : création d’un exécutable (optionnel)  

## Notes
Seules les lettres A-Z sont chiffrées  
Les espaces et caractères spéciaux sont conservés  
Avec la même configuration, il est possible de déchiffrer un message  

## Build (optionnel)

``` bash
pip install cx_Freeze
python setup.py build
```
