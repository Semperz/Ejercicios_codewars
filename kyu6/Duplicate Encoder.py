#The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string.
#Ignore capitalization when determining if a character is a duplicate.


#1st try
def duplicate_encode(word):
    resultado = []
    word = word.lower()
    for i in word:
        if word.count(i) > 1:
            resultado.append(')')

        else:
            resultado.append('(')

    return ''.join(resultado)

#Refactor
def duplicate_encode(word):
    finalString =""
    for char in word.lower():
        if word.lower().count(char) > 1:
            finalString = finalString + ')'
        else:
            finalString = finalString + '('
    return finalString