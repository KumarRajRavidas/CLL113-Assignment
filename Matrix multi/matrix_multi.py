import os
def matrix_multi(li):
	M1=[]
	M2=[]
	# nm=li[0]
	n=int(li[0][0])
	m=int(li[0][1])
	for i in range(1,n+1):#for finding first matrix
		M1.append(li[i])
	n1m1=li[n+1]
	n1=int(li[n+1][0])
	m1=int(li[n+1][1])
	for k in range(n+2,len(li)):#for finding second matrix
		M2.append(li[k])
	result= [[0 for row in range(m1)] for col in range(n)]# m1 and n type of matrix 
	for i in range(len(M1)):
    		for j in range(len(M2[0])):
    				for k in range(len(M2)):
    						result[i][j] += int(M1[i][k]) * int(M2[k][j])
	return result

file = open("C:\\Users\\RAJ__DAS\\Desktop\\NEW.txt") # C:\Users\RAJ__DAS\Desktop\ you need to change the addres of input file
line = file.readline()#line read 
li=[]
items = line.split()
test=int(items[0])
t=0
while line and test>t:
	# print 't is =',t
	line = file.readline()
	items=line.split()
	if len(items)!=0:
		li.append(items)
	if len(items)==0 :
		t=t+1
		matrix_result=matrix_multi(li)
		out=str(matrix_result)
		outToFile = open("C:\\Users\\RAJ__DAS\\Desktop\\newopt.txt","a")
		# outToFile.write('matrix value is=')
		outToFile.write(out)
		outToFile.write("\n")
		outToFile.write("\n")
		del li[:]
#########################################################################
##input
# 4 
# 1 3
# 2 9 1
# 3 2
# 4 6
# 6 1
# 9 2

# 2 3
# 5 1 3
# 9 2 1
# 3 4
# 3 6 1 5
# 5 1 0 9
# 1 0 2 4

# 5 4
# 8 9 7 6 
# 2 5 7 9 
# 0 9 96 5
# 99 88 11 0
# 0 5 2 6 
# 4 3 
# 7 8 9 
# 0 6 3 
# 3 67 0 
# 8 66 9 

# 2 2
# 7 8 
# 0 9
# 2 3
# 890 876 123
# 976 32 98

##output
# [[71, 23]]

# [[23, 31, 11, 46], [38, 56, 11, 67]]

# [[125, 983, 153], [107, 1109, 114], [328, 6816, 72], [726, 2057, 1155], [54, 560, 69]]

# [[14038, 6388, 1645], [8784, 288, 882]]
###################################################################################