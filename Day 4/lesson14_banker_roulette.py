names = names_string.split(", ")
# The code above converts the input into an array seperating
#each name in the input by a comma and space.
# 🚨 Don't change the code above 👆

import random
# Get the total number of items in list.
num_items = len(names)
# Generate random numbers between 0 and the last index.
random_choices = random.randint(0, num_items - 1)
# Pick out random person from list of names using the random number.
person_who_will_pay = names[random_choices]

print(person_who_will_pay + ' is going to buy the meal today!')

