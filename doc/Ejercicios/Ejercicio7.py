#Ejercicio 7: Extraer los primeros tres nucleótidos de cada secuencia 

#Pedir al usuario que ingrese varias secuencias de ADN separadas por comas.
sequences = input("Ingrese las secuencias de ADN separadas por comas: ").split(",")

codondes_inicio = [sequence.strip()[:3] for sequence in sequences]
print(f"Los primeros tres nucleótidos de cada secuencia son: {codondes_inicio}")

#codondes_inicio = [sequence[:3] for sequence in sequences] cuando no se usan espacios de separacion