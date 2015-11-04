import matplotlib.pyplot as plt
import numpy

x = [1, 2, 3]
y = [5, 7, 4]

x2 =[1, 2, 3]
y2 =[10, 14, 12]

plt.plot(x, y, label='First Line')
plt.plot(x2, y2, label='Second Line')
plt.xlabel('Plot Number')
plt.ylabel('Important Var')
plt.title('Interesting Graph\nPlotting is fun!')
plt.legend()
plt.show()
