import csv

def load():
    file = open( "domande.csv" , "r")
    lettore = csv.DictReader(file,delimiter = "/")
    domandeTot = {}
    for riga in lettore:
        if riga["Argomento"] not in domandeTot:
            domandeTot[riga["Argomento"]] = []
        domandeTot[riga["Argomento"]].appen((riga["Argomento"], riga["Domanda"], riga["RispostaA"], riga["RispostaB"], riga["RispostsC"], riga["RispostaEsatta"]))
    file.close()
    
    return domandeTot


class elencodomande:
    def __init__(self):
        self.listaDomande = load()
        return

if __name__ == "__main__":
    e = elencodomande()
    print(e.listaDomande)
    for n in e.listaDomande:
        print(n)