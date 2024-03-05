print("Welcome to my computer game!")

playing = input("Do you want to play?  ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play:)")
score = 0

answer = input("Which language this code is has been wrote? \n ")
if answer.lower() == "python":
    print('correct')
    score +=1
else:
    print("Incorrect")

answer = input("what does CPU stand for? \n ")
if answer.lower() == "central processing unit":
    print('correct')
    score +=1
else:
    print("Incorrect")

answer = input("what does GPU stand for? \n ")
if answer.lower() == "graphic processing unit":
    print('correct')
    score +=1
else:
    print("Incorrect")

answer = input("what does RAM stand for? \n ")
if answer.lower() == "random access":
    print('correct')
    score +=1
else:
    print("Incorrect")

print("You got " + str(score) + " question correct!")
print("You got " + str((score /4) *100) + " %.")