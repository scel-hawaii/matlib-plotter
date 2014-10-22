#imports
import matplotlib.pyplot as plt
import numpy as np

#Fields
x = [1, 2, 3, 4, 9, 10]
y = [2, 4, 6, 8, 9, 12]
w = [1, 3, 6, 9, 10]
z = [1, 3, float('nan'), 7, 8]

#Practice Plot
plt.plot(x,y)
plt.plot(w,z)
plt.title('Practice Plot')
plt.show()
