def get_max_heart_rate(age):
    base_max = 220
    return base_max - age


def remove_vowels(sentence):
    new_sentence = ''
    for letter in sentence:
        if letter.lower() not in ['a', 'e', 'i', 'o', 'u']:
            new_sentence += letter

    return new_sentence


first_age = 18
print get_max_heart_rate(first_age)

second_age = 27
print get_max_heart_rate(second_age)

print remove_vowels("Hello World!")
print remove_vowels("A sentencE with RaNDOm casing")
