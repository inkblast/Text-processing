import string

#read setting file
setting = open("setting.txt","r")

input_file = setting.readline()
no_of_columns = int(setting.readline())
sortorder = setting.readline()
mywords = setting.readline().split(',')


word_count = 0
words = []
uniqe_words = set()
longest_word_length = 0
longest_words = []
mywords_count =[]

#read input file
f = open(input_file.strip(), "r")

for lines in f:

    line = lines.split()


    for word in line:
        if word == "--":
            continue
        else:
            word = word.strip(string.punctuation)
            word =word.lower()
            words.append(word)
            uniqe_words.add(word)
            word_count +=1
            if len(word) >= longest_word_length:
                longest_word_length = len(word)




f.close()


for _ in words:
    if len(_) == longest_word_length:
        longest_words.append(_)

for wor in mywords:
    mywords_count.append(str(words.count(wor)))

mywords_count = list(zip(mywords,mywords_count))


wd = [words[i:i+int(no_of_columns)] for i in range(0,len(words),int(no_of_columns))]

#display word list in file
for w in wd:
    w = "".join(element.ljust(longest_word_length +1) for element in w)
    print(w)

#write output file
output = open("EAPoe_output.txt",'w')
uniqe_words = list(uniqe_words)
#sort uniqe words
if sortorder == "d":
    uniqe_words.sort(reverse=True)
else:
    uniqe_words.sort()
uwd = [uniqe_words[i:i+int(no_of_columns)] for i in range(0,len(uniqe_words),int(no_of_columns))]


for u in uwd:
    u = "".join(element.ljust(longest_word_length +1) for element in u)
    output.write(f"|{u}\n|\n")

output.close()

#Statistics
print("="*(longest_word_length*no_of_columns))
print("output file EAPoe_output.txt has been written.")
print("Statistics on Words in Tell-Tale Heart:")
print('The number of  words in Tell-Tale Heart is',word_count)
print("The number of unique words is",len(uniqe_words))
print(f"The longest word has {longest_word_length} letters")
print("longest words:",*longest_words)
print("my words count:")

#myword count
for mw in mywords_count:
    mw = "".join(element.ljust(longest_word_length +1) for element in mw)
    print(mw)


#display output file
o = open("EAPoe_output.txt","r")

print(o.read())

o.close()




