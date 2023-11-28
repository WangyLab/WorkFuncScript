import matplotlib.pyplot as plt

x = []
y = []
with open("LOCPOT_Z", mode='r') as f:
    first_line = f.readline()
    name_x = first_line.split()[1]
    name_y = first_line.split()[2]
    for line in f:
        xy=line.rstrip().split()
        x.append(float(xy[0]))
        y.append(float(xy[1]))

plt.plot(x,y)
plt.show()

# Setting the work function calculation area
start_value = 14.0
end_value = 17.0

values_to_average = []
count = 0

for i, x_value in enumerate(x):
    if start_value <= x_value <= end_value:
        values_to_average.append(y[i])
        count += 1

if count > 0:
    average = sum(values_to_average) / count
    print("average value:", average)
else:
    print("No data points within the specified range")