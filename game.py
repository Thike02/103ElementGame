import webbrowser
import screen_module as sm
import function

sm.root.title("103 Element Game")
sm.root.state('zoomed')
sm.root.configure(bg="#ffffff")

sm.subLabel1.place(x=940, y=20)

sm.subLabel2.place(x=1350, y=20)

sm.firstFrame.bind("<Button-1>", function.startToGame)
sm.firstFrame.pack(pady=40)

sm.titleLabel1.place(x=25, y=60)
sm.titleLabel2.place(x=270, y=120)
sm.titleLabel3.place(x=380, y=260)

sm.countLabel.place(x=930, y=420)


sm.inputElement.place(x=810, y=535, width=300, height=50)
sm.inputElement.configure(bg='#ffffff')
sm.inputElement.bind("<Return>", function.judge)

sm.reset.bind("<Button-1>", function.gameToStart)
sm.backToStart.bind("<Button-1>", function.clearToStart)


sm.rule1.place(x=480, y=650)
sm.rule2.place(x=480, y=700)
sm.rule3.place(x=480, y=740)
sm.rule4.place(x=480, y=780)

sm.credit1.place(x=480, y=840)
sm.credit2.place(x=700, y=845)
sm.credit3.place(x=480, y=900)

url = "https://hyper-frog.net/mod-element/"

sm.credit4.place(x=700, y=905)
sm.credit4.bind("<Button-1>", lambda e: webbrowser.open_new(url))

sm.root.mainloop()
