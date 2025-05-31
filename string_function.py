#Define the function, passing a string as an argument, use a counter and for loop to increment through the word
def get_length(Seattle):
  counter = 0
  for l in Seattle:
    counter += 1
  return counter
#Print the output of the function, passing the string to function and printing the total number of letters
print(get_length("Seattle"))
