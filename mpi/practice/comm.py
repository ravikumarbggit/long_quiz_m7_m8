from mpi4py import MPI # Importing mpi4py package from MPI module
# Defining a function
def main():
    # Creating a Communicator
    comm = MPI.COMM_WORLD
    #number of the process running the code
    rank = comm.Get_rank()
    # total number of processes running
    size = comm.Get_size()
    # master process
    if rank == 0:
        data = 123 # Defining a integer
        # master process sends data to worker processes by
        # going through the ranks of all worker processes
        for i in range(1, size):
            # Sending the data to each process
            comm.send(data, dest=i, tag=i)
            print('Process {} sent data:'.format(rank), data)
    # worker processes
    else:
        # each worker process receives data from master process
        data = comm.recv(source=0, tag=rank)
        print('Process {} received data:'.format(rank), data)
main()