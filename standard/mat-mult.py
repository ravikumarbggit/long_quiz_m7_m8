import random
import time

# Define the size of the matrices
rows_A, cols_A = 300, 400
rows_B, cols_B = 400, 200

# Populate matrix A with random values
A = [[random.random() for _ in range(cols_A)] for _ in range(rows_A)]

# Populate matrix B with random values
B = [[random.random() for _ in range(cols_B)] for _ in range(rows_B)]

# Define result matrix with zeros
result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

# timer start
start_time = time.time()

# Perform matrix multiplication manually
for i in range(rows_A):
    for j in range(cols_B):
        for k in range(cols_A):
            result[i][j] += A[i][k] * B[k][j]

# timer end
end_time = time.time()

# Display result and time taken
print("Matrix multiplication completed.")
print(f"Time taken: {end_time - start_time:.6f} seconds")