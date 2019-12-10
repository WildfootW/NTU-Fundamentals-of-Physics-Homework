# -*- coding: utf-8 -*-
#!/usr/bin/env python
#   Author: WildfootW
#

from vpython import *

rope_origin_length = 2
rope_spring_constant = 150000
ball_radius = 0.1
ball_mass = 1
ball_lifted_angle = 30 / 180 * pi
earth_rotation_velocity = 2 * pi / (1.0 * 60.0 * 60.0) # coriolis omega
location_latitude = 25 / 180 * pi

# constant
gravity = vec(0, -1 * 9.80665, 0)

# scene
scene = canvas(width = 800, height = 600,     # unit: pixels
               center = vec(0, -1, 0),      # camera will continually look to center
               background = vec(0.10546875, 0.38671875, 0.17968750))

# object
#title_text = text(text = "Pendulum", align = "center") # read-only
scene.caption = "Pendulum"
ceiling = box(length = 3, width = 3, height = 0.1, color = color.black)
ball = sphere(radius = ball_radius, color = color.orange,
              make_trail = True, trail_type = "points", interval = 20, retain = 80)
ball.v = vec(0, 0, 0)
ball.m = ball_mass
rope = cylinder(radius = 0.02)

# init status
#title_text.pos = vec(0, scene.center.y * 2, 0)
ceiling.pos = vec(0, (ceiling.height / 2), 0)

ball.pos = vec(0, -rope_origin_length - ball_mass * -gravity.y / rope_spring_constant, 0)
rope.pos = vec(ball.pos.x, 0, 0)

rope_length = -ball.pos.y
ball.pos.x = ball.pos.x - rope_length * sin(ball_lifted_angle)
ball.pos.y = -rope_length * cos(ball_lifted_angle)
rope.axis = ball.pos - rope.pos

count = 0
is_last_half = False
ball_v_record = [0, 0, 0]
angle_between_east_west = 0

#time.sleep(3) # let vpython load init state

# sport
dt = 10 ** -3
while True:
    rate(10 ** 4) # limit execute amount in 1 second

    if count == 1000:
        break

    ball.pos = ball.pos + ball.v * dt
    rope.axis = ball.pos - rope.pos

    rope_force = rope_spring_constant * (mag(rope.axis) - rope_origin_length) * norm(rope.axis) * -1
    coriolis_acceleration = 2 * earth_rotation_velocity * vec(-ball.v.z * sin(location_latitude) - ball.v.y * cos(location_latitude), ball.v.x * cos(location_latitude), ball.v.x * sin(location_latitude))
    ball.a = rope_force / ball_mass + gravity + coriolis_acceleration
    ball.v = ball.v + ball.a * dt

    ball_v_record.append(mag(ball.v))
    ball_v_record.pop(0)
    if ball_v_record[0] > ball_v_record[1] and ball_v_record[1] < ball_v_record[2]:
        if is_last_half:
            count += 1
            is_last_half = False
        else:
            is_last_half = True
    last_ball_v = ball.v
    angle_between_east_west = acos(dot(vec(ball.pos.x, 0, ball.pos.z), vec(1, 0, 0)) / mag(vec(ball.pos.x, 0, ball.pos.z)) / mag(vec(1, 0, 0))) / pi * 180
    #angle_between_east_west = acos(dot(vec(ball.v.x, 0, ball.v.z), vec(1, 0, 0)) / mag(vec(ball.v.x, 0, ball.v.z)) / mag(vec(1, 0, 0))) / pi * 180
    if angle_between_east_west > 90:
        angle_between_east_west = 180 - angle_between_east_west

    summarize =  "Pendulum swing " + str(count) + " times. "
    summarize += "Angle between east-west and the swing projection is " + str(angle_between_east_west)  + " degree."
    scene.caption = summarize
    #print(summarize)

print(summarize)

# show answer in scene
# warning: if the text is too long, it take vpython long time to render and sometimes will cause some problem
text(text = "The deviate angle is : " + str(angle_between_east_west) + " degrees", pos = vec(-1.5, -2.3, 0), align = "left", height = 0.1)

