import tkinter as tk
import screen_module as sm
import datetime
import numpy as np
import sqlite3
import time

startTime = 0
clearTime = 0
qCount = 0
number = np.array(range(52), dtype='int64') + 1
answer = 1
conn = sqlite3.connect('element.db')
cursor = conn.cursor()


def gameToStart(self):
    sm.inputElement.delete(0, tk.END)
    sm.inputElement["state"] = "readonly"

    sm.secondFrame.pack_forget()
    sm.firstFrame.pack(pady=40)
    sm.titleLabel1.place(x=25, y=60)
    sm.titleLabel2.place(x=270, y=120)
    sm.titleLabel3.place(x=380, y=260)

    sm.reset.place_forget()

    sm.showNumber1.place_forget()
    sm.showNumber2.place_forget()
    sm.showNumber3.place_forget()
    sm.number1.place_forget()
    sm.number2.place_forget()
    sm.number3.place_forget()

    reset(self)


def startToGame(self):
    global startTime
    sm.inputElement["state"] = tk.NORMAL
    sm.firstFrame.pack_forget()

    sm.secondFrame.pack(pady=40)
    sm.titleLabel1.place_forget()
    sm.titleLabel2.place_forget()
    sm.titleLabel3.place_forget()
    sm.reset.place(x=1200, y=535)

    sm.showNumber1.place(x=50, y=25)
    sm.showNumber2.place(x=370, y=25)
    sm.showNumber3.place(x=690, y=25)

    np.random.shuffle(number)
    questionCounter(self)
    selectNumber(self)
    startTime = datetime.datetime.now()


def gameToClear(self):
    global startTime, clearTime
    sm.inputElement.delete(0, tk.END)
    sm.inputElement["state"] = "readonly"
    sm.timeLabel.place(x=890, y=460)
    playTime = (str(clearTime - startTime)[:-3])
    sm.timeLabel["text"] = playTime
    sm.rule1.place_forget()
    sm.rule2.place_forget()
    sm.rule3.place_forget()
    sm.rule4.place_forget()

    sm.reset.place_forget()
    sm.backToStart.place(x=1200, y=535)

    sm.credit1.place_forget()
    sm.credit2.place_forget()
    sm.credit3.place_forget()
    sm.credit4.place_forget()


def clearToStart(self):
    sm.secondFrame.pack_forget()
    sm.timeLabel.place_forget()

    sm.firstFrame.pack(pady=40)
    sm.titleLabel1.place(x=25, y=60)
    sm.titleLabel2.place(x=270, y=120)
    sm.titleLabel3.place(x=380, y=260)

    sm.rule1.place(x=480, y=650)
    sm.rule2.place(x=480, y=700)
    sm.rule3.place(x=480, y=740)
    sm.rule4.place(x=480, y=780)

    sm.backToStart.place_forget()

    sm.credit1.place(x=480, y=840)
    sm.credit2.place(x=700, y=845)
    sm.credit3.place(x=480, y=900)
    sm.credit4.place(x=700, y=905)

    reset(self)


def selectNumber(self):
    global number, answer
    selectThreeNumber = number[0:3]
    number = number[3:]
    pos = np.zeros(3)
    product = 1

    for i in range(3):
        product = product * (selectThreeNumber[i] % 13 + 1)
        if (selectThreeNumber[i] % 13 + 1) < 10:
            pos[i] = 20

    answer = product % 103
    sm.number1.place(x=70 + pos[0], y=100)
    sm.number2.place(x=70 + pos[1], y=100)
    sm.number3.place(x=70 + pos[2], y=100)
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
    number = np.array(range(52), dtype='int64') + 1


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
