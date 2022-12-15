import matplotlib.pyplot as plt

plt.clf()

# Pie chart,slices will be ordered, 
# plotted counter-clockwise:

labels = 'Frogs', 'Hogs', 'Dogs', 'Cats'
sizes = [15, 30, 45, 10]

# only "explode" the 2nd slice(i.e. 'Hogs')
explode = (0, 0.1, 0, 0)

plt.title("PIE CHART EXAMPLE")
plt.pie(sizes, explode, labels,autopct='%1.1f%%')
#autopct='%1.1f%%'
plt.show()
