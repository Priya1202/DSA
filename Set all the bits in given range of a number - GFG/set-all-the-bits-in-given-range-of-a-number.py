#User function Template for python3

class Solution:
    def setAllRangeBits(self, N , L , R):
        # code here 
        b =[]
        L=L-1
        R=R-1
        ans=0
        while(N>=1):
            p=N%2
            b.append(p)
            N=N//2
        b = b[::-1]
        for i in range(0,len(b)):
            if(i<=(len(b)-L-1) and i>=(len(b)-R-1)):
                if b[i]==0:
                    b[i]=1
        for i in range(0,len(b)):
            po = pow(2,(len(b)-1-i))
            ans=ans + b[i]*po
        return ans
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,L,R=map(int,input().split())
        
        ob = Solution()
        print(ob.setAllRangeBits(N,L,R))
# } Driver Code Ends