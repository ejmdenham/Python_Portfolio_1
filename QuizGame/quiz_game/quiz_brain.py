class QuizBrain:
    def __init__(self, q_list):
        self.list = q_list
        self.score = 0

    def next_question(self):
        for num, i in enumerate(self.list, 1):
            answer = input(f"\nQ{num}: {i.text} (True/False)?: ")
            if answer.lower() == i.answer.lower():
                self.score += 1
                print("You got it right!")
            else:
                print(f"Wrong! The correct answer was: {i.answer}")
            print(f"Your current score is: {self.score}/{num}")
        else:
            print("\ngame_over!")
            print(f"Your final score was: {self.score}/{num}! ({round(self.score/num,2)})")
