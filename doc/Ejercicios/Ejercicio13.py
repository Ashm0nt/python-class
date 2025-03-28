#Ejercicio 13: Contar nucleótidos en cada secuencia

#Pide al usuario que ingrese varias secuencias de ADN separadas por comas.
sequences = input("Ingrese las secuencias de ADN separadas por comas: ").upper().split(",")

#Contar nucleótidos en cada secuencia
count = [f"A: {sequence.count('A')}, T: {sequence.count('T')}, C: {sequence.count('C')}, G: {sequence.count('G')}" for sequence in sequences]


#Imprimir el resultado
print (count)