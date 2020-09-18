from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

MILLISECS_PER_SEC = 1000

class SimWindow(object):
    def __init__(self, rows, cols):
        self.fig = plt.figure()
        self.rows = rows
        self.cols = cols
        self.views = []
        self.simFrame = None

    def add_view(self, view):
        view.axis = self.fig.add_subplot(self.rows, self.cols, len(self.views))
        self.views.append(view)

        if not self.simFrame:
            self.simFrame = view.simFrame

    def next_frame(self, frame):
        for v in self.views:
            v.next_frame()

    def start(self):
        anim = FuncAnimation(self.fig, self.next_frame, interval=MILLISECS_PER_SEC*self.simFrame.timestep)

        plt.show()
        
