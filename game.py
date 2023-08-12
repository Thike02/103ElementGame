import webbrowser
import screen_module as sm
import function

sm.root.title("103 Element Game")
sm.root.state('zoomed')
sm.root.configure(bg="#ffffff")
sm.root.bind("<Key-F5>", function.game_to_start)
sm.root.bind("<Key-Escape>", lambda event: sm.root.destroy(), '+')
sm.root.iconbitmap(default=function.get_absolute_path('103Element.ico'))

sm.sub_label_frame.pack(pady=0)
sm.sub_label1.place(x=460, y=20)
sm.sub_label2.place(x=870, y=20)

sm.title_frame.bind("<Button-1>", function.start_to_game)
sm.title_frame.pack(pady=0)
sm.title_label1.place(x=25, y=60)


sm.title_label2.place(x=270, y=120)
sm.title_label3.place(x=260, y=260)
sm.title_label1.focus_set()
sm.title_label1.bind("<Button-1>", function.start_to_game)
sm.title_label1.bind("<Key-space>", function.start_to_game, '+')
sm.title_label2.bind("<Button-1>", function.start_to_game)
sm.title_label3.bind("<Button-1>", function.start_to_game)

sm.move_frame.pack(pady=10)
sm.count_label.place(x=450, y=0)
sm.input_element.place(x=330, y=100, width=300, height=50)

sm.input_element.configure(bg='#ffffff')
sm.input_element.bind("<Key-Return>", function.judge)
sm.reset.bind("<Button-1>", function.game_to_start)
sm.back_to_start.bind("<Button-1>", function.clear_to_start)

sm.rule_frame.pack(pady=0)
sm.rule1.place(x=10, y=30)
sm.rule2.place(x=10, y=70)
sm.rule3.place(x=10, y=110)
sm.rule4.place(x=10, y=150)

sm.credit_frame.pack(pady=0)
sm.credit1.place(x=10, y=40)
sm.credit2.place(x=230, y=45)
sm.credit3.place(x=10, y=95)

url = "https://hyper-frog.net/mod-element/"

sm.credit4.place(x=230, y=100)
sm.credit4.bind("<Button-1>", lambda e: webbrowser.open_new(url))

sm.root.mainloop()

sm.root.quit()
