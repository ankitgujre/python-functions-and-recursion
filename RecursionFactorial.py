# the function which call itself is called recursion

# def factorial(x):
#     if x == 1:
#         return 1
#     else:
#         return(x*factorial(x-1))

# num = int(input("Enter number: "))
# print("The factorial of ",num,"is ",factorial(num) )

x = lambda a: a+10
print(x(5))