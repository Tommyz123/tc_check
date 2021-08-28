
x = input('Enter the password:')
if x == '123':
	print('welcome boss')
	name = input('Enter your name:')
	age = input('Enter your age:')
	age = float(age)
	if age <= 20:
		print('you so young!')
	weight = input('Enter your weight:')
	weight = float(weight)
	if weight >= 100:
		print('you too fat!!')
	height = input('Enther your height:')
	print('your name:', name)
	print('your age:',age)
	print('your weight:', weight)

if x == '520':
	print('We help you find your Star Signs')
	birthM = input('Enter the month for you born:')
	birthM = int(birthM)
	birthD = input('Enter the day for you born:')
	birthD = int(birthD)
	if birthM == 3:
		if birthD >= 1 and birthD <= 20:
			print('Pisces')
		if birthD >= 21 and birthD <= 31:
			print('Aries')
	if birthM == 4:
		if birthD >= 1 and birthD <= 20:
			print('Aries')
		if birthD >= 21 and birthD <= 30:
			print('Taurus')
	if birthM == 5:
		if birthD >= 1 and birthD <= 21:
			print('Taurus')
		if birthD >= 22 and birthD <=31:
			print('Gemini')
	if birthM == 6:
		if birthD >= 1 and birthD <= 21:
			print('Gemini')
		if birthD >= 22 and birthD <= 31:
			print('Cancer')
	if birthM == 7:
		if birthD >= 1 and birthD <= 22:
			print('Cancer')
		if birthD >= 23 and birthD <= 31:
			print('Leo')
	if birthM == 8:
		if birthD >= 1 and birthD <= 23:
			print("Leo")
		if birthD >= 24 and birthD <= 31:
			print('Virgo')
	if birthM == 9:
		if birthD >= 1 and birthD <= 23:
			print('Virgo')
		if birthD >= 24 and birthD <= 31:
			print('Libra')
	if birthM == 10:
		if birthD >= 1 and birthD <= 23:
			print('Libra')
		if birthD >= 24 and birthD <= 31:
			print('Scorpio')
	if birthM == 11:
		if birthD >= 1 and birthD <= 22:
			print('Scorpio')
		if birthD >= 23 and birthD <= 31:
			print('Sagittarius')
	if birthM == 12:
		if birthD >= 1 and birthD <= 21:
			print('Sagittarius')
		if birthD >= 22 and birthD <= 31:
			print('Capricorn')
	if birthM == 1:
		if birthD >= 1 and birthD <= 20:
			print('Capricorn')
		if birthD >= 22 and birthD <= 31:
			print('Aquarius')
	if birthM == 2:
		if birthD >= 1 and birthD <= 19:
			print('Aquarius')
		if birthD >= 20 and birthD <= 31:
			print('Pisces')





