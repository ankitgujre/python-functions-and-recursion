
def countDigit(li):
    count = {} 
    for i in li:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count

li = list(input("Enter list: "))
print(countDigit(li))