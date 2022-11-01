# Autor: Jesús Chaves
# Programa en cython para el cálculo de la orbita 
# Fecha 01 de Noviembre

from math import sqrt

cdef class Planet(object):

    cdef:
        float x
        float y 
        float z
        float vx
        float vy
        float vz
        float m

    def __init__(self):
    	# some initial position and velocity
        self.x = 1.0
        self.y = 0.0
        self.z = 0.0
        self.vx = 0.0
        self.vy = 0.5
        self.vz = 0.0
        
        # some mass
        self.m = 1.0

def single_step(Planet planet, float dt):
    """ Make a single time step"""
    
    # Compute force: gravity towards origin
    cdef float distance = sqrt(planet.x**2 + planet.y**2 + planet.z**2)
    cdef float Fx = -planet.x / (distance**3)
    cdef float Fy = -planet.y / (distance**3)
    cdef float Fz = -planet.z / (distance**3)
    
    # Time step position, according to velocity
    planet.x += dt * planet.vx
    planet.y += dt * planet.vy
    planet.z += dt * planet.vz

    # Time step velocity, according to force and mass
    planet.vx += (dt * Fx) / planet.m
    planet.vy += (dt * Fy) / planet.m
    planet.vz += (dt * Fz) / planet.m


def c_step_time (planet,float time_span,int n_steps):
    """Make a number of time steps forward"""
    cdef double dt

    dt = time_span / n_steps
    cdef int j
    for j in range(n_steps):
        single_step(planet, dt)
