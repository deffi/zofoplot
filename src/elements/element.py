from styles import StyleContainer, StyleAccessor

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
