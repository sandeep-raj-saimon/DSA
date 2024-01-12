class Solution:
    def check (self, mat, target, n):

        for i in range(n):
            for j in range(n):
                if (mat[i][j] != target[i][j]):
                    return False

        return True

    def rotate (self, mat, n):

        for i in range(n):
            for j in range(i,n):
                mat[i][j],mat[j][i] = mat[j][i],mat[i][j]
        for i in range(n):
            mat[i].reverse()
    
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:

        n = len(mat)
        m = len(target)

        if (n != m):
            return False

        for i in range(4):
            if (self.check(mat, target, n)):
                return True
            self.rotate(mat, n)
