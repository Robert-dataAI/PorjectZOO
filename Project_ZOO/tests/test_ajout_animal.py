from Project_ZOO.modeles.animal import Animal
from Project_ZOO.modeles.zoo import Zoo

# Création de quelques animaux
lion = Animal(1.60, 200, "Lion")
tigre = Animal(1.50, 180, "Tigre")

# Création d'un zoo avec une liste d'animaux
zoo1 = Zoo([lion])

# Affichage du zoo
zoo1.afficher_animaux()

# Ajout d'un nouvel animal
zoo1.ajouter_animal(tigre)

# Affichage après l'ajout
print("\nAprès l'ajout du tigre :")
zoo1.afficher_animaux()