import random
import math

# Grabs number of dice to roll
number_of_die = int(input("How many PCs are making this check? "))

# Finds the number of rolls needed to pass for indexing later
checkindex = math.ceil(number_of_die/2)
print ("Minimum PC's needed to pass is", checkindex)

# Gathers the related ability mods for the PCs
mods = []
for i in range(0,number_of_die):
    print("Mod for PC",i,":")
    ele = int(input())
    mods.append(ele)

# Gets the DC for the check to compare against later
dc = int(input("What is the DC of the check? "))

# Sample array and sample modded array to confirm that mod adding works as intended
sample_array = []
modded_array = []
sample_elements = 0
while sample_elements < number_of_die:
    roll = int(random.random()*20+1)
    sample_array.append(roll)
    modded_array.append(roll+mods[sample_elements])
    sample_elements += 1

print("Sample array without mods added:")
for x in sample_array:
    print(x)
print("Sample array with mods added:")
for x in modded_array:
    print(x)


# Sets up a baseline number of successes and trials that will be divided against each other to find the odds of success
successes = 0
trials = 0

# Loops through a process of creating an arrate with the randomly generated d20 rolls plus their corresponding ability mods, sorts them in descending order, then checks to see if the bottom of the top half of the rolls is higher than the DC. If so, it will add to the successes.
while trials < 10**6:
    temp_array = []
    temp_elements = 0
    while temp_elements < number_of_die:
        temp_array.append(int(random.random()*20+1)+mods[temp_elements])
        temp_elements += 1
    temp_array.sort(reverse=True)
    if temp_array[checkindex-1] >= dc:
        successes +=1
    trials += 1

# Takes the successes divided by the total number of trials and converts it to a percentage with two decimal places
odds = str(round(float(successes/trials*100),2)) + "%"

print("Successes:",successes,"Trials:",trials)

print ("For a DC",dc,"group check, there is roughly a",odds,"chance of passing.")