import copy

def css_styles(initial_styles):
    initial_styles2 = copy.deepcopy(initial_styles)
    def add_style(selector, property, value):
        if not selector in initial_styles2:
            dict = {}
            dict[property] = value
            initial_styles2[selector] = dict
        else:
            initial_styles2[selector][property] = value
        return initial_styles2
    return add_style