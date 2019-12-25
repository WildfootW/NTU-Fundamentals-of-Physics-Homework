# -*- coding: utf-8 -*-
#!/usr/bin/env python
#   Author: WildfootW
#

from vpython import *

earth_init = {"radius": 6.371E6, "mass": 5.97E24}
moon_init = {"radius": 1.317E6, "mass": 7.36E22}
sun_init = {"radius": 6.95E8, "mass": 1.99E30}
earth_orbit = {"radius": 1.495E11, "velocity": 2.9783E4}
moon_orbit = {"radius": 3.84E8, "velocity": 1.022E3}
orbit_theta = 5.145 / 180 * pi

# constant
gravity = vec(0, -1 * 9.80665, 0)
newtonian_constant = 6.674E-11

# scene
scene = canvas(width = 800, height = 600,     # unit: pixels
               center = vec(0, -0.2, 0),      # camera will continually look to center
               background = vec(0.10546875, 0.38671875, 0.17968750))
scene.lights = []
local_light(pos = vector(0, 0, 0))

# class
class Planet(sphere):
    mass = 0
    velocity = vector(0, 0, 0)

# function
def calculate_gravitational_force(self, other):
    magnitude = newtonian_constant * self.mass * other.mass / mag2(self.pos - other.pos)
    return magnitude * norm(other.pos - self.pos)

# object
#title_text = text(text = "Moon Orbit Precession", align = "center") # read-only
scene.caption = "Moon Orbit Precession"
planets = []
earth = Planet(mass = earth_init["mass"], radius = earth_init["radius"] * 10, texture = {"file": textures.earth}, make_trail = False)
planets.append(earth)
moon = Planet(mass = moon_init["mass"], radius = moon_init["radius"] * 10, color = color.white, make_trail = False)
planets.append(moon)
sun = Planet(mass = sun_init["mass"], radius = sun_init["radius"] * 10, color = vec(0.95703125, 0.6875, 0.25390625), emissive = True, make_trail = False)
planets.append(sun)
moon_tilting_arrow = arrow(color = color.white, shaftwidth = 0.5 * earth.radius)

# init status
#title_text.pos = vec(0, scene.center.y * 2, 0)

sun.pos = vector(0, 0, 0)
#earth.pos = vector(earth_orbit["radius"], 0, 0)
#earth.velocity = vector(0, earth_orbit["velocity"], 0)
#moon.pos = earth.pos + vector(moon_orbit["radius"] * cos(orbit_theta), 0, moon_orbit["radius"] * sin(orbit_theta))
#moon.velocity = vector(0, moon_orbit["velocity"], 0)

E = moon.mass / (earth.mass + moon.mass)
M = earth.mass / (earth.mass + moon.mass)
earth.pos = vec(-E * moon_orbit["radius"] * cos(orbit_theta) + earth_orbit["radius"], -E * moon_orbit["radius"] * sin(orbit_theta), 0)
earth.velocity = vec(0, 0, E * moon_orbit["velocity"] - earth_orbit["velocity"])
moon.pos = vec(M * moon_orbit["radius"] * cos(orbit_theta) + earth_orbit["radius"], M * moon_orbit["radius"] * sin(orbit_theta), 0)
moon.velocity = vec(0, 0, -M * moon_orbit["velocity"] - earth_orbit["velocity"])
moon_tilting_arrow.pos = earth.pos
moon_tilting_arrow.axis = 4.5 * earth.radius * norm(cross(moon.pos - earth.pos, moon.velocity - earth.velocity))

# sport
dt = 60 * 60 * 6
current_time = 0
record_timestamp = [0, 0]
last_value = 0
while True:
    rate(1000) # limit execute amount in 1 second
    current_time += dt

#    for planet in planets:
#        planet.pos = planet.pos + planet.velocity * dt
#
#        if planet == earth:
#            scene.center = earth.pos
#
#        resultant_force = vector(0, 0, 0)
#        for other_planet in planets:
#            if planet == other_planet:
#                continue
#            resultant_force += calculate_gravitational_force(planet, other_planet)
#
#        planet.acceleration = resultant_force / planet.mass
#        planet.velocity = planet.velocity + planet.acceleration * dt
    moon.acceleration = -newtonian_constant * earth.mass * moon.mass / mag2(moon.pos-earth.pos) * norm(moon.pos-earth.pos) / moon.mass-newtonian_constant*sun.mass*moon.mass/mag2(moon.pos-sun.pos)*norm(moon.pos-sun.pos)/moon.mass
    earth.acceleration = -newtonian_constant * earth.mass * moon.mass / mag2(moon.pos-earth.pos) * norm(earth.pos-moon.pos) / earth.mass-newtonian_constant*sun.mass*earth.mass/mag2(earth.pos-sun.pos)*norm(earth.pos-sun.pos)/earth.mass
    moon.velocity += moon.acceleration * dt
    moon.pos += moon.velocity * dt
    earth.velocity += earth.acceleration * dt
    earth.pos += earth.velocity * dt
    scene.center = earth.pos

    moon_tilting_arrow.pos = earth.pos
    moon_tilting_arrow.axis = 4.5 * earth.radius * norm(cross(moon.pos - earth.pos, moon.velocity - earth.velocity))

    if cross((moon.pos - earth.pos), moon.velocity - earth.velocity).x * last_value < 0:
        if not record_timestamp[0] == 0:
            print((current_time - record_timestamp[0]) / (60 * 60 * 24 * 365.25), end = "")
            print(" years")
        record_timestamp.append(current_time)
        record_timestamp.pop(0)
    last_value = cross((moon.pos - earth.pos), moon.velocity - earth.velocity).x



