#4) Se introduc vârstele a 3 persoane. Afişaţi vârstele cuprinse între 18 şi 60 de ani. 

a=int(input('Varsta primei persoane'))
b=int(input('Varsta persoanei a doua'))
c=int(input('Varsta persoanei a treia'))
if (18<a<60) and (18<b<60) and (18<c<60):
    print ( a, b, c)
elif (18<a<60) and (18<b<60) and ((18>c) or (c>60)):
    print( a, b)
elif (18<a<60) and ((b<18) or (b>60)) and (18<c<60):
    print( a, c)
elif ((a<18) or (a>60)) and  (18<b<60) and (18<c<60):
    print( b, c)
elif (18<a<60) and ((b<18) or (b>60)) and ((c<18) or (c>60)):
    print(a)
elif ((a<18) or (a>60)) and  (18<b<60) and ((c<18) or (c>60)):
    print(b)
elif  ((a<18) or (a>60)) and ((b<18) or (b>60)) and (18<c<60):
    print(c)
else:
    print('Toate varstele sunt ori mai mici sau egale cu 18 ori mai mare sau egale cu 60')