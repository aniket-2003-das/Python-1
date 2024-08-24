# n = 4
# product = 1
# for i in range(n):
#     product = product * (i+1)
# print(product)

def factorial_iter(n):
    product = 1
    for i in range(n):
        product = product * (i+1)
    return product

f = factorial_iter(7)
print(f)

# Printing factorial of a number using recursive function.
def factorial_recursive(n):
    if n == 1 or n==0 :
       return 1
    return n* factorial_recursive(n-1)

F = factorial_recursive(5)
print(F)
