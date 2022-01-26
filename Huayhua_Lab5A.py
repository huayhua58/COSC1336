#ACC COSC 1336
#Lab 5A
#Lucero Huayhua

#This program asks the user for five test scores
#uses the average of the test scores
#to determine a letter grade based on average number
#displays average and its corresponding letter grade


#get five test scores, calculates the average,
#and average is passed to determine_grade function
def main():
    #loop checks that each score is in range 1-100
    #user will enter score again if number is outside of range
    
    score_1=float(input('Enter score #1 in range 1-100: '))
    while score_1 <= 0 or score_1 >= 101:
        print ('Error: Scores must be between 1 and 100')
        score_1=float(input('Enter score #1 in range 1-100: '))

    score_2=float(input('Enter score #2 in range 1-100: '))
    while score_2 <= 0 or score_2 >= 101:
        print ('Error: Scores must be between 1 and 100')
        score_2=float(input('Enter score #2 in range 1-100: '))
        
    score_3=float(input('Enter score #3 in range 1-100: '))
    while score_3 <= 0 or score_3 >= 101:
        print ('Error: Scores must be between 1 and 100')
        score_3=float(input('Enter score #3 in range 1-100: '))

    score_4=float(input('Enter score #4 in range 1-100: '))
    while score_4 <= 0 or score_4 >= 101:
        print ('Error: Scores must be between 1 and 100')
        score_4=float(input('Enter score #4 in range 1-100: '))
        
    score_5=float(input('Enter score #5 in range 1-100: '))
    while score_5 <= 0 or score_5 >= 101:
        print ('Error: Scores must be between 1 and 100')
        score_5=float(input('Enter score #5 in range 1-100: '))

    #calculates the average of scores entered
    #determine_grade function accepts the numeric average
    average = (score_1+score_2+score_3+score_4+score_5)/5
    determine_grade(average)

#uses numeric average to assign different letter grades
#displays average and letter grade
def determine_grade(average):
    if average < 60:
        letter_grade= "F"
    elif average < 70:
        letter_grade = "D"
    elif average < 80:
        letter_grade= "C"
    elif average < 90:
        letter_grade = "B"
    else:
        letter_grade = "A"
        
    print('Your average is:', format(average, ',.2f'),', which is a(n)',letter_grade)

main()
