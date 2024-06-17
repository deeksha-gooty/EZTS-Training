# In a dice game 2 players are playing P1 and P2. both player is rolling the dice one by one and
# getting score and that score is getting added to the total score of the player.

# A player can get a chace of rolling the dice again if his total Score is Disivible by 2 and
# dice face is not divisible by 2.

# If the player having the dice face and total Score both are even then the player will not get
# the chace of rolling the dice again.

# If the player Score is odd and the dice face is also odd then the dice face value will be 
# decreased from the total socre of the player

# You will be given a list of 10 dice face number as input find the will and also print 
# the total score of each player.

def dice_score(arr):
    p1=0
    p2=0
    curr_player=1
    for i in arr:
        if curr_player==1:
            
            if p1%2==0 and i%2!=0:
                p1+=i
                curr_player=1
            elif p1%2!=0 and i%2!=0:
                p1-=i
            else:
                curr_player=2
        else:
            
            if p2%2==0 and i%2!=0:
                p2+=i
                curr_player=2
            elif p2%2!=0 and i%2!=0:
                p2-=i
            else:
                curr_player=1
    if p1>p2:
        winner="Player1"
    elif p2>p1:
        winner="Player2"
    else:
        winner="Draw"
    
    return winner,p1,p2

arr=[4,3,5,6,2,7,4,1,5,1]
winner,p1,p2 = dice_score(arr)
print(f"Winner: {winner}")
print(f"Player 1 Score: {p1}")
print(f"Player 2 Score: {p2}")