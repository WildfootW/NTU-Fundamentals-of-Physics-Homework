from vpython import *

scene = canvas(width=800, height=800, background=vector(0.4,0.4,0.1))
G = 6.673E-11
mass = {"earth": 5.97E24, "moon": 7.36E22, "sun":1.99E30}
radius = {"earth": 6.371E6*10, "moon": 1.317E6*10, "sun":6.95E8*10} 
earth_orbit = {"r": 1.495E11, "v": 2.9783E4}
moon_orbit = {"r": 3.84E8, "v": 1.022E3}
theta = 5.145*pi/180.0

scene.lights = []
local_light(pos = vector(0,0,0))##turn off the light

E = mass["moon"] / (mass["earth"]+mass["moon"])
M = mass["earth"] / (mass["earth"]+mass["moon"])

earth = sphere(pos = vec(-E*moon_orbit["r"]*cos(theta)+earth_orbit["r"], -E*moon_orbit["r"]*sin(theta), 0), m = mass["earth"], texture={"file":textures.earth}, radius=radius["earth"], make_trail=0)

moon = sphere(pos = vec(M*moon_orbit["r"]*cos(theta)+earth_orbit["r"], M*moon_orbit["r"]*sin(theta), 0), m = mass["moon"], color=color.white, radius=radius["moon"])

sun = sphere(pos=vector(0,0,0), radius = radius["sun"], color = color.orange, emissive=True)

earth.v = vec(0, 0, E*moon_orbit["v"] - earth_orbit["v"])
moon.v = vec(0, 0, -M*moon_orbit["v"] - earth_orbit["v"])

arr = arrow(color = color.green, shaftwidth = 0.5*radius["earth"],pos=earth.pos)
arr.axis = (4.5*radius["earth"] * norm(cross(moon.pos-earth.pos,moon.v-earth.v)))

dt = 60*60*6
T = 0
flag = 1
remove = 0

while (1): 
    rate(1000)

    moon.a = -G * mass["earth"] * mass["moon"] / mag2(moon.pos-earth.pos) * norm(moon.pos-earth.pos) \
    / mass["moon"]-G*mass["sun"]*mass["moon"]/mag2(moon.pos-sun.pos)*norm(moon.pos-sun.pos)/mass["moon"]
    
    earth.a = -G * mass["earth"] * mass["moon"] / mag2(moon.pos-earth.pos) * norm(earth.pos-moon.pos) \
    / mass["earth"]-G*mass["sun"]*mass["earth"]/mag2(earth.pos-sun.pos)*norm(earth.pos-sun.pos)/mass["earth"]
    
    moon.v += moon.a * dt
    moon.pos += moon.v * dt
    
    earth.v += earth.a * dt
    earth.pos += earth.v * dt
    
    arr.pos = earth.pos
    arr.axis = (4.5*radius["earth"]*norm(cross((moon.pos-earth.pos), moon.v-earth.v)))
    scene.center = earth.pos
    
    T += dt

    if (cross((moon.pos-earth.pos),moon.v-earth.v).x > 0) and (flag == 1):
        if (remove == 1):
            print(T / (86400*365))
            T = 0
            flag = 0
        elif (remove == 0):
            T = 0
            flag = 0
            remove = 1
        else :
            pass
            
    if (cross((moon.pos-earth.pos),moon.v-earth.v).x < 0) and (flag == 0):
        flag = 1
    else:
        pass

    

