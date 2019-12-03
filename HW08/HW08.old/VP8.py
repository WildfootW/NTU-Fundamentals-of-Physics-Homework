#youtube : https://youtu.be/j3t8NfPK7WY
from vpython import * 
from diatomic import *

N = 20
L = ((24.4E-3/(6E23))*N)**(1/3.0)/50
m = 14E-3/6E23
k, T = 1.38E-23, 298.0
initial_v = (3*k*T/m)**0.5
COs=[]

scene = canvas(width = 400, height =400, align = 'left', background = vec(1, 1, 1)) 
container = box(length = 2*L, height = 2*L, width = 2*L, opacity=0.4, color = color.yellow ) 
energies = graph(width = 600, align = 'left', ymin=0)

c_avg_com_K = gcurve(color = color.green)
c_avg_v_K = gcurve(color = color.purple)
c_avg_r_K = gcurve(color = color.blue)
c_avg_v_P = gcurve(color = color.red)

def collision_or_not (obj1, obj2):
    if (mag(obj1.pos - obj2.pos) <= 2*size) and dot(obj1.pos - obj2.pos , obj1.v - obj2.v) <0:
        obj1.v, obj2.v = collision(obj1, obj2)
    
    return obj1.v, obj2.v


for i in range(0,N): 
    O_pos = vec(random()-0.5, random()-0.5, random()-0.5)*L # random() yields a random number between 0 and 1 
    CO = CO_molecule(pos=O_pos, axis = vector(1.0*d, 0, 0)) # generate one CO molecule
    CO.C.v = vector(initial_v*random(), initial_v*random(), initial_v*random()) # set up the initial velocity of C randomly 
    CO.O.v = vector(initial_v*random(), initial_v*random(), initial_v*random()) # set up the initial velocity of O randomly 
    COs.append(CO)

t = 0
dt = 5E-16

total_com_K, total_v_K, total_r_K, total_v_P = 0, 0, 0, 0

while (1):
    rate(3000)
    t += dt
    for CO in COs:
        CO.time_lapse(dt)

    for i in range(0,N-1): # the first N-1 molecules
        for j in range(i+1,N): # from i+1 to the last molecules, to avoid double checking 
            
            COs[i].O.v, COs[j].O.v = collision_or_not(COs[i].O, COs[j].O)

            COs[i].C.v, COs[j].C.v = collision_or_not(COs[i].C, COs[j].C)
        
            COs[i].O.v, COs[j].C.v = collision_or_not(COs[i].O, COs[j].C)
        
            COs[i].C.v, COs[j].O.v = collision_or_not(COs[i].C, COs[j].O)
                
    for i in range(0,N):
        if L - COs[i].O.pos.x <= size or COs[i].O.pos.x + L <= size:
            COs[i].O.v.x *= -1
        elif L - COs[i].O.pos.y  <= size or COs[i].O.pos.y + L <= size:
            COs[i].O.v.y *= -1
        elif L - COs[i].O.pos.z <= size or COs[i].O.pos.z + L <= size:
            COs[i].O.v.z *= -1
        
        if L - COs[i].C.pos.x <= size or COs[i].C.pos.x + L <= size:
            COs[i].C.v.x *= -1
        elif L - COs[i].C.pos.y <= size or COs[i].C.pos.y + L <= size:
            COs[i].C.v.y *= -1
        elif L - COs[i].C.pos.z <= size or COs[i].C.pos.z + L <= size:
            COs[i].C.v.z *= -1
        ## change this to check and handle the collision of the atoms of all molecules on all 6 walls

        total_com_K += COs[i].com_K() * dt
        total_v_K += COs[i].v_K() * dt
        total_v_P += COs[i].v_P() * dt
        total_r_K += COs[i].r_K() * dt


    c_avg_com_K.plot( pos=(t, total_com_K / t) )
    c_avg_v_K.plot( pos=(t, total_v_K / t) )
    c_avg_r_K.plot( pos=(t, total_r_K / t) )
    c_avg_v_P.plot( pos=(t, total_v_P / t) )