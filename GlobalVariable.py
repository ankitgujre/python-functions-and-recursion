z = 25

def myfunction():
    print(z)
    global y
    y = 10
    
myfunction()

print(y)