import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6]#data
y = [1, 2, 3, 4, 5, 6]

fig = plt.figure()

plt.plot([0, 10], [0, 10], 'ro') #not sure yet
plt.scatter(x, y, 'line01')#scatters our data in

plt.xlabel('x axis') #axis labels
plt.ylabel('y axis')

plt.show()