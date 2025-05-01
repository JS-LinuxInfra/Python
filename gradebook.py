#Last semister gradebook 2D list
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

#Subjects list
subjects = ["physics", "calculus", "poetry", "history"]

#Grades list
grades = [98, 97, 85, 88]

#Gradebook 2D list
gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]

#Full gradebook empty list to be populated later
full_gradebook = []

#Change CS grade
gradebook.append(["computer science", 100])

#Change VA grade
gradebook.append(["visual arts", 93])

#Update score for CS
gradebook[5][1] = 98

#Remove numerical grade for VA
gradebook[2].remove(85)

#Add pass/fail to Poetry
gradebook[2] = ["Poetry", "Pass"]

#Populate full gradebook with other two gradebook lists
full_gradebook = last_semester_gradebook + gradebook

#Print and validate the results
print(full_gradebook)
