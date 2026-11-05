from .animal import Animal

class Serpent(Animal):

    def __init__(self, taille, poids, name, espece: str, poison: bool):
        super().__init__(taille, poids, name)

        self.espece = espece
        self.__poison = poison

    def get_poison(self):
         return self.__poison

    def set_poison(self, poison):
         self.__poison = poison

    def montrer_information(self):
            return f"Les attibuts du Animal sont Nom: {self.name} - taille: {self.taille} mètres - poids: {self.poids} kgrs - Espéce: {self.espece} - Venimeuse: {self.get_poison()}"

 #   def montre_espece(self):
 #       return f"L'espèce est: {self.espece} "

    def se_deplacer(*args):
        return f"Je rampe \n"

