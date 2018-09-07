
def upperLetterMaker(word) : # this function is to capitalize the first letter of a word or two
    upperLetter = word[0:1] # gets first letter of the word
    upperStr = upperLetter.upper() # changes letter to uppercase
    word = upperStr + word[1:] # adding the upper case letter to the rest of the word
    return (word)

def lowerLetterMaker(word) : # to lower the first letter of a word
    lowerLetter = word[0:1]
    lowLowLow = lowerLetter.lower()
    word = lowLowLow + word[1:]
    return (word)

useSentance = input("Enter a sentence: ") # getting user senctence
useSentance = useSentance.lower() # changing it all to lowercase
useSentance = useSentance + " " # incase no period is used at the end

list = []
list2 = [] # this is for a list of word from the user sentence

str = ""  # blank string to be used
for letter in useSentance : # goes through each letter of the sentence
    if letter == " " : # if a blank spot will add the word to list2 and clear str for more letters
        str =  upperLetterMaker(str)
        list2.append(str)
        str = ""
    elif letter == "." : # for people whom write proper english
        str = upperLetterMaker(str)
        list2.append(str)
        str = ""
    elif letter != " ": # adding the letters to a str for making a whole word
        str += letter
        list.append(letter)
    else:
        list2.append(str)

#print(list) # for testing puroposes
#print(list2)
#print (useSentance)

camelCaseWord = "" # empty string for the final print out word
for i in list2 : # going trought list2 and getting each word then compining them together
    if i == list2[0] : # for the first word on the list
        camelCaseWord = lowerLetterMaker(i)
    else :
        camelCaseWord += i
        #print(camelCaseWord) # for testing code

print (camelCaseWord)

# trying to branch on git