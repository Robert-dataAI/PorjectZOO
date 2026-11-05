from src.Project_ZOO.modeles.animal import Animal
from src.Project_ZOO.modeles.serpent import Serpent
from src.Project_ZOO.modeles.oiseau import Oiseu


def main():

    # Solicitar la edad (convertida a número entero)
    taille = float(input("Taille de l'animal: "))
    # Solicitar la altura (convertida a número decimal, ej: 1.75)
    poids = float(input("Poids de l'animal: "))
    animal = Animal(taille, poids)


    print(animal.montrer_information())


    # Solicitar la edad (convertida a número entero)
    taille = float(input("Taille de la serpent: "))
    # Solicitar la altura (convertida a número decimal, ej: 1.75)
    poids = float(input("Poids de la serpent: "))
    # Solicitar la altura (convertida a número decimal, ej: 1.75)
    espece = str(input("Espèce animal: "))
    #poison = bool(input("Serpent venimeux: "))
    animal2 = Serpent(taille, poids, espece, False)
    animal2.set_poison(True)
    

    print(animal2.montrer_information())
    print(animal2.se_deplacer())

    # Solicitar la edad (convertida a número entero)
    taille = float(input("Taille de l'oiseau: "))
    # Solicitar la altura (convertida a número decimal, ej: 1.75)
    poids = float(input("Poids de l'oiseau: "))
    # Solicitar la altura (convertida a número decimal, ej: 1.75)
    espece = str(input("Espèce de l'oiseau: "))
    altitude_max = float(input("Altitude maximale de vol: "))
    

    animal3 = Oiseu(taille, poids, espece, altitude_max)

    print(animal3.montrer_information())
    print(animal3.se_deplacer())


if __name__ == "__main__":
    main()