def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    # row, col = len(matrix), len(matrix[0])
    # ans=[]
    # def right(r,c1,cn):
    #     return matrix[r][c1:cn+1]
    # def down(r1,rn,c):
    #     return [matrix[r][c] for r in range(r1,rn+1)]
    # def left(r,cn,c1):
    #     return matrix[r][c1:cn+1][::-1]
    # def up(rn,r1,c):
    #     return [matrix[r][c] for r in range(rn,r1-1,-1)]
    
    # r1,rn,c1,cn=0,row-1,0,col-1
    # while r1<=rn and c1<=cn:
    #     ans+=right(r1,c1,cn)
    #     r1+=1
    #     if r1>rn: break
    #     ans+=down(r1,rn,cn)
    #     cn-=1
    #     if c1>cn: break
    #     ans+=left(rn,cn,c1)
    #     rn-=1
    #     if r1>rn: break
    #     ans+=up(rn,r1,c1)
    #     c1+=1
    # return ans

    # Simple & elegant solution
    # Use direction to change right <-> left, down<->up
    # and keep reducing max limit till it hits zero
    
    r,c, row, col = 0,-1,len(matrix), len(matrix[0])
    dir=1
    ans=[]
    while row>0 and col>0:
        for _ in range(col):
            c+=dir
            ans.append(matrix[r][c])
        row-=1
        for _ in range(row):
            r+=dir
            ans.append(matrix[r][c])
        col-=1
        dir*=-1

    return ans


matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(spiralOrder(matrix))