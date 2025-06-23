def conta_tanto(frase):
    count = frase.lower().count("tanto")
    nuova_frase = "Io ti voglio " + "tanto " * (count + 1) + "bene <3 <3 <3"
    return nuova_frase
frase_input = input("Inserisci una frase: ")
risultato = conta_tanto(frase_input)
print(risultato)