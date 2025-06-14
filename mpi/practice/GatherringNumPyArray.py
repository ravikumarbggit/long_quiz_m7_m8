from mpi4py import MPI # Importing mpi4py package from MPI module
import numpy as np # Importing numpy package under a name np
# Defining a function
def main():
    # communicator
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()   # number of the process running the code
    size = comm.Get_size()   # total number of processes running
    numDataPerRank = 10   # Number of elements in a array for each rank
    # Creating a sender buffer array
    sendbuf = np.linspace(rank * numDataPerRank + 1,(rank + 1) * numDataPerRank,numDataPerRank)
    # Printing the result
    print('Rank: ',rank, ', sendbuf: ',sendbuf)
    recvbuf = None
    if rank == 0:
        # Creating a receiver buffer array
        recvbuf = np.empty(numDataPerRank * size, dtype='d')
    # Gathering the Information
    comm.Gather(sendbuf, recvbuf, root = 0)
    # Display the result
    if rank == 0:
        print('Rank: ',rank, ', recvbuf received: ',recvbuf)
# Calling a function
main()