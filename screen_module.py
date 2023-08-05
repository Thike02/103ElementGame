import tkinter as tk
import tkinter.font as tf


root = tk.Tk()

subLabel1 = tk.Label(root,
                     text="「トランプを3枚出してその積を103で割った余りの値の元素をいかに早く言うか」",
                     font=('游ゴシック', 8, 'bold'),
                     bg="#ffffff",
                     foreground="#000000"
                     )

subLabel2 = tk.Label(root,
                     text="Python Version",
                     font=('游ゴシック', 8, 'bold'),
                     bg="#ffffff",
                     foreground="#000000"
                     )

countLabel = tk.Label(root,
                      text=str(0) + "/17",
                      font=('游ゴシック', 14, 'bold'),
                      bg="#ffffff",
                      foreground="#000000"
                      )

timeLabel = tk.Label(root,
                     text="",
                     font=('游ゴシック', 18, 'bold'),
                     bg="#ffffff",
                     foreground="#000000"
                     )

firstFrame = tk.Frame(root,
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
titleLabel1 = tk.Label(firstFrame,
                       text=title1,
                       font=('游ゴシック', 28, 'bold'),
                       bg="#343434",
                       foreground="#ffffff"
                       )

title2 = "元素をいかに早く言うか"
titleLabel2 = tk.Label(firstFrame,
                       text=title2,
                       font=('游ゴシック', 28, 'bold'),
                       bg="#343434",
                       foreground="#ffffff"
                       )

titleLabel3 = tk.Label(firstFrame,
                       text="クリックしてスタート",
                       font=('游ゴシック', 16, 'bold'),
                       bg="#343434",
                       foreground="#ffffff"
                       )

rule1 = tk.Label(root,
                 text="◆ ルール説明",
                 font=('游ゴシック', 20, 'bold'),
                 bg="#ffffff"
                 )

rule2 = tk.Label(root,
                 text="1. 画面に出現する3つの数字の積を計算してください.",
                 font=('游ゴシック', 16, 'bold'),
                 bg="#ffffff"
                 )

rule3 = tk.Label(root,
                 text="2. その値を103で割った余りを計算してください.",
                 font=('游ゴシック', 16, 'bold'),
                 bg="#ffffff"
                 )

rule4 = tk.Label(root,
                 text="3. その値を元素番号とみて該当する元素を記入してください(アルファベットのみ).",
                 font=('游ゴシック', 16, 'bold'),
                 bg="#ffffff"
                 )

credit1 = tk.Label(root,
                   text="◆ アプリ製作者",
                   font=('游ゴシック', 20, 'bold'),
                   bg="#ffffff"
                   )

credit2 = tk.Label(root,
                   text="Thike",
                   font=('游ゴシック', 16, 'bold'),
                   bg="#ffffff"
                   )

credit3 = tk.Label(root,
                   text="◆ 本家様",
                   font=('游ゴシック', 20, 'bold'),
                   bg="#ffffff"
                   )

urlFont = tf.Font(underline=True, size=16)
credit4 = tk.Label(root,
                   text=title1 + title2,
                   cursor="hand2",
                   font=urlFont,
                   bg="#ffffff",
                   fg="blue"
                   )

inputElement = tk.Entry(root, font=('游ゴシック', 20, 'bold'), state='readonly')

showNumber1 = tk.Frame(secondFrame,
                       width=220,
                       height=300,
                       bg="#ffffff",
                       relief=tk.RIDGE,
                       )

showNumber2 = tk.Frame(secondFrame,
                       width=220,
                       height=300,
                       bg="#ffffff",
                       relief=tk.RIDGE,
                       )

showNumber3 = tk.Frame(secondFrame,
                       width=220,
                       height=300,
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

reset = tk.Button(root,
                  text="RESET",
                  font=('游ゴシック', 18, 'bold'),
                  bg="#343434",
                  foreground="#ffffff"
                  )

backToStart = tk.Button(root,
                        text="← TITLE",
                        font=('游ゴシック', 18, 'bold'),
                        bg="#343434",
                        foreground="#ffffff"
                        )
