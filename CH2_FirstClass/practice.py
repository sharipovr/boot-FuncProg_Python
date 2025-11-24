def restore_documents(originals, backups):
    combined = originals + backups

    mapped = map(lambda x: x.upper(), combined)
    filtered = filter(lambda x: not x.isdigit(), mapped)
    return set(filtered)
