import matplotlib.pyplot as plt
weight =[56,34,78,23,45,67,89,87,65,43]
height =[112,165.5,134,156.7,192,173,156,134,198,167]
plt.scatter(weight, height,c='g', marker='*')
plt.xlabel('weight',fontsize=15)
plt.ylabel('height',fontsize=15)
plt.title('scatter plot height vs weight',fontsize=20)
plt.show()
