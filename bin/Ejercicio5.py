#Ejercicio 5: Convertir de tsv a fasta

#Lee el archivo de entrada dna_sequences.txt
input_file = "dna_sequences.txt"
output_file = "dna_sequences.fa"
with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    for line in infile:
        #Convertir las secuencias en formato tsv dna_sequences.txt a formato fasta.
        id, seq=line.strip().split("\t")

        #Guarda las secuencias en un archivo dna_sequences.fa
        outfile.write(f">{id}\n{seq.upper()}\n")