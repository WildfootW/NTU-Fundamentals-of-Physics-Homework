# -*- coding: utf-8 -*-
#!/usr/bin/env python
#   Author: WildfootW
#

from vpython import *

N = 4
groups_amount = 5
rope_origin_length = 0.5
rope_spring_constant = 150000
ball_radius = 0.02
ball_mass = 0.5
ball_lifted_amount = N
ball_lifted_angle = 30 / 180 * pi

# constant
gravity = vec(0, -1 * 9.80665, 0)

# scene
scene = canvas(width = 800, height = 600,     # unit: pixels
               center = vec(0, -0.2, 0),      # camera will continually look to center
               background = vec(0.10546875, 0.38671875, 0.17968750))

# function
def calculate_velocity_after_collision(ball_a, ball_b):
    ret_v_a = ball_a.v + 2 * (ball_b.m / (ball_a.m + ball_b.m)) * (ball_a.pos - ball_b.pos) * dot(ball_b.v - ball_a.v, ball_a.pos - ball_b.pos) / dot(ball_a.pos - ball_b.pos, ball_a.pos - ball_b.pos)
    ret_v_b = ball_b.v + 2 * (ball_a.m / (ball_a.m + ball_a.m)) * (ball_b.pos - ball_a.pos) * dot(ball_a.v - ball_b.v, ball_b.pos - ball_a.pos) / dot(ball_b.pos - ball_a.pos, ball_b.pos - ball_a.pos)
    return (ret_v_a, ret_v_b)

# object
#title_text = text(text = "Newton's cradle", align = "center") # read-only
scene.caption = "Newton's cradle"
ceiling = box(length = 0.8, width = 0.8, height = 0.1, color = color.black)
balls = []
for i in range(groups_amount):
    ball = sphere(radius = ball_radius, color = color.orange)
    ball.v = vec(0, 0, 0)
    ball.m = ball_mass
    balls.append(ball)
ropes = []
for i in range(groups_amount):
    rope = cylinder(radius = 0.005)
    ropes.append(rope)

# init status
#title_text.pos = vec(0, scene.center.y * 2, 0)
ceiling.pos = vec(0, (ceiling.height / 2), 0)

for i in range(groups_amount):
    balls[i].pos = vec(ball_radius * (groups_amount - 1) * -1 + ball_radius * i * 2, -rope_origin_length - ball_mass * -gravity.y / rope_spring_constant, 0)
    ropes[i].pos = vec(balls[i].pos.x, 0, 0)
    ropes[i].axis = balls[i].pos - ropes[i].pos

for i in range(ball_lifted_amount):
    rope_length = -balls[i].pos.y
    balls[i].pos.x = balls[i].pos.x - rope_length * sin(ball_lifted_angle)
    balls[i].pos.y = -rope_length * cos(ball_lifted_angle)
    ropes[i].axis = balls[i].pos - ropes[i].pos

#time.sleep(3) # let vpython load init state

# sport
dt = 10 ** -4
while True:
    rate(1 / dt) # limit execute amount in 1 second

    for i in range(groups_amount):
        balls[i].pos = balls[i].pos + balls[i].v * dt
        ropes[i].axis = balls[i].pos - ropes[i].pos

        rope_force = rope_spring_constant * (mag(ropes[i].axis) - rope_origin_length) * norm(ropes[i].axis) * -1
        balls[i].a = rope_force / ball_mass + gravity
        balls[i].v = balls[i].v + balls[i].a * dt

    for i in range(groups_amount - 1):
        if mag(balls[i].pos - balls[i + 1].pos) <= ball_radius * 2 and dot(balls[i].pos - balls[i + 1].pos, balls[i].v - balls[i + 1].v) <= 0:
            (balls[i].v, balls[i + 1].v) = calculate_velocity_after_collision(balls[i], balls[i + 1])
