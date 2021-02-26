def largestPrimeFactor(n):
	i = 2
	while i < n:
		if n % i == 0:
			n = n / i
		i += 1
	return int(n)
	
print(largestPrimeFactor(600851475143))

