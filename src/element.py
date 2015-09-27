from style import Style, StyleContainer, StyleAccessor

# Anything that can by styled
class Element:
    # classes: a list of object classes. If nothing is passed, an empty list
    # will be used.
    def __init__(self, styles, classes = None, id_ = None):
        self.style_container = StyleContainer(styles)
        self.style = StyleAccessor(self.style_container)

        self.classes = classes or []
        self.id_ = id_
        
    # Must be implemented to return a list of all children; all instances of
    # Element subclasses, but can be different ones.
    def children(self):
        raise NotImplementedError()
    
    # Prints a representation of the tree with all properties to stdout.
    # indentString is the string that is used for indenting, and indentLevel
    # is the number of times the indent string is prepended to each line on this
    # level.
    def dump(self, indentString = "  ", indentLevel = 0):
        indentPrefix = indentString * indentLevel

        # Create the description for this Element
        description = self.__class__.__name__
        if self.id_:
            description += ' ' + repr(self.id_)
        if self.classes:
            description += ' ' + repr(self.classes)
        
        # Add the styles to the description
        if self.style_container.style_list:
            style_descriptions = ["%s: %s" % (style.name, style.value) for style in self.style_container.style_list]
            description += ' (' + ", ".join(style_descriptions) + ')'
        
        # Output the description for this element
        print(indentPrefix + description)
        
        # Output the styles in the tree
        #self.style_container.dump(indentString * (indentLevel + 1))
        
        # Recursively output the children as a tree
        for child in self.children():
            child.dump(indentString, indentLevel + 1)

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
