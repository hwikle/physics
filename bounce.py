from physlib import *
from SimView import *
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt

simFrame = PhysicsFrame()
simFrame.timestep = 1/50
ball = PointMass2D(1)
ball.add_force(lambda t:np.array([0, -G*ball.mass]))
simFrame.add_child(ball)

view = SimView()
view.simFrame = simFrame

def animFunc(frame):
    simFrame.step()
    view.render()

anim = FuncAnimation(view.fig, animFunc, interval=1000/50)

plt.show()

