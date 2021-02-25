# program takes a text from a file and calculates the percentage of each letter in it

# define a function that will calculate the characters from a text
def count_char(self, char):
  count = 0
  for c in text: 
    if c == char:
      count += 1
  return count

# present the menu to the user
files = ["William Shakespeare, 'Sonnet 18'", "Edgar Alan Po, 'The Raven'", "William Blake, 'Infant Joy'", "Hilda Doolittle, 'The pool'"]
filenum = input("Enter a number of a file you'd like to open:\n{0} - 1\n{1}\t\t - 2\n{2}\t\t - 3\n{3}\t\t - 4\n> ".format(files[0], files[1],files[2],files[3]))

# print a title and a content of a file
with open(filenum, 'r') as f:
  text = f.read()
  title_and_author = files[(int(filenum)-1)]
  separator = title_and_author.find(", ")
  author = title_and_author[0 : separator]
  title = title_and_author[separator+2 :]
  print("Title: {0}\nAuthor: {1}\n\n{2}\n\nA number of characters in the text: {3}\n\nPercentage of each character in the text:".format(title, author, text, str(len(text))))
  # change all characters to lower case to be used in the next loop 
  text = text.lower()

# calculate and print percentage of each letter in the text
for char in "abcdefghijklmnopqrstuvxyz":
  perc = 100 * (count_char(text, char) / len(text))
  print("{0} - {1}%".format(char, round(perc, 2)))
