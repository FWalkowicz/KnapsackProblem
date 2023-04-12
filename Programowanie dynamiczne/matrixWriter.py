from dynamic_solution import reconstruct_optimal_solution, construct_optimal_solution

max_weight = 20
item_weight = [5, 7, 14, 5, 14, 11, 10, 11, 7, 6]
item_worth = [75, 100, 94, 41, 79, 114, 106, 94, 117, 79]
answer, matrix = construct_optimal_solution(max_weight, item_worth, item_weight)

with open("solution.txt", "w") as f:
    answer, matrix = construct_optimal_solution(max_weight, item_worth, item_weight)
    _, reg_mat = reconstruct_optimal_solution(matrix, item_weight)
    f.write(str(reg_mat))