import csv

domandeRecanati=[]
domandeRoma=[]

def load():
    file=open("domande.csv")
    lettore=csv.DictReader(file,delimiter="/")

    for riga in lettore:
        if riga["Argomento"] == "Recanati":
            domandeRecanati.append(riga)
        if riga["Argomento"] == "Roma":
            domandeRoma.append(riga)
        
    file.close()
    
load()