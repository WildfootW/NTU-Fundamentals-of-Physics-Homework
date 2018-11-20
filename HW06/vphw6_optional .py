
from vpython import *
scene = canvas(width=500, height=400, fov = 0.03, align = 'left', center=vec(0.3, 0, 0), background=vec(0.5,0.5,0)) 

size, m = 0.02, 0.2 
L = 0.2
k, K = 20, 5.0
b0 = 0.05 * m * sqrt(k/m)
b1 = 0.0025 * m * sqrt(k/m)
omegad = sqrt((k+K)/m)

wall_left = box(length = 0.005, height = 0.3, width = 0.3, color = color.blue, pos = vec(0,0,0)) # left wall
wall_right = box(length = 0.005, height = 0.3, width = 0.3, color = color.blue, pos = vec(3*L,0,0)) # right wall

ball0 = sphere(radius = size, color = color.red)
ball1 = sphere(radius = size, color = color.red)
spring0 = helix(radius = 0.015, thickness = 0.01)
spring1 = helix(radius = 0.015, thickness = 0.01, pos = vec(2*L,0,0))
spring2 = helix(radius = 0.01, thickness = 0.005, pos = vec(L,0,0))

oscillation0 = graph(width = 450, align = 'left', xtitle = 't', ytitle = 'x', background = vec(0.5,0.5,0)) 
func0 = gcurve(color=color.magenta, graph = oscillation0)
oscillation1= graph(width = 450, align = 'left', xtitle = 't', ytitle = 'average_power', background = vec(0.5,0.5,0)) 
func1 = gdots(color=color.magenta, graph = oscillation1)

ball0.pos = vector(L, 0 , 0) 
ball1.pos = vector(2*L, 0 , 0)
ball0.v = vector(0, 0, 0)
ball1.v = vector(0, 0, 0)
ball0.m, ball1.m = m, m
spring1.pos = vector(2*L, 0,0 )
spring2.pos = vector(L, 0, 0)

t, dt = 0, 0.001
T = 0
work, oldwork = 0, 0

status = 0
count = 0

def spring_force(kk, spring_axis):
    return -kk * (mag(spring_axis) - L) * norm(spring_axis)

while (1):
    rate(1000)
    sinforce = 0.1 * sin(omegad*t) * vec(1,0,0)

    spring0.axis = ball0.pos - spring0.pos
    spring1.pos = ball1.pos
    spring1.axis = wall_right.pos - ball1.pos
    spring2.axis = ball1.pos - ball0.pos

    spring_force0 =  spring_force(k, spring0.axis)
    spring_force1 = spring_force(k, spring1.axis)
    spring_force2 = spring_force(K, spring2.axis)
    
    airforce0 = -ball0.v * b0 
    airforce1 = -ball1.v * b1 
    
    ball0.a = (spring_force0 + airforce0 + sinforce - spring_force2) / ball0.m # ball acceleration = spring force /m - damping
    ball1.a = (spring_force2 + airforce1 - spring_force1) / ball1.m # ball acceleration = spring force /m - damping  
    ball0.v += ball0.a*dt
    ball1.v += ball1.a*dt
    ball0.pos += ball0.v*dt
    ball1.pos += ball1.v*dt

    t += dt
    T += dt
    
    func0.plot(pos=(t, ball0.pos.x - L))
    work += dot(sinforce, ball0.v)*dt

    if (status == 1):
        if (ball0.v.x * oldballv <0):
            count += 1
            if (count == 2):
                func1.plot(t, work/T)
                work = 0
                count = 0
                T = 0
    oldballv = ball0.v.x
    status = 1
    
    
