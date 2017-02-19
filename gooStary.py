def goo():
	"""
	#sys.path.insert(0, 'F:\Dev\Py')
	DO THIS TO IMPORT FILE:
	sys.path.append('F:\\Dev\\Py')
	"""
	import sys
	f=input('podaj nazwe pliku: ')
	if not os.path.isfile('F:\\Dev\\Py\\'+f):
		print('Nie ma takiego pilku!')
		return None
	print('Your programm is running!')
	print('--------------------------')
	exec(open('F:\\Dev\\Py\\'+f).read())
