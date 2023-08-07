import webbrowser
import screen_module as sm
import function

sm.root.title("103 Element Game")
sm.root.state('zoomed')
sm.root.configure(bg="#ffffff")
sm.root.bind("<Key-F5>", function.gameToStart)

sm.subLabelFrame.pack(pady=0)
sm.subLabel1.place(x=460, y=20)
sm.subLabel2.place(x=870, y=20)

sm.titleFrame.bind("<Button-1>", function.startToGame)
sm.titleFrame.pack(pady=0)
sm.titleLabel1.place(x=25, y=60)
sm.titleLabel2.place(x=270, y=120)
sm.titleLabel3.place(x=380, y=260)
sm.titleLabel3.bind("<Button-1>", function.startToGame)

sm.moveFrame.pack(pady=10)

sm.countLabel.place(x=460, y=0)
sm.inputElement.place(x=340, y=100, width=300, height=50)
sm.inputElement.configure(bg='#ffffff')
sm.inputElement.bind("<Key-Return>", function.judge)
sm.inputElement.focus_set()
sm.reset.bind("<Button-1>", function.gameToStart)
sm.backToStart.bind("<Button-1>", function.clearToStart)

sm.ruleFrame.pack(pady=0)
sm.rule1.place(x=10, y=30)
sm.rule2.place(x=10, y=70)
sm.rule3.place(x=10, y=110)
sm.rule4.place(x=10, y=150)

sm.creditFrame.pack(pady=0)
sm.credit1.place(x=10, y=40)
sm.credit2.place(x=230, y=45)
sm.credit3.place(x=10, y=95)

url = "https://hyper-frog.net/mod-element/"

sm.credit4.place(x=230, y=100)
sm.credit4.bind("<Button-1>", lambda e: webbrowser.open_new(url))

sm.root.mainloop()
