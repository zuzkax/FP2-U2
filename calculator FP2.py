import bisect

wagi = [1,2,4,8,16,32,64,128,256,512]
def na_bin(x):
    wynik = []
    if x < 0:
        x = x *-1
    while x > 0:
        if x % 2 == 0:
            wynik.append(0)
            x = x/2
        else:
            wynik.append(1)
            x = x//2
    return wynik[::-1]


def add_bin(bin1, bin2):
    max_len = max(len(bin1), len(bin2)) #uzupełnienia do równej długości
    bin1 = bin1.zfill(max_len)
    bin2 = bin2.zfill(max_len)

    transfer = 0
    output = []

    for i in range(max_len - 1, -1, -1):
        bit1 = int(bin1[i])
        bit2 = int(bin2[i])
        bit_sum = bit1 + bit2 + transfer #dodanie pojedynczych bitów + prxzeniesienie
        output.insert(0, str(bit_sum % 2)) #insert(pozycja, znak)
        transfer = bit_sum // 2

    if transfer: #jeżeli zostanie przeniesienie
        output.insert(0, "1")

    return "".join(output)

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



def binary_search(arr,x):
    index = bisect.bisect_left(arr, x)
    if index != len(arr) and arr[index] == x:
        return True  # Znaleziono element x w liście
    else:
        return False  # Element x nie jest w liście



def z10_na_u2(x):
    output1 = na_bin(x)
    output1.insert(0,0)
    if x > 0:
        return output1
    if x < 0:
        if binary_search(wagi, x*-1):
            return na_bin(x)
        else:
            output2 = ''
            for znak in output1:
                output2 += str(znak ^ 1)  # not, negacja
            output2 = add_bin(output2, "1")
            return output2



def z10_na_u2_odwrocone(x):
    output1 = na_bin(x)
    output1.insert(0,0)
    if x < 0:
        return output1
    if x > 0:
        if binary_search(wagi, x):
            return na_bin(x)
        else:
            output2 = ''
            for znak in output1:
                output2 += str(znak ^ 1)  # not, negacja
            output2 = add_bin(output2, "1")
            return output2



def na_FP2(x):
    if type(x) == float: #jeżeli liczba nie jest całkowita
        d = int(input("podaj dokładnosc zapisu części ułamkoweuj"))
        part1 = na_bin(int(x))
        part2 = cz_ulamkowa(x % 1, d)
        c = len(part1) - 1
        cu2 = z10_na_u2(c) #cecha zakodowana w u2
        cu2_reverse = z10_na_u2_odwrocone(c) #cecha zakodowana w u2 odwróconym

        # składanie do kupy
        output1 = []
        output2 = []
        if x > 0:  # jeżeli liczba + najstarszy bit =0
            output1.append(0)
            output2.append(0)
        else:  # jeżeli liczba - najstarszy bit = 1
            output1.append(1)
            output2.append(1)

        output1.append(cu2)
        output1.append(part1[1:] + part2)

        output2.append(cu2_reverse)
        output2.append(part1[1:] + part2)

        return output1, output2

    else:
        l_bin = na_bin(x) #zamiana na binarną
        c = len(l_bin) - 1 #wyznacznie cechy
        cu2 = z10_na_u2(c) #cecha zakodowana w u2
        cu2_reverse = z10_na_u2_odwrocone(c) #cecha zakodowana w u2 odwróconym

        #składanie do kupy
        output1 = []
        output2 = []
        if x > 0: #jeżeli liczba + najstarszy bit =0
            output1.append(0)
            output2.append(0)
        else: #jeżeli liczba - najstarszy bit = 1
            output1.append(1)
            output2.append(1)

        output1.append(cu2)
        output1.append(l_bin[1:])

        output2.append(cu2_reverse)
        output2.append(l_bin[1:])

        return output1, output2


x = float(input("podaj liczbę którą chcesz przedstawić w FP2"))
output1, output2 = na_FP2(x)
print("cecha zakodowana w U2 zwykłym", output1)
print("bit znaku:", output1[0])
print("cecha:", output1[1])
print("matysa:", output1[2])

print("cecha zakodowana w U2 odwróconym", output2)
print("bit znaku:",output2[0])
print("cecha:", output2[1])
print("matysa:", output2[2])
