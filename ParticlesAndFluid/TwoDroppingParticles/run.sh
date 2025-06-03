cd CFD
mpirun -np 4 cfdemSolverIB -parallel > run.log 2>&1
reconstructParMesh -mergeTol 1e-06
reconstructPar -noLagrangian
foamToVTK
cd ..
