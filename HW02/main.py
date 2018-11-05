from vpython import *

##preparation
g = 9.8
size = 0.25

scene = canvas(center = vec(0,5,0), width=600, background=vec(0.3,0.45,0.1), align = 'left')
floor = box(length=30, height=0.01, width=4, color=color.blue)
ball = sphere(radius = size, color=color.red, make_trail=True, trail_radius = size/3)

oscillation = graph(width = 450, align = 'right')
funct1 = gcurve(graph = oscillation, color=color.blue, width=4) 

theta = pi/4
ball.pos = vec(-15, size, 0)
ball.v = vec(20*cos(theta), 20*sin(theta), 0)
c_drag = 0.9
displacement = vec(0, 0, 0)
displacement += ball.pos

dt = pow(10,-4) ##the delta time 
t = 0 ##sum of time
times = 0 ##the times the ball hits the floor
hpoint = vec(0, 0, 0)


##main sport
while(times < 4): 
    rate(10**4)
    t = t+dt
    ball.v += vec(0, -g, 0)*dt - c_drag*ball.v*dt
    ball.pos += ball.v*dt
    
    if(ball.pos.y <= size and ball.v.y<0):
        ball.v.y = -ball.v.y
        times += 1

    if(ball.pos.y >= hpoint.y):
        hpoint.y = ball.pos.y

    funct1.plot( pos=(t, pow( (ball.v.x**2 + ball.v.y**2 + ball.v.z**2), 1/2) ) ) ## to draw the graph
    

##graphdrawing
displacement = ball.pos - displacement
msg = text(text = 'displacement = ' + str(displacement), pos = vec(-10, 11, 0))
msg = text(text = 'the hightest point = ' + str(hpoint), pos = vec(-10, 9, 0))
msg = text(text = "The speed w.r.t the time on the right side", pos = vec(-10, 7, 0))
print('displacement = '+str(displacement))
print('the hightest point = '+str(hpoint))
