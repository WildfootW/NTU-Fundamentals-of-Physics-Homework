#https://www.youtube.com/watch?v=uQlFuW6Akg0&feature=youtu.be
from vpython import *

##-----initialize-----
g = 9.8 #gravity
size = 0.25 #ball's size

scene = canvas(width=500, height=500, center=vec(0,5,0), background=vec(0.4,0.5,0.1))
floor = box(length=30, height=0.01, width=10, color=color.black)
ball = sphere(radius=size, color=color.red, make_trail=True, trail_radius=0.05)
msg = text(text="Free Fall", pos=vec(-15,7,0))

##-----status-----

ball.pos = vec(-15,5,0) #initial pos
initialpoint = vec(0,0,0)
initialpoint = vec(0,0,0)+ball.pos #record the pos
ball.v = vec(6,8,0) #initial velocity
a1 = arrow(color=color.yellow, shaftwidth=0.05)
a1.pos = ball.pos
a1.axis = vec(ball.v.x/2, ball.v.y/2, ball.v.z/2)
t = 0 #to sum up time
path = 0 #to calculate the path

##-----sport-----

dt = 234
dt = pow(10,-5)
while ball.pos.y >= size:
    rate(pow(10,5))
    #ball.pos.x = ball.pos.x + ball.v.x*dt
    #ball.pos.y = ball.pos.y + ball.v.y*dt
    path = path + pow( (ball.v.x*dt)**2 + (ball.v.y*dt)**2 + (ball.v.z*dt)**2 , 1/2)
    ball.pos = ball.pos + ball.v*dt
    ball.v.y = ball.v.y - g*dt
    a1.axis = vec(ball.v.x/2, ball.v.y/2, ball.v.z/2)
    a1.pos = ball.pos
    t = t + dt #t's sum

displacement = vec(0,0,0)
displacement = vec(0,0,0) + ball.pos - initialpoint

##-----print-----

msg.visible = False
msg = text(text = "The displacement is " + str(displacement) + ".", pos= vec(-15, 12,0))
print("The displacement is " + "<" +str(displacement.x)+", "+str(displacement.y)+", "+str(displacement.z)+">")

msg = text(text="It takes " + str(t) + " during the whole sport.", pos= vec(-15,11,0))
print ("It takes " + str(t) + " seconds during the whole sport.")

msg = text(text="The path is " + str(path) + ".", pos= vec(-15,10,0))
print ("The path is " + str(path) + ".")
