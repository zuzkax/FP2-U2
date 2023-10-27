#zapisywanie na minimalnej liczbie bitow w kodzie u2 zwykłym
'''
zakres = [2**0, 2**1, 2**2, 2**3, 2**4, 2**5, 2**6, 2**7, 2**8, 2**9 ]
wagi = [ 1   ,2    ,4    ,8    ,16   ,32   ,64   ,128,   256,  512 ]
liczba bitów = stopien potegi + 1 = index(wagi[sufit od x) + 1
sufit od x = najbliższa większą liczbe dla x, x = 7 ==> sufit od x = 8
'''
# znajdz sufit od x
# jeżeli sufit od x = x: czy potrzebne jest rozpatrzenie tego wyjątku ???
# jeżeli x < 0 to pierwszy bit ustaw na 1
# pętla ustawiająca bity (brutforce)
# jeżeli x > 0 zacznij petle ustawiającą bity od bitu przedostatniego a bit ostatni ustaw na 0
# jeżeli x = 0 wszystkie bity ustaw na 0

'''
petla ustawiająca bity
wynik = []
suma = x

if x < 0:
    for i in range(stopien potegi + 1):
        if suma - wagi[i] >= 0:
            suma -= wagi[i]
            wynik.append(1)
        elif suma - wagi[i] < 0:
            wynik.append(0)            
'''
wagi = [1   ,2    ,4    ,8    ,16   ,32   ,64   ,128,   256,  512 ]

def sufit(x):
    if wagi.count(x) == 1: #jeżeli x znajduje sie w wagi
        return x
    else:
        for i in range(len(wagi)):
            if x < wagi[i]:
                return wagi[i]


def z10_na_u2(x):
    wynik = []
    waga_bitu_ostatniego = sufit(x)
    if x < 0:
        wynik.append(1)
        suma = x + (waga_bitu_ostatniego * -1)
        for i in range(wagi.index(waga_bitu_ostatniego)):
            if suma - wagi[i] >= 0:
                suma -= wagi[i]
                wynik.append(1)
            elif suma - wagi[i] < 0:
                wynik.append(0)

    elif x >= 0:
        wynik.append(0)
        suma = x
        for i in range(wagi.index(waga_bitu_ostatniego)):
            if suma - wagi[i] >= 0:
                suma -= wagi[i]
                wynik.append(1)
            elif suma - wagi[i] < 0:
                wynik.append(0)
    return wynik



print(z10_na_u2(8))






