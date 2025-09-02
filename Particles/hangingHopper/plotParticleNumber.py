import numpy as np
import matplotlib.pyplot as plt
import re
from matplotlib import rc
import pandas as pd

rc('font',**{'family':'serif','serif':['Times'],'size':7})
rc('text', usetex=True)

df = pd.read_csv("stat_reference.txt", delim_whitespace=True, header=None, comment='#')
df = df.replace(r"[()]", "", regex=True)
values0 = df.values

t0 = values0[:,0]
f0 = values0[:,1]/values0[0,1]

df = pd.read_csv("stat_diameter.txt", delim_whitespace=True, header=None, comment='#')
df = df.replace(r"[()]", "", regex=True)
values1 = df.values

t1 = values1[:,0]
f1 = values1[:,1]/values1[0,1]

df = pd.read_csv("stat_angle.txt", delim_whitespace=True, header=None, comment='#')
df = df.replace(r"[()]", "", regex=True)
values2 = df.values

t2 = values2[:,0]
f2 = values2[:,1]/values2[0,1]

df = pd.read_csv("stat3_friction.txt", delim_whitespace=True, header=None, comment='#')
df = df.replace(r"[()]", "", regex=True)
values3 = df.values

t3 = values3[:,0]
f3 = values3[:,1]/values3[0,1]

step = 100
for i in range(0,t0.size,step):
    fig = plt.figure()

    plt.xlim([0,5])
    plt.ylim([0.9,1.04])

    ax1 = fig.add_subplot(111)

    ax1.set_xlabel('$t$ [s]',size=9)
    ax1.set_ylabel('N(t)/N(0)',size=9)

    plt.xticks(np.arange(0, 5.001, 1))
    plt.yticks(np.arange(0.9, 1.0401, 0.05))

    ax1.plot(t0, f0,  c='r', linewidth=0.5, label='base')
    if i>0:
        ax1.plot(t1[:i], f1[:i],  c='b', linewidth=0.5, label='diameter')
        ax1.plot(t2[:i], f2[:i],  c='g', linewidth=0.5, label='angle')
        ax1.plot(t3[:i], f3[:i],  c='orange', linewidth=0.5, label='wall friction')

    if i>0 and i<t0.size-1:
        ax1.plot(t1[i-1], f1[i-1], 'bo', markersize=2)
        ax1.plot(t2[i-1], f2[i-1], 'go', markersize=2)
        ax1.plot(t3[i-1], f3[i-1], 'o', color='orange', markersize=2)

    leg = ax1.legend(loc='upper left',frameon=False,ncol=2)

    plt.subplots_adjust(top=0.95,bottom=0.2,left=0.2,right=0.84)

    fig.set_size_inches(3, 2.1)
    t = i/100
    filename = f"N_{t:01d}.png"
    plt.savefig(filename, dpi=250)

