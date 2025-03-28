#Ejercicio 12: Encontrar secuencias que contengan un codón de parada

#Pide al usuario que ingrese varias secuencias de ADN separadas por comas.
sequences = input("Ingrese las secuencias de ADN separadas por comas: ").upper().split(",")


#Codones de parada
sequences_stop = [sequence.strip() for sequence in sequences if "TAA" in sequence or "TAG" in sequence or "TGA" in sequence]

#Imprimir el resultado

print(f"Las secuencias que contienen un codón de parada son: {sequences_stop}")

#Otra version
#stop_codons = ["TAA", "TAG", "TGA"]
#sequences_stop =[sequence for sequence in sequences if any(codon in sequence for codon in stop_codons)]