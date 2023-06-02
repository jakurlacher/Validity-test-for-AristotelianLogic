#This program tests the validity of a syllogism as according to the star test
#In Introduction to Logic, 2nd Edition by Gensler.

#Enter an Aristotelian syllogism from the command prompt after aristotle.py
#Convert words as follows: all == a, some === s, no == ~, is ==,
#is not == n, #therefore == t
#If no specifying words are presented on the left hand side, default to 'all'
#Example: A is B translates to all A is B
#Represent variables as capital letters

#EXAMPLE

#Syllogism:
#All A* is B
#No B* is C*
#Therefore no A is C

#Command prompt: aristotle.py aAB ~BC t~AC



import sys

class Variable:
    def __init__(self, name, star_value, position):
        self.name = name
        self.star_value = star_value
        self.position = position


count = 0
right_hand_star_value_counter = 0
starred_variables = []
unstarred_variables = []

for line in sys.argv:
    count += 1 #Exclude the words running the program
    if(count == 1):
        continue

    list_of_letters = []
    for letter in line:
        if letter.isupper():
            list_of_letters.append(letter)

    if len(list_of_letters) != 2 :
        print('Improper input')
        continue

    #Therefore ...
    if count == len(sys.argv):
        if line[0] != 't':
            print('Last line does not start with t')
            quit
        else:
            #Left hand side
            if line[1] == 'a' or line[1].isupper() or line[1] == '~':
                first_variable = Variable(list_of_letters[0], 0, 0 )
            elif line[1] == 's':
                first_variable = Variable(list_of_letters[0], 1, 0)
            #Right hand side
            if 'n' in line:
                if line[1] == '~':
                    second_variable = Variable(list_of_letters[1], 1, 1)
                else:
                    second_variable = Variable(list_of_letters[1], 0, 1)
            else:
                if line[1] == '~':
                    second_variable = Variable(list_of_letters[1], 0, 1)
                else:
                    second_variable = Variable(list_of_letters[1], 1, 1)




    else:
    #Premises
    #Left hand side
        if line[0] == 'a' or line[0].isupper() or line[0] == '~':
            first_variable = Variable(list_of_letters[0], 1, 0 )
        elif line[0] == 's':
            first_variable = Variable(list_of_letters[0], 0, 0)

        #Right hand side
        if 'n' in line:
            if line[0] == '~':
                second_variable = Variable(list_of_letters[1], 0, 1)
            else:
                second_variable = Variable(list_of_letters[1], 1, 1)
        else:
            if line[0] == '~':
                second_variable = Variable(list_of_letters[1], 1, 1)
            else:
                second_variable = Variable(list_of_letters[1], 0, 1)

    print(first_variable.name, first_variable.star_value, first_variable.position)
    print(second_variable.name, second_variable.star_value, second_variable.position)


    #if pass starred once test
    if first_variable.star_value == 1 :
        starred_variables.append(first_variable.name)

    if second_variable.star_value == 1 :
        starred_variables.append(second_variable.name)
        #right hand star test
        right_hand_star_value_counter += 1

    #starred only once test
    if first_variable.star_value == 0 :
        unstarred_variables.append(first_variable.name)
    if second_variable.star_value == 0 :
        unstarred_variables.append(second_variable.name)
#EVALUATION OF VALIDITY
#2 parts to determine if valid or invalid: Each variable must be starred
#once and exactly once, and there must be one and only one variable
#starred on the right hand side.

#Determine if each variable is starred once and only once:
pass_starred_once = 0
if len(starred_variables) == len(set(starred_variables)):
    pass_starred_once = 1

pass_only_once = 1
for variable in unstarred_variables:
    if variable not in starred_variables:
        pass_only_once = 0

print('starred once test: ' + str(pass_starred_once))
#Determine if one and only one variable is starred on the right hand side:
pass_right_hand_side_test = 0
if right_hand_star_value_counter == 1:
    pass_right_hand_side_test = 1

print('right hand side test: ' + str(pass_right_hand_side_test))
if pass_right_hand_side_test == 1 and pass_starred_once == 1 and pass_only_once == 1:
    print('valid')
else:
    print('invalid')
