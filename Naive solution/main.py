import time


def sorting_knapsack(ceny, wagi):
    sortowanie = []
    for i in range(len(ceny)):
        sortowanie.append([ceny[i], wagi[i], round(ceny[i] / wagi[i], 1)])

    return sortowanie


def fill_knapsack(n, waga_plecaka, cena_plecaka, posortowane):
    for j in range(n):
        if waga_plecaka + posortowane[j][1] <= pojemnosc:
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
    pojemnosc = 50
    wagi = [11, 10, 5, 19, 19, 12, 8, 17, 6, 8, 5, 5, 13, 15, 20, 9, 1, 16, 16, 10, 12, 13, 5, 15, 5, 20, 19, 17, 9, 4,
            18, 14, 1, 11, 16, 3, 9, 3, 2, 11, 9, 19, 5, 13, 12, 11, 9, 6, 12, 5, 17, 7, 15, 5, 12, 11, 1, 11, 17, 16,
            8, 14, 16, 13, 20, 9, 14, 17, 9, 7, 13, 20, 13, 13, 13, 7, 6, 17, 10, 5, 1, 2, 7, 5, 14, 3, 19, 10, 2, 18,
            15, 8, 11, 16, 19, 9, 17, 12, 14, 5]
    ceny = [47, 90, 94, 82, 40, 13, 93, 65, 45, 23, 22, 18, 90, 79, 93, 78, 16, 16, 54, 98, 50, 54, 82, 59, 87, 16, 80,
            67, 59, 11, 79, 52, 28, 96, 15, 57, 63, 11, 73, 54, 82, 18, 78, 38, 63, 31, 75, 95, 68, 11, 29, 22, 20, 63,
            50, 30, 45, 89, 84, 97, 18, 74, 82, 95, 44, 81, 82, 77, 90, 55, 15, 74, 37, 73, 30, 44, 78, 33, 91, 45, 85,
            82, 72, 79, 30, 86, 10, 35, 38, 50, 21, 53, 59, 63, 65, 52, 26, 69, 42, 18]
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
