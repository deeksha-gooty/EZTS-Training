def lps_array(p):
    lps=[0]
    j=0
    for i in range(1,len(p)):
        if p[i]==p[j]:
            lps.append(j+1)
            j=j+1
        else:
            j=0
            lps.append(j)
    return lps

def KMPAlgo(p,s):
    lps=lps_array(p)
    print(lps)
    i=0
    j=0
    n=len(s)-1
    m=len(p)-1
    while (n-i)>=(m-j):
        if p[j]==s[i]:
            i+=1
            j+=1
        if j==m:
            print(i-j)
            j=lps[j-1]
        elif i<n and p[j]!=s[i]:
            if j!=0:
                j=lps[j-1]
            else:
                i+=1

if __name__=="__main__":
    s="ABABCABCABCABDAA"
    p="ABCAB"
    KMPAlgo(p,s)