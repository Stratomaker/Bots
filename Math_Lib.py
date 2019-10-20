# coding: utf8
import urllib
import re
import constants as cons

def Request(question):
	#question = raw_input('your question:')

	question = question
	#.replace(',','.')
	fullurl = cons.myurl + urllib.urlencode({'input':question,'appid':cons.mykey})
	print(fullurl)

	xml_tree = urllib.urlopen(fullurl)
	string_tree = xml_tree.read()
	#print(string_tree)
	return string_tree

def Find_Img(source):
	#pics = re.findall(r'Plot.|\n+(http.+)\'', string_tree)
	pics = re.findall(r'Plot[\s\S]+http[^\']+', source)
	pics = ''.join(pics)
	links = re.findall(r'http[^\']+', pics)
	for count in range(len(links)):
		links[count] = links[count].replace('amp;','')
	return links[0]

def Split_String(source):
	#pics = re.findall(r'Plot.|\n+(http.+)\'', string_tree)
	#reqs = re.findall(r'title=\'Input\'[\s\S]+<plaintext>[^\<]+', source)
	pods = source.split('\n')
	for count in range(len(pods)):
		pods[count] = pods[count].strip()
	return pods

def Find_Input(source):
	if "<pod title='Input'" in source:
		pattern = re.compile('<plaintext>.+</plaintext>')
		for count in range(source.index("<pod title='Input'"), len(source)):
			#print(reqs[count])
			if pattern.match(source[count]):
				return source[count].replace('<plaintext>', '').replace('</plaintext>', '')
	else:
		return 'None'

def Find_Roots(source):
	if "<pod title='Roots'" in source:
		tag = "Roots"
	elif "<pod title='Root'" in source:
		tag = "Root"
	elif "<pod title='Real root'" in source:
		tag = "Real root"
	elif "<pod title='Real roots'" in source:
		tag = "Real roots"
	else:
		return 'None'

	roots = list()
	pattern = re.compile("<plaintext>.+</plaintext>")
	stopper = re.compile("<pod title=\'.+\'")
	for count in range(source.index("<pod title=\'" + tag + "\'") + 1, len(source)):
		#print(reqs[count])
		if pattern.match(source[count]):
			roots.append(source[count].replace('<plaintext>', '').replace('</plaintext>', ''))
		elif stopper.match(source[count]):
			break
	return '; '.join(roots)

def Find_Result(source):
	if "<pod title='Result'" in source:
		pattern = re.compile('<plaintext>.+</plaintext>')
		for count in range(source.index("<pod title='Result'"), len(source)):
			#print(reqs[count])
			if pattern.match(source[count]):
				return source[count].replace('<plaintext>', '').replace('</plaintext>', '')
	else:
		return 'None'

def Find_Values(source):
	if "<pod title='Values'" in source:
		tag = 'Values'
	else:
		return 'None'
	pattern_st = re.compile('<plaintext>.+')
	pattern_ed = re.compile('.+</plaintext>')
	for count in range(source.index("<pod title=\'" + tag + "\'"), len(source)):
		#print(source[count])
		if pattern_st.match(source[count]):
			limit = re.findall(r'>(.+)', source[count])
			values = limit[0] + '\n'
			limit = re.findall(r'(.+)<', source[count+1])
			#print(limit)
			return values + limit[0]
	return 'None'

def Find_Decimal(source):
	if "<pod title='Decimal approximation'" in source:
		pattern = re.compile('<plaintext>.+</plaintext>')
		for count in range(source.index("<pod title='Decimal approximation'"), len(source)):
			#print(reqs[count])
			if pattern.match(source[count]):
				return source[count].replace('<plaintext>', '').replace('</plaintext>', '')
	else:
		return 'None'

def Find_Limit(source):
	if "<pod title='Limit'" in source and "<pod title='Limit from the right'" not in source:
		tag = 'Limit'
	elif "<pod title='Limit from the right'" in source:
		tag = 'Limit from the right'
	else:
		return 'None'
	pattern = re.compile('<plaintext>.+</plaintext>')
	for count in range(source.index("<pod title=\'" + tag + "\'"), len(source)):
		#print(reqs[count])
		if pattern.match(source[count]):
			limit = re.findall(r'>.+= (.+)<', source[count])
			return limit[0]
	return 'None'

def Find_Deriva(source):
	if "<pod title='Partial derivatives'" in source:
		tag = 'Partial derivatives'
	else:
		return 'None'
	pattern = re.compile('<plaintext>.+</plaintext>')
	for count in range(source.index("<pod title=\'" + tag + "\'"), len(source)):
		#print(reqs[count])
		if pattern.match(source[count]):
			limit = re.findall(r'>.+=(.+)<', source[count])
			return limit[0]
	return 'None'

