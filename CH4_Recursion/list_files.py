def list_files(parent_directory, current_filepath=""):
    result = []
    for k in parent_directory:
        new_filepath = current_filepath + "/" + k
        if parent_directory[k] == None:
            result.append(new_filepath)
        else:
            result.extend(list_files(parent_directory[k], new_filepath))

    return result