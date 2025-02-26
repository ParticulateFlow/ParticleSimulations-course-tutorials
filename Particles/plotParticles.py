# trace generated using paraview version 5.7.0
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'STL Reader'
back_80000stl = STLReader(FileNames=['./post/back_80000.stl'])

# create a new 'STL Reader'
bottom1_80000stl = STLReader(FileNames=['./post/bottom1_80000.stl'])

# create a new 'STL Reader'
bottom2_80000stl = STLReader(FileNames=['./post/bottom2_80000.stl'])

# create a new 'STL Reader'
cylinder_80000stl = STLReader(FileNames=['./post/cylinder_80000.stl'])

# create a new 'Legacy VTK Reader'
dump80000vtk = LegacyVTKReader(FileNames=['./post/dump80000.vtk'])

# create a new 'STL Reader'
sides_80000stl = STLReader(FileNames=['./post/sides_80000.stl'])

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1017, 795]

# show data in view
back_80000stlDisplay = Show(back_80000stl, renderView1)

# get color transfer function/color map for 'STLSolidLabeling'
sTLSolidLabelingLUT = GetColorTransferFunction('STLSolidLabeling')

# trace defaults for the display properties.
back_80000stlDisplay.Representation = 'Surface'
back_80000stlDisplay.ColorArrayName = ['CELLS', 'STLSolidLabeling']
back_80000stlDisplay.LookupTable = sTLSolidLabelingLUT
back_80000stlDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
back_80000stlDisplay.SelectOrientationVectors = 'None'
back_80000stlDisplay.ScaleFactor = 0.04000000134110451
back_80000stlDisplay.SelectScaleArray = 'STLSolidLabeling'
back_80000stlDisplay.GlyphType = 'Arrow'
back_80000stlDisplay.GlyphTableIndexArray = 'STLSolidLabeling'
back_80000stlDisplay.GaussianRadius = 0.0020000000670552256
back_80000stlDisplay.SetScaleArray = [None, '']
back_80000stlDisplay.ScaleTransferFunction = 'PiecewiseFunction'
back_80000stlDisplay.OpacityArray = [None, '']
back_80000stlDisplay.OpacityTransferFunction = 'PiecewiseFunction'
back_80000stlDisplay.DataAxesGrid = 'GridAxesRepresentation'
back_80000stlDisplay.PolarAxes = 'PolarAxesRepresentation'

# reset view to fit data
renderView1.ResetCamera()

#changing interaction mode based on data extents
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.1, 0.0, 10000]
renderView1.CameraFocalPoint = [0.1, 0.0, -0.005]

# show color bar/color legend
back_80000stlDisplay.SetScalarBarVisibility(renderView1, True)

# show data in view
bottom1_80000stlDisplay = Show(bottom1_80000stl, renderView1)

# trace defaults for the display properties.
bottom1_80000stlDisplay.Representation = 'Surface'
bottom1_80000stlDisplay.ColorArrayName = ['CELLS', 'STLSolidLabeling']
bottom1_80000stlDisplay.LookupTable = sTLSolidLabelingLUT
bottom1_80000stlDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
bottom1_80000stlDisplay.SelectOrientationVectors = 'None'
bottom1_80000stlDisplay.ScaleFactor = 0.01
bottom1_80000stlDisplay.SelectScaleArray = 'STLSolidLabeling'
bottom1_80000stlDisplay.GlyphType = 'Arrow'
bottom1_80000stlDisplay.GlyphTableIndexArray = 'STLSolidLabeling'
bottom1_80000stlDisplay.GaussianRadius = 0.0005
bottom1_80000stlDisplay.SetScaleArray = [None, '']
bottom1_80000stlDisplay.ScaleTransferFunction = 'PiecewiseFunction'
bottom1_80000stlDisplay.OpacityArray = [None, '']
bottom1_80000stlDisplay.OpacityTransferFunction = 'PiecewiseFunction'
bottom1_80000stlDisplay.DataAxesGrid = 'GridAxesRepresentation'
bottom1_80000stlDisplay.PolarAxes = 'PolarAxesRepresentation'

# show color bar/color legend
bottom1_80000stlDisplay.SetScalarBarVisibility(renderView1, True)

# show data in view
bottom2_80000stlDisplay = Show(bottom2_80000stl, renderView1)

# trace defaults for the display properties.
bottom2_80000stlDisplay.Representation = 'Surface'
bottom2_80000stlDisplay.ColorArrayName = ['CELLS', 'STLSolidLabeling']
bottom2_80000stlDisplay.LookupTable = sTLSolidLabelingLUT
bottom2_80000stlDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
bottom2_80000stlDisplay.SelectOrientationVectors = 'None'
bottom2_80000stlDisplay.ScaleFactor = 0.01
bottom2_80000stlDisplay.SelectScaleArray = 'STLSolidLabeling'
bottom2_80000stlDisplay.GlyphType = 'Arrow'
bottom2_80000stlDisplay.GlyphTableIndexArray = 'STLSolidLabeling'
bottom2_80000stlDisplay.GaussianRadius = 0.005
bottom2_80000stlDisplay.SetScaleArray = [None, '']
bottom2_80000stlDisplay.ScaleTransferFunction = 'PiecewiseFunction'
bottom2_80000stlDisplay.OpacityArray = [None, '']
bottom2_80000stlDisplay.OpacityTransferFunction = 'PiecewiseFunction'
bottom2_80000stlDisplay.DataAxesGrid = 'GridAxesRepresentation'
bottom2_80000stlDisplay.PolarAxes = 'PolarAxesRepresentation'

# show color bar/color legend
bottom2_80000stlDisplay.SetScalarBarVisibility(renderView1, True)

# show data in view
cylinder_80000stlDisplay = Show(cylinder_80000stl, renderView1)

