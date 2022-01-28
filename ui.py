from tkinter import Tk
from tkinter import Canvas
from tkinter import Button
from tkinter import Label
from tkinter import PhotoImage
from tkinter import messagebox
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface():
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(
            width=300,
            height=250,
            highlightthickness=0
        )
        self.canvas.config(bg="white", highlightthickness=0)
        self.q_box = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Question",
            font=("Arial", 20, "italic"))
        self.score = Label(
            text="Score: 0",
            bg=THEME_COLOR,
            fg="white",
            font=("Arial", 12, "bold")
            )
        t_img = PhotoImage(file="images/true.png")
        f_img = PhotoImage(file="images/false.png")
        self.t_button = Button(
            image=t_img,
            highlightthickness=0,
            command=self.true_selected
            )
        self.f_button = Button(
            image=f_img,
            highlightthickness=0,
            command=self.false_selected
            )

        self.score.grid(column=1, row=0)
        self.canvas.grid(column=0, row=1, columnspan=2,
                         pady=50)
        self.t_button.grid(column=0, row=2)
        self.f_button.grid(column=1, row=2)

        self.get_next_question()

        self.update_score_box()

        self.window.mainloop()

    def update_score_box(self):
        self.score.config(text=f"Score: {self.quiz.score}")

    def get_next_question(self):
        self.canvas.config(bg="white")
        question = self.quiz.next_question()
        self.canvas.itemconfigure(self.q_box, text=question)

    def true_selected(self):
        self.get_feedback(self.quiz.check_answer("True"))

    def false_selected(self):
        self.get_feedback(self.quiz.check_answer("false"))

    def get_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        if self.quiz.question_number < 10:
            self.window.after(1000, self.get_next_question)
            self.window.after(100, self.update_score_box)
        else:
            self.window.after(1000, self.update_score_box)
            messagebox.showinfo(title="You Finished",
                                message=f"You got {self.quiz.score}"
                                f" out of {self.quiz.question_number} correct")
