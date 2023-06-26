import random


def leet_pass(words1, numbers2, qty3):
    leet_replacements = {
        'A': ['4', '@'],
        'E': '3',
        'L': '1',
        'O': '0',
        'S': ['5', '$'],
        'T': '7'
    }

    passwords1 = set()

    for word in words1:
        for number in numbers2:
            leet_word = ''
            for char in word.upper():
                if char in leet_replacements:
                    replacement = leet_replacements[char]
                    if isinstance(replacement, list):
                        replacement = random.choice(replacement)  # Choose a random replacement option
                    leet_word += replacement
                else:
                    leet_word += char

            passwords1.add(leet_word + number)
            passwords1.add(number + leet_word)

    return list(passwords1)[:qty3]
