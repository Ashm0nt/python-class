#Ejercicio 9: Transformar secuencias de ADN en ARN 

#Pedir ak usario que ingrese varias secuencias de ADN separadas por comas.
sequences = input("Ingrese las secuencias de ADN separadas por comas: ").split(",")

#Transformar las secuencias de ADN en ARN
sequences_arn =[sequence.replace("T", "U").split() for sequence in sequences]

print(f"Las secuencias de ARN son: {sequences_arn}")

