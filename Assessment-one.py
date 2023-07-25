sentences = ['This is a HP Laptop.', 'HIIT is located in Wuse Zone 6.', 
             'I attend Nile University of Nigeria.','I made the most delicious Cinnamon Rolls on Sunday evening.']
def longest_sentence(sentences):
    return max(sentences, key = len)
print('The longest sentence is: ')
print(longest_sentence(sentences))

random_stuff = ['London', '15000', '345.678', '445', 'Riyadh', 'Madinah']
alphabetic_strings = []

def new_list(alphabets):
    for i in alphabets:
        if i.isalpha():
            alphabetic_strings.append(i)
new_list(random_stuff)
print(alphabetic_strings)

#OR

random_stuff = ['London', '15000', '345.678', '445', 'Riyadh', 'Madinah']
def new_list(words):
    return[value for value in words if value.isalpha()]
print(new_list(random_stuff))