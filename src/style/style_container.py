import warnings
from style.style_value import StyleValue

class StyleContainer:
    '''
    A container for several Styles. Each Element has a StyleContainer,
    populated with all of its properties.
    '''
    def __init__(self, style_descriptors, parent_style_container):
        '''
        style_descriptors is a list of StyleDescriptor.
        parent_style_container is the container of the style to inherit from.
        '''
        # Based on the style descriptors, create the individual style values.
        
        # A list of style values for accessing in order
        self.style_list = []
        # A dictionary of style values for accessing by name
        self.style_dict = {}
        
        for style_descriptor in style_descriptors:
            # Extract the basic properties
            name    = style_descriptor.name
            inherit = style_descriptor.inherit
            
            # Find the parent StyleValue (if the style cannot be inherited, the
            # parent StyleValue will be None.  
            if not inherit:
                # The style value cannot be inherited 
                parent_style_value = None
            elif parent_style_container is None:
                warnings.warn("Inheritable style in top-level element: %s" % name)
                parent_style_value = None
            elif not parent_style_container.has_style(name):
                warnings.warn("No matching parent for inheritable style: %s" % name)
                parent_style_value = None
            else:
                parent_style_value = parent_style_container.get_style(name)

            # Create the style value
            style_value = StyleValue(name, parent_style_value)
            
            # Insert the style value into the list and dictionary
            self.style_list.append(style_value)
            self.style_dict[name] = style_value
        
    def has_style(self, name):
        return (name in self.style_dict) 

    def get_style(self, name):
        if not name in self.style_dict:
            raise AttributeError

        return self.style_dict[name]
    
    def dump(self, indent_prefix = ""):
        for style in self.style_list:
            style.dump(indent_prefix)
