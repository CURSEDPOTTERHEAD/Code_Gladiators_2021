def virus(V, str1):
    M,N = len(V),len(str1)
    i,j=0,0
    while(j<M and i<N):
        if str1[i] == V[j]:
            i+=1
        j+=1 
    return i == N


V = input().strip()
N = int(input())
for i in range(N):
    str1 = input().strip() 
    if virus(V,str1):
        print("POSITIVE")
    else:
        print("NEGATIVE")
