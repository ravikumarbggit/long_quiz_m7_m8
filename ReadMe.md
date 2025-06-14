
## Matrix Multiplication

## Standard matrix multiplication

```bash
python .\standard\mat-mult.py
```

![Screenshot of Standard matrix multiplication.](/assets/images/standard-mat-mult.png)

Time taken is **2.7** seconds


## MPI base matrix multiplication with 2 nodes
```bash
mpiexec /np 2 python .\mpi\mat-mult.py
```

![Screenshot of MPI based matrix multiplication with 2 nodes.](/assets/images/mp-mat-mult-2-nodes.png)


Time taken is **0.61** seconds


## MPI base matrix multiplication with 4 nodes
```bash
mpiexec /np 4 python .\mpi\mat-mult.py
```


![Screenshot of MPI based matrix multiplication with 4 nodes.](/assets/images/mp-mat-mult-4-nodes.png)

Time taken is **0.38** seconds


## Banchmarking result

Matrix dimension

rows_A, cols_A = 300, 400
rows_B, cols_B = 400, 200

With standard multiplication matrix multiplication took 2.7 seconds

With MPI 2 nodes it took 0.61 seconds
With MPI 4 nodes it took 0.32 seconds

Improvement in performance

((New Value - Old Value) / Old Value) * 100

**the performance improved by approximately _88.15%_** :tada:

## Appendix

### To run MPI rank

```bash
mpiexec /np 4 python .\mpi\practice\rank.py
```

### To run MPI comm

```bash
mpiexec /np 2 python .\mpi\practice\comm.py
```

### Ro run MPI passing dictionary

```bash
mpiexec /np 3 python .\mpi\practice\passing_dict.py
```

### Non blocking array

```bash
mpiexec /np 4 python .\mpi\practice\nonblockingarray.py
```

### overlapping commuication

```bash
mpiexec /np 2 python .\mpi\practice\overlappingCommunication.py
```

### Broadcasting dictionary

```bash
mpiexec /np 4 python .\mpi\practice\BroadcastingDictionary.py
```

### Broadcasting numpy array

```bash
mpiexec /np 4 python .\mpi\practice\BroadcastingNumpy.py
```

### Scattering numpy array

```bash
mpiexec /np 6 python .\mpi\practice\ScatteringNumpyArray.py
```

### Gathering numpy array

```bash
mpiexec /np 2 python .\mpi\practice\GatherringNumPyArray.py
```

### Gathering numpy array

```bash
mpiexec /np 2 python .\mpi\practice\ReducingNumpyArray.py
```

