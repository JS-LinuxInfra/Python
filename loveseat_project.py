#This is a description of a Loveseat that is for sale
lovely_loveseat_description = """
Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.
"""
#This is the set price for the Loveseat
lovely_loveseat_price = 254.00

#This is the description of a Settee that is for sale
stylish_settee_description = """
Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.
"""
#This is the set price for the Settee
stylish_settee_price = 180.50

#This is the description of a Lamp that is for sale
luxurious_lamp_description = """
Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.
"""
#This is the set price for the Lamp
luxurious_lamp_price = 52.15

#This allows calculation of sales tax
sales_tax = .088

#Customer one spend
customer_one_total = lovely_loveseat_price + luxurious_lamp_price
customer_one_tax = customer_one_total * sales_tax
customer_one_total += customer_one_tax

#Customer one purchases
customer_one_itemization = "Lovely Loveseat," + " " + "Luxurious Lamp"

#This will calculate the sales tax due
customer_one_tax = customer_one_total * sales_tax

#This will print out the receipt
print("Customer One Items")
print(customer_one_itemization)
print("Customer One Total:")
print(customer_one_total)

Output:
Customer One Items
Lovely Loveseat, Luxurious Lamp
Customer One Total:
333.09119999999996
