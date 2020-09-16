import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

MILLISECS_PER_SEC = 1000
VIEW_WIDTH = 2 
VIEW_HEIGHT = 5
MARKER = 'bo'
POINT_SIZE = 20


class SimView(object):
    def __init__(self):
        self.simFrame = None
        self.fig = plt.figure()
        self.xlims = [-VIEW_WIDTH/2, VIEW_WIDTH/2]
        self.ylims = [-VIEW_HEIGHT, 0]

        self.ax1 = self.fig.add_subplot(1, 2, 1)
        self.ax2 = self.fig.add_subplot(1, 2, 2)

    def nextFrame(self, frame):

        # TODO: impl.artistement user-defined nextFrame function

        self.simFrame.step()

        self.ax1.clear()
        self.ax1.set_xlim(self.xlims)
        self.ax1.set_ylim(self.ylims)

        for c in self.simFrame.children:
            self.ax1.plot(c.position[0], c.position[1], MARKER, markersize=POINT_SIZE)
            self.ax2.plot(self.simFrame.time, self.simFrame.calc_energy(), 'bo')

    def start(self):
        
        anim = FuncAnimation(self.fig, self.nextFrame, interval=MILLISECS_PER_SEC*self.simFrame.timestep)
        plt.show()
        
