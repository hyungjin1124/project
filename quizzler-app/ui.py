from re import L
from tkinter import *
from quiz_brain import QuizBrain

CANVAS_FONT = ('Arial', 15, 'italic')
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        # create window
        self.quiz = quiz
        self.window = Tk()
        self.window.title('Quizzler')
        
        # set background color
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        # create score
        self.score_label = Label(text=f'Score: 0', bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        # create canvas
        self.canvas = Canvas(height=250, width=300, bg='white')
        self.question_text = self.canvas.create_text(150, 125, width=280, font=CANVAS_FONT)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # create false/true button
        true_img = PhotoImage(file='quizzler-app/images/true.png')
        self.true_btn = Button(self.window, image=true_img, highlightthickness=0, borderwidth=0, command=self.true_pressed)
        self.true_btn.grid(row=2, column=0)

        false_img = PhotoImage(file='quizzler-app/images/false.png')
        self.false_btn = Button(self.window, image=false_img, highlightthickness = 0, borderwidth=0, command=self.false_pressed)
        self.false_btn.grid(row=2, column=1)
        
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        """If there are any questions left, move on to the next question, and if not, end the quiz."""
        self.canvas.configure(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.configure(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def true_pressed(self):
        """when user press the true button, give feedback"""
        self.give_feedback(self.quiz.check_answer('true'))

    def false_pressed(self):
        """when user press the false button, give feedback"""
        self.give_feedback(self.quiz.check_answer('false'))

    def give_feedback(self, is_right):
        """if user's answer is right, change canvas's baground color to green.
        if not, change to red. And go to next_question."""
        if is_right:
            self.canvas.configure(bg='green')
        else:
            self.canvas.configure(bg='red')
            
        self.window.after(1000, self.get_next_question)

