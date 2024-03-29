import sys,math
from windowquerie import scan,file_len,getCellPos,writeToFile,initMatrices

def mindist(q,cell,limitsarray):
    qpointposition = getCellPos(q[1],q[2],limitsarray)
    dist = 0
    xstep = (limitsarray[1] - limitsarray[0]) / 10
    ystep = (limitsarray[3] - limitsarray[2]) / 10
    #cell is on top
    if(qpointposition[0] == cell[0] and cell[1]>qpointposition[1]):
        dqy = abs(q[2])
        dy = limitsarray[2]+cell[1]*ystep
        dist = (dqy-dy)**2
        dist = math.sqrt(dist)
    #cell is on bottom
    elif(qpointposition[0] == cell[0] and cell[1]<qpointposition[1]):
        dqy = abs(q[2])
        dy = limitsarray[2]+(cell[1]+1)*ystep
        dist = (dqy-dy)**2
        dist = math.sqrt(dist)
    #cell is left
    elif(cell[1]==qpointposition[1] and cell[0]<qpointposition[0]):
        dqx = abs(q[1])
        dx = limitsarray[0]+(cell[0]+1)*xstep
        dist = (dqx-dx)**2
        dist = math.sqrt(dist)
    #cell is right
    elif(cell[1]==qpointposition[1] and cell[0]>qpointposition[0]):
        dqx = abs(q[1])
        dx = limitsarray[0]+cell[0]*xstep
        dist = (dqx-dx)**2
        dist = math.sqrt(dist)
    #cell is on top right
    elif(cell[1]>qpointposition[1] and cell[0]>qpointposition[0]):
        dqx = abs(q[1])
        dqy = abs(q[2])
        dx = limitsarray[0]+cell[0]*xstep
        dy = limitsarray[2]+cell[1]*ystep
        dist = (dqx-dx)**2 + (dqy-dy)**2
        dist = math.sqrt(dist)
    #cell is on top left
    elif(cell[1]>qpointposition[1] and cell[0]<qpointposition[0]):
        dqx = abs(q[1])
        dqy = abs(q[2])
        dx = limitsarray[0]+(cell[0]+1)*xstep
        dy = limitsarray[2]+cell[1]*ystep
        dist = (dqx-dx)**2 + (dqy-dy)**2
        dist = math.sqrt(dist)
    #cell is on bottom right
    elif(cell[1]<qpointposition[1] and cell[0]>qpointposition[0]):
        dqx = abs(q[1])
        dqy = abs(q[2])
        dx = limitsarray[0]+cell[0]*xstep
        dy = limitsarray[2]+(cell[1]+1)*ystep
        dist = (dqx-dx)**2 + (dqy-dy)**2
        dist = math.sqrt(dist)
    #cell is on bottom left
    elif(cell[1]<qpointposition[1] and cell[0]<qpointposition[0]):
        dqx = abs(q[1])
        dqy = abs(q[2])
        dx = limitsarray[0]+(cell[0]+1)*xstep
        dy = limitsarray[2]+(cell[1]+1)*ystep
        dist = (dqx-dx)**2 + (dqy-dy)**2
        dist = math.sqrt(dist)
    return dist

def minpointsdist(q1,q2,limitsarray):
    q1pointposition = getCellPos(q1[1],q1[2],limitsarray)
    q2pointposition = getCellPos(q2[1],q2[2],limitsarray)
    q1x = abs(q1[1])
    q1y = abs(q1[2])
    q2x = abs(q2[1])
    q2y = abs(q2[2])
    dist = (q1x-q2x)**2 + (q1y-q2y)**2
    dist = math.sqrt(dist)
    return dist

def idItem(item):
    if(len(item)==4):
        return "cell"
    elif(len(item)==3):
        return "point"

def sortedQueue(queue):
    queue = sorted(queue, key=lambda distance: distance[-1])
    return queue

