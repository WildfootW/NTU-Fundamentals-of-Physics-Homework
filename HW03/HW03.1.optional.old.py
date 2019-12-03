from vpython import *

##preparation

scene = canvas(width=500, height=500, center=vec(0, -0.2, 0), align = 'left', background=vec(0.4,0.4,0.2)) 
oscillation = graph(width=450,align='right')
func = gvbars(delta = 0.3, graph=oscillation , color = color.green)

sizes = [0.06, 0.04] # for balls’ sizes 
ms = [0.2, 0.12]
L = 0.5
k = 1.5

##make the device

balls = [] 

for i in range(2):
    ball = sphere(pos = vec(0+i*1.1*L , sizes[i], 0), radius = sizes[i], color = color.cyan) 
    ball.v = vec(0, 0, 0)
    balls.append(ball)

spring = helix(pos = vec(0, 0, 0), radius=0.02, thickness =0.01, axis = balls[1].pos-balls[0].pos) 

##sports & graphs

t = 0
dt = pow(10,-4)
times = 0
counts = 0
P = 0
v = []

while (P <= 7):
    rate(pow(10,4))
    for i in range(2):
        spring.axis = balls[1].pos - balls[0].pos
        spring.pos = balls[0].pos
        spring_force = -k * (mag(spring.axis) - L) * spring.axis.norm()
        
        balls[i].a =  spring_force / ms[i]
        balls[i].v += balls[i].a * dt
        balls[i].pos += balls[i].v * dt

    v.append(balls[0].v.x)

    if (times >= 1):
        if v[times] * v[times-1] < 0: ##v for different direction
            counts += 1 

    if (counts == 2): ##counts 2 times is a period
        P += 1
        func.plot(P,t) ##the period
        counts = 0
        print ("The period is " + str(t) + " seconds.")
        t = 0 ##renew the time to calculate the period

    t += dt
    times += 1

print ("The periods are showed above!")