# def answer(n):
#     # your code here
#     # 23 -> 24 -> 12 -> 6 -> 3 -> 2 -> 1
#     # 23 -> 22 -> 11 -> 10 -> 5 -> 4 -> 2 -> 1
#     def recursiveAnswer(n, count):
#         if n == 1:
#             return count
#         else:
#             count += 1
#             if n % 2 == 0:
#                 return recursiveAnswer(n/2, count)
#             else:
#                 return min([recursiveAnswer(n+1, count), 
#                 recursiveAnswer(n-1, count)])
#     n = long(n)
#     count = 0
#     return recursiveAnswer(n, count)
# The above method is correct in theory but for big numbers, there is a large stack trace
# due to how python handles a stack trace, it is too big to continue and a runtime error is created
# Mainly because a variable is being passed through and it is kept in memory. So instead of carrying the steps,
# I will recursively calculate the steps ala fibonnazi through a map structure. This way I am not storing this
# through every recursive call.

def answer(n):
    # your code here
    # 23 -> 24 -> 12 -> 6 -> 3 -> 2 -> 1
    # 23 -> 22 -> 11 -> 10 -> 5 -> 4 -> 2 -> 1
    operations = {1: 0, 2: 1}
    def calcSteps(n):
        if n in operations:
            return operations[n]
        if n % 2 == 0:
            operations[n] = calcSteps(n / 2) + 1
        else:
            operations[n] = min(calcSteps((n+1) / 2) + 2, 
                calcSteps((n-1) / 2) + 2)
        return operations[n]
    n = long(n)
    return calcSteps(n)
