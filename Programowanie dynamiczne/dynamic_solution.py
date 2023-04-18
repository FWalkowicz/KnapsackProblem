from typing import List, Tuple


def fill_optimal_solution_row(
    previous_row: List[int], item_weight: List[int], item_worth: List[int], i: int
):
    current_row = [0 for index in range(len(previous_row))]
    for w in range(len(previous_row)):
        current_row[w] = (
            previous_row[w]
            if item_weight[i - 1] > w
            else max(
                previous_row[w],
                item_worth[i - 1] + previous_row[w - item_weight[i - 1]],
            )
        )
    return current_row


def construct_optimal_solution(
    knapsack_weight_limit: int, item_worth: List[int], item_weight: List[int]
):

    if len(item_worth) != len(item_weight):
        raise ValueError("Listy wartości i ciężarów mają różne długości.")
    n = len(item_worth)
    W_plus_one = knapsack_weight_limit + 1
    solution_matrix = [[0 for j in range(W_plus_one)] for k in range(n + 1)]
    for i in range(1, n + 1):  # zerowy wiersz zawiera same zera(z założenia algorytmu)
        solution_matrix[i] = fill_optimal_solution_row(
            solution_matrix[i - 1], item_weight, item_worth, i
        )
    return (
        solution_matrix[len(solution_matrix) - 1][len(solution_matrix[0]) - 1],
        solution_matrix,
    )


def backward_solve(
    I: int,
    W: int,
    value_change_register_matrix: List[List[int]],
    item_weight: List[int],
):
    knapsack_content_indices = []
    while I != 0:
        if value_change_register_matrix[I - 1][W - 1] == 1:
            knapsack_content_indices.append(I)
            W = W - item_weight[I - 2]
        I = I - 1
    return knapsack_content_indices


def reconstruct_optimal_solution(
    solution_matrix: Tuple[Tuple[int]], item_weight: List[int]
):
    W = len(solution_matrix[0])
    I = len(solution_matrix)
    value_change_register_matrix = [[0 for w in range(W)] for i in range(I)]
    for i in range(I):
        for w in range(W):
            value_change_register_matrix[i][w] = (
                0 if solution_matrix[i][w] == solution_matrix[i - 1][w] else 1
            )
    return (
        backward_solve(I, W, value_change_register_matrix, item_weight),
        value_change_register_matrix
        )


def solve_01_knapsack(
    knapsack_weight_limit: int, item_worth: List[int], item_weight: List[int]
):
    """
    Rozwiązuje zero-jedynkowy problem plecakowy.
    @Parametry
    ---
    `knapsack_weight_limit`: maksymalna waga zawartości plecaka
    `item_worth`: lista wartości rzeczy, które możemy włożyć do plecaka
    `item_weight`: lista wag rzeczy, które można włożyć do plecaka.
                            Długość i kolejność wartości powinna być zgodna z item_worth.
    @return_values
    ---
    - optymalna wartość plecaka
    - macierz optymalnego rozwiązania
    - lista wag optymalnej zawartości
    - lista wartości optymalnej zawartości
    """
    try:
        final_value, optimal_solution_matrix = construct_optimal_solution(
            knapsack_weight_limit, item_worth, item_weight
        )
    except ValueError:
        return print("Listy wartości i ciężarów mają różne długości.")
    optimal_items_indices, _ = reconstruct_optimal_solution(
        optimal_solution_matrix, item_weight
    )
    optimal_items_worth = [item_worth[index - 2] for index in optimal_items_indices]
    optimal_items_weight = [item_weight[index - 2] for index in optimal_items_indices]

    return (
        final_value,
        optimal_solution_matrix,
        optimal_items_weight,
        optimal_items_worth
    )
