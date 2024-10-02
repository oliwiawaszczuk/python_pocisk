import math

from matplotlib import pyplot as plt

from const import delta_t, g


def idealne_warunki(time, x0, y0, v0, alph):
    x_points = []
    y_points = []

    # alph = math.radians(alph)

    t = 0
    while t <= time:
        x_t = x0 + v0 * math.cos(alph) * t
        y_t = y0 + v0 * math.sin(alph) * t - 0.5 * g * t * t
        x_points.append(x_t)
        y_points.append(y_t)

        if y_t < 0:
            break

        t += delta_t

    plt.plot(x_points, y_points)
    plt.show()
