from mpi4py import MPI # Importing mpi4py package from MPI module
# Defining a function
def main():
    # Creating a communicator
    comm = MPI.COMM_WORLD
    # number of the process running the code
    rank = comm.Get_rank()
    # total number of processes running
    size = comm.Get_size()
    # master process
    if rank == 0:
        # Generate a dictionary with arbitrary data in it
        data = {'States' : ["Hyderabad", "Goa", "Punjab"]}
        # master process sends data to worker processes by
        # going through the ranks of all worker processes
        for i in range(1, size):
            # Sending data
            comm.send(data, dest=i, tag=i)
            # Displaying the results
            print('Process {} sent data:'.format(rank), data)
    # worker processes
    else:
        # each worker process receives data from master process
        data = comm.recv(source=0, tag=rank)
        # Displaying the results
        print('Process {} received data:'.format(rank), data)
# Calling the function
main()