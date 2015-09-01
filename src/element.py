from collections import namedtuple

Style = namedtuple("Style", ["name", "inherit"]) 

class Element:
    def __init__(self, classes = None):
        self.classes = classes
        
    def children(self):
        raise NotImplementedError()
    
    def styles(self):
        raise NotImplementedError()

    def dump(self, indentString = "  ", indentLevel = 0):
        indentPrefix = indentString * indentLevel
        print(indentPrefix + str(self.__class__.__name__) + " " + str(self.classes))
        
        for child in self.children():
            child.dump(indentString, indentLevel + 1)
        


class Chart(Element):
    def __init__(self, classes = None):
        super(Chart, self).__init__(classes)
        self.serien = []
        
    def children(self):
        return self.serien
        
    def add_series(self, series):
        self.serien.append(series)
        
    def create_series(self, *args, **kwargs):
        self.add_series(Series(*args, **kwargs))

class Series(Element):
    def __init__(self, classes = None, x = None, y = None):
        super(Series, self).__init__(classes)
        self.points = [Point(None, px, py) for px, py in zip(x, y)]
        
    def children(self):
        return self.points

class Point(Element):
    def __init__(self, classes = None, x = None, y = None):
        super(Point, self).__init__(classes)
        self.x = x
        self.y = y

    def children(self):
        return []
    