def fill_optimal_solution_row(
    previous_row: list[int], item_weight: list[int], item_worth: list[int], i: int
):
    current_row = [0 for index in range(len(previous_row))]
    for w in len(previous_row):
        current_row[w] = (
            previous_row[w]
            if item_weight[i - 1] > w
            else max(
                previous_row[w], item_worth[i - 1] + previous_row[w - item_worth[i - 1]]
            )
        )
    return current_row


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
        solution_matrix[i] = fill_optimal_solution_row(
            solution_matrix[i - 1], item_weight, item_worth, i
        )
    return (
        solution_matrix[len(solution_matrix)][len(solution_matrix[0])],
        solution_matrix,
    )

#TODO add solution reconstruction