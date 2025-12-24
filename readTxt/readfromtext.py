import random

file = open('testFile.txt', 'r')
read = file.readlines()
modified = []

for line in read:
    modified.append(line.strip())

print (random.choice(modified))