def evaluate(text, cells):
    if not isinstance(text,str) or not text.startswith('='):return text
    terms=text[1:].split('+');total=0
    for term in terms:
        try:total+=float(term)
        except ValueError:total+=float(cells.get(term,0) or 0)
    return total
