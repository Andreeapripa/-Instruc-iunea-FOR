#10)La ferma de găini Copanul este democraţie. Fiecare găină primeşte exact acelaşi număr de boabe de porumb. Cele care nu pot
#fi împărţite vor fi primite de curcanul Clapon. Să se spună cine a primit mai multe boabe şi cu cât. În caz de egalitate, se va
#afişa numărul de boabe primite şi cuvântul "egalitate". Datele se vor citi în următoarea ordine: numărul de găini, iar dupa aceea
#numărul de boabe de porumb.
g=int(input('Numarul de gaini='))
p=int(input('Numarul de boabe de porumb='))
if (p//(g+1)) and (p%(g+1)==0):
    print('Numarul primit de boabe este', int(p/(g+1)), 'egalitate')
elif p/g :
    print('Curcanul Clapon a primit mai mult cu', p%(g+1), 'boabe')