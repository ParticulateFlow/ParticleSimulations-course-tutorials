cd CFD
rm -r 0
cp -r orig.0 0
rm -r constant/polyMesh
blockMesh

decomposePar
cd ..
