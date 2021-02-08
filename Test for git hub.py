import re
while True:
	number = input()
	checker = r'[981][0-9]{7}'
	if re.match(checker, number):
		print('Valid')
	else:
		print('Invalid')
