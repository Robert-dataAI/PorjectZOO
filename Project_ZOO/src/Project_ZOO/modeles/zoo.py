from .animal import Animal

class Zoo:
    def __init__(self, animaux=None):
        if animaux is None:
            self.animaux = []
        else:
            self.animaux = animaux

    # Méthode pour ajouter un animal au zoo
    def ajouter_animal(self, animal):
        if isinstance(animal, Animal):
            self.animaux.append(animal)
        else:
            print("Erreur : l'objet ajouté doit être un Animal.")

    # Surcharge de l'opérateur +
    def __add__(self, autre_zoo):
        if isinstance(autre_zoo, Zoo):
            return Zoo(self.animaux + autre_zoo.animaux)
        return NotImplemented

    # Affichage du contenu du zoo
    def afficher_animaux(self):
        print("Animaux du zoo : ")
        for animal in self.animaux:
            print("-", animal)
