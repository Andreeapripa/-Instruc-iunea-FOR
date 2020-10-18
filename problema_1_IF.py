#1) Se introduc trei date de forma număr curent elev, punctaj. Afişaţi numărul elevului cu cel mai mare punctaj.
a=int(input('Numarul curent pentru primul elev:'))
x=int(input('Punctajul pentru primul elev:'))
b=int(input('Numarul curent pentru al doilea elev:'))
y=int(input('Punctajul pentru al doilea elev:'))
c=int(input('Numarul curent pentru al treilea elev:'))
z=int(input('Punctajul pentru al treilea elev:'))
if (y>x) and (y>z):
    print('Punctajul maxim il are elevul cu numarul curent', b)
if (z>y) and (z>x):
    print('Punctajul maxim il are elevul cu numarul curent', c)
if (x>y) and (x==z):
    print('Punctajul maxim il are elevul cu numarul curent', a)
if (x==y) and (x>z):
    print('Punctajul maxim il are elevul cu numarul curent', a)
if (x==y) and (x==z):
    print('Punctajul maxim il are elevul cu numarul curent', a)