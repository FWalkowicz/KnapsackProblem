# Opis 
***Problem Plecakowy*** - polega na tym, aby spakować jak najwiecej rzeczy tak aby ich wartość byłja jak największa. Od początku wiadomo jest ile jest rzeczy oraz jaka jest ich cena oraz waga. Rzeczy możemy pakować do plecaka wielokrotnie. Upraszczając, jak zapakować plecak aby jego zawartość była jak najcenniejsza.

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
