from dynamic_solution import solve_01_knapsack

knapsack_limit = 101
show_matrix = True

values = [79, 32, 47, 18, 26, 85, 33, 40, 45, 59]
weights = [85, 26, 48, 21, 22, 95, 43, 45, 55, 52]

solution = solve_01_knapsack(knapsack_limit, values, weights)

print(
    f"Optymalna wartość plecaka: {solution[0]}",
    "Optymalna zawartość plecaka:",
    f"Wartości: {solution[2]}",
    f"Wagi:     {solution[3]}",  # yes, i did align the text with spaces
    sep="\n",
)
if show_matrix == True:
    print("Macierz optymalnego rozwiązania:")
    for row in solution[1]:
        print(row)
