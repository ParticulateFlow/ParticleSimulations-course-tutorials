cd CFD
reconstructPar -fields '(U Us voidfraction)' > ../post.log 2>&1
foamToVTK -fields '(U Us voidfraction)' >> ../post.log 2>&1
cd ..
python3 plotProbes.py >> post.log 2>&1
python3 plotParticles.py >> post.log 2>&1
