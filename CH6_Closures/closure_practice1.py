def new_collection(initial_docs):
    initial_docs2 = initial_docs.copy()
    def inner_func(doc):
        initial_docs2.append(doc)
        return initial_docs2
    return inner_func