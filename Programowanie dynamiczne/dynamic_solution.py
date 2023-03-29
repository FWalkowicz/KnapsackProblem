def fill_optimal_solution_row(previous_row: list[int], item_weight: list[int]):
    raise NotImplementedError

def construct_optimal_solution(
    knapsack_weight_limit: int, item_worth: list[int], item_weight: list[int]
):
    """
    Rozwiązuje zero-jedynkowy problem plecakowy.
    @Parametry
    ---
    `knapsack_weight_limit`: maksymalna waga zawartości plecaka
    `item_worth`: lista wartości rzeczy, które możemy włożyć do plecaka
    `item_weight`: lista wag rzeczy, które można włożyć do plecaka.
                            Długość powinna być taka sama co item_worth.
    """
    if len(item_worth) != len(item_weight):
        raise ValueError("Listy wartości i ciężarów mają różne długości.")
    n = len(item_worth)
    W_plus_one = knapsack_weight_limit + 1
    solution_matrix = [[0 for j in range(n + 1)] for k in range(W_plus_one)]
    for i in range(
        1, len(n + 1)
    ):  # zerowy wiersz zawiera same zera(z założenia algorytmu)
        for w in range(W_plus_one):
            raise NotImplementedError
