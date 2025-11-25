def count_nested_levels(nested_documents, target_document_id, level=1):
    for doc_id in nested_documents:
        if doc_id == target_document_id:
            return level
        new_level = level + 1
        found_level= count_nested_levels(nested_documents[doc_id], target_document_id, new_level)
        if found_level != -1:
          return found_level
    
    return -1