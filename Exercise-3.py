# KHON BANEGA KARODPATHI
questions=[["who is the president of india","droupathi murmu","modi","jagan","kcr",4],
           ["who is the president of india","droupathi murmu","modi","jagan","kcr",4],
           ["who is the president of india","droupathi murmu","modi","jagan","kcr",4],
           ["who is the president of india","droupathi murmu","modi","jagan","kcr",4],
           ["who is the president of india","droupathi murmu","modi","jagan","kcr",4],
           ["who is the president of india","droupathi murmu","modi","jagan","kcr",4]]

levels=[100,1000,10000,100000,1000000,10000000]
money=0
i=0
for i in range(0,len(questions)):
    question=questions[i]
    print(f"question for Rs.{levels[i]}")
    print(f"a.{question[1]}   b.{question[2]}")
    print(f"c.{question[3]}   d.{question[4]}")
    reply=int(input("enter your answer(1-4)"))
    if(reply==question[-1]):
        print(f"correct answer,you won Rs.{levels[i]}")
        if(i==4):
            money=1000
        elif(i==9):
            money=10000
        elif(i==14):
            money=100000
        elif(i==20):
            money=1000000
        elif(i==25):
            money=10000000
    else:
        print("wrong answer")
        break