from flask import Flask, request
from flask import render_template

app = Flask(__name__)


Questions=[]

@app.route('/')
def homepage():
	questions = ["What is always coming, but never arrives?",
			     "What is it that lives if it is fed, and dies if you give it a drink?",
			     "What can one catch that is not thrown?"]
	answers = ["Tomorrow",
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
		return render_template('homepage.html', questions=questions, yourAns=yourAns , answers=answers, score=score, wrongScore=wrongScore)
		return render_template('homepage.html')

# @app.route('/q_2')
# def q_2():

# 	return render_template('q_2.html')

# @app.route('/q_3')
# def q_3():

# 	return render_template('q_3.html')

# @app.route('/q_4')
# def q_4():

# 	return render_template('q_4.html')

# @app.route('/q_5')
# def q_5():

# 	return render_template('q_5.html')

# @app.route('/gameover')
# def gameover():

# 	return render_template('gameover.html')




if __name__ == '__main__':
    app.run()
