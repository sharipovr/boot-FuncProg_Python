def add_format(default_formats, new_format):
    new_default_formats = default_formats.copy()
    new_default_formats[new_format] = True
    return new_default_formats

def remove_format(default_formats, old_format):
    new_default_formats = default_formats.copy()
    new_default_formats[old_format] = False
    return new_default_formats
