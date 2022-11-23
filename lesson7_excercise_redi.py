#Count the occurrences of the word ‘redi’ in the phrase: "ReDI school is awesome! Yes redi is really cool"
# a) Cut the sentence into two on the character ! Output the first part in lower case and the second part in uppercase
# b) ask the user what word to search for 
# c) give the starting position of the searched word

redi_string = "     ReDI school is awesome! Yes redi is really cool        "
sub_string = "REDI"

# convert string to lowercase
temp_str = redi_string.lower()

# use count function
count = temp_str.count(sub_string.lower())
print("The REDI count is:", count)

# cut the string into 2 pieces
length_of_word=len(redi_string)
half_the_length=int(length_of_word/2)

ex_mark_position=redi_string.find('!')
first_half=redi_string[0:ex_mark_position]
second_half=redi_string[ex_mark_position+1:length_of_word]

print(first_half.strip().lower())
print(second_half.strip().upper())
