from elements import Element
from styles import Style

class Point(Element):
    ### Initialization
    def __init__(self, classes = None, id_ = None, x = None, y = None):
        styles = [
            Style("color", True, None),
            Style("shape", True, None),
            Style("size" , False, None) # TODO inherit this from point-size?
            ]
        super(Point, self).__init__(styles, classes, id_)
        self.x = x
        self.y = y

    ### Element methods
    def children(self):
        return []
