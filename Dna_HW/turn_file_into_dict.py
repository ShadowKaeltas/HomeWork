def turn_file_into_dict(file_):
	_dict = {}
	n = 0
	key = ''
	for line in file_:
		for letter in line:		
			if letter != ' ' and n == 1:
				if 'top' in key:
					_dict[key.strip().strip('top')] = letter.strip()
					_dict[previous_key.strip()] = 'Stop'
				else:
					_dict[key.strip()] = letter.strip()
				previous_key = key
				key = ''
				n = 0
			elif letter == ' ':
				n += 1
			elif letter != ' ':
				key += letter
				n = 0
	return(_dict)
	file_.close()	
