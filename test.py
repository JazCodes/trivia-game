print('welcome to a simple trivia game')
print('you will answer 5 questions, each question will get you 1 point')


questions = ["What is always coming, but never arrives?",
			 "What is it that lives if it is fed, and dies if you give it a drink?",
			 "What can one catch that is not thrown?"]

answers = ["tomorrow",
		   "fire",
		   "cold"]


corrAns = []
wrongAns = []
score = 0
wrongScore = 0

for question in questions:
	print(question)

	yourAns = input("YOUR ANSWER: ")
	print()

	if yourAns in answers:
		corrAns.append(question)
		score += 1
	else:
		wrongAns.append(question)
		wrongScore += 1

for each in corrAns:
	print()
	print("YOUR ANSWER WAS CORRECT FOR QUESTION :", each)

for fail in wrongAns:
	print("YOUR ANSWER WAS INCORRECT FOR QUESTION :", fail)

print ("YOUR TOTAL SCORE :", score)
