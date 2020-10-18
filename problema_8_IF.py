#8) Să se afişeze cel mai mare număr par dintre doua numere introduse în calculator. 
a=int(input('Primul numar este'))
b=int(input('Al doilea numar este'))
if (a%2==0) and (b%2==0):
    if a>b:
        print(a)
    else:
        print(b)
else:
    print('Numerele nu sunt pare')