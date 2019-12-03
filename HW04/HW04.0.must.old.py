from vpython import *

## preparation
scene = canvas(width = 500, height = 500, center = vec(0, -0.3 , 0), background = vec(0.4,0.4,0.1)) 
ceiling = box(length = 0.8, height = 0.005, width = 0.8, color = color.red)

N = 2
N2 = 5
g = 9.8
size, m = 0.02, 0.5 
L, k = 0.5, 15000
theda = pi/6


## func of collision

def af_col_v(m1, m2, v1, v2, x1, x2): # as the example
    v1_new = v1 + 2*(m2/(m1+m2))*(x1-x2) * dot (v2-v1, x1-x2) / dot (x1-x2, x1-x2) 
    v2_new = v2 + 2*(m1/(m1+m2))*(x2-x1) * dot (v1-v2, x2-x1) / dot (x2-x1, x2-x1) 
    return (v1_new, v2_new)

balls1=[]
balls2=[]
springs1=[]
springs2=[]

for i in range(N):
    ball = sphere(radius = size, color = color.yellow) ## for the ball
    ball.v = vec(0, 0, 0)
    ball.pos = vec((-L - m*g/k)*sin(theda)+i*2*size, (-L - m*g/k)*cos(theda), 0)
    balls1.append(ball)

    spring = cylinder(radius = 0.005) ## for the spring
    spring.pos=vec(0+2*size*i,0,0)
    spring.axis=balls1[i].pos-spring.pos
    springs1.append(spring)

for i in range(N2 - N):
    ball = sphere(radius = size, color=color.yellow) ## for the ball
    ball.v = vec(0, 0, 0)
    ball.pos = vec((i+N)*2*size,(-L - m*g/k), 0)
    balls2.append(ball)

    spring = cylinder(radius = 0.005) ##for the spring
    spring.pos = vec((i+N)*2*size,0, 0)
    spring.axis = balls2[i].pos - spring.pos
    springs2.append(spring)

balls = balls1 + balls2
springs = springs1 + springs2


dt = pow(10,-4) 
t = 0
while (1) :
    rate(pow(10,4))
    t += dt

    for i in range(N):
        springs1[i].axis = balls1[i].pos - springs1[i].pos
        spring_force = - k * (mag(springs1[i].axis) - L) * springs1[i].axis.norm()
        balls1[i].a = vector(0, - g, 0) + spring_force / m
        balls1[i].v += balls1[i].a*dt
        balls1[i].pos += balls1[i].v*dt

    for i in range(N2 - N):
        springs2[i].axis= balls2[i].pos - springs2[i].pos
        spring_force = - k * (mag(springs2[i].axis) - L) * springs2[i].axis.norm()
        balls2[i].a = vector(0, - g, 0) + spring_force / m
        balls2[i].v += balls2[i].a*dt
        balls2[i].pos += balls2[i].v*dt
    
    for i in range(4):
        if (mag(balls[i].pos - balls[i+1].pos) <= 2*size) and \
        (dot(balls[i].pos-balls[i+1].pos, balls[i].v-balls[i+1].v) <= 0) : 
            (balls[i].v, balls[i+1].v) = \
            af_col_v (m, m, balls[i].v, balls[i+1].v, balls[i].pos, balls[i+1].pos) ## call the abovementioned func
        else:
            pass