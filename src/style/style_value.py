# A descriptor for a style; for example, "color" might be a Property of a line,
# and it might be inherited from its parent.
class StyleValue:
    def __init__(self, name, parent):
        self._name   = name
        self._parent = parent
        
        self.value = None

    def get_name(self):
        return self._name

    def resolve_value(self):
        '''
        Returns (value, inherited), where value is the resolved value and
        inherited is True if the value has been inherited.  
        ''' 
        if self.value is not None:
            # This Style has a value
            return (self.value, False)
        elif self._parent is not None:
            # This Style does not have an own value, but the value can be
            # inherited.
            value, _ = self._parent.resolve_value()
            return (value, True)
        else:
            # This Style does not have an own value and the value cannot be
            # inherited.
            return (None, False)

    def dump(self, indent_prefix = ""):
        print(indent_prefix + "%s: %s" % (self._name, self.value))


if __name__ == "__main__":
    from style import StyleDescriptor, StyleContainer, StyleAccessor
    
    line_styles = [
        StyleDescriptor("color"    , False),
        StyleDescriptor("width"    , False),
        StyleDescriptor("dash-type", False),
        ]
    
    style_container = StyleContainer(line_styles, None)
    style = StyleAccessor(style_container)
    
    # Set properties in different ways
    style.color = "red"
    style["width"] = 4
    
    # Dump the container
    style_container.dump("* ")
    
    # Get properties in different ways
    print(style.color, style.width)
    print(style["color"], style["width"])
