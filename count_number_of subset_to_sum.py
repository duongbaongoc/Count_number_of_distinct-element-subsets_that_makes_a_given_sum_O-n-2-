def answer(s):
	###################################
	#make a table of subset perfect sum
	
	#initialize the table
	table = []
	for i in range(s-1):
		table.append([0]*(s+1))
	
	#fill the table with values
	table[0][0] = 1
	table[0][1] = 1
	for i in range(1,s-1):
		for j in range(s+1):
			if (i-1>=0):
				table[i][j] += (table[i-1][j] != 0)*1
			if (j-i-1>=0):
				table[i][j] += (table[i-1][j-i-1] != 0)*4
				
	###################################
	#modify table values to store number of paths
	
	for i in range(1,s-1):
		for j in range(s+1):
			if (table[i][j] == 1):
				table[i][j] = table[i-1][j]
			elif (table[i][j] == 4):
				table[i][j] = table[i-1][j-i-1]
			elif (table[i][j] == 5):
				table[i][j] = table[i-1][j] + table[i-1][j-i-1]
	
	return table[s-2][s]

	
	
	
	
	
	
	
	
	
	
	
	
	
