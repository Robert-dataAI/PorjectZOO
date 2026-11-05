class Animal:

    def __init__(self, taille: float, poids: float, name: str = ''):
        self.taille = taille
        self.poids = poids
        self.name = name

    def __str__(self):
        return f"{self.name} ({self.taille})"

    def montrer_information(self):
        return f"Les attibuts du Animal sont Nom: {self.name} - taille: {self.taille} mètres - poids: {self.poids} kgrs"

    def se_deplacer(*args):
        pass
