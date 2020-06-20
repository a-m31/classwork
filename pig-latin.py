# This program translates English to Pig Latin

vowels = ['A','a','E','e','I','i','O','o','U','u']

english = input("Enter word or phrase to translate: ")
split_words = english.split()

for word in split_words:
    index=0

    # Translate words that start with vowel(s)
    if word[index] in vowels:
        translation = word+'yay'

    # Translate words that start with consonant(s)
    else:
        if any(char in vowels for char in word):
            while word[index] not in vowels:
                index+=1
                translation = word[index:]+word[:index]+'ay'

        # Also account for words that contain only consonants
        else:
            translation = word+'ay'

    print(translation,end=" ")
