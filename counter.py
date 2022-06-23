import re


f = open("EAPoe.txt", "r")

vowels = ['a', 'e', 'i', 'o', 'u','A','E', 'I', 'O', 'U']


number_of_lines = 0
number_of_words = 0
number_of_characters = 0
number_of_vowels = 0
number_of_spaces = 0
for line in f:
    line = line.strip("\n")
    words = re.split(r"\s", line)
    number_of_lines += 1
    number_of_words += len(words)
    number_of_characters += len(line)
	
    for i in range(len(words)):
        if re.search(r"^spider[s]?[.!,?';]*", words[i]):
            words[i] = "elephant"
		#print(words[i])

    for cha in line:
        if cha in vowels:
            number_of_vowels +=1
        elif cha == " ":
            number_of_spaces +=1


f.close()


print(" number of words:", number_of_words, "\n", "number of characters:", number_of_characters, "\n", "number of lines:", number_of_lines, "\n", "number of vowels:", number_of_vowels)
