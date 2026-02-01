import numpy as np
import matplotlib.pyplot as plt

counts = np.array([8885,9570,10366,11772,12661,14163,15590,17102,18804,20800,22949,25035,27686])
background = 1009
net_counts = counts - background
t = np.array([72,66,60,54,48,42,36,30,24,18,12,6,0])
print(net_counts)
plt.plot(t, net_counts, marker='o', label='Data points')
plt.hlines(13843, xmin=0, xmax=max(t), colors='r', linestyles='dashed', label='Half Value Line (13843 counts)')
plt.vlines(39, ymin=0, ymax=max(net_counts), colors='r', linestyles='dashed', label='Half value thickness (39 mm)')
plt.xlabel('Absorber Thickness (mm)')
plt.ylabel('Net Counts')
plt.title('Net Counts vs Thickness of Al')
plt.legend()
plt.grid()
plt.show()