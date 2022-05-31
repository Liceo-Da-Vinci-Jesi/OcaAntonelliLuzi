import csv

def load():
    file = open( "domande.csv" , "r")
    lettore = csv.DictReader(file,delimiter = " ")
    domandeCanti=[]
    for riga in lettore:
        if riga["Argomento"] == "Canti":
            print(riga)
    file.close()
    
    return

load()