#Imports random number 
import random

#random number generator
random_number = random.randint(1, 10)

#Answer to question
if random_number == 1:
 print("Yes - definetly")
elif random_number == 2:
 print("It is decidedly so")
elif random_number == 3:
 print("Without a doubt")
elif random_number == 4:
 print("reply hazy, try again")
elif random_number == 5:
 print("Ask again later")
elif random_number == 6:
 print("Better not tell you now")
elif random_number == 7:
 print("My sources say no")
elif random_number == 8:
 print("Outlook not so good")
elif random_number == 9:
 print("Very doubtful")
elif random_number == 10:
 print("Highly likely")
#else:
 # print("Error")

#Name of the person asking the question
name = "Justin"

#What is the question
question = ""

#answer
answer = ""

#User asks a question and the magic eight ball answers
#if name == "":
# print(question)
# print("Magic 8-Ball's answer:")
#else: 
# print(name, "asks", question)
# print("Magic 8-Ball's answer:")
if question == "":
 print(name)
 print("Please ask a question.")
else:
 print(name, "asks", question)
 print("Magic 8-Ball's answer:", answer)

Output:
My sources say no
Justin
Please ask a question.
