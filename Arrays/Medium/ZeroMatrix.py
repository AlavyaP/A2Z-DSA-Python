'''
Coding Ninja >  https://www.codingninjas.com/studio/problems/zero-matrix_1171153?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
LeetCode > https://www.codingninjas.com/studio/problems/zero-matrix_1171153?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
Problem Statement: Given a matrix if an element in the matrix is 0 then you will have to set its entire column and row to 0 and then return the matrix.
Examples
Input: matrix=[[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Explanation: Since matrix[2][2]=0.Therfore the 2nd column and 2nd row wil be set to 0.
'''
# Brute Force >> Time Complexity is O((N*M)+(N+M))+ O(N*M)
def rowZero(matrix,n,m,i):
    for j in range (m):
        if matrix[i][j] != 0 :
            matrix[i][j] = -1 
    
def coloumZero(matrix,n,m,j):
    for i in range (n):
        if matrix[i][j] != 0 :
            matrix[i][j] = -1 
                
def setZeros(matrix,n,m): 
    for i in range (n):
        for j in range (m):
            if matrix[i][j] == 0:
                rowZero(matrix,n,m,i)
                coloumZero(matrix,n,m,j)
                
    for i in range (n):
        for j in range (m):
            if matrix[i][j] == -1 :
                matrix[i][j] = 0
    
    return matrix


# Test Run 
# print (setZeros([[0,1,2,0],[3,4,5,2],[1,3,1,5]],3,4))


# Better Approach 
def betterMatrix(matrix,n,m):
    col = [0] *m
    row = [0] *n
    for i in range (n):
        for j in range (m):
            if matrix[i][j] ==0 :
                col[j] = 1 
                row[i] = 1
    

    for i in range (n):
        for j in range (m):
            if (row[i] == 1  or col[j] == 1 ) :
                matrix[i][j] = 0
                
    return matrix


# Test Run 
# print (betterMatrix([[0,1,2,0],[3,4,5,2],[1,3,1,5]],3,4))


# Optimal Approach n = is rows and m = is coloums
def optimalMatrix(matrix,n,m):
    col0 = 1
    for i in range (n):
        for j in range (m):
            if matrix[i][j] == 0 :
                # mark the i-th row
                matrix[i][0] = 0
                
                # mark the j-th index 
                if j != 0 :
                    matrix[0][j] = 0 
                else :
                    col0= 0 
                    
    # Step 2 > to mark with 0 from (1,1) to (n-1,m)
    for i in range (1,n):
        for j in range (1,m):
            if matrix[i][j] != 0 :
                
                # check for the col and row 
                if matrix[i][0] == 0 or matrix[0][j] ==0  :
                    matrix[i][j] = 0
                    
    # Step 3 : Finally mark the 1st col and then 1st  row 
    if matrix[0][0] == 0 :
        for j in range (m):
            matrix[0][j] = 0
    if col0 == 0 :
        for i in range (n):
            matrix[i][0] = 0 
    return matrix 


# Test Run 
print (optimalMatrix([[0,1,2,0],[3,4,5,2],[1,3,1,5]],3,4))

    