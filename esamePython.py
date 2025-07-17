# Cristian Istrati SM3201630


#classe ExamException per sollevare eccezioni

class ExamException(Exception):
    pass

#classe CSVTimeSeriesFile per aprire un file .csv ed in base alla città richiesta ritornare 
# una lista di liste contenti data e temperatura per la determinata data
class CSVTimeSeriesFile():

    #inizializzazione tramite la variabile "name"
    def __init__(self,name):
        self.name=name

    #metodo per ricavare i dati
    def get_data(self, città):

        #variabili di supporto
        lista3valori=[]
        listafinish=[]
        
        #provo ad aprire il file, se non ci riesco alza una eccezione
        try:
            file=open(self.name)
            
            #salto la prima riga contenente i headers
            next(file)

            #"pulisco" i dati e aggiungo quelli necessari in una lista
            for riga in file:
                riga_pulita=riga.strip().split(",")
                lista3valori.append([riga_pulita[0],riga_pulita[1],riga_pulita[3]])
            
            #provo a cercare la città richiesta, se non la trovo alzo un eccezione
            try:
                for elemento in lista3valori:
                    if elemento[2]==città:

                        #se la trovo provo a convertire il valore in float, se non ci riesco lo skippo,
                        # se ci riesco lo aggiungo alla lista finale
                        try:
                            elemfloat=float(elemento[1])
                            if isinstance(elemfloat,float):
                                listafinish.append([elemento[0],elemfloat])
                                tmp+=1
                        except:
                            continue
            except Exception:
                raise ExamException("Errore: il nome della città non è presente nel file")
            return listafinish
        except Exception:
            raise ExamException("Errore: impossibile aprire il file")

#----------------------------------------------------------------------------------------------------


def compute_slope(time_series, first_year, last_year):

    #controllo che first_year e  last_year siano degli interi, in altro caso alzo una eccezione
    #se l'anno di partenza è maggiore dell'anno finale ne alzo una
    if not isinstance(first_year, int):
        raise ExamException("first_year tipologia sbagliata")
    if not isinstance(last_year, int):
        raise ExamException("last_year tipologia sbagliata")
    if first_year>=last_year:
        raise ExamException("anno di partenza maggiore di anno finale")
    
    #variabili di appoggio per dopo, la maggior parte, contatori o liste/dizionari temporanei
    dizionario_temporaneo={}
    dizionario_vero={}
    diffanni=last_year-first_year
    tmptemporanee=[]
    listaannomedie=[]
    contatore=0
    sommaAnni=0
    sommaTmpAnni=0


    for i,elemento in enumerate(time_series):

        #voglio ricavare l'anno, quindi pulisco il dato di partenza
        #voglio anche creare una variabile di appoggio "annodopo" per 
        # prendere i valori solo dall'anno necessario e fermarsi prima di "annodopo"
        anno=str(elemento[0]).strip().split("-")[0]

        if i in range(len(time_series)-1):
            annodopo=str(time_series[i+1][0]).strip().split("-")[0]

        tmptemporanee.append(elemento[1])
        if i in range(len(time_series)-1):

            #se ho almeno 6 temperature per anno, metto la lista 
            # delle temperature in un dizionario con chiave il loro anno
            if anno != annodopo:
                if len(tmptemporanee)>=6:
                    dizionario_temporaneo[anno]=tmptemporanee
                    tmptemporanee=[]

    #scelgo nel dizionario temporaneo solo gli anni richiesti e li metto nel dizionario vero
    for i,elemento in enumerate(dizionario_temporaneo):
        first_year=str(first_year)
        if elemento>=first_year and int(elemento)<last_year+1:
            for i in range(diffanni):
                dizionario_vero[elemento]=dizionario_temporaneo[elemento]

    #faccio la media delle temperature e le metto in una 
    # lista di liste che hanno anno, media di temperatura
    for elemento in dizionario_vero:
        somma=0
        conta=0
        for valore in dizionario_vero[elemento]:
            somma+=valore
            conta+=1
        media=somma/conta
        listaannomedie.append([elemento,media])
    
    #calcolo la media degli anni e delle temperature
    for elemento in listaannomedie:
        annoFloat=float(elemento[0])
        sommaTmpAnni+=elemento[1]
        sommaAnni+=annoFloat
        contatore+=1
    mediaAnni=sommaAnni/contatore
    mediaTmpAnni=sommaTmpAnni/contatore

    #calcolo per il coefficente angolare con le variabili trovare
    for elemento in listaannomedie:
        annoFloat=float(elemento[0])
        totAnniSopra=annoFloat-mediaAnni
        totTmpSopra=elemento[1]-mediaTmpAnni
        totAnniSopraSeconda=totAnniSopra*totAnniSopra
    coefficente_angolare=totAnniSopra*totTmpSopra/totAnniSopraSeconda
    return coefficente_angolare
        


if __name__=="__main__":
    filepath="GlobalLandTemperaturesByMajorCity.csv"
    fileCSV= CSVTimeSeriesFile(filepath)
    print(compute_slope(fileCSV.get_data('Rome'),1920,1940))