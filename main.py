from functools import cache

import PIL.Image as pil
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

WIDTH = 2000
HEIGHT = 2000
DPI = 3
DIFF_X = lambda point: point[1]
DIFF_Y = lambda point: -point[0]
DT = 1 / 10
SCALE_FACTOR = 10

points = []


def transformImage(img_name, diff_x, diff_y):
    global points
    img = np.array(pil.open("cats/" + img_name))
    w, h, _ = img.shape
    for x in range(len(img)):
        for y in range(len(img[0])):
            [points.append([(x - w // 2) * SCALE_FACTOR, (y - h // 2) * SCALE_FACTOR, *img[x][y]])
             if img[x][y][3] >= 230 else 0]

    @cache
    def calcDiff(x, y):
        return x + int(diff_x([x, y]) * DT), y + int(diff_y([x, y]) * DT)

    def updateDot(dot):
        dot[0], dot[1] = calcDiff(dot[0], dot[1])
        return dot

    def dotsToMap(dots):
        field = np.full((WIDTH, HEIGHT, 4), (200, 200, 200, 255))
        for dot in dots:
            for i in range(SCALE_FACTOR):
                for j in range(SCALE_FACTOR):
                    if (0 <= dot[0] + i + WIDTH // 2 < WIDTH and
                            0 <= dot[1] + j + HEIGHT // 2 < HEIGHT):
                        field[dot[0] + i + WIDTH // 2][dot[1] + j + HEIGHT // 2] = dot[2:]
        return field

    fig, ax = plt.subplots(figsize=(WIDTH, HEIGHT), dpi=DPI)
    ax.set_axis_off()
    im = ax.imshow(dotsToMap(points), interpolation='nearest', vmin=0, vmax=1)

    def update(frame):
        dots = np.array(list(map(updateDot, points)))
        field = dotsToMap(dots)
        im.set_data(field)
        return im,

    ani = FuncAnimation(fig, update, frames=100000, interval=30, blit=True)
    plt.show()


transformImage("rzhaka.png", DIFF_X, DIFF_Y)
