# -*- coding: utf-8 -*-
#!/usr/bin/env python
#   Author: WildfootW
#

from vpython import *

ball_radius = 0.05
ball_mass = 0.2
ball_init_position_relative_x = [-0.06, 0, -0.1]
group_init_position_absolute_z = [-3 * ball_radius, 0 * ball_radius, 3 * ball_radius]
ball_init_velocity = [vec(1, 0, 0), vec(2, 0, 0), vec(2.2, 0, 0)]
groups_amount = 3
spring_origin_length = 0.5
spring_constant = [15, 12, 17]

# constant
gravity = vec(0, -1 * 9.80665, 0)

# scene
scene = canvas(width = 800, height = 600,     # unit: pixels
               center = vec(0, 0.2, 0),        # camera will continually look to center
               background = vec(0.10546875, 0.38671875, 0.17968750))
et_graph = graph(width = 800, height = 600,
                 title = "Energy - Time",
                 xtitle = "time (s)", ytitle = "energy (J)")
aet_graph = graph(width = 800, height = 600,
                  title = "Average Energy - Time",
                  xtitle = "time (s)", ytitle = "average energy (J/s)")
et_curve_kinetic    = gcurve(graph = et_graph,  color = color.blue, width = 4)
et_curve_potential  = gcurve(graph = et_graph,  color = color.red,  width = 4)
aet_curve_kinetic   = gcurve(graph = aet_graph, color = color.blue, width = 4)
aet_curve_potential = gcurve(graph = aet_graph, color = color.red,  width = 4)

# object
#title_text = text(text = "Three balls doing horizontal SHMs", align = "center") # read-only
floor = box(length = 0.8, width = 0.8, height = 0.1, color = color.black)
wall  = box(length = 0.1, width = 0.8, height = 0.1, color = color.gray(0.5))
balls = []
for i in range(groups_amount):
    ball = sphere(radius = ball_radius, color = color.orange)
    balls.append(ball)
springs = []
for i in range(groups_amount):
    spring = helix(radius = 0.02, thickness = 0.01)
    spring.k = spring_constant[i]
    springs.append(spring)

# init status
#title_text.pos = vec(0, scene.center.y * 2, 0)
floor.pos = vec(0, (floor.height / 2) * -1, 0)
wall.pos = vec((floor.length / 2 - wall.length / 2) * -1, wall.height / 2, 0)
for i in range(groups_amount):
    balls[i].pos = vec(wall.pos.x + wall.length / 2 + spring_origin_length + ball_init_position_relative_x[i], balls[i].radius, group_init_position_absolute_z[i])
    balls[i].v = ball_init_velocity[i]
for i in range(groups_amount):
    springs[i].pos = vec(wall.pos.x + wall.length / 2, balls[i].radius, group_init_position_absolute_z[i])
    springs[i].axis = balls[i].pos - springs[i].pos
current_time = 0
total_kinetic = 0
total_potential = 0

#time.sleep(3) # let vpython load init state

# sport
dt = 10 ** -3
while True:
    rate(1 / dt) # limit execute amount in 1 second
    current_time = current_time + dt

    sum_kinetic = 0
    sum_potential = 0

    for i in range(groups_amount):
        balls[i].pos = balls[i].pos + balls[i].v * dt
        springs[i].axis = balls[i].pos - springs[i].pos

        spring_force = springs[i].k * (mag(springs[i].axis) - spring_origin_length) * norm(springs[i].axis) * -1
        balls[i].a = spring_force / ball_mass
        balls[i].v = balls[i].v + balls[i].a * dt
        balls[i].kinetic = 0.5 * ball_mass * pow(mag(balls[i].v), 2)
        balls[i].potential = 0.5 * springs[i].k * pow(mag(springs[i].axis) - spring_origin_length, 2)
        sum_kinetic += balls[i].kinetic
        sum_potential += balls[i].potential

    et_curve_kinetic.plot(pos = (current_time, sum_kinetic))
    et_curve_potential.plot(pos = (current_time, sum_potential))
    total_kinetic += sum_kinetic
    total_potential += sum_potential
    aet_curve_kinetic.plot(pos = (current_time, total_kinetic / current_time))
    aet_curve_potential.plot(pos = (current_time, total_potential / current_time))

    summarize =  "The average kinetic is " + str(total_kinetic / current_time) + " (J/s). "
    summarize += "The average potential is " + str(total_potential / current_time) + " (J/s).\n"
    scene.caption = summarize

'''
print(summarize)

# show answer in scene
# warning: if the text is too long, it take vpython long time to render and sometimes will cause some problem
text(text = "Displacement: " + str(ball.pos - ball_init_position) + " (m)", pos = vec(-2, 12, 0), align = "left")
text(text = "Max height: " + str(ball_max_height) + " (m)", pos = vec(-2, 10, 0), align = "left")
'''