def Find_Lmax(source):
	if "<pod title='Local maxima'" in source:
		tag = 'Local maxima'
	elif "<pod title='Local maximum'" in source:
		tag = 'Local maximum'
	else:
		return 'None'
	pattern = re.compile('<plaintext>.+</plaintext>')
	for count in range(source.index("<pod title=\'" + tag + "\'"), len(source)):
		#print(reqs[count])
		if pattern.match(source[count]):
			limit = re.findall(r'>.+}(.+)<', source[count])
			return limit[0]
	return 'None'

def Find_Gmax(source):
	if "<pod title='Global maxima'" in source:
		tag = 'Global maxima'
	elif "<pod title='Global maximum'" in source:
		tag = 'Global maximum'
	else:
		return 'None'
	pattern = re.compile('<plaintext>.+</plaintext>')
	for count in range(source.index("<pod title=\'" + tag + "\'"), len(source)):
		#print(reqs[count])
		if pattern.match(source[count]):
			limit = re.findall(r'>.+}(.+)<', source[count])
			return limit[0]
	return 'None'

def Find_Lmin(source):
	if "<pod title='Local minima'" in source:
		tag = 'Local minima'
	elif "<pod title='Local minimum'" in source:
		tag = 'Local minimum'
	else:
		return 'None'
	pattern = re.compile('<plaintext>.+</plaintext>')
	for count in range(source.index("<pod title=\'" + tag + "\'"), len(source)):
		#print(reqs[count])
		if pattern.match(source[count]):
			limit = re.findall(r'>.+}(.+)<', source[count])
			return limit[0]
	return 'None'

def Find_Gmin(source):
	if "<pod title='Global minima'" in source:
		tag = 'Global minima'
	elif "<pod title='Global minimum'" in source:
		tag = 'Global minimum'
	else:
		return 'None'
	pattern = re.compile('<plaintext>.+</plaintext>')
	for count in range(source.index("<pod title=\'" + tag + "\'"), len(source)):
		#print(reqs[count])
		if pattern.match(source[count]):
			limit = re.findall(r'>.+}(.+)<', source[count])
			print(limit)
			return limit[0]
	return 'None'

def Find_Sum(source):
	if "<pod title='Sum'" in source:
		tag = 'Sum'
	elif "<pod title='Infinite sum'" in source:
		tag = 'Infinite sum'
	elif "<pod title='Regularized result'" in source:
		tag = 'Regularized result'
	elif "<pod title='Approximated sum'" in source:
		tag = 'Approximated sum'
	else:
		return 'None'
	pattern = re.compile('<plaintext>.+</plaintext>')
	for count in range(source.index("<pod title=\'" + tag + "\'"), len(source)):
		#print(source[count])
		if pattern.match(source[count]):
			suma = re.findall(r'>.+= (.+)<', source[count])
			if len(suma) == 0:
				suma = re.findall(r'>.+(~~.+)<', source[count])
			if 'infinity' in suma[0]:
				suma = re.findall(r'[^\^]+', suma[0])
			return suma[0]
	return 'None'

def Find_Solution(source):
	if "<pod title='Solution'" in source:
		tag = "Solution"
	elif "<pod title='Solutions'" in source:
		tag = "Solutions"
	else:
		return 'None'

	roots = list()
	pattern = re.compile("<plaintext>.+</plaintext>")
	stopper = re.compile("<pod title=\'.+\'")
	for count in range(source.index("<pod title=\'" + tag + "\'") + 1, len(source)):
		#print(reqs[count2])
		if pattern.match(source[count]):
			roots.append(source[count].replace('<plaintext>', '').replace('</plaintext>', ''))
		elif stopper.match(source[count]):
			break
	return '; '.join(roots)

def Find_Integ(source):
	if "<pod title='Indefinite integral'" in source and "<pod title='Definite integral'" not in source:
		tag = 'Indefinite integral'
	elif "<pod title='Definite integral'" in source:
		tag = 'Definite integral'
	else:
		return 'None'
	pattern = re.compile('<plaintext>.+</plaintext>')
	for count in range(source.index("<pod title=\'" + tag + "\'"), len(source)):
		#print(reqs[count])
		if pattern.match(source[count]):
			limit = re.findall(r'>.+=(.+)<', source[count])
			print(limit)
			return limit[0]
	return 'None'

def Find_Conv(source):
	if "<pod title='Convergence tests'" in source:
		tag = 'Convergence tests'
	else:
		return 'None'
	pattern = re.compile('<plaintext>.+</plaintext>')
	for count in range(source.index("<pod title=\'" + tag + "\'"), len(source)):
		#print(reqs[count])
		if pattern.match(source[count]):
			limit = re.findall(r'>(.+)<', source[count])
			return limit[0]
	return 'None'
