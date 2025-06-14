from mpi4py import MPI # Importing mpi4py package from MPI module
import numpy as np # Importing numpy package under a name np
# Defining a function
def main():
    # communicator
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()   # number of the process running the code
    size = comm.Get_size()   # total number of processes running
    numDataPerRank = 10   # Number of elements in a array for each rank
    data = None # Starting with an empty  data
    if rank == 0:
        # Creating a Numpy array.
        data = np.linspace(1, size * numDataPerRank,numDataPerRank * size)
    # when size = 2 (using -n 2), data = [1.0:20.0]
    recvbuf = np.empty(numDataPerRank, dtype='d') # allocate space for recvbuf
    # scatter operation
    comm.Scatter(data, recvbuf, root=0)
    # Displaying the result
    print('Rank: ',rank, ', recvbuf received: ',recvbuf)
# Calling the main function
main()