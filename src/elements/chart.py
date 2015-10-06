from styles import Style
from .element import Element
from .series import Series

class Chart(Element):
    ### Initialization
    def __init__(self, classes = None, id_ = None):
        styles = [
            Style("background_color", False, None),
            ]
        super(Chart, self).__init__(styles, classes, id_)
        self.serien = []
        
    ### Element methods
    def children(self):
        return self.serien
        
    ### Child handling
    def add_series(self, series):
        self.serien.append(series)
        
    def create_series(self, *args, **kwargs):
        self.add_series(Series(*args, **kwargs))


