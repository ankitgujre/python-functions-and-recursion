num = int(input("Enter a number: "))
power = len(str(num))

def armstrong_sum(n):
    if n == 0:
        return 0
    return (n % 10) ** power + armstrong_sum(n // 10)

if armstrong_sum(num) == num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")