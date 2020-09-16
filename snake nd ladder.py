import random
def cl(p):
   
    ladders={7:20,18:49,27:82,35:91,48:62,60:90,71:80,88:99}
    if(p in ladders):
         print("ladder")
         return(ladders[p])
    else:
        return p
def cs(p):
    
    snakes={13:2,25:10,36:20,45:11,68:32,77:50,89:6,98:43}
    if(p in snakes):
        print("snake")
        return(snakes[p])
    else:
        return p
def re(p):
    if p==end:
        return True
    else:
        return False
end=100
def play():
    p1n=input("player1 enter your name  ")
    p2n=input("player2 enter your name  ")
    p1=0
    p2=0
    turn=0
    while(1):
        if turn%2==0:
            print(p1n," your turn")
            c=input("press 1 to roll, 0 to quit")
            if(c==0):
                print(p1n," scored=p1")
                print(p2n," scored=p2")
                print("quiting the game, thanks for playing")
                break
            else:
                dice=random.randint(1,6)
                print("dice showed",dice)
                p1=p1+dice
                p1=cl(p1)
                p1=cs(p1)
                if p1>end:
                    p1=end
                print(p1n," you scored=",p1)
                if(re(p1)):
                    print(p1n," won")
                    break
        else:
            print(p2n," your turn")
            c=input("press 1 to roll, 0 to quit")
            if(c==0):
                print(p1n," scored=p1")
                print(p2n," scored=p2")
                print("quiting the game, thanks for playing")
                break
            else:
                dice=random.randint(1,6)
                print("dice showed",dice)
                p2=p2+dice
                p2=cl(p2)
                p2=cs(p2)
                if p2>end:
                    p2=end
                print(p2n," you scored=",p2)
                if(re(p2)):
                    print(p2n," won")
                    break
            
        turn=turn+1
play()