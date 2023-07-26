def reverse_word(word : str):
    return word[::-1]

def is_palindrome(word):
    if word[::-1] == word:
        return True
    else:
        return False

print(is_palindrome('level'))
print(reverse_word('Hello'))

words = ['Cake', 'Croissant', 'Beignet', 'Panettone', 'Eclair']
def new_list(reversed_words):
    return[value[::-1] for value in reversed_words ]
print(new_list(words))

score_list = [93, 66, 78, 40, 87]
def grade_average(score):
    for i in score_list:
        if i >= 90:
          print('Your grade is A, Excellent result!')
        elif i >= 80:
            print('Your grade is B, Very Good!')
        elif i >= 70:
                print('Your grade is C, Good but put in more effort. ')
        elif i >= 60:  
                print('Your grade is D, you need to work harder!')
        else:
                print('Your grade is F, Sorry you have failed!')
(grade_average(score_list))