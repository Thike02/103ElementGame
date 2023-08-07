import tkinter as tk
import tkinter.font as tf


root = tk.Tk()

subLabelFrame = tk.Frame(root,
                         width=960,
                         height=40,
                         bg="#ffffff",
                         relief=tk.FLAT,
                         )
subLabel1 = tk.Label(subLabelFrame,
                     text="「トランプを3枚出してその積を103で割った余りの値の元素をいかに早く言うか」",
                     font=('游ゴシック', 8, 'bold'),
                     bg="#ffffff",
                     foreground="#000000"
                     )

subLabel2 = tk.Label(subLabelFrame,
                     text="Python Version",
                     font=('游ゴシック', 8, 'bold'),
                     bg="#ffffff",
                     foreground="#000000"
                     )

titleFrame = tk.Frame(root,
                      width=960,
                      height=350,
                      bg="#343434",
                      relief=tk.FLAT,
                      )

secondFrame = tk.Frame(root,
                       width=960,
                       height=350,
                       bg="#343434",
                       relief=tk.FLAT,
                       )

title1 = "トランプを3枚出してその積を103で割った余りの値の"
titleLabel1 = tk.Label(titleFrame,
                       text=title1,
                       font=('游ゴシック', 28, 'bold'),
                       bg="#343434",
                       foreground="#ffffff"
                       )

title2 = "元素をいかに早く言うか"
titleLabel2 = tk.Label(titleFrame,
                       text=title2,
                       font=('游ゴシック', 28, 'bold'),
                       bg="#343434",
                       foreground="#ffffff"
                       )

titleLabel3 = tk.Label(titleFrame,
                       text="クリックしてスタート",
                       font=('游ゴシック', 16, 'bold'),
                       bg="#343434",
                       foreground="#ffffff"
                       )

ruleFrame = tk.Frame(root,
                     width=960,
                     height=180,
                     bg="#ffffff",
                     relief=tk.FLAT,
                     )

rule1 = tk.Label(ruleFrame,
                 text="◆ ルール説明",
                 font=('游ゴシック', 20, 'bold'),
                 bg="#ffffff",
                 foreground="#000000"
                 )

rule2 = tk.Label(ruleFrame,
                 text="1. 画面に出現する3つの数字の積を計算してください.",
                 font=('游ゴシック', 16, 'bold'),
                 bg="#ffffff"
                 )

rule3 = tk.Label(ruleFrame,
                 text="2. その値を103で割った余りを計算してください.",
                 font=('游ゴシック', 16, 'bold'),
                 bg="#ffffff"
                 )

rule4 = tk.Label(ruleFrame,
                 text="3. その値を原子番号とみて該当する元素を記入しEnterを押してください(元素記号のみ).",
                 font=('游ゴシック', 16, 'bold'),
                 bg="#ffffff"
                 )

creditFrame = tk.Frame(root,
                       width=960,
                       height=140,
                       bg="#ffffff",
                       relief=tk.FLAT,
                       )

credit1 = tk.Label(creditFrame,
                   text="◆ アプリ製作者",
                   font=('游ゴシック', 20, 'bold'),
                   bg="#ffffff"
                   )

credit2 = tk.Label(creditFrame,
                   text="Thike",
                   font=('游ゴシック', 16, 'bold'),
                   bg="#ffffff"
                   )

credit3 = tk.Label(creditFrame,
                   text="◆ 本家様",
                   font=('游ゴシック', 20, 'bold'),
                   bg="#ffffff"
                   )

urlFont = tf.Font(underline=True, size=16)
credit4 = tk.Label(creditFrame,
                   text=title1 + title2,
                   cursor="hand2",
                   font=urlFont,
                   bg="#ffffff",
                   fg="blue"
                   )

moveFrame = tk.Frame(root,
                     width=980,
                     height=150,
                     bg="#ffffff",
                     relief=tk.RIDGE,
                     )

inputElement = tk.Entry(moveFrame,
                        font=('游ゴシック', 20, 'bold'),
                        state='readonly'
                        )

countLabel = tk.Label(moveFrame,
                      text=str(0) + "/17",
                      font=('游ゴシック', 14, 'bold'),
                      bg="#ffffff",
                      foreground="#000000"
                      )

timeLabel = tk.Label(moveFrame,
                     text="",
                     font=('游ゴシック', 18, 'bold'),
                     bg="#ffffff",
                     foreground="#000000"
                     )

reset = tk.Button(moveFrame,
                  text="RESET",
                  font=('游ゴシック', 18, 'bold'),
                  bg="#343434",
                  foreground="#ffffff"
                  )

backToStart = tk.Button(moveFrame,
                        text="← TITLE",
                        font=('游ゴシック', 18, 'bold'),
                        bg="#343434",
                        foreground="#ffffff"
                        )

showNumber1 = tk.Frame(secondFrame,
                       width=220,
                       height=250,
                       bg="#ffffff",
                       relief=tk.RIDGE,
                       )

showNumber2 = tk.Frame(secondFrame,
                       width=220,
                       height=250,
                       bg="#ffffff",
                       relief=tk.RIDGE,
                       )

showNumber3 = tk.Frame(secondFrame,
                       width=220,
                       height=250,
                       bg="#ffffff",
                       relief=tk.RIDGE,
                       )


number1 = tk.Label(showNumber1,
                   text="10",
                   font=('游ゴシック', 50, 'bold'),
                   bg="#ffffff",
                   foreground="#000000"
                   )

number2 = tk.Label(showNumber2,
                   text="10",
                   font=('游ゴシック', 50, 'bold'),
                   bg="#ffffff",
                   foreground="#000000"
                   )

number3 = tk.Label(showNumber3,
                   text="10",
                   font=('游ゴシック', 50, 'bold'),
                   bg="#ffffff",
                   foreground="#000000"
                   )

message = tk.Label(secondFrame,
                   text="暇だったんだね･･･",
                   font=('游ゴシック', 36, 'bold'),
                   bg="#343434",
                   foreground="#ffffff"
                   )
