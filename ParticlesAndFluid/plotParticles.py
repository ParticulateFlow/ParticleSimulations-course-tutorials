import vtk
import numpy as np
from matplotlib import rc
import matplotlib.pyplot as plt
import matplotlib.patches as patches

rc('font',**{'family':'serif','serif':['Times'],'size':11})
rc('text', usetex=True)

def read_vtk(filename):
    # Read VTK file
    reader = vtk.vtkPolyDataReader()
    reader.SetFileName(filename)
    reader.Update()

    # Get particle positions and radii
    points = reader.GetOutput().GetPoints()
    radii = reader.GetOutput().GetPointData().GetArray('radius')

    particle_positions = np.array([points.GetPoint(i) for i in range(points.GetNumberOfPoints())])
    particle_radii = np.array([radii.GetValue(i) for i in range(radii.GetNumberOfValues())])
    
    return particle_positions, particle_radii

def plot_particles_2d(positions, radii, filename):
    fig, ax = plt.subplots()
    ax.scatter(positions[:, 1], positions[:, 0], s=radii * 1000, c='b', alpha=0.5)
    ax.set_xlabel('')
    ax.set_ylabel('')
    ax.set_aspect('equal', 'box')
    ax.set_xlim([-0.1, 0.1])
    ax.set_ylim([-0.1, 0.2])
    ax.set_xticks(np.linspace(-0.1, 0.1, 3))  # 6 ticks from 0 to 10
    ax.set_yticks(np.linspace(-0.1, 0.2, 4))
    
    circle = patches.Circle((0,0), 0.01, edgecolor='black', facecolor='black', linewidth=2)
    ax.add_patch(circle)
    
    plt.savefig(filename, dpi=1000)

for i in range(1,11):
    positions, radii = read_vtk('DEM/post/dump'+str(i)+'00000.vtk')
    plot_particles_2d(positions, radii, 'particles_'+str(i)+'.png')
