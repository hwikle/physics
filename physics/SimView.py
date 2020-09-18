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
        self.axes = None
        self.xlims = [-VIEW_WIDTH/2, VIEW_WIDTH/2]
        self.ylims = [-VIEW_HEIGHT, 0]

    def nextFrame(self, frame):
        raise NotImplementedError("Extend this class to implement")
        
