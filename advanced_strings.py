#Defines a function that takes two string inputs
def username_generator(first_name, last_name):
#Defines a VAR that slices the first three letters of the first string and slices the first four letters of the second string
  user_name = first_name[:3] + last_name[:4]
#Returns the username variable concatenating the slices for both of the strings
  return user_name
#Prints the output of slicing and concatenating both strings in the function to the terminal
print(username_generator("Abe", "Simpson"))

#Defines a function that takes one string input
def password_generator(user_name):
#Defines a VAR that shifts the position of each letter in the username over by one to the right, returning the final letter to the front of the string
  password1 = f"{user_name[-1]}{user_name[:-1]}"
#Defines a VAR that shifts the position of each letter in the username over by one to the left, returning the first letter to the end of the string
  password2 = f"{user_name[1:]}{user_name[0]}"
#Returns each updated password variable with the above defined slices
  return password1,password2
#Defines each VAR from the function so each string is printed on it's own line on the terminal instead of being returned in a tuple
password1,password2 = password_generator("AbeSimp")
#Prints the outputs of both VARS returned in the function on their own line as a string instead of the default behavior of being returned as a tuple
print(password1)
print(password2)
