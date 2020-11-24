def FizzBuzz(num):
	if type(num) not in [int, float]:
		raise TypeError("num must be non-negative real number only")
	if num == 0:
		return 0

	elif num % 3 == 0 and num % 5 == 0:
		return 'FizBuz'
	elif num % 5 == 0:
		return 'Buz'
	elif num % 3 == 0:
		return 'Fiz'
	else:
		return num
