# -*- coding: utf-8 -*-
#!/usr/bin/env python
#   Author: WildfootW
#

from vpython import *
from scipy.constants import physical_constants

OPTIONAL = True
ball_init_position = vec(-15, 5, 0)
ball_init_velocity = vec(6, 8, 0)
path_length = 0
duration = 0

# constant
gravity = vec(0, -1 * physical_constants['standard acceleration of gravity'][0], 0)

# scene
scene = canvas(width = 960, height = 720,     # unit: pixels
               center = vec(0, 10, 0),        # camera will continually look to center
               background = vec(0.10546875, 0.38671875, 0.17968750))

# object
floor = box(length = 30, width = 15, height = 1, color = color.black)
title_text = text(text = "Projectile motion", align = "center") # text is read-only
ball = sphere(radius = 0.25, color = color.orange,
              make_trail = True, trail_radius = 0.05)
velocity_arrow = arrow(shaftwidth = 0.05, color = color.yellow)

# init status
floor.pos = vec(0, (floor.height / 2) * -1, 0)
title_text.pos = vec(0, scene.center.y * 2, 0)
ball.pos = ball_init_position
ball.v = ball_init_velocity
velocity_arrow.pos = ball.pos
velocity_arrow.axis = ball.v / 2

# sport
dt = 10 ** -3
while ball.pos.y - ball.radius > 0:
    rate(1 / dt) # limit execute amount in 1 second
    if OPTIONAL:
        path_length += mag(ball.v) * dt
        duration += dt
    ball.pos = ball.pos + ball.v * dt
    ball.v = ball.v + gravity * dt
    velocity_arrow.pos = ball.pos
    velocity_arrow.axis = ball.v / 2

    summarize = "The displacement is " + str(ball.pos - ball_init_position) + "(< m, m, m>).\n"
    if OPTIONAL:
        summarize += "The flying time in the air is " + str(duration) + "(s).\n"
        summarize += "The path length is " + str(path_length) + "(m)."
    scene.caption = summarize

print(summarize)

# show answer in scene
# warning: if the text is too long, it take vpython long time to render and sometimes will cause some problem
text(text = "Displacement: " + str(ball.pos - ball_init_position), pos = vec(-2, 12, 0), align = "left")
if OPTIONAL:
    text(text = "Duration: " + str(duration), pos = vec(-2, 10, 0), align = "left")
    text(text = "Path length: " + str(path_length), pos = vec(-2, 8, 0), align = "left")

