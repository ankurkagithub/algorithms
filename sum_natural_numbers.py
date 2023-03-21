#Doing sum using iterative approach

def sum_NN(n):
    sum = 0
    for i in range(n+1):
        sum += i
    return sum


# Doing sum using recursive approach
def sum_list(N):
    # Base case
    if len(N) == 0:
        return 0
    # recursion + calculation
    return N[0] + sum_list(N[1:])

# List comprehension
alist = [num for num in range(1,10)]

# Using print functions.
print(sum_list(alist))
print(sum_NN(9))
