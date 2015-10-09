from styles import StyleValue
from .element import Element
from .point import Point

class Series(Element):
    ### Initialization
    def __init__(self, parent, classes = None, id_ = None, x = None, y = None):
        styles = [
            StyleValue(self, "color"     , False, None),
            StyleValue(self, "shape"     , False, None),
            StyleValue(self, "line-width", False, None)
            ]
        super(Series, self).__init__(parent, styles, classes, id_)
        
        self.points = [Point(self, None, None, px, py) for px, py in zip(x, y)]
        
    ### Element methods
    def children(self):
        return self.points

