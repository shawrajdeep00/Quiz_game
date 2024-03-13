print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("In which year first quantum computer (2-qubit) was created? ")
if answer.lower() == "1998":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Who is the father of quantum computing? ")
if answer.lower() == "David Deutsch":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What do we call the pieces of information in a quantum computer? ")
if answer.lower() == "Qubits":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("When the information is between 0 and 1 in a quantum computer, what do we call this? ")
if answer.lower() == "Superposition":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")


answer = input("Quantum computers are very good at dealing with_____ ")
if answer.lower() == "Uncertainty":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")