import numpy as np
import matplotlib.pyplot as plt
import re
from matplotlib import rc
import pandas as pd

rc('font',**{'family':'serif','serif':['Times'],'size':7})
rc('text', usetex=True)

df = pd.read_csv("postProcessing/probes1/0/U", delim_whitespace=True, header=None, comment='#')
df = df.replace(r"[()]", "", regex=True)
values = df.astype(float).values

fig = plt.figure()

plt.xlim([0,25])
plt.ylim([-0.1,0.1])

ax1 = fig.add_subplot(111)

ax1.set_xlabel('$t$ [s]',size=9)
ax1.set_ylabel(r'$\displaystyle u_{\textrm{y}}$ [m/s]',size=9)

plt.xticks(np.arange(0, 25.001, 5))
plt.yticks(np.arange(-0.1, 0.1001, 0.05))


ax1.plot(values[:, 0], values[:, 2],  c='r', linewidth=0.5, label='x = 2.5D')

leg = ax1.legend(loc='upper left',frameon=False,ncol=1)

plt.subplots_adjust(top=0.95,bottom=0.2,left=0.2,right=0.84)

fig.set_size_inches(3, 2.1)
plt.savefig('velProbe.png', dpi=1000)

