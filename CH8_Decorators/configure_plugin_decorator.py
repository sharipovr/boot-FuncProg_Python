def configure_plugin_decorator(func):
    def wrapper(*args):
        d = dict(args)
        return func(**d)
    
    return wrapper
