#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


# } Driver Code Ends

class Solution:
        
    #Function to check if Kth bit is set or not.
    def checkKthBit(self, n,k):
        #Your code here
        b=[]
        while(n>=1):
            p = n%2
            b.append(p)
            n=n//2
        b = b[::-1]
        if(k>len(b)-1 or k<0):
            return False
        elif(b[len(b)-k-1]==1):
            return True
        else:
            return False

#{ 
 # Driver Code Starts.


    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        k=int(input())
        obj = Solution()
        if obj.checkKthBit(n,k):
            print("Yes")
        else:
            print("No")
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends