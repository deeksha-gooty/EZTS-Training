# Problem 3

# You are given an integer array cards where cards[i] represents the value of the ith card. 
# A pair of cards are matching if the cards have the same value.

# Return the minimum number of consecutive cards you have to pick up to have a pair of 
# matching cards among the picked cards. If it is impossible to have matching cards, return -1.

 
# Input: cards = [3,4,2,3,4,7],[3,4,5,3,2,4,2,6,6]
# Output: 4
# Explanation: We can pick up the cards [3,4,2,3] which contain a matching pair of cards 
# with value 3. Note that picking up the cards [4,2,3,4] is also optimal.

cards=list(map(int,input().split()))
min=999
f=False
for i in range(len(cards)):
    s=0
    for j in range(i+1,len(cards)):
        if cards[i]==cards[j]:
            s=j-i+1
            if min>s:
                min=s
                f=True
if f:
    print(min)
else:
    print(-1)


