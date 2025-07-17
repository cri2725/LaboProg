"""
import random
class Person():
    def __init__(self,name,surname):
        self.name=name
        self.surname=surname
    def __str__(self):
        return f"sono {self.name} {self.surname}"
    def saluto_salutone(self):
        n=random.randint(0,2)
        if n==0:
            return f"ciao hai beccato {n} e ciao"
        elif n==1:
            return f"ciao hai beccato {n} e ciaone"
        else:
            return f"ciao hai beccato {n} e ciaonene"
class Student(Person):
    def __str__(self):
        return f"ciao sono {self.name} {self.surname} e sono uno studente"

na="Paolo"
sur="Rossi"
persona=Person(na,sur)
print(f"il nome è {persona.name}")
print(f"il cognome è {persona.surname}")
print(persona)
print(persona.saluto_salutone())
nom="gino"
cogn="peppino"
studente=Student(nom,cogn)
print(studente)
print(studente.saluto_salutone())
"""
"""
Create un oggetto CSVFile che rappresenti un file CSV, e che:
    1. venga inizializzato sul nome del file csv, e
    2. abbia un attributo “name” che ne contenga il nome
    3. abbia un metodo “get_data()” che torni i dati dal file CSV come lista di liste,
    ad es: [ [’01-01-2012’, ’266.0'] , [’01-02-2012’, ’145.9’], ... ]
"""
"""
class CSVfile():
    def __init__(self,nomeFile):
        if not isinstance(nomeFile,str):
            raise TypeError(f"{nomeFile} non è una stringa")
        self.name=nomeFile
    def get_data(self,start=None,end=None):
        lista_dati=[]
        try:
            with open("/home/cri2725/programmazione/LaboProg/CSVfiles/"+self.name, "r") as file:
                if start is None and end is None:
                    for elmento in file:
                        rigapulita=elmento.strip().split(",")
                        if rigapulita[0] != "Date":
                            lista_dati.append(rigapulita)
                else:
                    end=str(end)
                    start=str(start)
                    end=end.strip()
                    start=start.strip()
                    try:
                        fine=int(end)
                        inizio=int(start)
                    except TypeError:
                        print("tipo sbagliato per start o end")
                    if fine < 0 or inizio < 0:
                        raise ValueError("start o end minori di zero")
                    if fine < inizio:
                        raise ValueError("fine minore dell'inizio")
                    for i,riga in enumerate(file):
                        if i<inizio:
                            continue
                        if i>fine:
                            break
                        rigapulita=riga.strip().split(",")
                        if rigapulita[0] != "Date":
                            lista_dati.append(rigapulita)
        except IOError as erroreIO:
            print(f"file non esistente | impossibile leggere il file {erroreIO}")
        return lista_dati
class NumericalCSVFile(CSVfile):
    def __init__(self,nomeFile):
        super().__init__(nomeFile)
    def get_data(self,start,end):
        dati_figlio=[]
        dati_genitore=super().get_data(start,end)
        for elemento in dati_genitore:
            try:
                elementonumerico=float(elemento[1])
            except ValueError:
                print("Errore")
            dati_figlio.append([elemento[0], elementonumerico])
        return dati_figlio
file="shampoo_sales.csv"
filecsvshampoo=CSVfile(file)
fcsvshampoonum=NumericalCSVFile(file)
print(f" {filecsvshampoo.get_data()}")
print(f"{fcsvshampoonum.get_data(3,5)}")
"""
"""
Esercizio 2: Classe Veicolo
Scrivete una classe denominata Veicolo che disponga di questi attributi dati:
    modello (per il modello del veicolo);
    marca (per la marca del veicolo);
    anno (per l'anno del veicolo).
    speed (per la velocità del veicolo)
E di questi metodi:
    __init__ che accetti come argomenti l'anno, il modello, e la marca. 
        Il metodo dovrebbe inoltre assegnare 0 all'attributo dati speed.
    __str__ che restituisce una stringa con i dettagli del veicolo (marca, modello, anno e velocità)
    accelerare che aggiunge 5 all'attributo dati speed ogni volta che viene chiamato.
    frenare che sottrae 5 dall'attributo dati speed ogni volta che viene chiamato.
    get_speed che restituisce la velocità corrente.
"""
"""
class Veicolo():
    def __init__(self, modello,marca,anno):
        self.modello=modello
        self.marca=marca
        self.anno=anno
        self.speed=0
    def __str__(self):
        return f"il veicolo è il modello {self.modello} della {self.marca} e del {self.anno} e va a {self.speed}"
    def accelerare(self):
        self.speed+=5
    def frenare(self):
        self.speed-=5
    def get_speed(self):
        return self.speed
"""
"""
macchina=Veicolo("Punto","Fiat","2009")
print(macchina)
macchina.accelerare();macchina.accelerare()
print(macchina)
print(macchina.get_speed())
"""
"""
Esercizio 3
- Crea una sottoclasse auto che ha in aggiunta l'attributo numero_porte 
e cambia il metodo __str__ di conseguenza
- Crea una sottoclasse moto che ha in aggiunta l'attributo tipo 
(ad esempio, "Sportiva" o "Touring") e cambia il metodo __str__ di conseguenza
"""
"""
class auto(Veicolo):
    def __init__(self, modello,marca,anno,numero_porte):
        super().__init__(modello,marca,anno)
        self.numero_porte=numero_porte
    def __str__(self):
        return super().__str__() + f" ed ha {self.numero_porte} porte"
macchina=auto("Punto","Fiat","2009",4)
print(macchina)
class moto(Veicolo):
    def __init__(self, modello,marca,anno,tipo):
        super().__init__(modello,marca,anno)
        self.tipo=tipo
    def __str__(self):
        return super().__str__()+f" ed è del tipo {self.tipo} "
motorino=moto("modelloahha","Ducati","2015","Sportiva")
print(motorino)
"""