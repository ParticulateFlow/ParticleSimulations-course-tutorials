import numpy as np
import matplotlib.pyplot as plt
import re
from matplotlib import rc
from matplotlib.ticker import FormatStrFormatter
import pandas as pd

rc('font',**{'family':'serif','serif':['Times'],'size':7})
rc('text', usetex=True)

df = pd.read_csv("DEM/stat.txt", delim_whitespace=True, header=None, comment='#')
df = df.replace(r"[()]", "", regex=True)
cm = df.astype(float).values


fig = plt.figure(0)

plt.xlim([0,5])
plt.ylim([-0.025,0.0])

ax1 = fig.add_subplot(111)

ax1.set_xlabel('$t$ [s]',size=9)
ax1.set_ylabel(r'$\displaystyle x_{\textrm{cm}}$ [m]',size=9)

plt.xticks(np.arange(0, 5.001, 1.0))
plt.yticks(np.arange(-0.025, 0.0001, 0.025))
ax1.yaxis.set_major_formatter(FormatStrFormatter('%.3f'))

ax1.plot(cm[:, 0], cm[:, 3],  c='r', linewidth=0.5, label='_nolabel_')

plt.annotate(
    'particles dropping and then\n settling in container',
    xy=(0.3, -0.005),
    xytext=(1, -0.008),
    arrowprops=dict(arrowstyle='->')
)

plt.annotate(
    'fluidization velocity reached',
    xy=(1.0, -0.02),
    xytext=(1.75, -0.022),
    arrowprops=dict(arrowstyle='->')
)


leg = ax1.legend(loc='upper right',frameon=False,ncol=1)

plt.subplots_adjust(top=0.95,bottom=0.2,left=0.2,right=0.84)

fig.set_size_inches(3, 2.1)
plt.savefig('particle_center_of_mass_coordinate.png', dpi=1000)



fig = plt.figure(1)

plt.xlim([0,5])
plt.ylim([-0.1,0.1])

ax1 = fig.add_subplot(111)

ax1.set_xlabel('$t$ [s]',size=9)
ax1.set_ylabel(r'$\displaystyle v_{\textrm{cm}}$ [m/s]',size=9)

plt.xticks(np.arange(0, 5.001, 1.0))
plt.yticks(np.arange(-0.1, 0.1001, 0.1))
ax1.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))

ax1.plot(cm[:, 0], cm[:, 4],  c='r', linewidth=0.5, label='_nolabel_')

plt.annotate(
    'particles dropping and then\n settling in container',
    xy=(0.3, -0.05),
    xytext=(1, -0.08),
    arrowprops=dict(arrowstyle='->')
)

plt.annotate(
    'fluidization velocity reached',
    xy=(0.85, 0.001),
    xytext=(0.25, 0.08),
    arrowprops=dict(arrowstyle='->')
)

leg = ax1.legend(loc='upper right',frameon=False,ncol=1)

plt.subplots_adjust(top=0.95,bottom=0.2,left=0.2,right=0.84)

fig.set_size_inches(3, 2.1)
plt.savefig('particle_center_of_mass_velocity.png', dpi=1000)
