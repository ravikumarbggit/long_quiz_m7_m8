from mpi4py import MPI # Importing mpi4py package from MPI module
# Defining a function
def main():
    comm = MPI.COMM_WORLD
    id = comm.Get_rank()            #number of the process running the code
    numProcesses = comm.Get_size()  #total number of processes running
    if id == 0:
        # Generate a dictionary with arbitrary data in it
        data = {'States' : ["Hyderabad", "Goa", "Punjab"]}
    else:
        # start with empty data
        data = None
    # Broadcasting the data
    data = comm.bcast(data, root=0)
    # Printing the data along with the id number
    print('Rank: ',id,', data: ' ,data)

# Calling a function
main()