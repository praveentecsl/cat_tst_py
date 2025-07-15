# traditional approach
# a = 0
# b = 1

# def fibonaci(i):
#     if i == 0:
#         return 0
#     elif i == 1:
#         return 1
#     elif i > 1:
#         return fibonaci(i-1) + fibonaci(i-2)
    

# x = int(input("Enter the index of your fibonacci number:"))

# result = fibonaci(x)

# print(f"The resulting number is: {result}")

# general approach

def fibonacci_series(n):

    list = [0]*(n+1)

    list[0] = 0

    if n > 1:
        list[1] = 1

        for i in range(2,n+1):

            list[i] = list[i-1] + list[i-2]

    return list[n]

x = int(input("enter the number for fib: "))
result = fibonacci_series(x)
print(f"result is: {result}")
