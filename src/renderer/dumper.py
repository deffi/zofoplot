class Dumper:
    # Prints a representation of the tree with all properties to stdout.
    # indentString is the string that is used for indenting, and indentLevel
    # is the number of times the indent string is prepended to each line on this
    # level.
    def dump(self, element, indentString = "  ", indentLevel = 0):
        indentPrefix = indentString * indentLevel

        # Create the description for this Element
        description = element.__class__.__name__
        if element.id_:
            description += ' ' + repr(element.id_)
        if element.classes:
            description += ' ' + repr(element.classes)

        # Add the styles to the description
        style_list = element.style_container.style_list
        if style_list:
            style_parts = [self.style_text(style) for style in style_list]
            description += ' (' + ", ".join(style_parts) + ')'
        
        # Output the description for this element
        print(indentPrefix + description)
        
        # Output the styles in the tree
        #element.style_container.dump(indentString * (indentLevel + 1))
        
        # Recursively output the children as a tree
        for child in element.children():
            self.dump(child, indentString, indentLevel + 1)

    def style_text(self, style):
        name = style.get_name()
        value, inherited = style.resolve_value()
        
        if inherited:
            return "%s: [%s]" % (name, value)
        else:
            return "%s: %s" % (name, value)
    
