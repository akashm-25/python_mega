file = open("example1.txt",'w')
lists = ["hello", "this" , "akash"]
for i in lists:
	file.write(i+"\n")
file.close()
