import matplotlib.pyplot as plt

#plt.plot(range(10), range(10))
#plt.show()
#these r not useful - do it class based

fig = plt.figure(figsize = (25, 17))
# ax = fig.add_subplot(3, 3, 9): 3 lines of plots 3 columns of plots, plot 9 (bottom right)
ax = fig.add_subplot(211)
ax.plot(range(10), range(10), lw=4, c='red', label='my label')
ax.scatter(range(10), range(10), s = 80, c='darkblue', label='my scatter')
ax.set_xlabel('x axis in metres', fontsize = 20)
ax.set_ylabel('y axis in days', fontsize = 20)
ax.set_title('titletitelitleitle', fontsize = 25)
ax.tick_params('both', labelsize = 20)
ax.legend(fontsize = 20)

ax1 = fig.add_subplot(212)
ax1.plot(range(10), range(10), lw=4, c='red', label='ddd')
ax1.scatter(range(10), range(10), s = 80, c='darkblue', label='my scatter')
ax1.set_xlabel('x axis in metres', fontsize = 20)
ax1.set_ylabel('y axis in days', fontsize = 20)
ax1.set_title('titletitelitleitle', fontsize = 25)
ax1.tick_params('both', labelsize = 30)
ax1.legend(fontsize = 20)

plt.show()