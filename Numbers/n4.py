while True:
    num = input("Enter a number: ")
    try:
        int(num)
        break
    except:
        print("That's not a number.")

def isPrime(x):
    if x >= 2:
        for i in range(2, x):
            if not (x % i):
                return False
    else:
        return False
    return True

for i in range(0, int(num)):
    if isPrime(i):
        print(i)
