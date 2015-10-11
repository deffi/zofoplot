from style import StyleDescriptor
from elements import Element
from .series import Series

chart_styles = [
    StyleDescriptor("background_color", False)
    ]

class Chart(Element):
    ### Initialization
    def __init__(self, parent = None, classes = None, id_ = None):
        super(Chart, self).__init__(parent, chart_styles, classes, id_)
        self.serien = []
        
    ### Element methods
    def children(self):
        return self.serien
        
    ### Child handling
    def add_series(self, series):
        self.serien.append(series)
        
    def create_series(self, *args, **kwargs):
        self.add_series(Series(*args, **kwargs))


