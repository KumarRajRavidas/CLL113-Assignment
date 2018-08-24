import os
def matrix(li):
    matrix=[]
    n=int(li[0][0])
    m=int(li[0][1])
    for i in range(1,n+1): #for finding first matrix
        matrix.append(li[i])
    	# return matrix
    return matrix_D(matrix,1.0)
def matrix_D(matrix, mul):
    width = len(matrix)
    if width == 1:
        return mul * float(matrix[0][0])
    else:
        sign = -1
        total = 0
        for i in range(width):
            m = []
            for j in range(1, width):
                buff = []
                for k in range(width):
                    if k != i:
                        buff.append(float(matrix[j][k]))
                m.append(buff)
            sign *= -1
            total += mul * matrix_D(m, sign * float(matrix[0][i]))
        return total

file = open("C:\\Users\\RAJ__DAS\\Desktop\\NEW1.txt") # C:\Users\RAJ__DAS\Desktop\
line = file.readline()#line read 
li=[]
items = line.split()
test=int(items[0])
t=0
while line and test>t:
	line = file.readline()
	items=line.split()
	if len(items)!=0:
		li.append(items)
	if len(items)==0 :
		t=t+1
		matrix_result=matrix(li)
		out=str(matrix_result)
		outToFile = open("C:\\Users\\RAJ__DAS\\Desktop\\newopt.txt","a")
		outToFile.write(out)
		outToFile.write("\n")
		outToFile.write("\n")
		del li[:]

###########################################
#Input
# 3
# 2 2
# 5 5
# 2 2

# 2 2
# 2.5 3.5 
# 80.1 9.3

# 2 2
# 1 2 
# 3 0 
#Output
# matrix value is=0.0

# matrix value is=-257.1

# matrix value is=-6.0
###########################################
