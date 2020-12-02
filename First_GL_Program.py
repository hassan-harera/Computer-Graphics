import glfw

if not glfw.init():
    raise Exception("");

window = glfw.create_window(600, 400, "first window", None, None)

if not window:
    glfw.terminate()
    raise Exception("Error")

glfw.set_window_pos(window, 300, 300)


while not glfw.window_should_close(window):
  glfw.poll_events()
  glfw.swap_buffers(window)

glfw.terminate()
