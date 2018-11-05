from vpython import *

##environment

scene = canvas(width=500, height=500, center=vec(0, -0.2, 0), align = 'left', background=vec(0.4,0.4,0.2)) 
ceiling = box(length=0.8, height=0.005, width=0.8, color=color.blue)


funcgraph0 = graph(width = 400, align = 'right') ##for kinetic energy
funcgraph1 = graph(width = 400, align = 'right') ##for potential energy
funcgraph2 = graph(width = 400, align = 'right') ##for ball1 1kavg & uavg 
funcgraph3 = graph(width = 400, align = 'right') ##for ball2 kavg & uavg 
funcgraph4 = graph(width = 400, align = 'right') ##for ball3 & uavg 

funct1 = gcurve(graph = funcgraph0, color=color.blue, width=4) ##ball 1
funct2 = gcurve(graph = funcgraph1, color=color.blue, width=4) ##ball 1
funct3 = gcurve(graph = funcgraph0, color=color.yellow, width=4) ## ball 2
funct4 = gcurve(graph = funcgraph1, color=color.yellow, width=4) ## ball 2
funct5 = gcurve(graph = funcgraph0, color=color.red, width=4) ## ball 3
funct6 = gcurve(graph = funcgraph1, color=color.red, width=4) ## ball 3

funct7 = gcurve(graph = funcgraph2, color=color.black, width=4) ## ball1 kavg
funct8 = gcurve(graph = funcgraph2, color=color.cyan, width=4) ## ball1 uavg
funct9 = gcurve(graph = funcgraph3, color=color.black, width=4) ## ball2 kavg
funct10 = gcurve(graph = funcgraph3, color=color.cyan, width=4) ## ball2 uavg
funct11 = gcurve(graph = funcgraph4, color=color.black, width=4) ## ball3 kavg
funct12 = gcurve(graph = funcgraph4, color=color.cyan, width=4) ## ball3 uavg

##condition

g = 9.8
size, m = 0.05, 0.2
L = [1, 2.718, 3.14] ##initial pos
k = [7, 4.3, 10.7] 
vi = [vec(0,-4.3333333333,0), vec(0,-8.88888888888888,0), vec(0,-11.111111111111111111,0)] ##initial velocity

##make the device

balls = [] 
springs =[]

for i in range(3):
    ball = sphere(pos = vec(0.2*(i-1), -L[i], 0), radius = size, color=color.red) 
    ball.v = vi[i]
    balls.append(ball)
for i in range(3):
    spring = helix(pos = vec(0.2*(i-1), 0, 0), radius=0.02, thickness =0.01) 
    spring.k = k[i]
    springs.append(spring)

##sports & graphs

t = 0
dt = 5*pow(10,-3)
ke = [0, 0, 0]
ue = [0, 0, 0]
for i in range(3):
    ke[i] = 1/2 * m * ( abs(vi[i].y) )**2 ##initial k
    ue[i] = 0 ##initial u

while( t < 5 ):
    rate(1/5*pow(10,3))
    for i in range(3):
        springs[i].axis = balls[i].pos - springs[i].pos 
        spring_force = -k[i] * (mag(springs[i].axis) - L[i]) * springs[i].axis.norm() 
        balls[i].a = vector(0, - g, 0) + spring_force / m
        balls[i].v += balls[i].a*dt
        balls[i].pos += balls[i].v*dt

        v = abs(balls[i].v.y)
        s = (balls[i].pos.y-(-L[i])) ##displacement
         

        if (i == 0):
            funct1.plot( pos=(t, 1/2*m*(v**2)) ) #ball1 k
            funct2.plot( pos=(t, 1/2*k[i]*(s**2)) ) #ball1 u
        elif (i == 1):
            funct3.plot( pos=(t, 1/2*m*(v**2)) ) #ball2 k
            funct4.plot( pos=(t, 1/2*k[i]*(s**2)) ) #ball2 u
        elif (i == 2):
            funct5.plot( pos=(t, 1/2*m*(v**2)) ) #ball3 k
            funct6.plot( pos=(t, 1/2*k[i]*(s**2)) ) #ball3 u
        
        ke[i] += 1/2*m*((balls[i].v.y)**2) ##sum 0f k
        ue[i] += 1/2*k[i]*(s**2) ##sum of u

        if (t != 0) : ##average k and u
            kavg = ke[i] / t
            uavg = ue[i] / t
            if (i == 0):
                funct7.plot( pos=(t, kavg) )#ball1 k 
                funct8.plot( pos=(t, uavg) )#ball1 u
            if (i == 1):
                funct9.plot( pos=(t, kavg) )#ball2 k
                funct10.plot( pos=(t, uavg) )#ball2 u
            if (i == 2):
                funct11.plot( pos=(t, kavg) )#ball3 k
                funct12.plot( pos=(t, uavg) )#ball3 u
        
    t += dt

print ("圖表分別是：\n藍色紅色黃色線為三球瞬時動能和三球瞬時位能\n黑色線和青色線為三球分別平鈞動能位能比較")