number = int(input("Insira um numero: "))

print(" A tabuada do numero {} é: ".format(number))

def multi(a, b):
    return a * b

for i in range(1, 11):
    print("{} x {} = {}".format(number, i, multi(number, i)))

c = 1 
while c != 11:
    print("{} x {} = {}".format(number, c, multi(number, c)))
    if c == 5:
        break
    c += 1