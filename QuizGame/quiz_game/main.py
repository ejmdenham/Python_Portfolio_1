from question_model import Question
from data import question_data as qd
from quiz_brain import QuizBrain

question_bank = []
for element in qd:
    question_bank.append(Question(element["question"], element["correct_answer"]))

quiz = QuizBrain(question_bank)

quiz.next_question()
