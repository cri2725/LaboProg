"""
variabile="bob"
try:
    float(variabile)
except Exception as eccezione:
    print("non posso farlo")
    print(f"valeva {variabile}")
    print(f"l'errore trovato è {eccezione}")
""" 
"""
try:
    with open("/home/cri2725/programmazione/LaboProg/CSVfiles/testoProva.txt", "r") as file:
        stringaFile=file.read()
        fileParametro=float(stringaFile)
except IOError:
    print("non riesco a leggere il file ")
except ValueError:
    print(f"non posso convertire {stringaFile} in numero")
except Exception:
    print("errore generico")
else:
    parametro=fileParametro
    print(f"il par * 2 è {parametro*2}")
finally:
    print("bob regna ")
"""
