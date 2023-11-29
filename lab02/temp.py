xlen_and_ylen = input()
xinput = input()
yinput = input()

len =xlen_and_ylen.split()

xlen = int(len[0])
ylen = int(len[1])

x= xinput.split()
y = yinput.split()

#print(x)

matrix = [[0 for _ in range(ylen+2)] for _ in range(xlen+2)]

for i in range(2,xlen+2):
    matrix[i][0]= x[i-2]
    
for j in range(2,ylen+2):
    matrix[0][j]= y[j-2]
    

p=2
q=2



while((p != xlen+1) and (q != ylen+1)):
    for p in range(2,xlen+2):
        for q in range(2, ylen+2):
            if (matrix[p][0] == matrix[0][q]):
                matrix[p][q] = matrix[p-1][q-1] + 1
                
        
            else:
                matrix[p][q] = matrix[p][q-1] if matrix[p][q-1] > matrix[p-1][q] else matrix[p-1][q]

#for n in matrix:
    #print(n)
    
l = []
p = xlen+1
q = ylen+1

a = 0

while(a< matrix[xlen+1][ylen+1]):
    if((matrix[p][0] == matrix[0][q]) and (matrix[p][q] > matrix[p-1][q-1])):
        l.append(str(matrix[p][0]))
        p = p-1
        q = q-1
        a = a+1
        
    else:
        if(int(matrix[p][q-1]) > int(matrix[p-1][q])):
            q = q-1
            
        else:
            p = p-1
            
    
revList = l[::-1]
answer = " ".join(revList)
print(answer)