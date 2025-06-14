from mpi4py import MPI # Importing mpi4py package from MPI module
import numpy as np # Importing numpy package under a name np
# Defining a function
def main():
    # communicator
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()   # number of the process running the code
    size = comm.Get_size()   # total number of processes running
    # Create numpy arrays on each process: For this experiment, the arrays have only one
    # entry that is assigned to be the rank of the processor
    value = np.array(rank,'d')
    # Displaying the value and its rank
    print(' Rank: ',rank, ' value = ', value)
    # initialize the np arrays that will store the results:
    value_sum      = np.array(0.0,'d')
    value_max      = np.array(0.0,'d')
    # perform the reductions:
    comm.Reduce(value, value_sum, op=MPI.SUM, root=0)
    comm.Reduce(value, value_max, op=MPI.MAX, root=0)
    # Displaying the result
    if rank == 0:
        print(' Rank 0: value_sum =    ',value_sum)
        print(' Rank 0: value_max =    ',value_max)
# Calling a function
main()