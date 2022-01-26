#ACC COSC 1336
#Lab 8.1 
#Lucero Huayhua

#This programs tells you the number of uppercase,
#lowercase, digits, and spaces
#that the text.txt file contains

def main():
    #open file to read content
    infile = open('text.txt','r')
    data = infile.read()
    #create variables to hold the count of each item
    upper_count=0
    lower_count=0
    digit_count=0
    space_count=0

#function to count each item
    for ch in data:
        if ch.isupper():
            upper_count += 1
        if ch.islower():
            lower_count += 1
        if ch.isdigit():
            digit_count += 1
        if ch.isspace():
            space_count += 1
    #display the number of each item
    print('The number of uppercase letters is  '+ str(upper_count))
    print('The number of lowercase letters is  '+ str(lower_count))
    print('The number of uppercase letters is  '+ str(digit_count))
    print('The number of uppercase letters is  '+ str(space_count))

main()
