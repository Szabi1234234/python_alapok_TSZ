'''Összehasonlító operátorok
==	egyenlő
!=	nem egyenlő
<	kisebb
>	nagyobb
<=	kisebb vagy egyenlő
>=	nagyobb vagy egyenlő
Logikai operátorok
and	és
or	vagy
not	nem
'''
'''
1. Feladat
Készíts egy programot, amely a felhasználótól bekér egy egész számot, majd megvizsgálja, hogy a megadott szám
- pozitív páros vagy
- negatív páratlan.
Az eredményről tájékoztatja a felhasználót.
'''
x = int(input('Mondj egy egész számot! '))

if x % 2 == 0 and x > 0:
    print("A szám páros és pozitív")
elif x % 2 != 0 and x < 0:
    print("A szám negatív és páratlan")
else :
    print("nem")
'''2. Feladat
Készíts egy programot, amely a felhasználótól két külön kérdésben megkérdezi, hogy az ikrek (Henrik és Hanna)
jönnek-e ma kosrazni! Például így: Jön Henrik ma kosarazni? (i/n). A program írja ki, hogy melyik állítás
igaz az alábbiak közül:
- egyikük sem jön kosarazni,
- mind a ketten jönnek kosarazni,
- csak az egyikük jön kosarazni.
'''
# henrik = input('Jon henrik ma kosarazni? ')
# hanna = input('Jon hanna ma kosarazni? ')
# hanna_lowercase = hanna.lower()
# henrik_lowercase = henrik.lower()
# if henrik_lowercase == "i" and hanna_lowercase == "i":
#     print('igen mindketten mennek')
# elif henrik_lowercase == "n" and hanna_lowercase == "n" :
#     print("egyikuk se megy")
# elif hanna_lowercase == "i" and henrik_lowercase =="n" :
#     print('csak Hanna jon')
# elif hanna_lowercase == "n" and henrik_lowercase== "i":
#     print("csak Henrik megy")
'''3. Feladat
Készíts egy programot, amely a felhasználó által megadott egész számról eldönti, hogy
- csak 3-mal osztható,
- csak 4-gyel osztható,
- 3-mal és 4-gyel is osztható,
- sem 3-mal, sem 4-gyel nem osztható!'''
(input("Adj meg egy egész szá"))



