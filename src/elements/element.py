from style import StyleContainer, StyleAccessor

# Anything that can by styled
class Element:
    # classes: a list of object classes. If nothing is passed, an empty list
    # will be used.
    def __init__(self, parent, style_descriptors, classes = None, id_ = None):
        self._parent = parent
        
        if parent:
            parent_style_container = parent.style_container
        else:
            parent_style_container = None
        
        self.style_container = StyleContainer(style_descriptors, parent_style_container)
        self.style = StyleAccessor(self.style_container)

        self.classes = classes or []
        self.id_ = id_
        
    # Must be implemented to return a list of all children; all instances of
    # Element subclasses, but can be different ones.
    def children(self):
        raise NotImplementedError()

    def get_parent(self):
        return self._parent
    