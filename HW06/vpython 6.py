## youtube : https://www.youtube.com/watch?v=ZUmfGF7A6Hw&feature=youtu.be
from vpython import *

scene = canvas(width = 800, height = 400, fov = 0.03\
, align = 'left', center = vec(0.3, 0, 0), background = vec(0.4, 0.4, 0.1)) 

diagram = graph(width = 800, align = 'left'\
, xtitle = 'omega', ytitle = 'average_power_comsumption',background = vec(0.2, 0.4, 0.1))

func = gcurve(color = color.magenta, graph = diagram)

class obj():
    pass

wall_left = obj()
ball = obj()
spring = obj()

size, m = 0.02, 0.2 
L, k = 0.2, 20
b = 0.05 * m * sqrt(k/m)
omega = [0.1*i + 0.7*sqrt(k/m) for i in range(1, int(0.5*sqrt(k/m)/0.1))] 

p_best = 0
omega_best = 0

for i in omega :                                ##i is omega_d
    ball.pos = vector(L, 0 , 0) 
    ball.v = vector(0, 0, 0)
    ball.m = m
    spring.pos = vector(0, 0, 0)
    
    t, dt = 0, 0.001 
    num_of_periods = 1

    T = 2 * pi / i

    work = 0
    p = 0

    while (1) :
        spring.axis = ball.pos - spring.pos
        force_of_spring = -k * (mag(spring.axis) - L) * norm(spring.axis)
        sinforce = vec(0.1*sin(i*t), 0, 0)
        airforce = - b * ball.v

        ball.a = (sinforce + force_of_spring + airforce) / ball.m
        ball.v += ball.a * dt
        ball.pos += ball.v * dt
        t += dt
        
        work += dot(sinforce, ball.v) * dt

        if (t/T >= num_of_periods):
            p = work / T
            num_of_periods += 1
            work = 0

            if (num_of_periods >= 100):
                func.plot(pos=(i, p))
                if (p >= p_best):
                    p_best = p 
                    omega_best = i

                break

print("\n================================================================================\n")
print ("when omega_d = " + str(omega_best) + " has largest steady-state average_power_comsumption.\n")
print("================================================================================\n")