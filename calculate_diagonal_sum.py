def calculate_diagonal_sum(matrix: List[List[int]]) -> int:
    """
    Calculates the sum of elements along the main and anti-diagonals 
    of a square matrix. Avoids double-counting the center element for odd-sized matrices.
    """
    n = len(matrix)
    total_sum = 0
    
    for i in range(n):
        # Add element from the main diagonal (i, i)
        total_sum += matrix[i][i]
        
        # Add element from the anti-diagonal (i, n - 1 - i)
        j_anti = n - 1 - i
        total_sum += matrix[i][j_anti]

    # If 'n' is odd, the center element was counted twice (once in main, once in anti).
    # The center element is located at index (n//2, n//2).
    if n % 2 == 1:
        center_index = n // 2
        total_sum -= matrix[center_index][center_index]
        
    return total_sum

# Example Usage (3x3 matrix):
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Sum = (1+5+9) + (3+5+7) - 5 = 15 + 15 - 5 = 25
# print(calculate_diagonal_sum(matrix)) # Output: 25
