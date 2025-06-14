from mpi4py import MPI # Importing mpi4py package from MPI module
import numpy as np # Importing Numpy Package undername np
# Defining a function
def main():
    # Creating a communicator
    comm = MPI.COMM_WORLD
    # number of the process running the code
    rank = comm.Get_rank()
    # Generating a random number
    randNum = np.zeros(1)
    # Generating a random float value in the open interval
    # diffNum = np.random.random_sample(1)
    if rank == 1:
        # Generating a random float value in the open interval
        randNum = np.random.random_sample(1)
        # Display the results
        print("Process", rank, "drew the number", randNum[0])
        # Sending the random number to the processes
        comm.Isend(randNum, dest=0)
        # Receiving the Passed random number from the process
        req = comm.Irecv(randNum, source=0)
        # Waiting for the reply
        req.Wait()
        # Displaying the received random number
        print("Process", rank, "received the number", randNum[0])
    if rank == 0:
        # Displaying the results before receiving the number
        print("Process", rank, "before receiving has the number", randNum[0])
        # Receiving the randomNumber
        req = comm.Irecv(randNum, source=1)
        # Waiting for the reply
        req.Wait()
        # Displaying the results
        print("Process", rank, "received the number", randNum[0])
        randNum *= 2
        # Sending the random Number
        comm.Isend(randNum, dest=1)
# Calling the function
main()