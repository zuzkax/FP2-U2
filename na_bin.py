'''
wpisac czesc calkowaita i ulamkowa osobno
'''



def na_bin(x):
    wynik = []
    while x > 0:
        if x % 2 == 0:
            wynik.append(0)
            x = x/2
        else:
            wynik.append(1)
            x = x//2
    return wynik[::-1]



def cz_ulamkowa(x,d): #d = dokładnosc
    wynik1 = []
    for i in range(d):
        x *= 2
        if x >= 1:
            wynik1.append(1)
            x -= 1
        else:
            wynik1.append(0)

    return wynik1

print(cz_ulamkowa(0.7,10))







