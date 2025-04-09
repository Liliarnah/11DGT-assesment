import easygui

easygui.msgbox("welcome to the random quiz, press ok to test your random knowedge. \n there is no choice.")
age = easygui.integerbox("first I will request your age, mortal creature")
if age <16 :
  continu = easygui.buttonbox("your years on this earth are nothing, leave child.", choices =["okay...", "nuh"])
  if continu == "nuh" :
    easygui.msgbox("you are a brave young mortal. \n continue")
  if continu == "okay..." :
    age = easygui.integerbox("bro just give me a diffrent age")
    if age >= 16 :
      easygui.msgbox("ok")
    if age < 16 :
      easygui.msgbox("bruh, whatever")
if age >= 16 :
  easygui.msgbox("you are old enough to continue \n go")
user_name = easygui.enterbox("now that i have your age, i need your name.")
true = easygui.buttonbox("is your chosen name " + user_name + "?", choices=["yes", "no"])
if true == "no":
   name = easygui.enterbox("give me your name then!")
   easygui.msgbox("we will start the random quiz now.")
if true == "yes":
   easygui.msgbox("we will start the random quiz now.")
questionlist = ["what is fish in swedish?", "what's a group of crows called?", "what bird is native to NZ?" ]
answerlist = ["fisk", "a murder"]
fakelist = ["sparrow", "brown quail", "goldfinch"]
q1 = easygui.enterbox(questionlist[0])
if q1 == answerlist[0] :
   easygui.msgbox("good job")
else :
  easygui.msgbox("you suck lol")
