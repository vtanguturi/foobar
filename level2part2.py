from itertools import combinations
# Form the largest number possible from a list of digits that is divisible by 3. This is to pass the coded message
def answer(l):
	l.sort(reverse = True)
	for i in reversed(range(1, len(l) + 1)):
		for combo in list(combinations(l, i)):
			if sum(combo) % 3 == 0: 
        return int(''.join(map(str, combo)))
	return 0
