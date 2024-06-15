from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class Quizinterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="score:0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.quest_text = self.canvas.create_text(150, 125, width=280,
                                                  text="question",
                                                  font=("Arial", 20, "italic"),
                                                  fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.img1 = PhotoImage(file="images/true.png")
        self.button1 = Button(image=self.img1, highlightthickness=0, command=self.right)
        self.button1.grid(row=2, column=0)

        self.img2 = PhotoImage(file="images/false.png")
        self.button2 = Button(image=self.img2, highlightthickness=0, command=self.wrong)
        self.button2.grid(row=2, column=1)

        self.next_question()

        self.window.mainloop()

    def next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score_label.config(text=f"Score:{self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.quest_text, text=q_text)
        else:
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.quest_text,
                                   text="you have reached to the end of the quiz.")
            self.button1.config(state="disabled")
            self.button2.config(state="disabled")

    def right(self):
        is_right = self.quiz.check_answer("True")
        self.feedback(is_right)

    def wrong(self):
        is_right = self.quiz.check_answer("False")
        self.feedback(is_right)

    def feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, func=self.next_question)
