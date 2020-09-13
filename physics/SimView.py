import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class SimView(object):
    def __init__(self):
        self.simFrame = None
        self.fig = plt.gcf()

    def nextFrame(self, frame):
        self.simFrame.step()
        #plt.clf()

        for c in self.simFrame.children:
            #plt.plot(c.position[0], c.position[1], 'o')
            plt.plot(self.simFrame.time, c.position[1], "o")
            

    def start(self):
        anim = FuncAnimation(self.fig, self.nextFrame)
        plt.show()
        
