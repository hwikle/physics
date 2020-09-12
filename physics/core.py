import numpy as np
from time import sleep

G = 9.8 # approx. Earth gravity, meters per second squared
T_STEP = 0.01

class PhysicsFrame(object):
    def __init__(self):
        self.time = 0 # current time in seconds   
        self.timestep = 1
        self.children = []
        self.view = None

    def add_child(self, child):
        assert(isinstance(child, PhysicsObject))
        self.children.append(child)

    def step(self):
        for child in self.children:
            # must update all velocities before updating positions, since new velocities may depend on positions
            child.apply_forces(self.time)
            child.update_velocity(self.timestep)
            child.reset_acceleration()

        for child in self.children:
            child.update_position(self.timestep)

        self.time += self.timestep

class PhysicsObject(object): # For future-proofing
    def __init__(self):
        pass

class Particle(PhysicsObject):
    def __init__(self, dimension, position):
        if not isinstance(position, np.ndarray):
            raise TypeError('Position must be ndarray')
        if position.shape[-1] != dimension:
            raise ValueError('Length of position vector does not match number of dimensions')
        self.dimension = dimension
        self.position = position
        self.velocity = np.zeros(dimension)
        self.acceleration = np.zeros(dimension)
 
class Particle2D(Particle):
    def __init__(self, position):
        super().__init(self, 2, position)

class Particle3D(Particle):
    def __init__(self, position):
        super().__init__(3, position)

class PointMass2D(PhysicsObject):
        def __init__(self, mass):
            super().__init__()

            self.mass = mass
            self.forces = []

        def add_force(self, forceFunc):
            self.forces.append(forceFunc)

        def apply_forces(self, t):
            for f in self.forces:
                self.acceleration += f.evaluate(t)/self.mass

        def update_velocity(self, delta_t):
            self.velocity += self.acceleration * delta_t
        
        def update_position(self, delta_t):
            self.position += self.velocity * delta_t

        def reset_acceleration(self):
            self.acceleration = np.zeros(2)

class MassiveObject(Particle):
    pass

class CordLength(MassiveObject):
    pass

class Cord(PhysicsObject):
    pass

class Force(PhysicsObject):
    def __init__(self):
        self.dimension = None
        self.is_constant = False
        self.vector = None
        self.function = None

    def evaluate(self, t):
        if self.is_constant:
            return self.vector
        else:
            return self.function(t)

if __name__ == '__main__':
    pass
