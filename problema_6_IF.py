#6) Andrei primeşte într-o zi trei note, nu toate bune. Se hotărăşte ca, dacă ultima notă este cel puţin 8, să le spună părinţilor toate
#notele primite iar dacă este mai mică decât 8, să le comunice doar cea mai mare notă dintre primele două. Introduceţi notele
#luate şi afişaţi notele pe care le va comunica părinţilor.
a=int(input('Prima nota primita este'))
b=int(input('A doua nota primita este'))
c=int(input('A treia nota primita este'))
if c>=8:
    print('Notele primite sunt', a, b, c)
else:
    if a>=b:
        print('Nota primita este ', a)
    else:
        print('Nota primita este', b)