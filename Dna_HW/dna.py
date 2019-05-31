dna = open('dna.fasta.txt', 'r')

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
	num_of_nucleotides = {'A':0,'T':0,'C':0,'G':0}
	n=0
	for line in dna:
		if line[0] != '>':
			n=1
			for letter in line:
				if letter == 'A':
					num_of_nucleotides['A'] = num_of_nucleotides['A'] + 1 
				elif letter == 'T':
					num_of_nucleotides['T'] = num_of_nucleotides['T'] + 1
				elif letter == 'C':
					num_of_nucleotides['C'] = num_of_nucleotides['C'] + 1
				elif letter == 'G':
					num_of_nucleotides['G'] = num_of_nucleotides['G'] + 1
		elif n!=0:
			for key,val in num_of_nucleotides.items(): 
				num_of_nucleotides_file.write('{}:{}'.format(key,val)+' ')
			num_of_nucleotides_file.write('\n')
			num_of_nucleotides_file.write(line + 'Nucleotides count:\n')
			num_of_nucleotides = {'A':0,'T':0,'C':0,'G':0}
		elif n==0:
			num_of_nucleotides_file.write(line + 'Nucleotides count:\n')
	for key,val in num_of_nucleotides.items(): 
			num_of_nucleotides_file.write('{}:{}'.format(key,val)+' ')
	return num_of_nucleotides_file
	num_of_nucleotides_file.close()


dna = open('dna.fasta.txt', 'r')
count_nucleotides(dna)
dna.close()


def translate_rna_to_protein(rna):
	rna_codon = open('rna_codon_table.txt' , 'r') 
	rna_codon_table = {}
	n = 0
	key = ''
	for line in rna_codon:
		for letter in line:		
			if letter != ' ' and n == 1:
				rna_codon_table[key.strip()] = letter.strip()
				key = ''
				n = 0
			elif letter == ' ':
				n += 1
			elif letter != ' ':
				key += letter
				n = 0
	rna_codon.close()
	nucliotide_count = 0
	nucliotide = ''
	protein = open('protein.txt' , 'w')
	for line in rna:
		if line[0] != '>':
			nucliotide_count = 0
			nucliotide = ''
			for letter in line:
				nucliotide += letter
				nucliotide_count += 1 		
				if 	nucliotide_count == 3	:
					for key in rna_codon_table.keys():
						if key == nucliotide:
							protein.write(rna_codon_table[key]+'-')
							nucliotide_count = 0
							nucliotide = ''
		elif line[0] == '>': protein.write('\n' + line + 'Protein chain' + '\n')
	protein.close()
	rna.close()


rna = open('rna.txt', 'r')
translate_rna_to_protein(rna)
rna.close()
