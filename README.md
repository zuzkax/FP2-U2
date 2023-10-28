# FP2-U2
=============   ALGORYTM Z 10 NA U2 ======================================== 
Zamienia liczby dziesiętne dodatnie:
  1. zamiana na binarny
  2. dodanie 0 na poczatku
Zamienia liczby dziesiętne ujemne:
  1. stworzenie zmiennej bin która przechowuje wynik funkcji na_bin, typ LISTA
  2. odwrócenie listy bin
  3. petla
     - negacja kazdego znaku w liscie
     - wynikiem petli jest string
  4. dodanie 1
  5. zmiana stringu na liste

-------------- algorytm dodawania binarnego ---------------------------------
1. zmienna maks_długosc
2. uzupełnenie zerami liczb
3. zmienna przeniesienie
4. petla od konca
   - zamiana i-tych bitow na int
   - suma bitów + przeniesienie
   - zapisanie wyniku dodania i-tych bitów
   - zaktualizowanie sumy
5. jeżeli zostało przeniesienie dodanie 1 na najstarszym bicie 




================ ALGORYTM Z 10 NA U2 ODWRÓCONE ================================
Jeżeli liczba jest ujemna:
  1. przeliczenie jej na sys bin funkcja na_bin
  2. dodanie 0 na najstrszym bicie
Jeżeli liczba jest dodatnia:
  1. dopełnienie = sufit - liczba
  2. ustalenie długosci dopełnienia (log pods.2 z sufitu)
  3. zakodowanie dopełnienia w systemie binarnym funkcją na_bin2
  4. dodanie 1 na najstarszym bicie 

-------------- algorytm na_bin2 ------------------------------------------------
arg (liczba, długość)
1. bin(liczba,2)[2:] # zamiana liczby na binarna, czytana od 3 elementu
2. petla while póki długosc liczby_bin nie bedzie równa dlugosci_arg

