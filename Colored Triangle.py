from idlelib import window
from turtle import color

from glfw import *
from OpenGL.GL import *
import numpy as np

if not init():
    raise Exception

window = create_window(500, 500,"", None, None);

if not window:
    terminate()
    raise Exception

make_context_current(window)
glClearColor(1, 0, 0, 1)

colors = [0, 1, 0,
          1, 0, 0,
          0, 0, 1]

positions = [0.5, -0.5, 0,
             0, 0.5, 0,
             -0.5, -0.5, 1]

colors = np.array(colors, dtype=np.float_)
positions = np.array(positions, dtype=np.float_)

glEnableClientState(GL_VERTEX_ARRAY)
glVertexPointer(3, GL_FLOAT, 0, positions)

glEnableClientState(GL_COLOR_ARRAY)
glColorPointer(3, GL_FLOAT, 0, colors)

while not window_should_close(window):
    poll_events()
    glClear(GL_COLOR_BUFFER_BIT)
    glDrawArrays(GL_TRIANGLES, 0, 3)
    swap_buffers(window)

terminate()
