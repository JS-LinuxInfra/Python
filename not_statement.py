#Define boolean values and map to variable
statement_one = False
statement_two = True
#Define variables
credits = 120
gpa = 1.8
#Create not statements and print to the terminal
if not credits >= 120:
  print("You do not have enough credits to graduate.")

if not gpa >= 2.0:
  print("Your GPA is not high enough to graduate.")

if not (credits >= 120) and not (gpa >= 2.0):
  print("You do not meet either requirement to graduate!")
