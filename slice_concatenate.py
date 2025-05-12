#Define variables
first_name = "Julie"
last_name = "Blevins"

#Create function that concatenates the first three letters of each variable
def account_generator(first_name,last_name):
  return(first_name[:3] + last_name[:3])

#Define new variable which takes the result of the function then prints to the terminal
new_account = account_generator(first_name,last_name)
print(new_account)
