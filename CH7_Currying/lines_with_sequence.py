import functools

def lines_with_sequence(char):
    def with_char(length):
        sequence = char * length
        def with_length(doc):
            lines = doc.split("\n")
            count = functools.reduce(lambda q, x: q+1 if sequence in x else q+0, lines, 0)
            return count
        return with_length
    return with_char