def appendedqueue(queue,item,point,limitsarray,appendedcells):
    if(idItem(item)=="cell" and (item not in appendedcells)):
        # appendedcells.append(item)
        distance = mindist(point,item,limitsarray)
        tempitem = item
        tempitem.append("cell")
        tempitem.append(distance)
        queue.append(tempitem)
    elif(idItem(item)=="point"):
        distance = minpointsdist(point,item,limitsarray)
        tempitem = item
        tempitem.append("point")
        tempitem.append(distance)
        queue.append(tempitem)
    queue = sortedQueue(queue)
    return queue

def initQueue(queue,point,limitsarray,cellmatrix,appendedcells):
    pointPos = getCellPos(point[1],point[2],limitsarray)
    tempmindist = mindist(point,cellmatrix[0],limitsarray)
    tempcell = cellmatrix[0]
    for cell in cellmatrix:
        if(pointPos[0]==cell[0] and pointPos[1]==cell[1]):
            tempcell = cell
            queue = appendedqueue(queue,cell,point,limitsarray,appendedcells)
        elif(pointPos[0]>=0 and pointPos[0]<=9 and pointPos[1]>=0 and pointPos[1]<=9):
            initcell = pointPos
            initcell[-2] = 0
            initcell[-1] = 0
            queue = appendedqueue(queue,initcell,point,limitsarray,appendedcells)
        else:
            print "\npoint outside the grid\n"
            for cell in cellmatrix:
                if(mindist(point,cell,limitsarray)<tempmindist):
                    tempcell = cell
                    tempmindist = mindist(point,tempcell,limitsarray)
            queue = appendedqueue(queue,tempcell,point,limitsarray,appendedcells)
        break


def getNearestNeighbor(queue,point,limitsarray,pointsmatrix,cellmatrix,appendedcells):
    while True:
        if(queue == [] ):
            print "NO MORE NEIGHBORS"
            exit(0)
        if(queue[0][-2]=="cell"):
            appendedcells.append(queue[0])
            c = queue[0]
            neighborcells = []
            for i in range(-1,2):
                for j in range(-1,2):
                    if(c[0]+i==c[0] and c[1]+j==c[1]):
                        continue
                    elif(c[0]+i>=0 and c[0]+i<=9 and c[1]+j>=0 and c[1]+j<=9):
                        for cell in cellmatrix:
                            if(cell[0]==c[0]+i and cell[1]==c[1]+j):
                                neighborcells.append(cell)
            queue.pop(0)
            for i in range(c[3]):
                queue = appendedqueue(queue,pointsmatrix[c[2]+i],point,limitsarray,appendedcells)
            for neighborcell in neighborcells:
                queue = appendedqueue(queue,neighborcell,point,limitsarray,appendedcells)
        elif(queue[0][-2]=="point"):
            p = queue[0]
            queue.pop(0)
            yield p




def main(k,x,y):
    k = int(k)
    x = float(x)
    y = float(y)

    matrices = initMatrices()
    cellmatrix = matrices[0]
    pointsmatrix = matrices[1]
    limitsarray = matrices[2]
    matrices = []
    queue = []
    appendedcells = []

    point = [-1,x,y]

    initQueue(queue,point,limitsarray,cellmatrix,appendedcells)

    neighbor = getNearestNeighbor(queue,point,limitsarray,pointsmatrix,cellmatrix,appendedcells)
    file = open('nearestNeighbors.txt', 'w')
    format = ['BeijingFile_Line','X','Y','Type','Distance']
    file.write(format.__str__()+'\n')
    print format

    count=0
    flag = k-1
    for j in range(k):
        n = next(neighbor).__str__()
        print n
        file.write(n+'\n')
        if(count==flag or count == len(pointsmatrix)-1):
            for cell in appendedcells:
                file.write(cell.__str__()+'\n')
                print cell
        count+=1
    file.close()

if __name__ == "__main__":
    main(sys.argv[1],sys.argv[2],sys.argv[3])
