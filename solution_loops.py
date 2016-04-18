sentence = raw_input('Please enter a sentence:')

new_sentence = ''
for letter in sentence:
    if letter.lower() not in ['a', 'e', 'i', 'o', 'u']:
        new_sentence += letter

print new_sentence
