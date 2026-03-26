cd TFM
reconstructPar -fields '(alpha.particles U.particles U.air)' > ../post.log 2>&1
foamToVTK -fields '(alpha.particles U.particles U.air)' >> ../post.log 2>&1
cd ..
python3 plotProbes.py >> post.log 2>&1
