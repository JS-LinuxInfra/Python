#Defines two variables
first_name = "Reiko"
last_name = "Matsuki"

#Create function, concatenate last three characters of first and last name, print the result
def password_generator(first_name,last_name):
  return first_name[2:] + last_name[4:]

#Creates new variable, assigns results of the function concatenation and prints the results to the terminal
temp_password = password_generator(first_name,last_name)
print(temp_password)
