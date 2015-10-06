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

if __name__ == "__main__":
    from styles import StyleContainer, StyleAccessor
    
    line_styles = [
        Style("color"    , False, None),
        Style("width"    , False, None),
        Style("dash-type", False, None),
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
