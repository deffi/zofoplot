import warnings

# A descriptor for a style; for example, "color" might be a Property of a line,
# and it might be inherited from its parent.
class StyleValue:
    def __init__(self, element, name, inherit, default):
        self._element = element
        self._name    = name
        self._inherit = inherit
        self._default = default
        
        self.value = None

    def get_name(self):
        return self._name

    def parent_style(self):
        if self._element is None:
            return None
        else:
            parent = self._element.get_parent()
            if parent.style_container.has_style(self._name):
                return parent.style_container.get_style(self._name)
            else:
                warnings.warn("The parent does not contain a style that should be inheritable")
                return None

    def resolve_value(self):
        '''
        Returns (value, inherited), where value is the resolved value and
        inherited is True if the value has been inherited.  
        ''' 
        
        if self.value is not None:
            # This Style has a value
            return (self.value, False)
        elif self._inherit is False:
            # This Style does not have an own value and the value cannot be
            # inherited.
            return (None, False)
        elif self._element is None:
            # The value could be inherited, but this Style is not associated
            # with an element
            warnings.warn("Inheritable Style does not have an element.")
            return (None, False)
        elif self._element.get_parent() is None:
            # The value could be inherited, but the associated element does not
            # have a parent
            warnings.warn("Inheritable Style's element does not have a parent")
            return (None, False)
        elif not self._element.get_parent().style_container.has_style(self._name):
            # The value could be inherited, but the associated element's parent
            # does not have a style of the same name
            warnings.warn("Inheritable Style not found in parent")
            return (None, False)
        else:
            # The value can be inherited; resolve recursively.
            value, _ = self._element.get_parent().style_container.get_style(self._name).resolve_value()
            return (value, True)

    def dump(self, indent_prefix = ""):
        print(indent_prefix + "%s: %s" % (self._name, self.value))


if __name__ == "__main__":
    from style import StyleContainer, StyleAccessor
    
    line_styles = [
        StyleValue(None, "color"    , False, None),
        StyleValue(None, "width"    , False, None),
        StyleValue(None, "dash-type", False, None),
        ]
    
    style_container = StyleContainer(line_styles)
    style = StyleAccessor(style_container)
    
    # Set properties in different ways
    style.color = "red"
    style["width"] = 4
    
    # Dump the container
    style_container.dump("* ")
    
    # Get properties in different ways
    print(style.color, style.width)
    print(style["color"], style["width"])
