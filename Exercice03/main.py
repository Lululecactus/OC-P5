words = ["python", "programmation", "langage", "ordinateur", "apprentissage"]
vowels = "aeiouyAEIOUY"

words_vowels_count = []

for word in words:
    vowel_count = 0
    for letter in word:
        if letter in vowels:
            vowel_count += 1
    
    words_vowels_count.append((word, vowel_count))

print(words_vowels_count)