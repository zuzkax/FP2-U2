#przeliczanie liczby dziesiętniej na minimalna liczbie bitow w kodzie u2 zwykłym

import bisect

wagi = [1,2,4,8,16,32,64,128,256,512]


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












