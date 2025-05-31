#Create function that takes two arguments and checks if the smaller string is in the larger string.
def contains(big_string,little_string):
  if little_string in big_string:
    return True
  else:
    return False
#Check and print the output on if the little string is in the larger string and return a boolean value as the result to the terminal.
print("melon" in "watermelon")
print("berry" in "watermelon")
