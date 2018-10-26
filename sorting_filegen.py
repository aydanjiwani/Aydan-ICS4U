import random
numberlist = []
for i in range(0,50000000):
	numberlist.append(random.randint(0,1000000))

f = open("sortingdata.txt", "a")
f.write(numberlist)

f.close()