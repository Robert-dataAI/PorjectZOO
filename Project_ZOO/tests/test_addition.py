from Project_ZOO.modeles.animal import Animal
from Project_ZOO.modeles.zoo import Zoo

# Création des animaux
lion = Animal(1.60, 200, "Lion")
tigre = Animal(1.50, 180, "Tigre")
elephant = Animal(3.5,6000,"Éléphant")
girafe = Animal(4.5,1200,"Girafe")

# Création de deux zoos distincts
zoo1 = Zoo([lion, tigre])
zoo2 = Zoo([elephant, girafe])

# Addition des deux zoos
zoo3 = zoo1 + zoo2

# Affichage des trois zoos
print("Premier zoo :")
zoo1.afficher_animaux()

print("\nDeuxième zoo :")
zoo2.afficher_animaux()

print("\nNouveau zoo après addition :")
zoo3.afficher_animaux()
