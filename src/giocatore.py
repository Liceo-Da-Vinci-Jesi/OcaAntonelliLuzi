#Gioco dell'oca classi

class Giocatore:
    def __init__(self,nome,posizione,icona):
        self.nome=nome
        self.posizione=posizione
        self.icona=icona
        
    def __str__(self):
        s="Benvenuto giocatore "+self.nome
        return s