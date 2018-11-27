mat=[]
dist=[]
N=0
def floyd():
	global N
	for i in range(N):
		temp_list=[]
		for j in range(N):
			temp_list.append(mat[i][j])
		dist.append(temp_list)
	
	for i in range(N):
		for j in range(N):
			for k in range(N):
				if (dist[j][i] + dist[i][k] < dist[j][k]):
                   			 dist[j][k] = dist[j][i] + dist[i][k]  

	printarray()

def printarray():
	 
    print("The shortest distances matrix:\n") 
    for i in range(N):
	for j in range(N):
            if (dist[i][j]==1010):
                print("xx  "), 
            else:
                print("%d   " %dist[i][j]),
        print("\n") 
     
				
	
if __name__=="__main__":

	s=0
	n=raw_input("Enter the number of vertices\n")
	N=int(n)	
	print("Enter the cost of edges and enter 1010 for infinite symbol\n")
	for i in range(N):
		temp_list=[]
		for j in range(N):
				val=raw_input(str(i+1)+" --> "+str(j+1)+": ")
				print("\n")
				temp_list.append(int(val))
		mat.append(temp_list)
	floyd()
