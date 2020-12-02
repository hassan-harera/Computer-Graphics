import glfw
import OpenGL.images as imgs
import cv2 as cv


def color_pixel(x0, y0):
    image[x0, y0] = [1, 1, 1]


def draw_line(x0, y0, x1, y1):
    n_steps = round(x1 - x0) if round(x1 - x0) > round(y1 - y0) else round(y1 - y0)
    x_step = (x1 - x0) / n_steps
    y_step = (y1 - y0) / n_steps
    for i in range(n_steps):
        color_pixel(round(x0), round(y0))
        # print(round(x0), round(y0))
        x0 += x_step
        y0 += y_step


image = cv.imread("img.jpg")
draw_line(0, 0, 499, 499)
cv.imshow("Image", image)

cv.waitKey(0)
