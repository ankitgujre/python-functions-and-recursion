# def add():
#     print("Hello")
    
# add()

def sec_Largest(li):
    large = float("-inf")
    seclarg = float("-inf")

    for i in li:
        if i > large:
            sec_Largest = large
            large = i
        if i > sec_Largest and i < large:
            sec_Largest = i
            
    return sec_Largest
li = [10,20,300,65]
li2 = [100,260,300,65]
li3 = [1,2,3,5,6,5,]

print(sec_Largest(li))
print(sec_Largest(li2))
print(sec_Largest(li3))


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