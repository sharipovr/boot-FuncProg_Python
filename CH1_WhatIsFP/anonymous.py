def file_type_getter(file_extension_tuples):
    result = {}
    for el in file_extension_tuples:
        for ext in el[1]:
            result[ext] = el[0]
    
    return lambda x: result.get(x, "Unknown")