cd CFD
mpirun -np 4 cfdemSolverPiso -parallel > run.log 2>&1
cd ..
