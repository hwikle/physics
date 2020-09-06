from physlib import *
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt

simFrame = PhysicsFrame()
simFrame.timestep = 1/50
ball = PointMass2D(1)
ball.add_force(lambda t:np.array([0, -G*ball.mass]))
simFrame.add_child(ball)
fig = plt.gcf()

def animFunc(frame):
    simFrame.step()
    simFrame.display_children()

anim = FuncAnimation(fig, animFunc, interval=1000/50)
plt.show()


