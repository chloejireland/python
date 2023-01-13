# open old file and new file
oldfile = open("alice-in-wonderland.txt", "r")
newfile = open("alice_words.txt", "w")



punctuation = "!#$%&()*+,./:;<=>?@[\]^_`{|}~0123456789'" # all that will be removed
newstring = ''
for sentence in oldfile: #remove all punctuation first
    for letter in sentence:
        if letter not in punctuation:
            newstring = newstring + letter # add letter to the string if not punctuation

newstring = newstring.replace('"', "") # getting rid of quotes
newstring = newstring.replace("--", " ") # getting rid of double dashes, not single 
newlist = newstring.split() # turning string into list

word_count = {} # creating dictionary
for word in newlist:
    word = word.lower() # all words should be lowercase
    word_count[word] = word_count.get(word, 0) + 1
word_list = list(word_count.items())
word_list.sort() # alphabetize 
newfile.write("Word              Count \n") 
newfile.write("======================= \n")
for tup in word_list:
    (word, num) = tup # unpacking the tuple
    word = str(word)
    num = str(num)
    word = word.ljust(20) # function learned from https://www.w3schools.com/python/ref_string_ljust.asp, aligns the output
    newfile.write(word)
    newfile.write(num + '\n')
