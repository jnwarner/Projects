w = input("Enter the width: ")
h = input("Enter the height: ")
c = input("Enter the cost per tile: ")

r = float(w) * float(h) * float(c)

print("It will cost $" + '{:.2f}'.format(r))
