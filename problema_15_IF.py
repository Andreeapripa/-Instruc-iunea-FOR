#15)Elevii clasei a V-a se repartizează în clase câte 25 în ordinea mediilor clasei a IV-a. Radu este pe locul x în ordinea mediilor. În
#ce clasa va fi repartizat (A, B, C, D sau E)?.
a=int(input('Al catalea este Radu'))
if (a>0) and(a<=125):
    if (a<=25):
        print('A') 
    if (a>25)and(a<=50):
        print('B')
    if (a>50) and (a<=75):
        print('C')
    if (a>75) and (a<=100):
        print('D')
    if (a>100) and (a<=125):
        print('E')
    else:
        print('error')