# -*- coding: utf-8 -*-
#!/usr/bin/env python
#   Author: WildfootW
#

from vpython import *

OPTIONAL = False
ball_radius = 0.25
ball_theta = pi / 4
ball_init_position = vec(-15, ball_radius, 0)
ball_init_velocity = vec(20 * cos(ball_theta), 20 * sin(ball_theta), 0)
drag_coefficient = 0.9

# constant
gravity = vec(0, -1 * 9.80665, 0)

# scene
scene = canvas(width = 800, height = 600,     # unit: pixels
               center = vec(0, 10, 0),        # camera will continually look to center
               background = vec(0.10546875, 0.38671875, 0.17968750))
graph_vt = graph(width = 800, height = 600,
                 title = "ball",
                 xtitle = "time (s)", ytitle = "speed (m/s)")
curve_vt = gcurve(graph = graph_vt, color = color.blue, width = 4)

# object
floor = box(length = 30, width = 15, height = 1, color = color.black)
title_text = text(text = "Bouncing Ball with Air Drag", align = "center") # read-only
ball = sphere(radius = ball_radius, color = color.orange,
              make_trail = True, trail_radius = 0.05)
velocity_arrow = arrow(shaftwidth = 0.05, color = color.yellow)

# init status
floor.pos = vec(0, (floor.height / 2) * -1, 0)
title_text.pos = vec(0, scene.center.y * 2, 0)
ball.pos = ball_init_position
ball.v = ball_init_velocity
velocity_arrow.pos = ball.pos
velocity_arrow.axis = ball.v / 2
bounce_amount = 0
ball_max_height = 0
current_time = 0

#time.sleep(3) # let vpython load init state

# sport
dt = 10 ** -3
while True:
    rate(1 / dt) # limit execute amount in 1 second

    if ball.pos.y - ball.radius <= 0 and ball.v.y < 0: # hit the ground
        bounce_amount += 1
        if bounce_amount == 3:
            break
        ball.v.y = -ball.v.y

    current_time = current_time + dt
    ball.pos = ball.pos + ball.v * dt
    ball.v = ball.v + gravity * dt - drag_coefficient * ball.v * dt
    velocity_arrow.pos = ball.pos
    velocity_arrow.axis = ball.v / 2

    if ball_max_height < ball.pos.y:
        ball_max_height = ball.pos.y

    curve_vt.plot(pos = (current_time, mag(ball.v)))
    summarize = "The displacement is " + str(ball.pos - ball_init_position) + " (< m, m, m>).\n"
    summarize += "The max height is " + str(ball_max_height) + " (m).\n"
    scene.caption = summarize

print(summarize)

# show answer in scene
# warning: if the text is too long, it take vpython long time to render and sometimes will cause some problem
text(text = "Displacement: " + str(ball.pos - ball_init_position) + " (m)", pos = vec(-2, 12, 0), align = "left")
text(text = "Max height: " + str(ball_max_height) + " (m)", pos = vec(-2, 10, 0), align = "left")

