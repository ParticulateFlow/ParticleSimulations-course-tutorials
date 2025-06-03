cd CFD
mpirun -np 4 cfdemSolverIB -parallel > run.log 2>&1
reconstructParMesh -mergeTol 1e-06 > ../post.log 2>&1
reconstructPar -noLagrangian -fields '(U Us voidfraction)' >> ../post.log 2>&1
foamToVTK -fields '(U Us voidfraction)' >> ../post.log 2>&1
cd ..
