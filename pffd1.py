#The textfile, travel_plans.txt, contains the summer travel plans for someone with
#some commentary. Find the total number of characters in the file and save to the variable num.

plans = open("travel_plans.txt","r")
travel = plans.read()
num = 0

for ch in travel:
    num = num + 1

print(num)
plans.close()


#We have provided a file called emotion_words.txt that contains lines of words
#that describe emotions. Find the total number of words in the file and assign
#this value to the variable num_words.

emotion = open("emotion_words.txt","r")
words = emotion.read()
new_words =words.strip().split()
num_words = 0

for ch in new_words:
    num_words = num_words + 1

print(num_words)
emotion.close()

#Assign to the variable num_lines the number of lines in the file school_prompt.txt.

school = open("school_prompt.txt","r")
lines= school.readlines()
num_lines = 0

for ln in lines:
    num_lines = num_lines + 1

print(num_lines)
school.close()

#Assign the first 30 characters of school_prompt.txt as a string to the variable
# beginning_chars.


place = open("school_prompt.txt","r")
school = place.read(30)
beginning_chars = ""

for ch in school:
    beginning_chars = beginning_chars + ch

print(beginning_chars)
place.close()

#Challenge: Using the file school_prompt.txt, assign the third word of every
#line to a list called three.

school = open("school_prompt.txt","r")
lines = school.readlines()
three = []
for ln in lines:
    new_s = ln.split()
    for ch in new_s[2:3]:
        three.append(ch)

print(three)
school.close()

#Challenge: Create a list called emotions that contains the first word of every
#line in emotion_words.txt.


book = open("emotion_words.txt","r")
words = book.readlines()
emotions = []

for ln in words:
    frst = ln.split()
    for ch in frst[:1]:
        emotions.append(ch)

print(emotions)

book.close()

#Assign the first 33 characters from the textfile, travel_plans.txt to the
#variable first_chars.


travel = open("travel_plans.txt","r")
place = travel.read(33)
first_chars = ""

for ch in place:
    first_chars = first_chars + ch

print(first_chars)
travel.close()

#Challenge: Using the file school_prompt.txt, if the character ‘p’ is in a word,
#then add the word to a list called p_words.

highs = open("school_prompt.txt","r")
school = highs.read().split()
p_words = []

for ch in school:
    if "p" in ch:
        p_words.append(ch)

print(p_words)


highs.close()
