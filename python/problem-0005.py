def listPrime(start, end):
	if start < 2:
		start = 2
	prime = []
	sieve = []
	for i in range(start, end + 1):
		if i not in sieve:
			prime.append(i)
			j = i * 2
			while j <= end:
				sieve.append(j)
				j += i
	return prime

def primeFactors(start, end):
	if start < 2:
		start = 2
	prime = listPrime(start, end)
	result = dict()
	for i in prime:
		result[i] = 0
	for i in range(start, end + 1):
		num = i
		factors = dict()
		for i in prime:
			factors[i] = 0
		con = True
		while con == True:
			for i in prime:
				if num == 1:
					con = False
				if num % i == 0:
					num = num / i
					factors[i] += 1
		for i in prime:
			if factors[i] > result[i]:
				result[i] = factors[i]
	smallest = 1
	for i in prime:
		smallest *= i ** result[i]
	return smallest
		
print(primeFactors(1, 10))
print(primeFactors(1, 20))

