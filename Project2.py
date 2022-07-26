import random
print("Numbers that aren't evenly divisible by 5 or 7")
counter = 0
while counter < 10:
    #Get a random number
    number = random.randint(1,999)
    if number % 7 == 0 or number % 5 == 0:
        #If it's evenly divisible by 5 or 7, bail out.
        continue
    else:
        #Otherwise, print it and keep going for a while.
        print(number)
    # Increment the loop counter.
    counter += 1
print("Loop is done")