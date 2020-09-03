import numpy as np
import matplotlib.pyplot as plt

G = 9.8

class PhysicsFrame(object):
    def __init__(self):
        self.time = 0
        self.children = []

    def add_child(self, child):
        assert(isinstance(child, PhysicsObject))
        self.children.append(child)

    def step(self):
        for child in self.children:
            # must update all velocities before updating positions, since new velocities may depend on positions
            child.apply_forces(self.time)
            child.update_velocity()
            child.reset_acceleration()

        for child in self.children:
            child.update_position()

        self.time += 1

    def display_children(self):
        for child in self.children:
            child.display(self.time)
        

class PhysicsObject(object):
    def __init__(self):
        pass

class PointMass(PhysicsObject):
        def __init__(self, mass):
            super().__init__()

            self.mass = mass
            self.position = np.zeros(2)
            self.velocity = np.zeros(2)
            self.acceleration = np.zeros(2)

            self.forces = []

        def add_force(self, forceFunc):
            self.forces.append(forceFunc)

        def apply_forces(self, t):
            for f in self.forces:
                self.acceleration += f(t)/self.mass

        def update_velocity(self):
            self.velocity += self.acceleration
        
        def update_position(self):
            self.position += self.velocity

        def reset_acceleration(self):
            self.acceleration = np.zeros(2)

        def display(self, t):
            plt.plot(t, self.position[1], 'o')

if __name__ == '__main__':
        simFrame = PhysicsFrame()
        m = PointMass(1)
        m.add_force(lambda t:np.array([0, -G]))
        simFrame.add_child(m)

        simFrame.display_children()

        for i in range(10):
            simFrame.step()
            simFrame.display_children()

        plt.show()
