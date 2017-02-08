def goo():
	f=input('podaj nazwe pliku: ')
	sys.path.insert(0, 'F:\Dev\Py')
	if not os.path.isfile('F:\\Dev\\Py\\'+f):
		print('Nie ma takiego pilku!')
		return None
	print('Your programm is running!')
	print('--------------------------')
	exec(open('F:\\Dev\\Py\\'+f).read())
