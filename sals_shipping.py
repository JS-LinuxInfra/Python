#Weight numerator
weight = 41.5

#Premium Shipping Flat Rate Charge
premium_ground_shipping = 125

#Ground Shipping Rate Calculator
if weight <= 2:
 print(1.50 * weight + 20)
elif weight <= 6:
 print(3.00 * weight + 20)
elif weight <= 10:
 print(4 * weight + 20)
else:
 print(4.75 * weight + 20) 

#Prints out reminder on the flat rate for premium shipping
print("Premium ground shipping costs $",premium_ground_shipping)

#Drone Shipping Rate Calculator
if weight <= 2:
 print(4.50 * weight)
elif weight <= 6:
 print(9.00 * weight)
elif weight <= 10:
 print(12 * weight)
else:
 print(14.25 * weight) 

Output:
217.125
Premium ground shipping costs $ 125
591.375
