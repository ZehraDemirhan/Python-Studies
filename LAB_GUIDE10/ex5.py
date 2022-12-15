import matplotlib.pyplot as plt
import numpy as np
plt.clf()
n_groups = 5
index = np.arange(n_groups)
print(index)
means_men = np.arange(1,10,2)*5
means_women = (25, 32, 34, 20, 25)
bar_width = 0.10
plt.bar(index,means_men, -bar_width,align='edge',color='r')
plt.bar(index,means_women, bar_width,align='edge',color='y')
plt.xlabel('Group')
plt.ylabel('Scores')
plt.title('Scores by group and gender')
plt.legend(['Men', 'Women'])
plt.show()
