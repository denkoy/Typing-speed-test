from tkinter import *
import random
from words import Words

def return_key_event(self):
    if self.text.get() == self.line1.cget('text') and self.remaining<=0:
        words=Words()
        new_string = random.choice(words.list) + " " + random.choice(words.list) + " " + random.choice(
            words.list) + " " + random.choice(words.list) + " " + random.choice(words.list)

        self.line1.config(text=self.line2.cget("text"))
        self.line2.config(text=new_string)
        speed=1000-self.timer_remaining
        print(self.timer_remaining)
        value=float(60/speed*5)
        self.values.append(value)
        wpm=sum(self.values)/len(self.values)
        self.speed.config(text=f"{round(wpm,2)} WPM")
        self.restart_timer=True
        self.text.delete(0, END)
class Buttons:
    def __init__(self):
        words=Words()
        string_one = random.choice(words.list) + " " + random.choice(words.list) + " " + random.choice(words.list) + " " + random.choice(words.list) + " " + random.choice(words.list)
        string_two = random.choice(words.list) + " " + random.choice(words.list) + " " + random.choice(words.list) + " " + random.choice(words.list) + " " + random.choice(words.list)
        self.line1 = Label(text=string_one, font=("Arial", 20, "bold"), bg="white", fg="green")
        self.line1.place(relx = 0.5, y=50, anchor = CENTER)
        self.line2 = Label(text=string_two, font=("Arial", 20, "bold"), bg="white", fg="green")
        self.line2.place(relx=0.5, y=100, anchor=CENTER)
        self.rules = Label(text="write line by line and click enter when you're ready. hf.", font=("Arial", 15, "bold"), bg="white", fg="red")
        self.rules.place(relx=0.5, y=150, anchor=CENTER)


        self.text=Entry(width=50)
        self.text.place(relx = 0.25, y=310)
        self.text.bind('<Return>', lambda event:return_key_event(self))

        self.start = Button(text="Start", command=lambda: self.countdown(5))
        self.start.place(x=310, y=380)
        self.start_timer = Label(text='', font=("Arial", 20, "bold"), bg="white", fg="green")
        self.start_timer.place(x=320, y=430)
        self.speed = Label(text='0.00 WPM', font=("Arial", 20, "bold"), bg="white", fg="green")
        self.speed.place(x=270, y=260)
        self.flag=0
        self.restart_timer=False
        self.values=[]
    def countdown(self, remaining=None):

        if self.flag==0:
            self.game_timer(1010)
            self.restart_timer=True
            self.flag=1
        if remaining is not None:
            self.remaining = remaining

        if self.remaining <= 0:
            self.start_timer.configure(text="Start!")
            self.start_timer.place(x=290, y=430)
            self.text.delete(0, END)
        else:
            self.start_timer.configure(text="%d" % self.remaining)
            self.remaining = self.remaining - 1
            self.start_timer.after(1000, self.countdown)


    def game_timer(self,remaining=None):
        if remaining is not None and self.restart_timer is False:
            self.timer_remaining = remaining
        if self.restart_timer is True:
            self.timer_remaining = 1000
            self.restart_timer=False
        self.timer_remaining = self.timer_remaining - 1
        self.start_timer.after(1000, self.game_timer)