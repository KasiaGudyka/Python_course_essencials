# prints every second character, reverse and vowels of a word

print("This program prints every second character, reverse and vowels of a word.")

def Check_vowels(s, vowels):
  final = [each for each in s if each in vowels]
  print("The vowels in the word are: ", ", ".join(final))

for i in range(int(input("How many words would you like to convert?: "))):
    s = str(input("Write a word: "))
    print("Every other characters are: ", s[::2])
    print("The word reversed is: ", s[::-1])
    vowels = "AaIiUuEeOo"
    Check_vowels(s, vowels)
