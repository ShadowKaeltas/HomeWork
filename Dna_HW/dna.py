def translate_from_dna_to_rna(dna):
	rna_file = open('rna1.txt' , 'w') 
	rna_file.write(dna.read().replace('T' , 'U'))
	rna_file.close()
	
	
dna = open('dna.fasta.txt', 'r')
translate_from_dna_to_rna(dna)
dna.close()


def count_nucleotides(dna):
	num_of_nucleotides_file = open('num_of_nucleotides.txt' , 'w')
	n,T,A,G,C = 0,0,0,0,0
	for line in dna:
		if line[0] != '>':
			T += line.count('T')
			A += line.count('A')
			C += line.count('C')
			G += line.count('G')
			n =1
		elif n :
			output_='A-' + str(A) + ' C-' + str(C)+ ' G-' + str(G) + ' T-' + str(T)
			T,A,G,C = 0,0,0,0
			num_of_nucleotides_file.write(output_)
	output_='A-' + str(A) + ' C-' + str(C)+ ' G-' + str(G) + ' T-' + str(T)
	num_of_nucleotides_file.write('\n' + output_)

		
dna = open('dna.fasta.txt', 'r')
count_nucleotides(dna)
dna.close()


from turn_file_into_dict import turn_file_into_dict


def translate_rna_to_protein(rna_):
	rna_codon = open('rna_codon_table.txt' , 'r') 
	codon_dict = turn_file_into_dict(rna_codon)
	protein = open('protein.txt' , 'w')	
	for line in rna:
		if line[0] != '>':
			nucliotide = ''
			for letter in line:
				nucliotide += letter		
				if len(nucliotide) == 3:
					protein.write(codon_dict[nucliotide] + '-')
					nucliotide = ''
		else: protein.write('\n')
	 

rna = open('rna.txt', 'r')
translate_rna_to_protein(rna)
rna.close()
