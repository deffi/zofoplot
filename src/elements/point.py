from elements import Element
from style import StyleValue

class Point(Element):
    ### Initialization
    def __init__(self, parent, classes = None, id_ = None, x = None, y = None):
        styles = [
            StyleValue(self, "color", True, None),
            StyleValue(self, "shape", True, None),
            StyleValue(self, "size" , False, None)
            ]
        super(Point, self).__init__(parent, styles, classes, id_)
        self.x = x
        self.y = y

    ### Element methods
    def children(self):
        return []
