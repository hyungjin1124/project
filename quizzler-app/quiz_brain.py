import html

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        """"If there's a quiz that hasn't been given, return true."""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """Give the next quiz."""
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        # unescape question text by using html module
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text} (True/False): "

    def check_answer(self, user_answer):
        """If the user's answer is correct, add 1 point."""
        # get correct_answer
        correct_answer = self.current_question.answer
        # if the user guessed correctly,
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False

