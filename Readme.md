# Opis 
***Problem Plecakowy*** - polega na tym, aby spakować jak najwiecej rzeczy tak aby ich wartość byłja jak największa. Od początku wiadomo jest ile jest rzeczy oraz jaka jest ich cena oraz waga. Rzeczy nie możemy pakować do plecaka wielokrotnie. Upraszczając, jak zapakować plecak aby jego zawartość była jak najcenniejsza.

## Matematyczny opis
Dostarczone dane:
- **Pojemność plecaka** - oznaczymy jako $W \in N$
- **Liczba przedmiotów** - $n_{i}$ gdzie $i=1,2,3,...,n$
- **Wagi przedmiotów** - $w_{1}, w_{2}, w_{3},...,w_{n}$ 
- **Wartość przedmiotu** - $v_{1}, v_{2}, v_{3},...,v_{n}$

Cel: zapełnienie plecaka tak aby tworzył pewien podzbiór $J \subset W$ oraz spełniał założenia:
1) $$\sum_{j \in J}{w_{j}\le W}$$
2) 
$$ \max ( \sum_{j \in J}{v_{j}}) $$

# Metoda zachłanna
Jak sama metoda mówi to podejście będzie się operało na zapakowaniu rzeczy.
To doprowadza nas do rozważenia 3 możliwych sposobów
1) Pakujemy najcenniejsze przedmioty
2) Pakujemy najlżejsze przedmioty
3) Pakujemy najcenniejsze przedmioty w przeliczeniu na np. 1kg

Pierwszym krokiem który wykonamy w naszym programie będzie zdefiniowanie wielkości plecaka oraz 2 tablic odpowiednio na wagi oraz ceny przedmiotów. W ten sposób także możemy okreścil wielkość tablicy z wartośćiami wag i cen.
```python
pojemnosc = 20                                       # pojemność plecaka
ceny = [75, 100, 94, 41, 79, 114, 106, 94, 117, 79]  # kolejne ceny przedmiotów
wagi = [5, 7, 14, 5, 14, 11, 10, 11, 7, 6]           # kolejne wagi przedmiotów
n = len(ceny)                                        # wielkość tablic
```

Gdy mamy zdefiniowane podstawowe informacje potrzebne do rozwiązania naszego zagadnienia, możemy utworzyć sobię nową tablicę do której wrzucimy wszystkie informacje  w celu późnejszego wygodniejszego rozwiązywania problemu. tablica będzie wielkości $3 \times n$.
```python
def sorting_knapsack(ceny, wagi):  
	sortowanie = []  # pusta tablica na nasze dane 
	for i in range(len(ceny)):  # pętla wielkośći ilośći przedmiotów
		# indeks: 0 - cena, 1 - waga, 2 - stosunek ceny do wagi zaokrąglody do 1 miejsca
		sortowanie.append([ceny[i], wagi[i], round(ceny[i] / wagi[i], 1)])  
	# zwracamy wypełnioną tablice
	return sortowanie
```

Dzięki tej operacji będziemy mogli sortować wszystkie rzeczy jednocześnie zależnie od naszej potrzeby np. po 0 elemencie kiedy będziemy potrzebowali najcenniejszych rzeczy, po 1 elemencie kiedy będziemy potrzebowali najlżejsze rzeczy oraz po 2 elemencie kiedy będziemy potzrebować stodunek wagi do ceny.

Opiszemy tutaj jeden przypadej dla najcenniejszych rzeczy(dwa kolejne przykłady są analogiczne różnią się tylko sortowaniem). Zaczynając nasz program musimy sprawdzić czy nasz plecak nie ma 0 wielkości lub czy są jakiekolwiek przedmioty do włożenia.
```python
start_time = time.time()  # start mierzenia czasu programu
if pojemnosc == 0 or n == 0:  # sprawdzenie założeń 
	return print("brak miejsca w plecaku lub brak przedmiotów")  
  
waga_plcaka = 0  # ustawienie początkowej wagi plecaka
cena_plecaka = 0  # ustawienie początkowej ceny plecaka
# sortowanie przy użyciu funkcji sorted() wbudowanej w python'a
# sortowanie tablicy będzie się różniło w zależności od potrzeb
posortowane = sorted(sortowanie, key=lambda item: item[0], reverse=True)
# wypełnianie plecaka jest takie samo dla każdego sposobu
wypelniony_plecak = fill_knapsack(n, waga_plcaka, cena_plecaka, posortowane)  
end_time = time.time()  # zakończenie mieżenia czasu programu
czas_programu = end_time - start_time  # końcowy czas
return wypelniony_plecak, czas_programu
```

