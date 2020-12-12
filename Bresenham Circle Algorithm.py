from matplotlib import pyplot as plt
import time

f = plt.figure(1, figsize=(8, 8))
ax = f.gca()
ax.set_xlim([-100, 100])
ax.set_ylim([-100, 100])
f.show()

# Assuming x2 > x1 and y2 > y1
r = 50
x = 0
y = r
# d is the decision to change y
d = 3 - 2 * r


def plot(_x, _y, _radius):
    ax.plot(_x, _y, 'ko')
    ax.plot(-_x, _y, 'ko')
    ax.plot(_x, -_y, 'ko')
    ax.plot(-_x, -_y, 'ko')

    ax.plot(_y, _x, 'ko')
    ax.plot(_y, -_x, 'ko')
    ax.plot(-_y, _x, 'ko')
    ax.plot(-_y, -_x, 'ko')
    f.canvas.draw()


while y >= x:
    plot(x, y, r)
    x = x + 1
    if d > 0:
        y = y - 1
        d = d + 4 * (x - y) + 10
    else:
        d = d + 4 * x + 6

plt.show()
