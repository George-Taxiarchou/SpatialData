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

def windowQ(x_low,x_high,y_low,y_high,limitsarray):
    if(x_low>x_high):
        print "Error x_low>x_high"
        exit(0)
    elif(y_low>y_high):
        print "Error y_low>y_high"
        exit(0)

    if(x_low<limitsarray[0] or x_high>limitsarray[1] or y_low<limitsarray[2] or y_high>limitsarray[3]):
        print "Error , query out of grid bounds"
        exit(0)

    firstcell = getCellPos(x_low,y_low,limitsarray)
    secondcell = getCellPos(x_high,y_high,limitsarray)

    cellsminX = firstcell[2]
    cellsminY = firstcell[3]
    cellsmaxX = secondcell[2]
    cellsmaxY = secondcell[3]

    print '\n'
    print [cellsminX,cellsmaxX,cellsminY,cellsmaxY]
    print "\n"


    intersectingcellsarray = []
    for i in range(firstcell[0],secondcell[0]+1):
        for j in range(firstcell[1],secondcell[1]+1):
            intersectingcellsarray.append([i,j])

    for cell in intersectingcellsarray:
        print cell[0] , cell[1]
        if(cell[0]>=cellsminX and cell[0]+1<=cellsmaxX and cell[1]>=cellsminY and cell[1]+1<=cellsmaxY):
            cell.append("full")

    return intersectingcellsarray


def main():
    griddir = open("grid.dir","r")
    gridgrd = open("grid.grd","r")
    # beijing = open('Beijing_restaurants.txt',"r")

    cellparser = scan(griddir,"dir")
    pointparser = scan(gridgrd,"grd")
    # beijingparser = scan(beijing,"dir")

    cellmatrix = []
    pointsmatrix = []
    # beijingmatrix = []

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

    print windowQ(39.68009,39.772154,116.070466,116.425554,limitsarray)



main()
