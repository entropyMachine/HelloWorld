# Transpose a matrix 

X = [[12,7],
    [4 ,4],
    [1 ,8]]

result = [[0,0,0],
         [0,0,0]]

# iterate rows
for i in range(len(X)):
# iterate columns
   for j in range(len(X[0])):
       result[j][i] = X[i][j]

for r in result:
   print(r)
