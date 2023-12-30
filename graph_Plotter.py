import matplotlib.pyplot as plt

x1 = [2, 4, 12, 20]
y1 = [2, 6, 7, 14]

left = [1, 2, 3, 4, 5]
height = [10, 14, 18, 34, 50]

tick_labels = ['one', 'two', 'three', 'four', 'five']

plt.bar(left, height, tick_label=tick_labels, width=0.8, color=['blue', 'orange'])

plt.plot(x1, y1, color='green', linestyle='dashed', marker='o', markerfacecolor='blue', markersize=12, linewidth=3, label='Line 1')

plt.ylim(1, 55)  # Adjusted ylim to better fit the data
plt.xlim(1, 25)

plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.title('Demo Graph - Bar and Line')

plt.legend()

plt.show()
