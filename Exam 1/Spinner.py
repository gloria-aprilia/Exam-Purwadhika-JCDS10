def counterClockwise(matrix):   #define the 'counterClockwise' function

    for i in range(len(matrix)):    #i is the index of matrix row
        for j in range(i):  #j is the index of matrix column
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]   #swap the value of matrix diagonally
    
    result = []     #initialize the resulting matrix
    for k in range(1,len(matrix)+1):    #k is the index of matrix row
        k = -k  #reverse the index of the matrix
        result.append(matrix[k])    #add element of 'matrix' to 'result' with reversed order
    
    return result   #return the value 
        
List_awal = [[1,2,3],[4,5,6],[7,8,9]]   #provide the matrix to rotate
print(counterClockwise(List_awal))  #display the rotated List_awal