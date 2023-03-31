import time


def sorting_knapsack(ceny, wagi):
    sortowanie = []
    for i in range(len(ceny)):
        sortowanie.append([ceny[i], wagi[i], round(ceny[i] / wagi[i], 1)])

    return sortowanie


def fill_knapsack(n, waga_plecaka, cena_plecaka, posortowane):
    for j in range(n):
        if waga_plecaka + posortowane[j][1] < pojemnosc:
            waga_plecaka += posortowane[j][1]
            cena_plecaka += posortowane[j][0]
    return waga_plecaka, cena_plecaka


def knapsack_most_valuable(pojemnosc, n, sortowanie):
    start_time = time.time()
    if pojemnosc == 0 or n == 0:
        return print("brak miejsca w plecaku lub brak przedmiotów")

    waga_plcaka = 0
    cena_plecaka = 0
    posortowane = sorted(sortowanie, key=lambda item: item[0], reverse=True)
    wypelniony_plecak = fill_knapsack(n, waga_plcaka, cena_plecaka, posortowane)
    end_time = time.time()
    czas_programu = end_time - start_time
    return wypelniony_plecak, czas_programu


def knapsack_lighest(pojemnosc, n, sortowanie):
    start_time = time.time()
    if pojemnosc == 0 or n == 0:
        return print("brak miejsca w plecaku lub brak przedmiotów")

    waga_plcaka = 0
    cena_plecaka = 0
    posortowane = sorted(sortowanie, key=lambda item: item[1])
    wypelniony_plecak = fill_knapsack(n, waga_plcaka, cena_plecaka, posortowane)
    end_time = time.time()
    czas_programu = end_time - start_time
    return wypelniony_plecak, czas_programu


def knapsack_weight_price_ratio(pojemnosc, n, sortowanie):
    start_time = time.time()
    if pojemnosc == 0 or n == 0:
        return print("brak miejsca w plecaku lub brak przedmiotów")

    waga_plcaka = 0
    cena_plecaka = 0
    posortowane = sorted(sortowanie, key=lambda item: item[2], reverse=True)
    wypelniony_plecak = fill_knapsack(n, waga_plcaka, cena_plecaka, posortowane)
    end_time = time.time()
    czas_programu = end_time - start_time
    return wypelniony_plecak, czas_programu


if __name__ == "__main__":
    pojemnosc = 20
    ceny = [75, 100, 94, 41, 79, 114, 106, 94, 117, 79]
    wagi = [5, 7, 14, 5, 14, 11, 10, 11, 7, 6]
    n = len(ceny)
    sortowanie = sorting_knapsack(ceny, wagi)
    most_valuable_cena_waga, most_valuable_czas = knapsack_most_valuable(
        pojemnosc, n, sortowanie
    )
    print(
        f"Wybór najcenniejszych rzeczy: \n Cena plecaka to: {most_valuable_cena_waga[1]}, "
        f"Waga plecaka to: {most_valuable_cena_waga[0]}, "
        f"operacja zakończona w czasie: {most_valuable_czas}"
    )
    lighest_cena_waga, lighest_czas = knapsack_lighest(pojemnosc, n, sortowanie)
    print(
        f"Wybór najlżejszych rzeczy: \n Cena plecaka to: {lighest_cena_waga[1]}, "
        f"Waga plecaka to: {lighest_cena_waga[0]}, "
        f"operacja zakończona w czasie: {lighest_czas}"
    )
    weight_price_ratio_cena_waga, weight_price_ratio_czas = knapsack_weight_price_ratio(
        pojemnosc, n, sortowanie
    )
    print(
        f"Wybór najcenniejszych rzeczy w stosunku do wagi: \n Cena plecaka to: {weight_price_ratio_cena_waga[1]},"
        f"Waga plecaka to: {weight_price_ratio_cena_waga[0]}, "
        f"operacja zakończona w czasie: {weight_price_ratio_czas}"
    )
