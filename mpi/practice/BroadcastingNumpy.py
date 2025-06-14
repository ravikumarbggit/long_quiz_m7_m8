from mpi4py import MPI # Importing mpi4py package from MPI module
import numpy as np # Importing numpy package under a name np
# Defining a function
def main():
    # communicator
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()   # number of the process running the code
    size = comm.Get_size()   # total number of processes running
    if rank == 0:
        # Generate a Numpy arary with arbitrary data in it
        data = np.ones(4)
    else:
        # start with empty data
        data = None
    # Broadcasting the data
    data = comm.bcast(data, root=0)
    # Printing the results
    if rank == 0:
        print('Process {} broadcast data:'.format(rank), data)
    else:
        print('Process {} received data:'.format(rank), data)
# Calling the main function
main()