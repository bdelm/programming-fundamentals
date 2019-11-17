import sys

inputted_string = sys.argv[1]

vowels = {'a','e','u','i','o','y'}

counter = 0

for char in inputted_string:
    if char.lower() in vowels:
        counter += 1

print(inputted_string + ' contains ' + str(counter) + ' vowels')


