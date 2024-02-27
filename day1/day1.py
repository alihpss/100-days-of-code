variavel = 5 

if variavel > 0:
    print("Learning sintax")
    
def first_function():
    print("Function works")

x, y ,z = ["Orange", "Banana", "Cherry"]

global_var = "awesome"

def change_global_var(): 
    global global_var
    global_var = "fantastic"

first_function()
change_global_var()

print(global_var)

print(x, y, z)
print(type(variavel))

for x in 'banana': 
    print(x)
    
txt = 'python is cool'

print('is' in txt)

a = "Hello, World!"
print(a[0:3])
print(a[:4])

quantity = 5
item_number = 441
price = 23.74

order = "I want {} pieces of item {} for {} dollars."
print(order.format(quantity, item_number, price))