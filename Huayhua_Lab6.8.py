#ACC COSC 1336
#Lab 6.8
#Lucero Huayhua

#This program reads a file 
#displayes random numbers generated
#displays the total of the numbers
#and the number of random numbers read from the file

#function to display numbers, determine number count in file
#and add all numbers

def display_numbers(file_to_read):
    random_num_file = open(file_to_read,'r')

    #declare variable to accumulate all numbers 
    total = 0
    #declare variable to store number of random numbers
    num_random_num = 0
    #read the first line and store number
    line = random_num_file.readline()

    #wcondition to execute when line contains numbers
    while line != "":
        num_random_num += 1
        random_num = int(line)
        total += random_num
        print(random_num)
        line = random_num_file.readline()

    #display total count, sum total of numbers
    print ('\nThe total of all the numbers in the file is ' + str(total)+\
           '\nThere are ' + str(num_random_num) + \
           ' numbers in the file')

def main():
    display_numbers('random_numbers.txt')


main()
        

    
