#Gioco dell'oca classi

class Giocatore:
    def __init__(self,nome,icona,posizione):
        self.nome=nome
        self.posizione=posizione
        self.icona=icona
        self.casella=0
        self.punteggio=0
        
    def __str__(self):
        s = "Benvenuto " + self.nome #" con posizione " + str(self.posizione) + ", con icona " + self.icona + " e nella casella " + str(self.casella)
        return s