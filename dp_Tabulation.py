#Tabulation Method
'''
p=[5,10,15,7,8,9,4]
w=[1,3,5,4,1,3,2]
'''

# def calc_max(p,w,c,n):
#     for i in range(1,n+1):
#         for j in range(1,c+1):
#             if j-w[i-1]<0:
#                 dp[i][j]=dp[i-1][j]
#             else:
#                 dp[i][j]=max(dp[i-1][j],p[i-1]+dp[i-1][j-w[i-1]])
#     return dp[n][c]

c=15
p=[5,10,15,7,8,9,4]
w=[1,3,5,4,1,3,2]
n=len(p)
dp=[[0 for i in range(c+1)] for j in range (n+1)]
for i in range(1,n+1):
    for j in range(1,c+1):
        if j-w[i-1]<0:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j],p[i-1]+dp[i-1][j-w[i-1]])
for i in dp:
    print(i)
print(dp[n][c])