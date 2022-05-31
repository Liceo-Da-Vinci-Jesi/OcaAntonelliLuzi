import csv

domandeRecanati=[]
domandeRoma=[]
domandeMilano = []
domandeBologna=[]
domandeFirenze=[]
domandePisa=[]
domandeNapoli=[]
domandeCanti=[]
domandeOperette=[]
domandeZibaldone=[]

def load():
    file=open("domande.csv")
    lettore=csv.DictReader(file,delimiter="/")

    for riga in lettore:
        if riga["Argomento"] == "Recanati":
            domandeRecanati.append(riga)
        if riga["Argomento"] == "Roma":
            domandeRoma.append(riga)
        if riga["Argomento"] == "Milano":
            domandeMilano.append(riga)
        if riga["Argomento"] == "Bologna":
            domandeBologna.append(riga)
        if riga["Argomento"] == "Firenze":
            domandeFirenze.append(riga)
        if riga["Argomento"] == "Pisa":
            domandePisa.append(riga)
        if riga["Argomento"] == "Napoli":
            domandeNapoli.append(riga)
        if riga["Argomento"] == "Canti":
            domandeCanti.append(riga)
        if riga["Argomento"] == "Operette":
            domandeOperette.append(riga)
        if riga["Argomento"] == "Zibaldone":
            domandeZibaldone.append(riga)
        
    file.close()