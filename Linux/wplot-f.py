#import matplotlib.pyplot as plt

x = []
y = []
with open("VLINE", mode='r') as f:
    next(f)
    for line in f:
        xy=line.rstrip().split()
        x.append(float(xy[0]))
        y.append(float(xy[1]))

sum = 0
for i in range(140,170):
    sum += y[i]

print(sum/30)
