# -*- coding: utf-8 -*-
#!/usr/bin/env python
#   Author: WildfootW
#

from vpython import *

ball_amount = 2
ball_radius = [0.06, 0.04]
ball_mass = [0.2, 0.12]
ball_init_position = [vec(-0.2, 0, 0), vec(0.2, 0, 0)]
ball_init_velocity = [vec(0, 0, 0), vec(0, 0, 0)]
spring_origin_length = 0.5
spring_constant = 15

# constant
gravity = vec(0, -1 * 9.80665, 0)
tolerance = 10 ** -4

# scene
scene = canvas(width = 800, height = 600,     # unit: pixels
               center = vec(0, 0.2, 0),        # camera will continually look to center
               background = vec(0.10546875, 0.38671875, 0.17968750))

# object
#title_text = text(text = "Three balls doing horizontal SHMs", align = "center") # read-only
balls = []
for i in range(ball_amount):
    ball = sphere(radius = ball_radius[i], color = color.orange)
    ball.mass = ball_mass[i]
    balls.append(ball)
spring = helix(radius = 0.02, thickness = 0.01)
spring.k = spring_constant

# init status
#title_text.pos = vec(0, scene.center.y * 2, 0)
for i in range(ball_amount):
    balls[i].pos = ball_init_position[i]
    balls[i].v = ball_init_velocity[i]
spring.pos = balls[0].pos
spring.axis = balls[1].pos - balls[0].pos
current_time = 0
max_length_timestamp = [0, 0]
length_record = [0, 0, 0]

#time.sleep(3) # let vpython load init state

# sport
dt = 10 ** -3
while True:
    rate(1 / dt) # limit execute amount in 1 second
    current_time = current_time + dt

    for i in range(ball_amount):
        balls[i].pos = balls[i].pos + balls[i].v * dt
    spring.pos = balls[0].pos
    spring.axis = balls[1].pos - balls[0].pos

    for i in range(ball_amount):
        spring_force = spring.k * (mag(spring.axis) - spring_origin_length) * norm(balls[i].pos - balls[i - 1].pos) * -1
        balls[i].a = spring_force / balls[i].mass
        balls[i].v = balls[i].v + balls[i].a * dt

    length_record.append(mag(spring.axis))
    length_record.pop(0)
    if length_record[0] < length_record[1] and length_record[1] > length_record[2]:
        max_length_timestamp.append(current_time)
        max_length_timestamp.pop(0)
        summarize = "The period is " + str(max_length_timestamp[1] - max_length_timestamp[0]) + " seconds."
        scene.caption = summarize
        print(summarize)

'''
print(summarize)

# show answer in scene
# warning: if the text is too long, it take vpython long time to render and sometimes will cause some problem
text(text = "Displacement: " + str(ball.pos - ball_init_position) + " (m)", pos = vec(-2, 12, 0), align = "left")
text(text = "Max height: " + str(ball_max_height) + " (m)", pos = vec(-2, 10, 0), align = "left")
'''
