
class StyleAccessor:
    '''
    A shortcut for accessing a property from a StyleContainer with
        line.style.width = 2
    instead of
        line.styles.style("width").value = 2
    '''
    
    # TODO styles with dashes
    
    def __init__(self, container):
        # Setting _container directly would result in a call to __setattr__,
        # which would result in a call to __getattr__ for _container.
        self.__dict__["_container"] = container

    def __getattr__(self, name):
        return self._container.get_style(name).value
    
    def __setattr__(self, name, value):
        self._container.get_style(name).value = value

