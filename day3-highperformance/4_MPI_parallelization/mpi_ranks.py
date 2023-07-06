from mpi4py import MPI

#Initializing MPI
comm = MPI.COMM_WORLD

#Get rank of running process
rank = comm.Get_rank()

#Print rank of each process
print("Rank:", rank)
