#In this kata you are required to, given a string, replace every letter with its position in the alphabet.

# anything in the text isn't a letter, ignore it and don't return it.

#"a" = 1, "b" = 2, etc.


alphabet = 'abcdefghijklmnopqrstuvwxyz'
def alphabet_position(text):
    positions = []
    for char in text:
        if char.lower() in alphabet:
            positions.append(str(alphabet.index(char.lower()) + 1))
    return ' '.join(positions)