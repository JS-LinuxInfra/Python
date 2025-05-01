#Modify via insertion and removal customer data list
customer_data = [["Ainsley", "Small", True], ["Ben", "Large", False], ["Chani", "Medium", True], ["Depak", "Medium", False]]
customer_data[1].remove(False)
customer_data[2][2] = False
#Print updated customer data
customer_data_final = customer_data + [["Amit", "Large", True], ["Karim", "X-Large", False]]
print(customer_data_final)
