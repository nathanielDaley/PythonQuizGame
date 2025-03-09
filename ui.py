import tkinter
from tkinter import *

THEME_COLOR = "#375362"
QUESTION_FONT = ("Arial", 20, "italic")

class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.score_text = Label(text="Score: 0", background=THEME_COLOR, fg="white")
        self.score_text.grid(column=1, row=0)

        self.question_canvas = Canvas(width=300, height=250, highlightthickness=0, background="white")
        self.question_canvas_text = self.question_canvas.create_text(150, 125, text="test",
                                                                     font=QUESTION_FONT, fill=THEME_COLOR)
        self.question_canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_button_image = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_button_image, highlightthickness=0)
        self.true_button.grid(column=0, row=2)

        false_button_image = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_button_image, highlightthickness=0)
        self.false_button.grid(column=1, row=2)



        self.window.mainloop()