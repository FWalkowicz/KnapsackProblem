# Opis 
***Problem Plecakowy*** - polega na tym, aby spakować jak najwiecej rzeczy tak aby ich wartość byłja jak największa. Od początku wiadomo jest ile jest rzeczy oraz jaka jest ich cena oraz waga. Rzeczy możemy pakować do plecaka wielokrotnie. Upraszczając, jak zapakować plecak aby jego zawartość była jak najcenniejsza.

## Matematyczny opis
Dostarczone dane:
- **Pojemność plecaka** - oznaczymy jako $W \in N$
- **Liczba przedmiotów** - $n_{i}$ gdzie $i=1,2,3,...,n$
- **Wagi przedmiotów** - $w_{1}, w_{2}, w_{3},...,w_{n}$ 
- **Wartość przedmiotu** - $v_{1}, v_{2}, v_{3},...,v_{n}$

Cel: zapełnienie plecaka tak aby tworzył pewien podzbiów $J \subset W$ oraz spełniał założenia:
1) $$\sum_{j \in J}{w_{j}\le W}$$
2) 
$$ \max ( \sum_{j \in J}{v_{j}}) $$

# Metoda zachłanna
Jak sama metoda mówi to podejście będzie się operało na zapakowaniu rzeczy.
To doprowadza nas do rozważenia 3 możliwych sposobów
1) Pakujemy najcenniejsze przedmioty
2) Pakujemy najlżejsze przedmioty
3) Pakujemy najcenniejsze przedmioty w przeliczeniu na np. 1kg

# Algorytm dokładny(programowanie dynamiczne)


# Linki
- http://math.uni.wroc.pl/~jagiella/p2python/skrypt_html/wyklad12.html
- https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiprbGQvOP9AhWH6CoKHfDtCVUQFnoECBEQAQ&url=https%3A%2F%2Fmattomatti.com%2Fpl%2Fa68&usg=AOvVaw1mj78zAeiDq9klzTbWhPc5
- https://rstudio-pubs-static.s3.amazonaws.com/774252_c52f2e0f116a40c9ae62330e38e9f1f1.html



