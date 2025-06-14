from mpi4py import MPI
import random
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Matrix dimensions (adjustable)
# rows_A, cols_A = 6, 4
# rows_B, cols_B = 4, 5
rows_A, cols_A = 300, 400
rows_B, cols_B = 400, 200


def generate_matrix(rows, cols):
    return [[random.random() for _ in range(cols)] for _ in range(rows)]

def multiply_chunk(chunk_A, B):
    result_chunk = []
    for row in chunk_A:
        result_row = [sum(a*b for a, b in zip(row, col)) for col in zip(*B)]
        result_chunk.append(result_row)
    return result_chunk


def mpi_matmult():
    if rank == 0:
        A = generate_matrix(rows_A, cols_A)
        B = generate_matrix(rows_B, cols_B)

        # Split A into chunks for each process
        chunk_size = rows_A // size
        chunks = [A[i * chunk_size:(i + 1) * chunk_size] for i in range(size)]

        start_time = time.time()
    else:
        chunks = None
        B = None

    # Scatter A chunks and broadcast B
    local_A = comm.scatter(chunks, root=0)
    B = comm.bcast(B, root=0)

    # Each process computes its chunk
    local_result = multiply_chunk(local_A, B)

    # Gather results
    gathered_result = comm.gather(local_result, root=0)

    if rank == 0:
        result = [row for chunk in gathered_result for row in chunk]
        end_time = time.time()
        print("MPI Matrix multiplication completed.")
        print(f"Time taken: {end_time - start_time:.6f} seconds")

mpi_matmult()