Wypełnianie naszego plecaka rzeczami dla wszytskich metod zachłannych odbywa się tak samo, jedyną różnicą będzie sposób sortowania naszej tablicy w zależności od interesujących nas wartości.
```python
def fill_knapsack(n, waga_plecaka, cena_plecaka, posortowane):  
	for j in range(n):  
		# sprawdzenie czy możemy dołożyć kolejny przedmiot do plecaka
		if waga_plecaka + posortowane[j][1] < pojemnosc:  
			# waga naszego plecaka to będzie stara waga + waga dodanego przedmiotu
			waga_plecaka += posortowane[j][1]  
			# wartość naszego plecaka to będzie stara wartość + wartość dodanego przedmiotu
			cena_plecaka += posortowane[j][0]  
	return waga_plecaka, cena_plecaka
```


# Algorytm dokładny(programowanie dynamiczne)

Tworzymy macierz o ilości wierszy równej ilości przedmiotów, jakie możemy włożyć do plecaka oraz ilości kolumn równej maksymalnej wadze plecaka.
Komórkę w tej macierzy oznaczymy jako $V[i, w]$, gdzie $i$ oznacza $i$-ty przedmiot, a $w$ oznacza plecak o maksymalnej wadze równej $w$.
Algorytm znajdowania optymalnej wartości polega na budowaniu optymalnej zawartości plecaka na podstawie optymalnych zawartości plecaków o mniejszej maksymalnej wadze, ale tym samym zestawie przedmiotów.

Pierwszy wiersz wypełniamy zerami, natomiast następne wiersze (oznaczane literą $i$) wypełniamy kolumnami rosnąco według zasad:

1. Jeśli nie możemy włożyć $i$-tego przedmiotu do plecaka ze względu na wagę, jego wartość jest taka sama jak w wierszu $i - 1$,
2. Jeśli możemy włożyć przedmiot do plecaka, sprawdzamy jaka kombinacja zawartości plecaka ma większą wartość:
    - obecna(przed dodaniem $i$-tego przedmiotu)
    - optymalna zawartość dla plecaka o maksymalnej wadze równej ($w$ minus waga $i$-tego przedmiotu) po dołożeniu $i$-tego przedmiotu
    Wybieramy wartość większą i kontynuujemy algorytm.

Ostatnia komórka ostatniego wiersza zawiera łączną wartość optymalnego rozwiązania. Aby otrzymać listę przedmiotów wrzuconych do plecaka, musimy utworzyć macierz i wypełnić ją wartościami według zasady:

Macierz wypełniamy kolumnami. Każdy element w kolumnie wypełniamy według warunku:

1. Jeśli wartości między obecną i poprzednią komórką w kolumnie są różne, wstawiamy 1,
2. W przeciwnym wypadku wstawiamy zero.

Mając macierz zmian, możemy zrekonstruować rozwiązanie przy pomocy poniższego algorytmu. Załóżmy, że początkowo $W$ jest równe liczbie kolumn macierzy rozwiązania. Wtedy:

1. Szukamy najniżej położonego wiersza, który posiada wartość 1 w kolumnie $W$,
2. Zapisujemy indeks tego wiersza do listy, a następnie wykreślamy wszystkie wiersze poniżej oraz zmniejszamy $W$ o wagę przedmiotu o tym indeksie,
3. Powtarzamy algorytm.

Końcowym efektem jest lista indeksów przedmiotów znajdujących się w plecaku.


# Linki
- http://math.uni.wroc.pl/~jagiella/p2python/skrypt_html/wyklad12.html
- https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiprbGQvOP9AhWH6CoKHfDtCVUQFnoECBEQAQ&url=https%3A%2F%2Fmattomatti.com%2Fpl%2Fa68&usg=AOvVaw1mj78zAeiDq9klzTbWhPc5
- https://rstudio-pubs-static.s3.amazonaws.com/774252_c52f2e0f116a40c9ae62330e38e9f1f1.html
