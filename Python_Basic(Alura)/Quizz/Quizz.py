print("Welcome to The Quizz!")

playing = input("Wanna play?")
score = 0
qnt = 0

if playing.lower() != "yes" :
    quit()

print("Okay! Let's play: ")

answer = input("What does CPU stand for? ")
qnt += 1
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
qnt += 1
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ")
qnt += 1
if answer.lower() == "power supply unity" or "power supply":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
qnt += 1
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does SSD stand for? ")
qnt += 1
if answer.lower() == "solid-state drive" or "solid state drive":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does DDR stand for? ")
qnt += 1
if answer.lower() == "double data rate":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does HDD stand for? ")
qnt += 1
if answer.lower() == "hard disk drive":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does USB stand for? ")
qnt += 1
if answer.lower() == "universal serial bus":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("you got " + str(score) + " answers correct out of " + str(qnt))





