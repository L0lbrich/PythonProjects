def sentencemaker(phrase):
    wordchanges = ('who','what','why')
    capitalized = phrase.capitalize()
    if phrase.startswith(wordchanges):
        return '{}?'.format(capitalized)
    else:
        return '{}.'.format(capitalized)
Usertext = []
while True:
    message = input('say something')
    if message == '/end':
        break
    else:
        Usertext.append(message)
print(Usertext)
        
        

