from physics.core import *
from physics.SimView import *
from physics.SimWindow import *
from matplotlib import pyplot as plt

class PositionView(SimView):
    def __init__(self):
        super().__init__()

    def next_frame(self):
        self.axis.clear()

        for c in self.simFrame.children:
            self.axis.plot(c.position[0], c.position[1], 'bo')

class EnergyView(SimView):
    def __init__(self):
        super().__init__()

    def next_frame(self):
        self.axis.plot(self.simFrame.time, self.simFrame.calc_energy(), 'ro')

# create and configure simulation frame
simFrame = PhysicsFrame()
simFrame.timestep = 1/50

# create ball in simulation frame
ball = PointMass2D(1)
simFrame.add_child(ball)

# create force object for gravity, and add to ball
gravity = Force()
gravity.is_constant = True
gravity.vector = np.array([0, -G*ball.mass])
ball.add_force(gravity)

# create simulation window
window = SimWindow(1, 2)

# attach view to simulation frame
pos_view = PositionView()
pos_view.simFrame = simFrame
window.add_view(pos_view)

energy_view = EnergyView()
energy_view.simFrame = simFrame
window.add_view(energy_view)

window.start()

#def animFunc(frame):
#    simFrame.step()
#    view.render()
#
#anim = FuncAnimation(view.fig, animFunc, interval=1000/50)
#
#plt.show()
#
