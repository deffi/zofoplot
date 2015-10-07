from elements import Element
from styles import Style

class Point(Element):
    ### Initialization
    def __init__(self, parent, classes = None, id_ = None, x = None, y = None):
        styles = [
            Style(self, "color", True, None),
            Style(self, "shape", True, None),
            Style(self, "size" , False, None) # TODO inherit this from point-size?
            ]
        super(Point, self).__init__(parent, styles, classes, id_)
        self.x = x
        self.y = y

    ### Element methods
    def children(self):
        return []
