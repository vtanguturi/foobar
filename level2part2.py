from itertools import combinations

def answer(l):
	l.sort(reverse = True)
	for i in reversed(range(1, len(l) + 1)):
		for combo in list(combinations(l, i)):
			if sum(combo) % 3 == 0: 
        return int(''.join(map(str, combo)))
	return 0
