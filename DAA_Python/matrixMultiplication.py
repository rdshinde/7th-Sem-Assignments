# matrix multiplication using threading
import threading

def matrixMultiplicationUsingThreading(matrix1, matrix2, result, row, col):
    result[row][col] = 0
    for i in range(len(matrix1[0])):
        result[row][col] += matrix1[row][i] * matrix2[i][col]


def matrixMultiplication(matrix1, matrix2):
    result = [[0 for i in range(len(matrix2[0]))] for j in range(len(matrix1))]
    threads = []
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            thread = threading.Thread(target=matrixMultiplicationUsingThreading, args=(
                matrix1, matrix2, result, i, j))
            threads.append(thread)
            thread.start()
    for thread in threads:
        thread.join()
    return result

# Driver code
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = matrixMultiplication(matrix1, matrix2)
for row in result:
    print(row)
