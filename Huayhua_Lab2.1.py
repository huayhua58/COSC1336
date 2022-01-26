#Lucero Huayhua
#Complete
#This program tells you how much sugar,butter,flour cups you'll need to make your desired amount of cookies

#assign a value to each measuring variable
sugar_48_cookies= 1.5 #cups
butter_48_cookies= 1 #cup
flour_48_cookies= 2.75 #cup

#ask user how many cookies they want to make
num_cookies=int(input('How many cookies would you like to make?'))

#calculate total cups needed for said amount
sugar_needed= (sugar_48_cookies/48)*num_cookies
butter_needed= (butter_48_cookies/48)*num_cookies
flour_needed= (flour_48_cookies/48)*num_cookies

#display the ingredients needed based on said amount cookies desired
print('To make',num_cookies, 'cookies, you will need:')
print(format(sugar_needed,'.2f'),'cups of sugar')
print(format(butter_needed,'.2f'),'cups of butter')
print(format(flour_needed,'.2f'),'cups of flour')
