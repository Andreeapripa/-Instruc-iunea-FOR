#13)La un concurs se dau ca premii primilor 100 de concurenţi, tricouri de culoare albă, roşie, albastră şi neagră, în această
#secvenţă. Ionel este pe locul x. Ce culoare va avea tricoul pe care-l va primi? 
a=100
b=int(input("Pe ce loc este Ionel? "))
if b<=100:
    if (b>0) and (b<=25):
        print("Ionel a primit un tricou de culoare alba")
    elif(b>25)and(b<=50):
        print("Ionel a primit un tricou de culoare rosie")
    elif(b>50)and(b<=75):
        print("Ionel a primit un tricou de culoare albastra ")
    elif(b>75)and(b<=100):
        print("Ionel a primit un tricou de culoare neagra ")
    else:
        print("Sunt doar 100 de locuri")