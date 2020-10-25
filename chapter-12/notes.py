

M =  [ [ i*j for i in range(6)] for j in range(6) ] 



rows = len(M) 
cols = len(M[0]) 

# print the matrix 
for i in range(rows):
    print(M[i])

# print the diagonal of the matrix 
for i in range(rows): 
    for j in range(cols):
        if i == j: 
            print(M[i][j]) 

# print only the boundary elements 
# for i in range(rows):
#     for j in range(cols):
#         if ( i == 0 and ( j == 0 or j == rows - 1 )) or \
#            ( i == cols - 1 and ( j == 0 or j == cols - 1 )):
#             print(M[i][j])
