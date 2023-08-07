import tkinter as tk
import screen_module as sm
import datetime
import sqlite3
import time
import random

startTime = 0
clearTime = 0
qCount = 0
number = list(range(1, 53))
answer = 1
conn = sqlite3.connect('element.db')
cursor = conn.cursor()


def gameToStart(self):
    sm.inputElement["state"] = tk.NORMAL
    sm.inputElement.configure(fg="black")
    sm.inputElement.delete(0, tk.END)
    sm.inputElement["state"] = "readonly"

    sm.secondFrame.pack_forget()
    sm.moveFrame.pack_forget()
    sm.ruleFrame.pack_forget()
    sm.creditFrame.pack_forget()

    sm.titleFrame.pack(pady=0)
    sm.moveFrame.pack(pady=10)
    sm.ruleFrame.pack(pady=0)
    sm.creditFrame.pack(pady=0)

    sm.reset.place_forget()
    sm.timeLabel.place_forget()
    sm.backToStart.place_forget()

    sm.showNumber1.pack_forget()
    sm.showNumber2.pack_forget()
    sm.showNumber3.pack_forget()

    reset(self)


def startToGame(self):
    global startTime
    sm.inputElement["state"] = tk.NORMAL
    sm.inputElement.focus_set()

    sm.titleFrame.pack_forget()
    sm.moveFrame.pack_forget()
    sm.ruleFrame.pack_forget()
    sm.creditFrame.pack_forget()

    sm.secondFrame.pack(pady=0)
    sm.moveFrame.pack(pady=10)
    sm.ruleFrame.pack(pady=0)
    sm.creditFrame.pack(pady=0)

    sm.reset.place(x=720, y=100)
    sm.message.place_forget()
    sm.showNumber1.pack(side=tk.LEFT, padx=50, pady=20, ipady=30)
    sm.showNumber2.pack(side=tk.LEFT, padx=50, pady=20, ipady=30)
    sm.showNumber3.pack(side=tk.LEFT, padx=50, pady=20, ipady=30)

    random.shuffle(number)
    questionCounter(self)
    selectNumber(self)
    startTime = datetime.datetime.now()


def gameToClear(self):
    global startTime, clearTime
    sm.inputElement["state"] = "readonly"
    sm.inputElement.configure(fg="#c0c0c0")
    sm.timeLabel.place(x=420, y=60)
    playTime = (str(clearTime - startTime)[:-3])
    sm.timeLabel["text"] = playTime

    sm.ruleFrame.pack_forget()
    sm.creditFrame.pack_forget()
    sm.showNumber1.pack_forget()
    sm.showNumber2.pack_forget()
    sm.showNumber3.pack_forget()
    sm.message.place(x=310, y=130)
    sm.reset.place_forget()
    sm.backToStart.place(x=700, y=100)


def clearToStart(self):
    sm.inputElement["state"] = tk.NORMAL
    sm.inputElement.configure(fg="black")
    sm.inputElement.delete(0, tk.END)
    sm.inputElement["state"] = "readonly"

    sm.secondFrame.pack_forget()
    sm.moveFrame.pack_forget()

    sm.titleFrame.pack(pady=0)
    sm.moveFrame.pack(pady=10)
    sm.ruleFrame.pack(pady=0)
    sm.creditFrame.pack(pady=0)

    sm.timeLabel.place_forget()
    sm.backToStart.place_forget()

    reset(self)


def selectNumber(self):
    global number, answer
    selectThreeNumber = number[0:3]
    number = number[3:]
    pos = [0]*3
    product = 1

    for i in range(3):
        product = product * (selectThreeNumber[i] % 13 + 1)
        if (selectThreeNumber[i] % 13 + 1) < 10:
            pos[i] = 20

    answer = product % 103
    sm.number1.place(x=70 + pos[0], y=105)
    sm.number2.place(x=70 + pos[1], y=105)
    sm.number3.place(x=70 + pos[2], y=105)
    sm.number1["text"] = str(selectThreeNumber[0] % 13 + 1)
    sm.number2["text"] = str(selectThreeNumber[1] % 13 + 1)
    sm.number3["text"] = str(selectThreeNumber[2] % 13 + 1)


def questionCounter(self):
    global qCount
    qCount = qCount + 1
    sm.countLabel["text"] = str(qCount) + "/17"


def reset(self):
    global qCount, number
    qCount = 0
    sm.countLabel["text"] = str(qCount) + "/17"
    number = list(range(1, 53))


def judge(self):
    global qCount, clearTime
    response = sm.inputElement.get()
    cursor.execute("select * from periodic where id=" + str(answer))
    ansElement = cursor.fetchone()[1]
    if response == ansElement:
        if qCount < 17:
            questionCounter(self)
            selectNumber(self)
        else:
            clearTime = datetime.datetime.now()
            gameToClear(self)
    else:
        sm.inputElement.configure(fg="red")
        sm.inputElement.update()
        time.sleep(0.3)
        sm.inputElement.configure(fg="black")

    sm.inputElement.delete(0, tk.END)
