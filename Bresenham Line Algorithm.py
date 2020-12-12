from matplotlib import pyplot as plt

f = plt.figure(1, figsize=(8, 8))
ax = f.gca()
ax.set_xlim([-1000, 1000])
ax.set_ylim([-1000, 1000])
f.show()



def get_Points(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0

    is_high_slope = False
    if abs(dy) > abs(dx):
        x0, y0 = y0, x0
        x1, y1 = y1, x1
        is_high_slope = True

    is_decreased = False
    if x0 > x1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0
        is_decreased = True

    dx = x1 - x0
    dy = y1 - y0

    # p = int(dx / 2.0)
    p = (2 * dy) - dx
    y = y0
    ystep = 1 if y0 < y1 else -1

    points = []
    for x in range(x0, x1 + 1):
        point = (y, x) if is_high_slope else (x, y)
        points.append(point)
        if p < 0:
            p = p + (2 * dy)
        else:
            y += ystep
            p = p + (2 * dy) - (2 * dx)
    if is_decreased:
        points.reverse()
    return points


for p in get_Points(0, 0, 100, 20):
    x, y = p
    ax.plot(x, y, "ko")

plt.show()
