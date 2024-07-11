def get_matrix(n, m, value):
    matrix = []
    for n_row in range(n):
        matrix.append([])
        for n_column in range(m):
            matrix[n_row].append(value)

    return matrix


# Alternative version
def get_matrix_my(n, m, value):
    matrix = []
    for n_row in range(n):
        row = []
        for n_column in range(m):
            row.append(value)
        matrix.append(row)

    return matrix


result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)