# trace defaults for the display properties.
cylinder_80000stlDisplay.Representation = 'Surface'
cylinder_80000stlDisplay.ColorArrayName = ['CELLS', 'STLSolidLabeling']
cylinder_80000stlDisplay.LookupTable = sTLSolidLabelingLUT
cylinder_80000stlDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
cylinder_80000stlDisplay.SelectOrientationVectors = 'None'
cylinder_80000stlDisplay.ScaleFactor = 0.002
cylinder_80000stlDisplay.SelectScaleArray = 'STLSolidLabeling'
cylinder_80000stlDisplay.GlyphType = 'Arrow'
cylinder_80000stlDisplay.GlyphTableIndexArray = 'STLSolidLabeling'
cylinder_80000stlDisplay.GaussianRadius = 1.e-04
cylinder_80000stlDisplay.SetScaleArray = [None, '']
cylinder_80000stlDisplay.ScaleTransferFunction = 'PiecewiseFunction'
cylinder_80000stlDisplay.OpacityArray = [None, '']
cylinder_80000stlDisplay.OpacityTransferFunction = 'PiecewiseFunction'
cylinder_80000stlDisplay.DataAxesGrid = 'GridAxesRepresentation'
cylinder_80000stlDisplay.PolarAxes = 'PolarAxesRepresentation'

# show color bar/color legend
cylinder_80000stlDisplay.SetScalarBarVisibility(renderView1, True)

# show data in view
dump80000vtkDisplay = Show(dump80000vtk, renderView1)

# trace defaults for the display properties.
dump80000vtkDisplay.Representation = 'Surface'
dump80000vtkDisplay.ColorArrayName = [None, '']
dump80000vtkDisplay.OSPRayScaleArray = 'id'
dump80000vtkDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
dump80000vtkDisplay.SelectOrientationVectors = 'None'
dump80000vtkDisplay.ScaleFactor = 0.02
dump80000vtkDisplay.SelectScaleArray = 'None'
dump80000vtkDisplay.GlyphType = 'Arrow'
dump80000vtkDisplay.GlyphTableIndexArray = 'None'
dump80000vtkDisplay.GaussianRadius = 0.001
dump80000vtkDisplay.SetScaleArray = ['POINTS', 'id']
dump80000vtkDisplay.ScaleTransferFunction = 'PiecewiseFunction'
dump80000vtkDisplay.OpacityArray = ['POINTS', 'id']
dump80000vtkDisplay.OpacityTransferFunction = 'PiecewiseFunction'
dump80000vtkDisplay.DataAxesGrid = 'GridAxesRepresentation'
dump80000vtkDisplay.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
dump80000vtkDisplay.ScaleTransferFunction.Points = [2.0, 0.0, 0.5, 0.0, 10224.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
dump80000vtkDisplay.OpacityTransferFunction.Points = [2.0, 0.0, 0.5, 0.0, 10224.0, 1.0, 0.5, 0.0]

# show data in view
sides_80000stlDisplay = Show(sides_80000stl, renderView1)

# trace defaults for the display properties.
sides_80000stlDisplay.Representation = 'Surface'
sides_80000stlDisplay.ColorArrayName = ['CELLS', 'STLSolidLabeling']
sides_80000stlDisplay.LookupTable = sTLSolidLabelingLUT
sides_80000stlDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
sides_80000stlDisplay.SelectOrientationVectors = 'None'
sides_80000stlDisplay.ScaleFactor = 0.04
sides_80000stlDisplay.SelectScaleArray = 'STLSolidLabeling'
sides_80000stlDisplay.GlyphType = 'Arrow'
sides_80000stlDisplay.GlyphTableIndexArray = 'STLSolidLabeling'
sides_80000stlDisplay.GaussianRadius = 0.002
sides_80000stlDisplay.SetScaleArray = [None, '']
sides_80000stlDisplay.ScaleTransferFunction = 'PiecewiseFunction'
sides_80000stlDisplay.OpacityArray = [None, '']
sides_80000stlDisplay.OpacityTransferFunction = 'PiecewiseFunction'
sides_80000stlDisplay.DataAxesGrid = 'GridAxesRepresentation'
sides_80000stlDisplay.PolarAxes = 'PolarAxesRepresentation'

# show color bar/color legend
sides_80000stlDisplay.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# get opacity transfer function/opacity map for 'STLSolidLabeling'
sTLSolidLabelingPWF = GetOpacityTransferFunction('STLSolidLabeling')

# set active source
SetActiveSource(dump80000vtk)

# create a new 'Glyph'
glyph1 = Glyph(Input=dump80000vtk,GlyphType='Sphere')
glyph1.OrientationArray = ['POINTS', 'No orientation array']
glyph1.ScaleArray = ['POINTS', 'No scale array']
glyph1.ScaleFactor = 1.0
glyph1.GlyphType.Radius = 0.0015
glyph1.GlyphTransform = 'Transform2'

# Properties modified on glyph1
glyph1.GlyphMode = 'All Points'

# show data in view
glyph1Display = Show(glyph1, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# hide data in view
Hide(dump80000vtk, renderView1)

# set active source
SetActiveSource(dump80000vtk)

# show data in view
dump80000vtkDisplay = Show(dump80000vtk, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(sides_80000stl)

# hide color bar/color legend
sides_80000stlDisplay.SetScalarBarVisibility(renderView1, False)

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.1, 0.0, 10000]
renderView1.CameraFocalPoint = [0.1, 0.0, -0.005]
renderView1.CameraViewUp = [1.0, 0, 0.0]
renderView1.CameraParallelScale = 0.22360680441398084

# save screenshot
SaveScreenshot('./particles.png', renderView1, ImageResolution=[1017, 795])
