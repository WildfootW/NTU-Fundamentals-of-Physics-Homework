# -*- coding: utf-8 -*-
#!/usr/bin/env python
#   Author: WildfootW
#

from vpython import *

OPTIONAL = True
ball_radius = 0.25
ball_init_position = vec(0, 0, 0)
ball_init_velocity = vec(0, 0, 0)
drag_coefficient = 0.3
tolerance = 10 ** -5

# constant
gravity = vec(0, -1 * 9.80665, 0)

# scene
scene = canvas(width = 800, height = 600,     # unit: pixels
               center = vec(0, 0, 0),        # camera will continually look to center
               background = vec(0.10546875, 0.38671875, 0.17968750))
graph_vt = graph(width = 800, height = 600,
                 title = "ball",
                 xtitle = "time (s)", ytitle = "speed (m/s)")
curve_vt = gcurve(graph = graph_vt, color = color.blue, width = 4)

# object
title_text = text(text = "ball dropped freely", align = "center") # read-only
ball = sphere(radius = ball_radius, color = color.orange,
              make_trail = True, trail_radius = 0.05)
velocity_arrow = arrow(shaftwidth = 0.05, color = color.yellow)

# init status
title_text.pos = vec(0, 3, 0)
ball.pos = ball_init_position
ball.v = ball_init_velocity
velocity_arrow.pos = ball.pos
velocity_arrow.axis = ball.v / 2
current_time = 0
previous_speed = mag(ball_init_velocity)

time.sleep(3) # let vpython load init state

# sport
dt = 10 ** -3
while True:
    rate(1 / dt) # limit execute amount in 1 second

    current_time = current_time + dt
    #ball.pos = ball.pos + ball.v * dt
    ball.v = ball.v + gravity * dt - drag_coefficient * ball.v * dt
    velocity_arrow.pos = ball.pos
    velocity_arrow.axis = ball.v / 2

    if abs(mag(ball.v) - previous_speed) < tolerance:
        summarize = "The terminal velocity is " + str(mag(ball.v)) + " (m/s)."
        scene.caption = summarize
        break;
    previous_speed = mag(ball.v)

    curve_vt.plot(pos = (current_time, mag(ball.v)))
    summarize = "The speed is " + str(mag(ball.v)) + " (m/s)."
    scene.caption = summarize

print(summarize)

# show answer in scene
# warning: if the text is too long, it take vpython long time to render and sometimes will cause some problem
text(text = "The terminal velocity is: " + str(mag(ball.v)) + " (m/s)", pos = vec(0, 1, 0), align = "center")

