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
    velocities = reader.GetOutput().GetPointData().GetArray('v')

    particle_positions = np.array([points.GetPoint(i) for i in range(points.GetNumberOfPoints())])
    particle_radii = np.array([radii.GetValue(i) for i in range(radii.GetNumberOfValues())])
    particle_velocities = np.array([velocities.GetValue(i) for i in range(velocities.GetNumberOfValues())])
    particle_velocities = particle_velocities.reshape(-1, 3)
    particle_velocity_magnitudes = np.sum(particle_velocities**2, axis=1)
    particle_velocity_magnitudes = np.sqrt(particle_velocity_magnitudes)
    
    return particle_positions, particle_radii, particle_velocity_magnitudes

def plot_particles_2d(positions, radii, velocity_magnitudes, filename):
    fig, ax = plt.subplots()
    scatter = ax.scatter(positions[:, 1], positions[:, 0], s=radii * 1000, c=velocity_magnitudes, cmap='coolwarm', vmin=0, vmax=0.5, alpha=0.5)
    cbar = fig.colorbar(scatter, ax=ax)
    cbar.set_label('$|u|$ [m/s]', labelpad=15, fontsize=14)
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

for i in range(1,51):
    positions, radii, velocity_magnitudes = read_vtk('DEM/post/dump'+str(i)+'0000.vtk')
    plot_particles_2d(positions, radii, velocity_magnitudes, 'particles_'+str(i)+'.png')
