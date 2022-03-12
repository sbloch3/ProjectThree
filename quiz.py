'''
Created on Mar 11, 2022

@author: ITAUser
'''
#Today I will be coding basic high school trivia
#The objective is to correctly write each section and make it run correctly for
#someone to use. This will be written by Sarah Bloch


#Make a variable called score to keep track of the correct answers. And set
#it to 0.
score = 0

#Ask the user question one. And store the users answer.
print("1. What is the powerhouse of the cell?")
print("A) mitochondria")
print("B) nucleus")
print("C) ribosome")
ans1 = input()

#Check if the answer is correct, if it is add one to score and print out
#"Correct"
#Else, print out "Incorrect, the correct answer is A."
if ans1 == "a":
    print("correct")
    score = score + 1
else:
    print("incorrect, the answer is a")
print("score", score)

#Ask the user question two. And store the users answer.
print("2. How many states compromise the United States?")
print("A) 13")
print("B) 45")
print("C) 50")
ans2 = input()

#Check if the answer is correct, if it is add one to score and print out
#"Correct"
#Else, print out "Incorrect, the correct answer is C."
if ans2 == "c":
    print("correct")
    score = score + 1
else:
    print("incorrect, the answer is c")
print("score", score)

#Ask the user question three. And store the users answer.
print(" In y = mx + b, what does m stand for?")
print("A) slope")
print("B) output")
print("C) I don't understand math")
ans3 = input()

#Check if the answer is correct, if it is add one to score and print out
#"Correct"
#Else, print out "Incorrect, the correct answer is A."
if ans3 == "a":
    print("correct")
    score = score + 1
else:
    print("incorrect, the answer is a")
print("score:", score)    
 
#Ask the user question four. And store the users answer.
print("In English, a person, place or thing is called:")
print("A) verb")
print("B)adjective")
print("C) noun")
ans4 = input()

#Check if the answer is correct, if it is add one to score and print out
#"Correct"
#Else, print out "Incorrect, the correct answer is C."
if ans4 == "c":
    print("correct")
    score = score + 1
else:
    print("incorrect, the answer is c")
print("score", score)


#Calculate the percentage the user got. And store it in a variable called p
p = score/4 * 100

#Print out the users score: "You got a [score]/4. Or a [p]%."
print("You got a", score,"/4. Or a", p,"%.")