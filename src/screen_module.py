import tkinter as tk
import tkinter.font as tf


root = tk.Tk()

sub_label_frame = tk.Frame(root,
                           width=960,
                           height=40,
                           bg="#ffffff",
                           relief=tk.FLAT,
                           )
sub_label1 = tk.Label(sub_label_frame,
                      text="「トランプを3枚出してその積を103で割った余りの値の元素をいかに早く言うか」",
                      font=('游ゴシック', 8, 'bold'),
                      bg="#ffffff",
                      foreground="#000000"
                      )

sub_label2 = tk.Label(sub_label_frame,
                      text="Python Version",
                      font=('游ゴシック', 8, 'bold'),
                      bg="#ffffff",
                      foreground="#000000"
                      )

title_frame = tk.Frame(root,
                       width=960,
                       height=350,
                       bg="#343434",
                       relief=tk.FLAT,
                       )


title1 = "トランプを3枚出してその積を103で割った余りの値の"
title_label1 = tk.Label(title_frame,
                        text=title1,
                        font=('游ゴシック', 28, 'bold'),
                        bg="#343434",
                        foreground="#ffffff"
                        )

title2 = "元素をいかに早く言うか"
title_label2 = tk.Label(title_frame,
                        text=title2,
                        font=('游ゴシック', 28, 'bold'),
                        bg="#343434",
                        foreground="#ffffff"
                        )

title_label3 = tk.Label(title_frame,
                        text="Spaceキーを押すまたはクリックしてスタート",
                        font=('游ゴシック', 16, 'bold'),
                        bg="#343434",
                        foreground="#ffffff"
                        )

rule_frame = tk.Frame(root,
                      width=960,
                      height=180,
                      bg="#ffffff",
                      relief=tk.FLAT,
                      )

rule1 = tk.Label(rule_frame,
                 text="◆ ルール説明",
                 font=('游ゴシック', 20, 'bold'),
                 bg="#ffffff",
                 foreground="#000000"
                 )

rule2 = tk.Label(rule_frame,
                 text="1. 画面に出現する3つの数字の積を計算してください.",
                 font=('游ゴシック', 16, 'bold'),
                 bg="#ffffff"
                 )

rule3 = tk.Label(rule_frame,
                 text="2. その値を103で割った余りを計算してください.",
                 font=('游ゴシック', 16, 'bold'),
                 bg="#ffffff"
                 )

rule4 = tk.Label(rule_frame,
                 text="3. その値を原子番号とみて該当する元素を記入しEnterを押してください(元素記号のみ).",
                 font=('游ゴシック', 16, 'bold'),
                 bg="#ffffff"
                 )

credit_frame = tk.Frame(root,
                        width=960,
                        height=140,
                        bg="#ffffff",
                        relief=tk.FLAT,
                        )

credit1 = tk.Label(credit_frame,
                   text="◆ アプリ製作者",
                   font=('游ゴシック', 20, 'bold'),
                   bg="#ffffff"
                   )

credit2 = tk.Label(credit_frame,
                   text="Thike",
                   font=('游ゴシック', 16, 'bold'),
                   bg="#ffffff"
                   )

credit3 = tk.Label(credit_frame,
                   text="◆ 本家様",
                   font=('游ゴシック', 20, 'bold'),
                   bg="#ffffff"
                   )

url_font = tf.Font(underline=True, size=16)
credit4 = tk.Label(credit_frame,
                   text=title1 + title2,
                   cursor="hand2",
                   font=url_font,
                   bg="#ffffff",
                   fg="blue"
                   )

move_frame = tk.Frame(root,
                      width=960,
                      height=150,
                      bg="#ffffff",
                      relief=tk.RIDGE,
                      )

input_element = tk.Entry(move_frame,
                         font=('游ゴシック', 20, 'bold'),
                         state='readonly'
                         )

count_label = tk.Label(move_frame,
                       text=str(0) + "/17",
                       font=('源の角ゴシック', 14, 'bold'),
                       bg="#ffffff",
                       foreground="#000000"
                       )

time_label = tk.Label(move_frame,
                      text="",
                      font=('游ゴシック', 18, 'bold'),
                      bg="#ffffff",
                      foreground="#000000"
                      )

reset = tk.Button(move_frame,
                  text="RESET",
                  font=('游ゴシック', 18, 'bold'),
                  bg="#343434",
                  foreground="#ffffff"
                  )

back_to_start = tk.Button(move_frame,
                          text="← TITLE",
                          font=('游ゴシック', 18, 'bold'),
                          bg="#343434",
                          foreground="#ffffff"
                          )

game_frame = tk.Frame(root,
                      width=960,
                      height=350,
                      bg="#343434",
                      relief=tk.FLAT,
                      )

show_number1 = tk.Frame(game_frame,
                        width=220,
                        height=250,
                        bg="#ffffff",
                        relief=tk.RIDGE,
                        )

show_number2 = tk.Frame(game_frame,
                        width=220,
                        height=250,
                        bg="#ffffff",
                        relief=tk.RIDGE,
                        )

show_number3 = tk.Frame(game_frame,
                        width=220,
                        height=250,
                        bg="#ffffff",
                        relief=tk.RIDGE,
                        )

message = tk.Label(game_frame,
                   text="暇だったんだね･･･",
                   font=('游ゴシック', 36, 'bold'),
                   bg="#343434",
                   foreground="#ffffff"
                   )

number1 = tk.Label(show_number1,
                   text="10",
                   font=('游ゴシック', 50, 'bold'),
                   bg="#ffffff",
                   foreground="#000000"
                   )

number2 = tk.Label(show_number2,
                   text="10",
                   font=('游ゴシック', 50, 'bold'),
                   bg="#ffffff",
                   foreground="#000000"
                   )

number3 = tk.Label(show_number3,
                   text="10",
                   font=('游ゴシック', 50, 'bold'),
                   bg="#ffffff",
                   foreground="#000000"
                   )
