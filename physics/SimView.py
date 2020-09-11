import matplotlib.pyplot as plt

class SimView(object):
    def __init__(self):
        self.simFrame = None
        self.fig = plt.gcf()
        self.axes = plt.gca()
        self.xlim = None
        self.ylim = None

    def render(self):
        plt.clf() # clear figure

        for c in self.simFrame.children:
            plt.plot(c.position[0], c.position[1], 'o')
