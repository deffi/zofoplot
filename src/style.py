# TODO: attribute is a Python term, use a different one (e. g. property)
class Attribute:
    def __init__(self, name, default = None, inherit = False):
        self.name = name
        self.default = default
        self.inherit = inherit

    def dump(self, indent_prefix = ""):
        print(indent_prefix + "%s: %s")

class StyleContainer:
    def __init__(self, attribute_list):
        self.attribute_list = attribute_list
        self.attribute_dict = { a.name: a    for a in attribute_list }
        self.value_dict     = { a.name: None for a in attribute_list } 

    def has_style(self, name):
        return (name in self.attribute_dict) 

    def set_style(self, name, value):
        if not name in self.attribute_dict:
            raise AttributeError
        
        self.value_dict[name] = value
    
    def get_style(self, name):
        if not name in self.attribute_dict:
            raise AttributeError

        return self.value_dict[name]
    
    def dump(self, indent_prefix = ""):
        for attribute in self.attribute_list:
            name = attribute.name
            value = self.value_dict[name]
            print(indent_prefix + "%s: %s" % (name, value))
            
        
    
class StyleAccessor:
    def __init__(self, container):
        # Setting _container directly would result in a call to __setattr__,
        # which would result in a call to __getattr__ for _container.
        self.__dict__["_container"] = container

    def __getattr__(self, name):
        return self._container.get_style(name)
    
    def __setattr__(self, name, value):
        self._container.set_style(name, value)


line_attributes = [
    Attribute("color"),
    Attribute("width"),
    Attribute("dash-type"),
    ]

style_container = StyleContainer(line_attributes)
style = StyleAccessor(style_container)

style.color = "red"
style.width = 4

style_container.dump()
print(style.color, style.width)

