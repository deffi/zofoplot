from styles import Style
from .element import Element
from .point import Point

class Series(Element):
    ### Initialization
    def __init__(self, classes = None, id_ = None, x = None, y = None):
        styles = [
            Style("color"     , False, None),
            Style("shape"     , False, None),
            Style("line-width", False, None)
            ]
        super(Series, self).__init__(styles, classes, id_)
        
        self.points = [Point(None, None, px, py) for px, py in zip(x, y)]
        
    ### Element methods
    def children(self):
        return self.points

