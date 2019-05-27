def is_isogram(string):
    character_check=[c.lower() for c in string if c.isalpha()]
    return len(set(character_check)) == len(character_check)
