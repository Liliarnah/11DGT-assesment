import easygui

continu = "yes"
while continu == "yes" :
  easygui.msgbox("welcome to the random quiz, press ok to test your random knowedge. \n there is no choice.")
  age = easygui.integerbox("first I will request your age, mortal creature")
  if age <16 :
    continu = easygui.buttonbox("your years on this earth are nothing, leave child.", choices =["okay...", "nuh"])
    if continu == "nuh":
      easygui.msgbox("you are a brave young mortal. \n continue")
    if continu == "okay..." :
      age = easygui.integerbox("bro just give me a different age")
      if age >= 16 :
        easygui.msgbox("ok")
      if age < 16 :
        easygui.msgbox("bruh, whatever")
  if age >= 16 :
    easygui.msgbox("you are old enough to continue \n go")
  user_name = easygui.enterbox("now that i have your age, i need your name.")
  if user_name.isnumeric():
    user_name = easygui.enterbox("give me a name not a number.")
    if user_name.isnumeric():
      easygui.msgbox("im gonna explode, stop.")
      user_name = easygui.enterbox("name")
  true = easygui.buttonbox("is your chosen name " + user_name + "?", choices=["yes", "no"])
  if true == "no":
    user_name = easygui.enterbox("give me your name then!")
    easygui.msgbox("we will start the random quiz now.")
  if true == "yes":
    easygui.msgbox("we will start the random quiz now.")
  questionlist = ["what is fish in swedish?", "what's a group of crows called?", "which bird is native to NZ?", "CH4 + O2 -->", "what is the core of magic called in Arcane?", "what is my most used digital brush called?" ]
  answerlist = ["fisk", "a murder", "whitehead", "CO2 + H2O", "the arcane", "pen(fade)"]
  fakelist1 = ["whitehead", "sparrow", "brown quail", "goldfinch"]
  fakelist2 = ["CO2 + H2O + soot", "CO + H2O", "CO + H2O + soot", "CO2 + H2O"]
  fakelist3 = ["digital brush", "air brush", "watercolour brush", "pencil mod(#1)", "pen(fade)"]
  points = 0
  q1 = easygui.enterbox(questionlist[0])
  if q1 == answerlist[0] :
      easygui.msgbox("good job " + user_name)
      points += 5
  else :
    easygui.msgbox("you suck lol")
  q2 = easygui.enterbox(questionlist[1])
  if q2 == answerlist[1] :
    easygui.msgbox("good job " + user_name)
    points += 5
  else :
    easygui.msgbox("you suck lol")
  q3 = easygui.enterbox(questionlist[4])
  if q3 == answerlist[4] :
    easygui.msgbox("gold star!")
    points += 5
  else :
    easygui.msgbox("loser")
  q4 = easygui.buttonbox(questionlist[2], choices = fakelist1)
  if q4 == answerlist[2] :
    easygui.msgbox("yippie")
    points += 5
  else :
    easygui.msgbox("bruh")
  q5 = easygui.buttonbox(questionlist[3], choices = fakelist2)
  if q5 == answerlist[3] :
    easygui.msgbox("yippie")
    points += 5
  else :
    easygui.msgbox("bruh")
  q6 = easygui.buttonbox(questionlist[5], choices = fakelist3)
  if q6 == answerlist[5] :
    easygui.msgbox("correct!")
    points += 5
  else :
    easygui.msgbox("WRONG")

  if points == 0 :
    easygui.msgbox("the mortal has finished their random quiz! your total amounts of points where 0")
  if points == 5 :
    easygui.msgbox("the mortal has finished their random quiz! your total amounts of points where 5")  
  if points == 10 :
    easygui.msgbox("horray! the mortal has finished their random quiz! your total amounts of points where 10")
  if points == 15 :
    easygui.msgbox("horray! the mortal has finished their random quiz! your total amounts of points where 15")
  if points == 20 :
    easygui.msgbox("horray! the mortal has finished their random quiz! your total amounts of points where 20")
  if points == 25 :
    easygui.msgbox("horray! the mortal has finished their random quiz! your total amounts of points where 25")
  if points == 30 :
    easygui.msgbox("horray! the mortal has finished their random quiz! your total amounts of points where 30")
  continu = easygui.buttonbox("do you wish to play again?", choices =["yes", "no"])
  if continu == "no":
      easygui.msgbox("lol bye loser")
