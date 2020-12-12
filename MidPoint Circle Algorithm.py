from matplotlib import pyplot as plt

f = plt.figure(1, figsize=(8, 8))
ax = f.gca()
ax.set_xlim([-1000, 1000])
ax.set_ylim([-1000, 1000])
f.show()


def circle(radius, offset):
    x, y = 0, radius
    plotCircle(x, y, radius, offset)


def symmetry_points(x, y, offset):
    ax.plot(x + offset, y + offset, "ro")
    ax.plot(-x + offset, y + offset, "ro")
    ax.plot(x + offset, -y + offset, "ro")
    ax.plot(-x + offset, -y + offset, "ro")
    ax.plot(y + offset, x + offset, "ro")
    ax.plot(-y + offset, x + offset, "ro")
    ax.plot(y + offset, -x + offset, "ro")
    ax.plot(-y + offset, -x + offset, "ro")


def plotCircle(x, y, radius, offset):
    d = 5 / 4.0 - radius
    symmetry_points(x, y, radius + offset)
    while x < y:
        print(d)
        if d < 0:
            x += 1
            d += 2 * x + 1
        else:
            x += 1
            y -= 1
            d += 2 * (x - y) + 1
        symmetry_points(x, y, radius + offset)


circle(200, 30)
plt.show()
