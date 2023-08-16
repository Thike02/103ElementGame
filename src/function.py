import tkinter as tk
import screen_module as sm
import datetime
import sqlite3
import time
import random
import sys
import os

pass_time = ["0"]*18
reserve_question = [0]*51
ans_element = ["0"]*17
q_count = 0
number = list(range(1, 53))
answer = 1
conn = sqlite3.connect('element.db')
cursor = conn.cursor()
MAX = 17
DIVNUM = 103
record_frame = tk.Frame(sm.root,
                        width=960,
                        height=420,
                        bg="#ffffff",
                        relief=tk.FLAT,
                        )


def get_absolute_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(os.path.dirname(sys.argv[0]))

    return os.path.join(base_path, relative_path)


def game_to_start(self):
    sm.input_element["state"] = tk.NORMAL
    sm.input_element.configure(fg="black")
    sm.input_element.delete(0, tk.END)
    sm.input_element["state"] = "readonly"

    sm.game_frame.pack_forget()
    sm.move_frame.pack_forget()
    sm.rule_frame.pack_forget()
    sm.credit_frame.pack_forget()
    children_widget = record_frame.winfo_children()
    for child in children_widget:
        child.destroy()
    record_frame.pack_forget()

    sm.title_frame.pack(pady=0)
    sm.move_frame.pack(pady=10)
    sm.rule_frame.pack(pady=0)
    sm.credit_frame.pack(pady=0)

    sm.title_label1.focus_set()
    sm.reset.place_forget()
    sm.time_label.place_forget()
    sm.back_to_start.place_forget()

    sm.show_number1.pack_forget()
    sm.show_number2.pack_forget()
    sm.show_number3.pack_forget()

    reset(self)


def start_to_game(self):
    global pass_time
    sm.input_element["state"] = tk.NORMAL
    sm.input_element.focus_set()

    sm.title_frame.pack_forget()
    sm.move_frame.pack_forget()
    sm.rule_frame.pack_forget()
    sm.credit_frame.pack_forget()

    sm.game_frame.pack(pady=0)
    sm.move_frame.pack(pady=10)
    sm.rule_frame.pack(pady=0)
    sm.credit_frame.pack(pady=0)

    sm.reset.place(x=720, y=100)
    sm.message.place_forget()
    sm.show_number1.pack(side=tk.LEFT, padx=50, pady=20, ipady=30)
    sm.show_number2.pack(side=tk.LEFT, padx=50, pady=20, ipady=30)
    sm.show_number3.pack(side=tk.LEFT, padx=50, pady=20, ipady=30)

    random.shuffle(number)
    pass_time[0] = datetime.datetime.now()
    question_counter(self)
    select_number(self)


def game_to_clear(self):
    global pass_time, reserve_question
    sm.input_element["state"] = "readonly"
    sm.input_element.configure(fg="#c0c0c0")
    sm.time_label.place(x=420, y=60)
    play_time = (str(pass_time[17] - pass_time[0])[:-3])
    sm.time_label["text"] = play_time

    sm.rule_frame.pack_forget()
    sm.credit_frame.pack_forget()
    sm.show_number1.pack_forget()
    sm.show_number2.pack_forget()
    sm.show_number3.pack_forget()
    sm.reset.place_forget()

    record_frame.pack(pady=0)
    show_each_clear_time(self)
    sm.message.place(x=310, y=130)
    sm.back_to_start.place(x=700, y=100)


def clear_to_start(self):
    global record_frame
    sm.input_element["state"] = tk.NORMAL
    sm.input_element.configure(fg="black")
    sm.input_element.delete(0, tk.END)
    sm.input_element["state"] = "readonly"

    sm.game_frame.pack_forget()
    sm.move_frame.pack_forget()
    children_widget = record_frame.winfo_children()
    for child in children_widget:
        child.destroy()
    record_frame.pack_forget()
    sm.time_label.place_forget()
    sm.back_to_start.place_forget()

    sm.title_frame.pack(pady=0)
    sm.move_frame.pack(pady=10)
    sm.rule_frame.pack(pady=0)
    sm.credit_frame.pack(pady=0)

    sm.title_label1.focus_set()

    reset(self)


def select_number(self):
    global number, answer, reserve_question, q_count
    select_three_number = number[0:3]

    number = number[3:]
    pos = [0]*3
    product = 1

    for i in range(3):
        select_three_number[i] = select_three_number[i] % 13 + 1
        reserve_question[3 * (q_count - 1) + i] = (select_three_number[i])

        product = product * (select_three_number[i])
        if (select_three_number[i]) < 10:
            pos[i] = 20

    answer = product % DIVNUM
    sm.number1.place(x=70 + pos[0], y=105)
    sm.number2.place(x=70 + pos[1], y=105)
    sm.number3.place(x=70 + pos[2], y=105)
    sm.number1["text"] = str(select_three_number[0])
    sm.number2["text"] = str(select_three_number[1])
    sm.number3["text"] = str(select_three_number[2])


def question_counter(self):
    global q_count
    q_count = q_count + 1
    sm.count_label["text"] = str(q_count) + "/17"


def reset(self):
    global q_count, number
    q_count = 0
    sm.count_label["text"] = str(q_count) + "/17"
    number = list(range(1, 53))


def judge(self):
    global q_count, pass_time, ans_element
    response = sm.input_element.get()
    cursor.execute("select * from periodic where id=" + str(answer))
    ans_element[q_count - 1] = cursor.fetchone()[1]
    if response == ans_element[q_count - 1]:
        pass_time[q_count] = datetime.datetime.now()
        if q_count < MAX:
            question_counter(self)
            select_number(self)
        else:
            game_to_clear(self)
    else:
        sm.input_element.configure(fg="red")
        sm.input_element.update()
        time.sleep(0.3)
        sm.input_element.configure(fg="black")

    sm.input_element.delete(0, tk.END)


def show_each_clear_time(self):
    for i in range(17):
        index = i + 1
        show_q_num = "Q" + str(index) + ": "
        show_q = "(" + (str(reserve_question[3 * i]) + ","
                        + str(reserve_question[3 * i + 1])
                        + ","
                        + str(reserve_question[3 * i + 2])
                        + ")  ")

        show_time = (str(pass_time[i + 1] - pass_time[i])[:-3])
        record1 = tk.Label(record_frame,
                           text=show_q_num,
                           font=('游ゴシック', 20, 'bold'),
                           bg="#ffffff",
                           foreground="#000000",
                           anchor=tk.W
                           )

        record2 = tk.Label(record_frame,
                           text="{}".format(show_q),
                           font=('游ゴシック', 20, 'bold'),
                           bg="#ffffff",
                           foreground="#000000",
                           anchor=tk.W
                           )

        record3 = tk.Label(record_frame,
                           text=ans_element[i],
                           font=('游ゴシック', 20, 'bold'),
                           bg="#ffffff",
                           foreground="#000000",
                           anchor=tk.W
                           )

        record4 = tk.Label(record_frame,
                           text=show_time,
                           font=('游ゴシック', 20, 'bold'),
                           bg="#ffffff",
                           foreground="#000000",
                           anchor=tk.W
                           )

        if i < 9:
            record1.place(x=10, y=30 + 40 * i)
            record2.place(x=80, y=30 + 40 * i)
            record3.place(x=230, y=30 + 40 * i)
            record4.place(x=290, y=30 + 40 * i)
        else:
            record1.place(x=490, y=30 + 40 * (i - 9))
            record2.place(x=560, y=30 + 40 * (i - 9))
            record3.place(x=710, y=30 + 40 * (i - 9))
            record4.place(x=770, y=30 + 40 * (i - 9))
