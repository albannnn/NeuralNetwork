#implémentation naïve d'un réseaux de neurones
from math import exp 
class Neurone : 
    def __init__(self, poids, seuil, next_couche, previous_couche):
        self.seuil = seuil
        self.poids = poids #tableau
        self.next_couche = next_couche 
        self.previous_couche = previous_couche 

    #getters et setters
    def get_poids(self):
        return self.poids
    def get_seuil(self): 
        return self.seuil 
    def set_poids(self, new_poids): 
        self.poids = new_poids 
    def set_seuil(self, new_seuil):
        self.seuil = new_seuil

class Couche: 
    def __init__(self, next, previous, bias):
        self.next_couche = next
        self.previous_couche = previous 
        self.bias = bias
        

def sigmoide(x, cte): 
    sig = 1 / (1+ exp(-cte*x))
    return sig 