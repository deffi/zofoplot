from collections import namedtuple

Style = namedtuple("Style", ["name", "inherit"]) 

class Element:
    def __init__(self, parent, objectClasses = []):
        self.parent = parent
        self.objectClasses = []
        
    def children(self):
        raise NotImplementedError()
    
    def styles(self):
        raise NotImplementedError()
