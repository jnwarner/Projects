while True:
    length = input("Enter the number of iterations: ")
    try:
        int(length)
        break
    except:
        print("Enter a number next time.")

x, y, z = 0, 1, 0

for i in range(int(length)):
    print(str(z))
    x = y
    y = z
    z = x + y
