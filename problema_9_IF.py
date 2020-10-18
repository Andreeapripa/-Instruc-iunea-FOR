#9) Pe o masă de biliard sunt bile albe, roşii şi verzi. Din fiecare culoare sunt bile de două dimensiuni: mari şi mici. Să se afişeze
#câte bile sunt în total pe masa de biliard. Un jucător vrea să-i spuneţi care bile sunt mai multe , cele mici sau cele mari, afişând
#numărul lor. De ce culoare sunt bilele cele mai numeroase? Precizaţi numărul lor. 
a=int(input('Numarul de bile albe mici:'))
A=int(input('Numarul de bile albe mari:'))
r=int(input('Numarul de bile rosii mici:'))
R=int(input('Numarul de bile rosii mari:'))
v=int(input('Numarul de bile verzi mici:'))
V=int(input('Numarul de bile verzi mari:'))
print('In total sunt', a+A+r+R+v+V, 'bile')
if (A+R+V)>(a+r+v):
    print('sunt mai multe bile mari, fiind', A+R+V)
elif (A+R+V)<(a+r+v):
    print('sunt mai multe bile mici, fiind', a+r+v)
else:
    print('numarul de bile mari este egal cu cel de bile mici, fiind', A+R+V)
if (A+a>=R+r) and (A+a>=V+v):
    print('bilele cele mai numeroase sunt cele alba, fiind', A+a)
elif(R+r>A+a) and (R+r>V+v):
    print('bilele cele mai numeroase sunt cele rosii, fiind', R+r)
else:
    print('bilele cele mai numeroase sunt cele verzi, fiind', V+v)