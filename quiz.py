print("Python Practice Quiz")

playing = input ("Start? ")

if playing != "yes":
    quit()

print("Let's play")
score = 0

answer = input("Is the ocean blue? ")
if answer == "no":
    print('false')
else:
    print('true')
    score += 1

answer = input("What does GPU stand for?")
if answer == "graphics processing unit":
    print('Correct')
    score += 1
else:
    print('Incorrect')

answer = input("What does RAM stand for?")
if answer == "random access memory":
    print('Correct')
    score += 1
else:
    print('Incorrect')

answer = input("What does CPU stand for?")
if answer == "central processing unit":
    print('Correct')
    score += 1
else:
    print('Incorrect')

print("You got " + str(score) + " questions correct.")









