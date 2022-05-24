#Gioco dell'oca classi

class Giocatore:
    def __init__(self,nome,icona,posizione):
        self.nome=nome
        self.posizione=posizione
        self.icona=icona
        self.casella=0
        
    def __str__(self):
        s="Benvenuto/a "+self.nome
        return s