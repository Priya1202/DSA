#User function Template for python3

class Solution:
    def removeConsecutiveCharacter(self, S):
        # code here
        sol = ""
        for i in range(0,len(S)-1):
            if(S[i]!=S[i+1]):
                sol += S[i]
        sol += S[-1]
        return sol

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        s = input()
        ob = Solution()
        print(ob.removeConsecutiveCharacter(s))

# } Driver Code Ends