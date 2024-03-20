from datetime import datetime

print(datetime.now().year)
def teste(*num): 
    print(num)
    

minha_lista = [1, 2, 3, 4, 5]
    
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

print(minha_lista)        
dobra(minha_lista)
print(minha_lista)
    
teste(2,4, 9, 12)