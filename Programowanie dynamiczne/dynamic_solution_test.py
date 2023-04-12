from typing import List

from dynamic_solution import construct_optimal_solution, reconstruct_optimal_solution

show_matrix = True


def presentation_problem_solution_should_return_296():
    max_weight = 20
    item_weight = [5, 7, 14, 5, 14, 11, 10, 11, 7, 6]
    item_worth = [75, 100, 94, 41, 79, 114, 106, 94, 117, 79]
    answer, matrix = construct_optimal_solution(max_weight, item_worth, item_weight)
    if answer == 296:
        return print("Passed!")
    for row in matrix:
        print(row)
    return print(f"not passed! returned {answer} instead of 296")


def optimal_solution_test(
    max_weight: List[int],
    item_weight: List[int],
    item_worth: List[int],
    correct_answer: int,
):
    answer, matrix = construct_optimal_solution(max_weight, item_worth, item_weight)
    if answer == correct_answer:
        return print("Passed!")
    for row in matrix:
        print(row)
    return print(f"not passed! returned {answer} instead of {correct_answer}")


if __name__ == "__main__":
    presentation_problem_solution_should_return_296()
    optimal_solution_test(6, [1, 2, 3], [10, 15, 40], 65)

    print("Test rekonstrukcji optymalnego rozwiązania")
    max_weight = 20
    item_weight = [5, 7, 14, 5, 14, 11, 10, 11, 7, 6]
    item_worth = [75, 100, 94, 41, 79, 114, 106, 94, 117, 79]
    answer, matrix = construct_optimal_solution(max_weight, item_worth, item_weight)
    if show_matrix == True:
        for row in matrix:
            print(row)
    else:
        optimal_items_indices = reconstruct_optimal_solution(matrix, item_weight)
        print([item_worth[index - 2] for index in optimal_items_indices])
        print([item_weight[index - 2] for index in optimal_items_indices])
