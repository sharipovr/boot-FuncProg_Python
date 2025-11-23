def add_prefix(document, documents):
    prefix = f"{len(documents)}. "
    new_doc = prefix + document
    new_documents = documents + (new_doc,)
    return new_documents
