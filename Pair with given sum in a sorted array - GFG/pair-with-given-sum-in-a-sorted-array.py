#User function Template for python3


class Solution:
    def Countpair (self, arr, n, sum) : 
        #Complete the function
        count = 0
        f = 0
        l = n-1
        while(l>f):
            p = arr[f]+arr[l]
            if p == sum:
                count+=1
                f+=1
            elif p > sum:
                l-=1
            elif p<sum:
                f+=1
        if count == 0:
            return -1
        else:
            return count
                

#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n = int(input())
    arr = list(map(int,input().strip().split()))
    K = int(input())
    res = Solution().Countpair(arr, n, K)
    print(res)



# } Driver Code Ends