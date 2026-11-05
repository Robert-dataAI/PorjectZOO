from .animal import Animal

class Oiseu(Animal):

    def __init__(self, taille, poids, name, couleur: str, altitude_max: float):
        super().__init__(taille, poids, name)

        self.couleur = couleur
        self.altitude_max = altitude_max
        

    def montrer_information(self):
        return f"Les attibuts du Animal sont Nom: {self.name} - taille: {self.taille} Centimetre - poids: {self.poids} grs - Couleur: {self.couleur} - Altitude Maximale: {self.altitude_max} Metres"

    def se_deplacer(*args):
        return f"Je vole"
