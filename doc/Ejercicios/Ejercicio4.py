#Ejercicio 4 Eliminar adpatadores de secuencias

#Leer el archivo de entrada
input_file = "4_input_adapters.txt"
output_file = "4_output_adapters.txt"

with open(input_file, "r") as infile, open (output_file, "w") as outfile:
    for line in infile:
        #Cortar adaptadores de la secuencia 4_input_adapters.txt
        secuencia_limpia = line.strip()[14:]

        #Manda la salida a un archivo 4_input_no_adapters.txt
        outfile.write(f"(secuencia_limpia)\n")

        #Opcion alterna 
        #print (secuencia_limpia, file=outfile, end="\n")
