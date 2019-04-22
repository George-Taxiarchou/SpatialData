import itertools
import numpy as np

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

    g = Grid(minX,maxX,minY,maxY)
    g.printGrid()

    print minX,maxX,minY,maxY
    griddir.close()
    gridgrd.close()



main()
