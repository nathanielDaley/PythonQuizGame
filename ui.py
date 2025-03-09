import tkinter
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
QUESTION_FONT = ("Arial", 20, "italic")

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.score_text = Label(text="Score: 0", background=THEME_COLOR, fg="white")
        self.score_text.grid(column=1, row=0)

        self.question_canvas = Canvas(width=300, height=250, highlightthickness=0, background="white")
        self.question_canvas_text = self.question_canvas.create_text(150, 125, width=280, text="test",
                                                                     font=QUESTION_FONT, fill=THEME_COLOR)
        self.question_canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_button_image = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_button_image, highlightthickness=0, command=self.submit_true)
        self.true_button.grid(column=0, row=2)

        false_button_image = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_button_image, highlightthickness=0, command=self.submit_false)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.question_canvas.config(background="white")
        self.score_text.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            question_text = self.quiz.next_question()
            self.question_canvas.itemconfigure(self.question_canvas_text, text=question_text)
        else:
            self.question_canvas.itemconfigure(self.question_canvas_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def submit_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def submit_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.question_canvas.config(background="green")
        else:
            self.question_canvas.config(background="red")
        self.window.after(1000, self.get_next_question)
