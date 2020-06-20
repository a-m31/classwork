# This program reverses the order of letters in a word

word=input("Enter word to reverse: ")

def reverse(word):
    if len(word)<2:
        return word
    else:
        return reverse(word[1:])+word[0]

print("Original word: ",word)
print("Reversed word: ",reverse(word))
