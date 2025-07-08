# python quiz game

# Stores 5 quiz questions in a tuple
questions = (' What is the correct way to print "Hello, World!"" in Python?', 
             " Which of the following is used to define a function in Python? ", 
             " What is the output of print(3 + 2 * 2)?", 
             " Which data type is mutable in Python?", 
             " How do you comment a single line in Python?")

#Stores answer choices (A-E) for each question in a nested tuple (a list inside a list).
options = (("A.print(Hello, World!) ", 'B.echo "Hello, World!" ', 'C. printf("Hello, World!") ', 'D. console.log("Hello, World!")', 'E.  System.out.println("Hello, World!")'),
           ("A. def", "B.function ", "C.define ", "D.func ", "E.fn "),
           ("A. 10 ", "B. 7 ", "C.12 ", "D. 5 ", "E. Error "),
           ("A. int ", "B.  str", "C. tuple", "D. list", "E. bool"),
           ("A. // This is a comment", "B. # This is a comment ", "C.  /* This is a comment */", "D. <!-- This is a comment --> ", "E. ''' This is a comment ''' "))

answers = ("A", "A", "B", "D", "B") #Stores the correct answers in ord
guesses = []  # Stores the user's answers
score = 0 #Counts how many answers are correct.
question_num = 0 ## Tracks current question (0 = first question)

for question in questions: # Prints the question and its multiple-choice options (A-E).
    print("-----------------")
    print (question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter (A, B, C, D): ").upper() #Asks the user to pick A, B, C, D, or E.
    guesses.append(guess) # Saves the guess


    if guess == answers[question_num]:  #If the guess matches the correct answer, it adds 1 point to score
            score += 1
            print("CORRECT!")
    else:
         print("INCORRECT!")
         print(f"{answers[question_num]} is the correct answer ") #If wrong, it shows the correct answer.

    question_num += 1 #Increases question_num so the next question loads.

print("-----------------")
print("     RESULT      ")
print("-----------------")


print("answer:  ", end="") #Shows all correct answers 
for answer in answers:
     print(answer,end=" ")
print()

print("guesses: ", end="") #Shows all user guesses
for guess in guesses:
     print(guess,end=" ")
print()

score = int(score / len(questions) * 100) #Calculates percentage score
print(f"Your score is: {score}%")