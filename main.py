from tkinter import *
from tkinter import messagebox
from article import article_list
import random
timer = None
FONT = "MS UI Gothic"

TITLECOLOR = "#31112C"
ARTICLECOLOR = "#0A1D37"

class TypeSpeed():
    def __init__(self):
        #____parameters_________#
        self.window = Tk()
        self.window.title("Typing Speed Test")
        self.window.minsize(width=700, height=450)
        self.window.config(padx=40, pady=10)
        #self.window.wm_attributes('-transparentcolor', self.window['bg'])
        self.background_image = PhotoImage(file="logo.png")
        self.background_label = Label(image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        #____board______#
        self.game_setting()

    def game_setting(self):
        self.count = 60
        self.count_time()
        self.produce_article()
        self.text_area()


    def count_time(self):
        self.show_time = Label(text=f"Left {self.count} sec", font=(FONT, 14, "bold"), fg="#F54748")
        self.show_time.grid(row=0, column=1,sticky="e")


    def produce_article(self):
        self.paragraph = random.choice(article_list)
        self.canvas = Canvas(width=650, height=250, highlightthickness=0)
        self.articlelabel = Label(text=f"Article:", font=(FONT, 14, "bold"), fg=TITLECOLOR)
        self.articlelabel.place(x=2, y=30)
        self.article = self.canvas.create_text(325, 125, text=f"{self.paragraph}", fill=ARTICLECOLOR,font=(FONT, 14), width=650)
        self.canvas.grid(row=1, column=0, columnspan=2)

    def text_area(self):
        self.typelabel = Label(text=f"Typing Area:",font=(FONT, 14, "bold"), fg=TITLECOLOR)
        self.typelabel.grid(row=2, column=0,sticky="w")
        self.text = Text(width=90, height=8)
        self.text.insert(END, "Put cursor in text area and enter to start test.")
        self.text.grid(row=3, column=0, columnspan=2)
        self.window.bind("<Return>", self.start_game)

    def start_game(self, e):
        self.count_down(e)
        self.text.delete(1.0, END)


    def count_down(self, e):
        global timer
        if self.count > 0:
            timer = self.window.after(1000, self.count_down, self.count-1)
            self.count -= 1
            self.show_time.config(text=f"Left {self.count} sec")
        else:
            self.window.after_cancel(timer)
            self.show_result()

    def show_result(self):
        compare_list = self.paragraph.lower().split(" ")
        typing = self.text.get(1.0, "end").lower()
        typing_lst = [word.strip() for word in typing.split(" ") if word != ""]

        wrong_words = 0
        if typing.strip() == "":
            typing_lst = []
        else:
            for i in range(len(typing_lst)):
                if typing_lst[i] != compare_list[i]:
                    wrong_words += 1

        message = f"Your Gross WPM is {len(typing_lst)}\n"
        if wrong_words > 0:
            message += f"but with {wrong_words} wrong words"
        messagebox.showinfo("Typing Test Result", message)
        self.window.destroy()
        self.__init__()


if __name__ == "__main__":
    type_test = TypeSpeed()
    type_test.window.mainloop()