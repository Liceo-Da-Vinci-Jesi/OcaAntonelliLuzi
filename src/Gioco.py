#Gioco dell'oca classi

class Giocatore:
    def __init__(self,nome,icona):
        self.nome=nome
        self.posizione=(0,0)
        self.icona=icona
        
    def __str__(self):
        s="Benvenuto/a "+self.nome
        return s