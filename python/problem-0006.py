def sumSquareDiff(num):
	sumOfSquare = 0
	squareOfSum = 0
	for i in range(1, num + 1):
		sumOfSquare += i ** 2
		squareOfSum += i
	squareOfSum *= squareOfSum
	return squareOfSum - sumOfSquare

print(sumSquareDiff(10))
print(sumSquareDiff(100))
