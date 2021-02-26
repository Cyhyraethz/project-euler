def palindromeCheck(num):
	fwd = str(num)
	bwd = str(num)[::-1]
	if fwd == bwd:
		return True

def largestPalindromeProduct(digits):
	largestFactor = '1'
	largestPalindrome = 0
	for i in range(digits):
		largestFactor += '0'
	for i in range(int(largestFactor))[::-1]:
		for j in range(int(largestFactor))[::-1]:
			if palindromeCheck(i * j) and i * j > largestPalindrome:
				largestPalindrome = i * j
	return largestPalindrome

print(largestPalindromeProduct(3))

