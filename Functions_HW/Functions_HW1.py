def letters_range(start , end = None , step = None ):
	alphabet =['a','b','c','d','e','f','g','h','i','j','k','l','m',
			   'n','o','p','q','r','s','t','u','v','w','x','y','z']
	start_point = 0
	end_point = len(alphabet)
	steps = 1	
	if start : 
		start_point = alphabet.index(start)
		if end :
			pass
		else:
			start_point = 0
			end_point = alphabet.index(start)
	if end :
		end_point = alphabet.index(end)
	if step:
		steps = step
	if type(steps) == dict:
		for letter in steps:
			alphabet[alphabet.index(letter)] = steps[letter]
		steps = 1
	print(alphabet[start_point:end_point:steps])
	
letters_range('b', 'w', 2)			
letters_range('g')
letters_range('g', 'p')
letters_range('g', 'p', {'l': 7, 'o': 0})
letters_range('p', 'g', -2)
letters_range('a')
		
