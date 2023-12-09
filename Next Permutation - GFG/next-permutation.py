#User function Template for python3

class Solution:
    def nextPermutation(self, N, arr):
        # code here
        if N<=2:
            arr[0],arr[1] = arr[1],arr[0]
            return arr
            
        pointer = N-2
        while pointer>=0 and arr[pointer+1]<=arr[pointer]:
            pointer-=1
        
        if pointer == -1:
            return arr[::-1]
            
        
        for x in range(N-1,pointer,-1):
            if arr[x]>arr[pointer]:
                arr[x],arr[pointer]=arr[pointer],arr[x]
                break
            
        arr[pointer+1:]=reversed(arr[pointer+1:])
        return arr
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        ans = ob.nextPermutation(N, arr)
        for i in range(N):
            print(ans[i],end=" ")
        print()
# } Driver Code Ends