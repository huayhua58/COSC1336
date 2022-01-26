#ACC COSC 1336
#Lab 3
#Lucero Huayhua
#This program determines the dollar amount of a discount of the individual package price
#based on the total number of packages purchased at Geekware Software
#and displays the new total amount of the purchase after the discount, if any, is applied

#get individual package price from user
package_price = int (input ('Enter the package price:'))

#get number of items purchased from user
quantity_purchased = int(input ('Enter the number of packages purchased:'))

#Discount based on quantity of items purchased
if quantity_purchased < 10:
    discount = 0;
elif 10 <= quantity_purchased and quantity_purchased <20:
    discount = 0.10  #10% discount
elif 20 <= quantity_purchased and quantity_purchased <50:
    discount = .20 #20% discount
elif 50 <= quantity_purchased and quantity_purchased <100:
    discount = .30 #30% discount
else:
    discount = .40   #40% discount                      

#calculate discount amount and determine new total amount
subtotal = quantity_purchased * package_price
discount_amount = discount * subtotal
total_amount = subtotal - discount_amount

#display the discount amount received and the new total amount of purchase
print (format('\nDiscount Amount:'), '$', format (discount_amount, ',.2f'))
print (format('\nTotal Amount:'),'$', format(total_amount, ',.2f'))



    

                            
                            
