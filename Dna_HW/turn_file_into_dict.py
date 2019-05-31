def turn_file_into_dict(file_):
	_dict = {}
	n = 0
	key = ''
	for line in file_:
		for letter in line:		
			if letter != ' ' and n == 1:
				_dict[key.strip()] = letter.strip()
				key = ''
				n = 0
			elif letter == ' ':
				n += 1
			elif letter != ' ':
				key += letter
				n = 0
	return(_dict)
	file_.close()	
