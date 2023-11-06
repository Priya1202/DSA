class Solution:
	def overlappedInterval(self, Intervals):
		#Code here
        temp=[]
        index = 0
        x = sorted(Intervals)
        for i in range(1,len(x)):
            if(x[index][1]>=x[i][0]):
                x[index][1]=max(x[index][1],x[i][1])
            else:
                index+=1
                x[index]=x[i]
        return x[:index+1]
#{ 
 # Driver Code Starts
		
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
    	n = int(input())
    	a = list(map(int, input().strip().split()))
    	Intervals = []
    	j = 0
    	for i in range(n):
    		x = a[j]
    		j += 1
    		y = a[j]
    		j += 1
    		Intervals.append([x,y])
    	obj = Solution()
    	ans = obj.overlappedInterval(Intervals)
    	for i in ans:
    		for j in i:
    			print(j, end = " ")
    	print()
# } Driver Code Ends