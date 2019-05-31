dna = open('dna.fasta.txt', 'r')


from turn_file_into_dict import turn_file_into_dict


def translate_from_dna_to_rna(dna):
	rna = open('rna.txt' , 'w')
	for line in dna:
		if line[0] != '>':
			for letter in line:
				if letter == 'T':
					rna.write('U')
				else:
					rna.write(letter)
		else: rna.write(line.rstrip() + " " + 'RNA:' + '\n')
	return rna
	rna.close()


translate_from_dna_to_rna(dna)
dna.close()


def count_nucleotides(dna):
	num_of_nucleotides_file = open('num_of_nucleotides.txt' , 'w')
	num_of_nucleotides = {}
	for line in dna:
		if line[0] != '>':
			for letter in line:
				if letter != '\n' and ' ':
					num_of_nucleotides[letter] +=  1
		else:
			if num_of_nucleotides:
				for key,val in num_of_nucleotides.items(): 
					num_of_nucleotides_file.write('{}:{}'.format(key,val)+' ' + '\n')
			num_of_nucleotides_file.write(line + 'Nucleotides count:\n')
			num_of_nucleotides = {'A':0,'T':0,'C':0,'G':0}
	for key,val in num_of_nucleotides.items(): 
			num_of_nucleotides_file.write('{}:{}'.format(key,val) + ' ' + '\n')
	return num_of_nucleotides_file
	num_of_nucleotides_file.close()


dna = open('dna.fasta.txt', 'r')
count_nucleotides(dna)
dna.close()


def translate_rna_to_protein(rna_):
	rna_codon = open('rna_codon_table.txt' , 'r') 
	codon_dict = turn_file_into_dict(rna_codon)
	protein = open('protein.txt' , 'w')
	for line in rna:
		if line[0] != '>':
			nucliotide_count = 0
			nucliotide = ''
			for letter in line:
				nucliotide += letter
				nucliotide_count += 1 		
				if 	nucliotide_count == 3	:
					for key in codon_dict.keys():
						if key == nucliotide:
							protein.write(codon_dict[key]+'-')
							nucliotide_count = 0
							nucliotide = ''
		else: protein.write('\n' + line + 'Protein chain' + '\n')
	protein.close()
	rna.close()


rna = open('rna.txt', 'r')
translate_rna_to_protein(rna)
rna.close()
