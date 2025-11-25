def find_longest_word(document, longest_word=""):
    if document.strip() == "":
        return longest_word
    
    w = document.split(maxsplit=1)
    
    if len(w[0]) > len(longest_word):
        longest_word = w[0]
    if len(w) == 1:
        return longest_word
    
    return find_longest_word(w[1], longest_word)
