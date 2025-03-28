#Ejercicio 11: Invertir secuencias de ADN

#Pide al usuario que ingrese varias secuencias de ADN separadas por comas.
sequences = input("Ingrese las secuencias de ADN separadas por comas: ").split(",")

#Invertir las secuencias 
sequences_inverted = [sequence[::-1].strip() for sequence in sequences]

print(f"Las secuencias invertidas son: {sequences_inverted}")