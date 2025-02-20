rm -r 0
cp -r orig.0 0
rm -r constant/polyMesh
rm -r surface
mkdir surface
blockMesh
foamToSurface surface/surface.stl
surfaceSplitByPatch surface/surface.stl
