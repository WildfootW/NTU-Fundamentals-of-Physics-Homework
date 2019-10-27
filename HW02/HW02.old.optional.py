from vpython import *

##preparation
g = 9.8
size = 0.25

scene = canvas(center = vec(0,5,0), width=600, background=vec(0.3,0.45,0.1), align = 'left')
floor = box(length=30, height=0.01, width=4, color=color.yellow)
ball = sphere(radius = size, color=color.red, make_trail=True, trail_radius = size/2)

oscillation = graph(width = 450, align = 'right')
funct1 = gcurve(graph = oscillation, color=color.blue, width=4) 

ball.pos = vec(-15, 30, 0)
ball.v = vec(0, 0, 0)
dt = pow(10,-4) ##the delta time 
t = 0 ##sum of time
c_drag = 0.3

print("Plz, wait.\nNow calculating...")

##main sport
while(1): 
    rate(10**4)
    t += dt
    ball.v += vec(0, -g, 0)*dt - c_drag*ball.v*dt
    ball.pos += ball.v*dt
    speed = pow( (ball.v.x**2 + ball.v.y**2 + ball.v.z**2), 1/2)
    rf_a = pow( ((c_drag*ball.v).x**2 + (c_drag*ball.v).y**2 + (c_drag*ball.v).z**2) , 1/2)

    if (g - rf_a < 0.01):
        print("the velocity is:"+str(ball.v))
        print("the speed is:"+str(speed))
        break
        
        
    funct1.plot( pos=(t, speed ) )## to draw the graph


##graphdrawing
msg = text(text = "the velocity is:"+str(ball.v), pos = vec(-10, 11, 0))
msg = text(text = "the speed is:"+str(speed), pos = vec(-10, 9, 0))
msg = text(text = "The speed w.r.t the time on the right side", pos = vec(-10, 7, 0))
