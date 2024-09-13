def ariana_says(word: str) -> str:
    """Return word repeated four times with the string ', next ' between each
    occurrence.
    
    >>> ariana_says('Thank u')
    'Thank u, next Thank u, next Thank u, next Thank u"
    """
    return f"{word}, next {word}, next {word}, next {word}"
