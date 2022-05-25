#Gioco dell'oca classi

class Giocatore:
    def __init__(self,nome,icona,posizione):
        self.nome=nome
        self.posizione=posizione
        self.icona=icona
        self.casella=0
        
    def __str__(self):
        s = "Giocaotore di nome " + self.nome + " con posizione " + str(self.posizione) + ", con icona " + self.icona + " e nella casella " + str(self.casella)
        return s


if __name__ == "__main__":
    prova = Giocatore("Paolo", "pippo.png", 2)
    print(prova)
    
    # sposto di una casella...
    prova.casella += 1
    print(prova)
    
    