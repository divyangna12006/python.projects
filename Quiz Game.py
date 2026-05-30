score = 0

print("Welcome to the Python Quiz!\n")

answer = input("1. What is the capital of India? ")
if answer.lower() == "new delhi":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is New Delhi.")

answer = input("\n2. How many continents are there on Earth? ")
if answer == "7":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is 7.")

answer = input("\n3. Which programming language are you learning? ")
if answer.lower() == "python":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is Python.")

answer = input("\n4. What is 5 + 3? ")
if answer == "8":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is 8.")

answer = input("\n5. Which planet is known as the Red Planet? ")
if answer.lower() == "mars":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is Mars.")

print("\nQuiz Finished!")
print("Your Score:", score, "/ 5")

if score == 5:
    print("Excellent!")
elif score >= 3:
    print("Good Job!")
else:
    print("Keep Practicing!")