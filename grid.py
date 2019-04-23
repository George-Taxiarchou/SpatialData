def scan(file):
    while True:
        field = next(file).split(" ")
        field = [f.strip() for f in field]
        field = [float(f) for f in field]
        yield field

class Cell():
    def __init__(self,gridx,gridy,minX,minY,maxX,maxY):
        self.gridx = gridx
        self.gridy = gridy
        self.minX = minX
        self.maxX = maxX
        self.minY = minY
        self.maxY = maxY
        cellpoints = []
        self.cellpoints = cellpoints
    def addPoint(self,point):
        self.cellpoints.append(point)

class Grid():
    def __init__(self,minX,maxX,minY,maxY):
        self.minX = minX
        self.maxX = maxX
        self.minY = minY
        self.maxY = maxY

        xstep = (maxX-minX)/10
        ystep = (maxY-minY)/10
        grid = []
        self.grid = grid

        for x in range(0,10):
            for y in range(0,10):
                cellminX = minX + x*xstep
                cellminY = minY + y*ystep
                cellmaxX = cellminX + xstep
                cellmaxY = cellminY + ystep
                cell = Cell(x,y,cellminX,cellminY,cellmaxX,cellmaxY)
                grid.append(cell)

    def getGrid(self):
        return self.grid

    def printGrid(self):
        for i in range(0,len(self.getGrid())):
            print [self.getGrid()[i].gridx
            ,self.getGrid()[i].gridy
            ,self.getGrid()[i].minX
            ,self.getGrid()[i].minY
            ,self.getGrid()[i].maxX
            ,self.getGrid()[i].maxY]


def main():
    restaurantFile = open ("Beijing_restaurants.txt","r")
    griddir = open("grid.dir","w")
    gridgrd = open("grid.grd","w")

    parser = scan(restaurantFile)
    numofCoords = int(next(parser)[0])

    coordsmatrix = []

    id = 1
    for i in range(numofCoords):
        coords = next(parser)
        x = coords[0]
        y = coords[1]
        coordsmatrix.append([x,y,id])
        id+=1


    coordsmatrix = sorted(coordsmatrix, key=lambda coordinate: coordinate[0])
    minX = coordsmatrix[0][0]
    maxX = coordsmatrix[-1][0]
    coordsmatrix = sorted(coordsmatrix, key=lambda coordinate: coordinate[1])
    minY = coordsmatrix[0][1]
    maxY = coordsmatrix[-1][1]
    coordsmatrix = sorted(coordsmatrix, key=lambda coordinate: coordinate[2])

    # tempmatrix.clear()

    grid = Grid(minX,maxX,minY,maxY)
    grid.printGrid()

    dx = (maxX - minX) / 10
    dy = (maxY - minY) / 10
    pointsadded=0
    # print len(coordsmatrix)
    # print coordsmatrix
    pointsmatrix = []
    for point in coordsmatrix:
        xposition = (point[0] - minX) / dx
        yposition = (point[1] - minY) / dy

        cellX =int( xposition )
        cellY =int( yposition )

        for cell in grid.getGrid():
            if(cellX==cell.gridx and cellY==cell.gridy):
                cell.addPoint(point)
                pointsmatrix.append(point)
                pointsadded+=1
            elif(cellX==10 and cell.gridx==9 and cellY==cell.gridy):
                cell.addPoint(point)
                pointsmatrix.append(point)
                pointsadded+=1
            elif(cellY==10 and cell.gridy==9 and cellX==cell.gridx):
                cell.addPoint(point)
                pointsmatrix.append(point)
                pointsadded+=1
            elif(cellX==10 and cellY==10 and cell.gridx==9 and cell.gridy==9):
                cell.addPoint(point)
                pointsmatrix.append(point)
                pointsadded+=1

    for cell in grid.getGrid():
        print cell.gridx,cell.gridy
        for cellpoint in cell.cellpoints:
            gridgrd.write(cellpoint[2].__str__()+" "+cellpoint[0].__str__()+" "+cellpoint[1].__str__()+"\n")
            # print cellpoint[2]

    print "Points in Grid : " + pointsadded.__str__()

    print minX,maxX,minY,maxY
    griddir.close()
    gridgrd.close()



main()
