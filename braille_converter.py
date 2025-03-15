# Braille conversion dictionary
BRAILLE_DICT = {
    'a': '⠁', 'b': '⠃', 'c': '⠉', 'd': '⠙', 'e': '⠑',
    'f': '⠋', 'g': '⠛', 'h': '⠓', 'i': '⠊', 'j': '⠚',
    'k': '⠅', 'l': '⠇', 'm': '⠍', 'n': '⠝', 'o': '⠕',
    'p': '⠏', 'q': '⠟', 'r': '⠗', 's': '⠎', 't': '⠞',
    'u': '⠥', 'v': '⠧', 'w': '⠺', 'x': '⠭', 'y': '⠽',
    'z': '⠵', ' ': '⠀', '.': '⠲', ',': '⠂', '!': '⠖',
    '?': '⠦', '"': '⠐', "'": '⠄', '@': '⠈', '#': '⠼',
    '1': '⠂', '2': '⠆', '3': '⠒', '4': '⠲', '5': '⠢',
    '6': '⠖', '7': '⠶', '8': '⠦', '9': '⠔', '0': '⠴'
}

def text_to_braille(text):
    """
    Convert text to Braille characters
    """
    if not text:
        return ""
    
    result = []
    for char in text.lower():
        result.append(BRAILLE_DICT.get(char, char))
    
    return ''.join(result)
