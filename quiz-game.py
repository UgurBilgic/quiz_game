print("Welcome to my quiz game")

playing = input("Do you want to play?\n")

if playing.lower() != "yes":
    print("See you then, goodbye :(")
    quit()

score = 0

answer = input("What is the capital of TURKEY\n")
if answer.lower() == "ankara":
    print("Correct!")
    score += 1
else:
    print("Incorrect")
    
answer = input("What is the capital of USA\n")
if answer.lower() == "washington":
    print("Correct!")
    score += 1
else:
    print("Incorrect")
    
answer = input("What is the capital of UK\n")
if answer.lower() == "london":
    print("Correct!")
    score += 1
else:
    print("Incorrect")
    
answer = input("What is the capital of GERMANY\n")
if answer.lower() == "berlin":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

print("You have answered " + str(score) + " question(s) correctly.")
print("You got %" + str((score / 4) * 100) + " success percentage")

