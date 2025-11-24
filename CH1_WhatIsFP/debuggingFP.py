def format_line(line):
    line = line.strip()
    line = line.upper()
    line = line.replace('.', '')
    
    return f"{line}..."
