#User function Template for python3

def downwardDiagonal(N, A): 
    # code here 
    arr=[]
    for i in range(0,N):
        row = 0
        col = i
        while col>=0:
            arr.append(A[row][col])
            col-=1
            row+=1
    for i in range(1,N):
        col = N-1
        row = i
        while row<=N-1:
            arr.append(A[row][col])
            col-=1
            row+=1
    return arr    
    
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        matrix =[]
        for i in range(n):
            row = list(map(int, input().strip().split()))
            matrix.append(row)
        ans = downwardDiagonal(n,matrix)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends