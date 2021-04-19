import matplotlib.pyplot as plt

x = [0, 1, -4]
y = [0, 6, 5]

plt.plot(x, y) #draws line between the points
plt.plot(y) #default values of x = 0, 1, 2, 3...
plt.plot(x) #default values of y = 0, 1, 2, 3...
plt.plot(x, y, 'o') #only plot points
plt.plot(x, y, marker = '*') #draws line between the points with pointing intersections
plt.plot(x, y, "o-.r") #marker|line|color

plt.show()

#https://www.w3schools.com/python/matplotlib_markers.asp
