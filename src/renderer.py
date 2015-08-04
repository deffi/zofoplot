import matplotlib.pyplot as plt

class Renderer:
    def render(self, chart):
        fig = plt.figure(dpi=100, figsize=(5,4)) # Size in inches
        ax = fig.add_subplot(111)
        
        # Stub
