sentence = input("Enter a sentence: ")

words = len(sentence.split())
vowels = 0
consonants = 0
digits = 0
spaces = 0
special_characters = 0

for char in sentence:
    if char.isalpha():
        if char.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1
    elif char.isdigit():
        digits += 1
    elif char.isspace():
        spaces += 1
    else:
        special_characters += 1

total_characters = len(sentence)
total_letters = vowels + consonants
vowel_percentage = (vowels / total_letters) * 100 if total_letters > 0 else 0

print("\n" + "=" * 50)
print("           DOCUMENT ANALYSIS REPORT")
print("=" * 50)

print("Sentence:", sentence)
print("Total characters:", total_characters)

print("\n--- Character Breakdown ---")
print("Words:", words)
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special characters:", special_characters)

print("\n--- Summary ---")
print("Total letters:", total_letters)
print("Vowel percentage: {:.1f}%".format(vowel_percentage))

print("\n" + "=" * 50)
print("Analysis Complete!")
print("=" * 50)
