from A import x
import time

x()
jk=input("难道这就是你分手的借口(y/n): ")
if jk=="y":
    aa=input("如果让你重新来过，你会不会爱我(y/n)：")
    if aa=="y":
        print("爱情让人拥有快乐")
        hgd=0
        while hgd<=100:
            hgd=hgd+10
            print("好感度：",hgd,"%")
        print("也会带来沉默...")
        time.sleep(23)
elif jk=="n":
    print("*世界线崩溃*")
    quit()
else:
    print("wtf....")
    quit()
