def flip_string(text):
    if len(text) <= 1:
        return text
    return flip_string(text[1:]) + text[:1]
