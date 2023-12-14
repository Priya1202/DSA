# Your task is to complete this function

class Solution:
    def matrixDiagonally(self,mat):
        # code here
        arr = []
        up = True
        row,col = (0,0)
        for i in range(0,len(mat)):
            if up:
                row = i
                col = 0
                while row>=0:
                    arr.append(mat[row][col])
                    row-=1
                    col+=1
            else:
                row = 0
                col = i
                while col>=0:
                    arr.append(mat[row][col])
                    row+=1
                    col-=1
            up = not up
        new = up
        for i in range(1,len(mat)):
            if new:
                row = len(mat)-1
                col = i
                while col<=len(mat)-1:
                    arr.append(mat[row][col])
                    row-=1
                    col+=1
            else:
                row = i
                col = len(mat)-1
                while row<=len(mat)-1:
                    arr.append(mat[row][col])
                    row+=1
                    col-=1
            new = not new
        return arr

#{ 
 # Driver Code Starts
# Driver Program
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        a = Solution().matrixDiagonally(matrix)
        for x in a:
            print(x,end=' ')
        print('')
# Contributed by: Harshit Sidhwa
# } Driver Code Ends