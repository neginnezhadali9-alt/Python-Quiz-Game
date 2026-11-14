print("Welcome to Quiz Game!")
print("Let's test your knowledge")

questions = [
    "what is the capital of France?",
    "Which planet is known as the Red Planet?",
    "Which force opposes the motion of an aircraft through the air?",
    "What is the layer between troposphere and stratosphere called?",
    "What is a variable in Python?"
]

options = [
    ["A) London", "B) Paris", "C) Berlin", "D) Rome"],
    ["A) Earth", "B) Venus", "C) Mars", "D) Jupiter"],
    ["A) Lift", "B) Weight", "C) Drag", "D) Thrust"],
    ["A) Tropopause", "B) Ionosphere", "C) Stratosphere", "D) Atmosphere"],
    ["A) A function", "B) A named storage for a value", "C) A loop", "D) A module"]
]

correct_answer = ["B", "C", "C", "A", "B"]

score = 0
i = 0
while i < len(questions):
    print("Question", i + 1)
    print(questions[i])

    j = 0
    while j < len(options[i]):
        print(options[i][j])
        j = j + 1

    answer = input("Enter your answer: ")

    if answer == correct_answer[i]:
        score = score + 1
        print("Correct answer!")
    else:
        print("Wrong answer!")

    i = i + 1

print("Final score:", score)

percentage = (score / 5) * 100
print("Percentage:", percentage, "%")

if percentage == 100:
    print("Excellent!")
elif percentage >= 50:
    print("Good job!")
else:
    print("Keep practicing!")



