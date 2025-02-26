import numpy as np
import matplotlib.pyplot as plt
import re
from matplotlib import rc
import pandas as pd

rc('font',**{'family':'serif','serif':['Times'],'size':7})
rc('text', usetex=True)

df = pd.read_csv("stat.txt", delim_whitespace=True, header=None, comment='#')
values = df.values

fig = plt.figure()

plt.xlim([0,4])
plt.ylim([0,12500])

ax1 = fig.add_subplot(111)

ax1.set_xlabel('$t$ [s]',size=9)
ax1.set_ylabel(r'$\displaystyle N_{\textrm{p}}$',size=9)

plt.xticks(np.arange(0, 4.001, 1.0))
plt.yticks(np.arange(0.0, 12500.001, 5000))


ax1.plot(values[:, 0], values[:, 1],  c='r', linewidth=0.5, label='_nolabel_')

leg = ax1.legend(loc='upper left',frameon=False,ncol=1)

plt.subplots_adjust(top=0.95,bottom=0.2,left=0.2,right=0.84)

fig.set_size_inches(3, 2.1)
plt.savefig('particleNumber.png', dpi=1000)

