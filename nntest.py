from math import sqrt
x = 39.68009
y = 116.4
id = 0

arr = []
with open("grid.grd","r") as file:
	row = file.readline()
	while(id < 51969):
		row = file.readline()
		rowArray = row.rstrip().split(" ")
		testX = float(rowArray[1])
		testY = float(rowArray[2])
		d = sqrt( ( (x - testX)**2 ) + ( (y - testY)**2 )  )
		arr.append([rowArray[0],rowArray[1],rowArray[2],d])
		id += 1

arr = sorted (arr, key=lambda x: x[3])

for i in range(15):
	print arr[i]
