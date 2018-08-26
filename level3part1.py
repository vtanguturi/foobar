def answer(n):
    # your code here
    # 23 -> 24 -> 12 -> 6 -> 3 -> 2 -> 1
    # 23 -> 22 -> 11 -> 10 -> 5 -> 4 -> 2 -> 1
    def recursiveAnswer(n, count):
        if n == 1:
            return count
        else:
            count += 1
            if n % 2 == 0:
                return recursiveAnswer(n/2, count)
            else:
                return min([recursiveAnswer(n+1, count), 
                recursiveAnswer(n-1, count)])
    n = long(n)
    count = 0
    return recursiveAnswer(n, count)
