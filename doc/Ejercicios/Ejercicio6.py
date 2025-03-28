#Ejercicio 6 Contar lienas en un archivo FASTA

# Lee el archivo de entrada dna_sequences.fa
input_file = "dna_sequences.fa"
with open(input_file, "r") as infile:
    lines = infile.readlines()
    #Cuenta cuántas secuencias hay en el archivo (líneas que comienzan con >)
    lines_filtred =[line for line in lines if line.startswith(">")]
    print(f"El archivo {input_file} tiene {len(lines_filtred)} secuencias.")