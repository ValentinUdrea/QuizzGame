from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
question_bank = []
for question in question_data:
    question_text = question["text"]#tapping into the text keys of the dictionaries
    question_answer = question["answer"]#tapping into the values of the dictionaries
    new_question = Question(question_text,question_answer)#and i can access the the keys and the values throw variables
    question_bank.append(new_question)#we add each dictionary item in the list

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
    quiz.check_answer()
print("You've completed the quiz")
print(f"Your final score is: {quiz.score}/{len(question_bank)}")




