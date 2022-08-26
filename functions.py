# Create a function for finding the factorial of a number
# def fact(a):
#     b = 1
#     for i in range(1, a + 1):
#         b *= i
#     print(f'Factorial of number {a} is {b}')
#
#
# fact(5)

# Check a given number is prime number or not using a function
def prime(a):
    count = 0
    for i in range(2, a):
        if a % i == 0:
            count += 1
    if count == 0:
        print(a, "is a prime number")
    else:
        print(a, "is not a prime number")


prime(8)
