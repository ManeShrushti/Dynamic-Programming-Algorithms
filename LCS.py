# X = "AGGTAB"
#Y ="GXTXAYB"
  
def lcs(s1,s2,l1,l2): 
  
    if l1==0 or l2==0: 
       return 0; 
    elif s1[l1-1]==s2[l2-1]: 
       return 1 + lcs(s1,s2,l1-1,l2-1); 
    else: 
       return max(lcs(s1,s2,l1,l2-1),lcs(s1,s2,l1-1,l2)); 

if __name__=='__main__':
	str1=raw_input("Enter the first string\n")
	str2=raw_input("Enter the first string\n")
	if(len(str1)< len(str2)):
		ans=lcs(str1,str2,len(str1),len(str2))
		print("Length of longest common subsequence is %d" %ans)
	else:
		ans=lcs(str2,str1,len(str2),len(str1))
		print("Length of longest common subsequence is %d" %ans)
