import numpy as np
import matplotlib.pyplot as plt
import re
from matplotlib import rc
from matplotlib.ticker import FormatStrFormatter
import pandas as pd

rc('font',**{'family':'serif','serif':['Times'],'size':7})
rc('text', usetex=True)

df = pd.read_csv("DEM/post/position_particle_1.txt", delim_whitespace=True, header=None, comment='#')
df = df.replace(r"[()]", "", regex=True)
r1 = df.astype(float).values

df = pd.read_csv("DEM/post/position_particle_2.txt", delim_whitespace=True, header=None, comment='#')
df = df.replace(r"[()]", "", regex=True)
r2 = df.astype(float).values


fig = plt.figure(0)

plt.xlim([0,0.3])
plt.ylim([0.0,4.0])

ax1 = fig.add_subplot(111)

ax1.set_xlabel('$t$ [s]',size=9)
ax1.set_ylabel(r'$\displaystyle z$ [m]',size=9)

plt.xticks(np.arange(0, 0.3001, 0.1))
plt.yticks(np.arange(0.0, 4.0001, 1.0))
ax1.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))

ax1.plot(r1[:, 0], r1[:, 3],  c='r', linewidth=0.5, label='particle 1')
ax1.plot(r2[:, 0], r2[:, 3],  c='b', linewidth=0.5, label='particle 2')


plt.annotate(
    'particles get into contact',
    xy=(0.15, 2.15),
    xytext=(0.025, 1.25),
    arrowprops=dict(arrowstyle='->')
)


plt.annotate(
    'particle 1 overtakes particle 2',
    xy=(0.295, 0.5),
    xytext=(0.075, 0.11),
    arrowprops=dict(arrowstyle='->')
)


leg = ax1.legend(loc='upper right',frameon=False,ncol=1)

plt.subplots_adjust(top=0.95,bottom=0.2,left=0.2,right=0.84)

fig.set_size_inches(3, 2.1)
plt.savefig('particle_positions.png', dpi=1000)
