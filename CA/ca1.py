numBefore = input("Enter num: ")
num = int(numBefore)

while num > 1:
    if (num % 2 == 0):
        num /= 2
        print(num)
    else:
        num *= 3
        num += 1
        print(num)
