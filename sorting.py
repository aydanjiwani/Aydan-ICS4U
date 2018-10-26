def Bubblesort (sortlist):
	donezo = false
	while(!donezo):
		donezo = true
		for i in range (0,len(sortlist)):
	
			if(sortlist[i] > sortlist[i+1])
				placeholder = sortlist[i]
				sortlist[i] = sortlist[i+1]
				sortlist[i+1] = placeholder
				donezo = false
	print(sortlist)
	return sortlist
	
	

def Insertionsort (sortlist):

		for i in range (0,len(sortlist)):
			current = sortlist[i]
			 while i>0 and sortlist[i-1]>current:
           sortlist[i] = sortlist[i-1]
           i = i-1
          sortlist[i] = current
	print(sortlist)
	return sortlist
	
	#note: the assignment calls for 50mb of data to be sorted, which is 50,000,000 bytes. 
	#Since these algorithms are O(n^2), the computer will have to perform 2.5E15 operations, taking approximately 10 days for a 2.7 GHZ processor 
	#Built in sort is (n logn), taking approximately 0.47 seconds with 2.7 GHz
	
f = open("sortingdata.txt", "r")

filelist = f

Bubblesort(filelist)
Insertionsort(filelist)
print(filelist.sorted())