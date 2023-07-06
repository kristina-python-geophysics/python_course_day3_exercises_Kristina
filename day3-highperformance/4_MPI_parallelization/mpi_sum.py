from mpi4py import MPI

#Initializing MPI
comm = MPI.COMM_WORLD

#Get rank of running process
rank = comm.Get_rank()

#Define number for each process
number = rank + 1

#Summarize
total = comm.reduce(number, op=MPI.SUM, root=0)

#Print the result from process with rank 0
if rank == 0:
	print("Sum:", total)
