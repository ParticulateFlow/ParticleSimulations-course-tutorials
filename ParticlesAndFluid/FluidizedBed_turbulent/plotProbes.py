import numpy as np
import matplotlib.pyplot as plt
import re
from matplotlib import rc
from matplotlib.ticker import FormatStrFormatter
import pandas as pd

rc('font',**{'family':'serif','serif':['Times'],'size':7})
rc('text', usetex=True)

df = pd.read_csv("TFM/postProcessing/probes1/0/U.air", delim_whitespace=True, header=None, comment='#')
df = df.replace(r"[()]", "", regex=True)
U = df.astype(float).values

df = pd.read_csv("TFM/postProcessing/probes1/0/U.particles", delim_whitespace=True, header=None, comment='#')
df = df.replace(r"[()]", "", regex=True)
Us = df.astype(float).values

df = pd.read_csv("TFM/postProcessing/probes1/0/alpha.particles", delim_whitespace=True, header=None, comment='#')
df = df.replace(r"[()]", "", regex=True)
volfraction = df.astype(float).values

fig = plt.figure(0)

plt.xlim([0,5])
plt.ylim([-0.5,3.0])

ax1 = fig.add_subplot(111)

ax1.set_xlabel('$t$ [s]',size=9)
ax1.set_ylabel(r'$\displaystyle u_{\textrm{g,z}}$ [m/s]',size=9)

plt.xticks(np.arange(0, 5.001, 2.5))
plt.yticks(np.arange(0.0, 3.001, 1))
ax1.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))

ax1.plot(U[:, 0], U[:, 3],  c='r', linewidth=0.5, label='z = 0.5')

leg = ax1.legend(loc='upper left',frameon=False,ncol=1)

plt.subplots_adjust(top=0.95,bottom=0.2,left=0.2,right=0.84)

fig.set_size_inches(3, 2.1)
plt.savefig('probe_U.png', dpi=1000)


fig = plt.figure(1)

plt.xlim([0,5])
plt.ylim([-0.5,1.5])

ax1 = fig.add_subplot(111)

ax1.set_xlabel('$t$ [s]',size=9)
ax1.set_ylabel(r'$\displaystyle u_{\textrm{s,z}}$ [m/s]',size=9)

plt.xticks(np.arange(0, 5.001, 2.5))
plt.yticks(np.arange(0.0, 1.001, 1.0))
ax1.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))

ax1.plot(Us[:, 0], Us[:, 3],  c='r', linewidth=0.5, label='z = 0.5')

leg = ax1.legend(loc='lower left',frameon=False,ncol=1)

plt.subplots_adjust(top=0.95,bottom=0.2,left=0.2,right=0.84)

fig.set_size_inches(3, 2.1)
plt.savefig('probe_Us.png', dpi=1000)


fig = plt.figure(2)

plt.xlim([0,5])
plt.ylim([0.0,1])

ax1 = fig.add_subplot(111)

ax1.set_xlabel('$t$ [s]',size=9)
ax1.set_ylabel(r'$\displaystyle \alpha_{\textrm{p}}$',size=9)

plt.xticks(np.arange(0, 5.001, 2.5))
plt.yticks(np.arange(0.0, 1.001, 0.5))
ax1.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))

ax1.plot(volfraction[:, 0], volfraction[:, 1],  c='r', linewidth=0.5, label='z = 0.5')

leg = ax1.legend(loc='upper left',frameon=False,ncol=1)

plt.subplots_adjust(top=0.95,bottom=0.2,left=0.2,right=0.84)

fig.set_size_inches(3, 2.1)
plt.savefig('probe_volumefraction.png', dpi=1000)
