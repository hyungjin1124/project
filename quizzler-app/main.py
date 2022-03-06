from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

# get question and correct_answer from data.py
question_bank = [Question(data["question"], data["correct_answer"]) for data in question_data]

# create quiz brain object
quiz = QuizBrain(question_bank)
# create quiz interface object
quiz_interface = QuizInterface(quiz)
