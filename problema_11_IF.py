#11)Se dau trei numere. Să se afişeze aceste numere unul sub altul, afişând în dreptul fiecăruia unul dintre cuvintele PAR sau IMPAR.
a=int(input('Primul numar este'))
b=int(input('Al doilea numar este'))
c=int(input('Al treilea numar este'))
if a%2==0:
    print(a, '-Par')
else:
    print(a, '-Impar')
if b%2==0:
    print(b, '-Par')
else:
    print(b, '-Impar')
if c%2==0:
    print(c, '-Par')
else:
    print(c, '-Impar')