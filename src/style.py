# So we have two ways of storing the values:
#   * in the Style class => the Style class is a container
#   * in a dict in the StyleContainer => the Style class ist just a descriptor.
#     This means that we can reuse the Style list for all instances of the same
#     Element.
# We'll go with the container approach for now.

# A descriptor for a style; for example, "color" might be a Property of a line,
# and it might be inherited from its parent.
class Style:
    def __init__(self, name, inherit, default):
        self.name = name
        self.inherit = inherit
        self.default = default
        
        self.value = None

    def dump(self, indent_prefix = ""):
        print(indent_prefix + "%s: %s" % (self.name, self.value))

# A container for several Styles. Each Element has a StyleContainer,
# populated with all of its properties.
class StyleContainer:
    def __init__(self, style_list):
        # We keep a list of styles because we want to retain their order
        self.style_list = style_list
        # We keep a dictionary of style by name becase we want to access them
        # by name.
        self.style_dict = { s.name: s for s in self.style_list }

    def has_style(self, name):
        return (name in self.style_dict) 

    def get_style(self, name):
        if not name in self.style_dict:
            raise AttributeError

        return self.style_dict[name]
    
    def dump(self, indent_prefix = ""):
        for style in self.style_list:
            style.dump(indent_prefix)
            
        
# A shortcut for accessing a property from a StyleContainer with
#     line.style.width = 2
# instead of
#     line.styles.style("width").value = 2
# TODO styles with dashes
class StyleAccessor:
    def __init__(self, container):
        # Setting _container directly would result in a call to __setattr__,
        # which would result in a call to __getattr__ for _container.
        self.__dict__["_container"] = container

    def __getattr__(self, name):
        return self._container.get_style(name).value
    
    def __setattr__(self, name, value):
        self._container.get_style(name).value = value

if __name__ == "__main__":
    line_styles = [
        Style("color"    , False, None),
        Style("width"    , False, None),
        Style("dash-type", False, None),
        ]
    
    style_container = StyleContainer(line_styles)
    style = StyleAccessor(style_container)
    
    style.color = "red"
    style.width = 4
    
    style_container.dump("* ")
    print(style.color, style.width)

