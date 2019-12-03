##https://youtu.be/nLVT08xK4-8
import numpy as np
from vpython import *

diagram = graph(width = 700, align = 'left', xtitle = 'wavevector', ytitle = 'angular frequency', background = vec(0.2,0.4,0)) 
func = gcurve(color=color.magenta, graph = diagram)

A, N = 0.1, 50
size, m, k, d = 0.06, 0.1, 10, 0.4

for n in range(1, int(N/2)):
    wave_vector = 2*pi / ((N*d) /n) ##((N*d) /n) is lamda because lamda * n is N * d
    phase = wave_vector * arange(N) * d
    
    ball_pos, ball_orig = np.arange(N) * d + A * np.sin(phase), np.arange(N) * d
    ball_v, spring_len = np.zeros(N), np.ones(N)*d
    
    t = 0
    dt = 0.001
    
    original_delta = ball_pos[1] - ball_orig[1]
    times = 0

    while(1):
        if (original_delta - ( ball_pos[1] - ball_orig[1]) < 10**-8) and \
        (t > 0.01):
            break
        else:
            spring_len[:-1] = ball_pos[1:] - ball_pos[:-1]
            spring_len[-1] = ball_pos[0] + N*d - ball_pos[-1]
            
            '''
            a_for_others = ((- k * (spring_len[:-1] - d) ) - \
            (- k * (spring_len[1:] - d))) / m
            a_for_ball0 = ((- k * (spring_len[0] - d)) - \
            (- k * (spring_len[-1] - d))) / m
            '''

            ball_v[0] += (((- k * (spring_len[-1] - d) ) - \
            (- k * (spring_len[0] - d))) / m) *dt
            '''a_for_ball0 * dt'''

            ball_v[1:] += (((- k * (spring_len[:-1] - d) ) - \
            (- k * (spring_len[1:] - d))) / m) *dt
            '''a_for_others * dt'''

            ball_pos += ball_v * dt

            t += dt
        
    func.plot(pos=(wave_vector, 2*pi / t))