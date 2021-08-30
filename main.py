def Update_CurrentStatus(L1, R1, L2, R2):
    print(" CURRENT STATUS")
    print("PLAYER 1 : " + str(L1) +"  " + str(R1))
    print("PLAYER 2 : " + str(L2) +"  " + str(R2))

def Attack(player1, player2):
    player2 = player2 + player1
    return player2
def CheckDeadHand(dead):
    if dead > 4:
        dead = 0

    return dead
def checkGameOver(left, right):
    if(left == 0 and right == 0):
        gameOver = 1
    else:
        gameOver = 0

    return gameOver

if __name__ == "__main__":
    L1 , R1, L2, R2 = 1, 1, 1, 1
    Update_CurrentStatus(L1, R1, L2, R2)
    gameOver = 0

    while(gameOver == 0):
        print("Enter move for player1 = ")
        move = input()
        if(move == 'A'):
            print("Enter the move combination = ")
            move1, move2 = input().split()
            if(move1 == 'L'):
                if(move2 == 'R'):
                    R2 =Attack(L1, R2)
                    R2 = CheckDeadHand(R2)
                 
                elif(move2 == 'L'):
                    L2 = Attack(L1, L2)
                    L2 = CheckDeadHand(L2)
                   
               
            elif(move1 == 'R'):
                if(move2 == 'L'):
                    L2 = Attack(R1, L2)
                    L2 = CheckDeadHand(L2)
                elif(move2 == 'R'):
                    R2 = Attack(R1, R2)
                                 
        elif(move == 'S'):
            print("Enter the move combination= ")
            move, split1, split2 = input().split()
            left = int(split1)
            right = int(split2)

            left = CheckDeadHand(left)
            right = CheckDeadHand(right)

            if (left + right) <= (L1 + R1):
                if(left + right) == (L1 + R1):
                    L1 = left
                    R1 = right
                else:
                    if(move == 'L'):
                        L1 = left
                        R1 = R1 + right
                        R1 = CheckDeadHand(R1)
                    elif(move == 'R'):
                        R1 = right
                        L1 = p1L1 + left
                        L1 = CheckDeadHand(L1)                 
        Update_CurrentStatus(L1, R1, L2, R2)

        gameOver = checkGameOver(L2, R2)
        if gameOver:
            winner = 'Player 1'
            break

        print("Enter move for player 2 = ")
        move = input()
        if (move == 'A'):
            print("Enter the move combination = ")
            move1, move2 = input().split()
            if(move1 == 'L'):
                if (move2 == 'R'):
                    R1 = Attack(L2, R2)
                    R2 = CheckDeadHand(R2)
                elif (move2 == 'L'):
                    L1 = Attack(L2, L1)
                    L1 = CheckDeadHand(L1)
                
                
            elif (move1 == 'R'):
                if (move2 == 'L'):
                    L1 =Attack(R2, L1)
                    L2 = CheckDeadHand(L2)
                    
                elif (move2 == 'R'):
                    R1 = Attack(R2, R1)
                    L2 = CheckDeadHand(L2)
                 
            
        elif (move == 'S'):
            print("Enter the move combination= ")
            move, split1, split2 = input().split()
            left = int(split1)
            right = int(split2)

            left = CheckDeadHand(left)
            right = CheckDeadHand(right)
            if (left + right) <= (L2 + R2):
                if (left + right) == (L2 + R2):
                    L2 = left
                    R2 = right
                else:
                    if (move == 'L'):
                        L2 = left
                        R2 = R2 + right
                        R2 = CheckDeadHand(R2)
                    elif (move == 'R'):
                        R2 = right
                        L2 = L2 + left
                        L2 = CheckDeadHand(L2)                    
        Update_CurrentStatus(L1, R1, L2,R2)
        gameOver = checkGameOver(L1, R1)
        if(gameOver == 1):
            winner = 'Player 2'

    print("  ")
    print("WINNER OF GAME IS:: " + winner)