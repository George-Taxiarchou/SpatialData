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
    return [cellX,cellY]

def windowQ(x_low,x_high,y_low,y_high,limitsarray):
    if(x_low>x_high):
        print "error x_low>x_high"
        exit(0)
    elif(y_low>y_high):
        print "error y_low>y_high"
        exit(0)
    firstcell = getCellPos(x_low,y_low,limitsarray)
    secondcell = getCellPos(x_high,y_high,limitsarray)
    intersectingcellsarray = []
    for i in range(firstcell[0],secondcell[0]+1):
        for j in range(firstcell[1],secondcell[1]+1):
            intersectingcellsarray.append([i,j])
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

    print windowQ(39.723371,39.72927,116.119278,116.163056,limitsarray)




main()
