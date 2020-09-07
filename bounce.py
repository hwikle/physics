from physlib import *
from SimView import *
#from matplotlib.animation import FuncAnimation
#import matplotlib.pyplot as plt

# create and configure simulation frame
simFrame = PhysicsFrame()
simFrame.timestep = 1/50

# create force object for gravity
gravity = Force()
gravity.is_constant = True
gravity.vector = np.array([0, -G*ball.mass])

# create ball in simulation frame, with gravity
ball = PointMass2D(1)
ball.add_force(gravity)
simFrame.add_child(ball)

# attach view to simulation frame
view = SimView()
simFrame.attach(view) # implement

simFrame.start()

#def animFunc(frame):
#    simFrame.step()
#    view.render()
#
#anim = FuncAnimation(view.fig, animFunc, interval=1000/50)
#
#plt.show()
#
