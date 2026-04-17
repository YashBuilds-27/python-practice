import random as r
def dice(user):  
    print("{---",user,"'s turn ---}")
    score=0
    for i in range(3):
        n=input("Press enter to Roll...")
        num=r.randint(1,6)
        print("Roll",i+1,":",num)
        score+=num
    print("---------------------")
    print("|",user.upper(),"'s TOTAL:",score,"|")
    print("---------------------")
    return score


while True:
    print("""---------------------
|***READY TO START***|
---------------------""")
    p1=input("Enter player 1 name:")
    p2=input("Enter player 2 name:")
    
    p1_score=dice(p1)
    p2_score=dice(p2)
    
    print("---------------------")
    if p1_score>p2_score:
        print(p1.upper(),"WINS")
    elif p2_score>p1_score:
        print(p2.upper(),"WINS")
    else:
        print("IT IS A TIE")
    print("---------------------")
    
    again=input("Play again? Press Y:")
    if again.lower()!="y":
        print("""\nThankyou for playing...
Exited!""")
        break