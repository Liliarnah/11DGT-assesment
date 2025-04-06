import easygui

continu = "okay...
while continu == "okay..." :
  easygui.msgbox("welcome to the random quiz press ok to test your random knowedge")
  age = easygui.integerbox("first i will request your age, mortal creature")
  if age >= 16:
    easygui.msg("you are old enough to continue")
  if age <16 :
     continu = easygui.buttonbox("your years on this earth are nothing, leave child", choices = ["okay...", "nuh")
     if coninu == "nuh" : 
        easygui.msg("you are a brave young mortal \n continue")
