from style import StyleDescriptor
from elements import Element
from .point import Point

series_styles = [
    StyleDescriptor("color"     , False),
    StyleDescriptor("shape"     , False),
    StyleDescriptor("line-width", False)
    ]

class Series(Element):
    ### Initialization
    def __init__(self, parent, classes = None, id_ = None, x = None, y = None):
        super(Series, self).__init__(parent, series_styles, classes, id_)
        
        self.points = [Point(self, None, None, px, py) for px, py in zip(x, y)]
        
    ### Element methods
    def children(self):
        return self.points

