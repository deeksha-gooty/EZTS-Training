'''
Available Coins: 1 5 7
Amount=18
What will be the min no. of coins required to pay the bill. 
'''
# coins=[1,5,7]
# amt=18
# res={1:0,5:0,7:0}
# while amt>0:
#     m=coins.pop(coins.index(max(coins)))   #Sort list in reverse
#     c=amt//m
#     res[m]+=c
#     amt=amt%m
# print(res)


def calculate(coins,amt):

    res=[float('inf')]*(amt+1)
    res[0]=0

    for i in range(1,amt+1):
        for co in coins:
            if i-co>=0:
                res[i]=min(res[i],res[i-co]+1) 
        print(res)
    print("\n")  
    return res[amt] if res[amt]!=float('inf') else -1

coins=[1,5,7]
amt=18
print(calculate(coins,amt))