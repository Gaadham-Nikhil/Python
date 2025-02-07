import json

#creating 4 variables to explain how a json file save data in it.
name = input("enter value as name ") 
place = input("enter value as place ")
animal = input("enter value as animal ")
thing  = input("enter value as thing ")

# How a json saves an list or an object
enum = [{'name': name, 'place': place,'animal': animal, 'thing': thing}]

#printing it in the form of a formatted string
for index, enum in enumerate(enum, start=1):
    print(f"{index} {name} - {place} - {animal} - {thing}")