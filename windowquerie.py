import sys

def scan(file,filetype):
    flag = 0
    if(filetype == "dir"):
        while True:
            if(flag==1):
                field = next(file).split(" ")
                field = [f.strip() for f in field]
                field = [int(f) for f in field]
                yield field
            else:
                field = next(file).split(" ")
                field = [f.strip() for f in field]
                field = [float(f) for f in field]
                flag = 1
                yield field
    elif(filetype == "grd"):
        while True:
            field = next(file).split(" ")
            field = [f.strip() for f in field]
            field = [float(f) for f in field]
            field[0] = int(field[0])
            yield field

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def getCellPos(x,y,limitsarray):
    dx = (limitsarray[1] - limitsarray[0]) / 10
    dy = (limitsarray[3] - limitsarray[2]) / 10
    xposition = (x - limitsarray[0]) / dx
    yposition = (y - limitsarray[2]) / dy
    cellX =int( xposition )
    cellY =int( yposition )
    return [cellX,cellY,xposition,yposition]

def writeToFile(my_list):
    with open('queryanswer.txt', 'w') as f:
        for item in my_list:
            f.write("%s\n" % item)

def windowQ(x_low,x_high,y_low,y_high,limitsarray,cellmatrix,pointsmatrix):
    queryanswer = []

    if(x_low>x_high):
        print "Error x_low>x_high"
        exit(0)
    elif(y_low>y_high):
        print "Error y_low>y_high"
        exit(0)

    firstcell = getCellPos(x_low,y_low,limitsarray)
    secondcell = getCellPos(x_high,y_high,limitsarray)

    cellsminX = firstcell[2]
    cellsminY = firstcell[3]
    cellsmaxX = secondcell[2]
    cellsmaxY = secondcell[3]

    intersectingcellsarray = []
    for i in range(firstcell[0],secondcell[0]+1):
        for j in range(firstcell[1],secondcell[1]+1):
            if(i<10 and j<10 and i>=0 and j>=0):
                intersectingcellsarray.append([i,j])

    for cell in intersectingcellsarray:
        if(cell[0]>=cellsminX and cell[0]+1<=cellsmaxX and cell[1]>=cellsminY and cell[1]+1<=cellsmaxY):
            cell.append("full")
        else:
            cell.append("check")

    numberofpointsadded = 0
    for cell in intersectingcellsarray:
        for cellmatrixcell in cellmatrix:
            if(cellmatrixcell[0]==cell[0] and cellmatrixcell[1]==cell[1]):
                if(cell[2]=="full"):
                    for i in range(cellmatrixcell[3]):
                        queryanswer.append(pointsmatrix[cellmatrixcell[2]+i])
                        numberofpointsadded+=1
                elif(cell[2]=="check"):
                    for i in range(cellmatrixcell[3]):
                        point = pointsmatrix[cellmatrixcell[2]+i]
                        pointposition = getCellPos(point[1],point[2],limitsarray)
                        pointx = pointposition[2]
                        pointy = pointposition[3]
                        if(pointx>=cellsminX and pointx<=cellsmaxX and pointy>=cellsminY and pointy<=cellsmaxY):
                            queryanswer.append(point)
                            numberofpointsadded+=1

    writeToFile(queryanswer)

                #AESTHETIC PRINTS START
    print "--------------------------------"
    for point in queryanswer:
        print point
    print "--------------------------------"
    print "--------------------------------------"
    for cell in intersectingcellsarray:
        if(cell[2]=="full"):
            print "Completely covered by window : " +"["+ cell[0].__str__()+","+cell[1].__str__() +"]"
        elif(cell[2]=="check"):
            print "Partially covered by window : "+"["+ cell[0].__str__()+","+cell[1].__str__() +"]"
    print "--------------------------------------"
    print "-----------------------------"
    print "WindowX_low : "+cellsminX.__str__()+"\nWindowX_high : "+cellsmaxX.__str__()+"\nWindowY_low : "+cellsminY.__str__()+"\nWindowY_max : "+cellsmaxY.__str__()
    print "-----------------------------"+"\n"+"-----------------------------"
    print "  Points in Window : " + numberofpointsadded.__str__()
    print "-----------------------------"
                #END OF PRINTS

def initMatrices():
    griddir = open("grid.dir","r")
    gridgrd = open("grid.grd","r")

    cellparser = scan(griddir,"dir")
    pointparser = scan(gridgrd,"grd")

    cellmatrix = []
    pointsmatrix = []

    numberofcells = file_len("grid.dir")
    numberofpoints = file_len("grid.grd")
    numberofrestaurants = numberofpoints

    limitsarray = next(cellparser)

    for i in range(numberofcells-1):
        cell = next(cellparser)
        cellmatrix.append(cell)
    for i in range(numberofpoints):
        point = next(pointparser)
        pointsmatrix.append(point)

    griddir.close()
    gridgrd.close()
    return [cellmatrix,pointsmatrix,limitsarray]

def main(argv1,argv2,argv3,argv4):

    argv1 = float(argv1)
    argv2 = float(argv2)
    argv3 = float(argv3)
    argv4 = float(argv4)

    matrices = initMatrices()
    cellmatrix = matrices[0]
    pointsmatrix = matrices[1]
    limitsarray = matrices[2]
    matrices = []

    windowQ(argv1,argv2,argv3,argv4,limitsarray,cellmatrix,pointsmatrix)

if __name__ == "__main__":
    main(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
