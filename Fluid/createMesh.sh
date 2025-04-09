rm -r 0
cp -r orig.0 0
rm -r constant/polyMesh
rm -r surface
mkdir surface
blockMesh > mesh.log 2>&1
foamToVTK >> mesh.log 2>&1
mv VTK VTK_mesh

# extract surface for usage as walls in DEM simulation
foamToSurface surface/surface.stl > /dev/null 2>&1
surfaceSplitByPatch surface/surface.stl > /dev/null 2>&1
# split inlet patch into two parts to create outlet for DEM particles
surfaceSubset surface/surface_in.stl surface/surface_in1.stl system/surfaceSubsetDict1 > /dev/null 2>&1
surfaceSubset surface/surface_in.stl surface/surface_in2.stl system/surfaceSubsetDict2 > /dev/null 2>&1
