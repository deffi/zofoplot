from elements import Element
from style import StyleDescriptor

point_styles = [
    StyleDescriptor("color", True ),
    StyleDescriptor("shape", True ),
    StyleDescriptor("size" , False)
    ]

class Point(Element):
    ### Initialization
    def __init__(self, parent, classes = None, id_ = None, x = None, y = None):
        super(Point, self).__init__(parent, point_styles, classes, id_)
        self.x = x
        self.y = y

    ### Element methods
    def children(self):
        return []
