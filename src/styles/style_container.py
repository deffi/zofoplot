class StyleContainer:
    '''
    A container for several Styles. Each Element has a StyleContainer,
    populated with all of its properties.
    '''
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
            
        
