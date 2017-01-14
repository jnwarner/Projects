def isPrime(x):
    if x >= 2:
        for i in range(2, x):
            if not (x % i):
                return False
    else:
        return False
    return True

x = 1

print("The first prime is 1.")

ans = 'y'

while ans == 'Y' or ans == 'y':
    ans = input('Would you like the next Prime? (y/n): ')

    if ans == 'n' or ans == 'N':
        break
    else:
        print("Ok!")

    x += 1
    while True:
        if isPrime(x):
            print("The next prime is " + str(x) + '.')
            break
        else:
            x += 1
