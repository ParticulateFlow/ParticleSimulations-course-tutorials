cd TFM
mpirun -np 8 twoPhaseEulerTurbFoam -parallel > run.log 2>&1
cd ..
