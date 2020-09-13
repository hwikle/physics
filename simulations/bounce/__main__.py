import sys
sys.path.append("~/Documents/programming/python/physics/physics")

from physics.core import *
from physics.SimView import *

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

# attach view to simulation frame
view = SimView()
view.simFrame = simFrame # implement

view.start()

#def animFunc(frame):
#    simFrame.step()
#    view.render()
#
#anim = FuncAnimation(view.fig, animFunc, interval=1000/50)
#
#plt.show()
#
