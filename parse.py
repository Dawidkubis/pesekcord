import re

def parse(enms, string):
	s = [i.strip() for i in string.split() if i != '']

	result = []
	
	for i in enms:
		if i[0] == '{' and i[-1] == '}':
			i = i[1:-1]
			result.append([x for x in s if re.fullmatch(i, x)])
			s = [x for x in s if not re.fullmatch(i, x)]
		else:
			s = [x for x in s if not re.fullmatch(i, x)]
	
	if s != []:
		print(f'error : {s}')

	return result
