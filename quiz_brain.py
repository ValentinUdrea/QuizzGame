#asking the user for then next question
#checking if the answer was correct
#checking if we are at the end of the quiz

class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0


    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else: False

    def next_question(self):
        current_question = self.question_list[self.question_number]#and quastion_number is the index that will be used from de dictionary
        self.question_number += 1


    def check_answer(self):
        check_answer = self.question_list[self.question_number]

        choice = input(f"Q.{self.question_number} {check_answer.text} (True/False): ")
        if choice == check_answer.answer:
            self.score += 1
            print("You got it right!")
        else:
            print("You got it wrong")
        print(f"The answer is {check_answer.answer}")
        print(f"Your current scoore is: {self.score}/{self.question_number}")
        print("\n")


