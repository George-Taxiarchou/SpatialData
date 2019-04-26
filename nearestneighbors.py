import sys,math
from windowquerie import scan,file_len,getCellPos,writeToFile,initMatrices

def mindist(q,cell,limitsarray):
    qpointposition = getCellPos(q[1],q[2],limitsarray)
    dist = 0
    #cell is on top
    if(qpointposition[0] == cell[0] and cell[1]>qpointposition[1]):
        dqy = abs(qpointposition[3])
        dy = cell[1]
        dist = (dqy-dy)**2
        dist = math.sqrt(dist)
    #cell is on bottom
    elif(qpointposition[0] == cell[0] and cell[1]>qpointposition[1]):
        dqy = abs(qpointposition[3])
        dy = cell[1]+1
        dist = (dqy-dy)**2
        dist = math.sqrt(dist)
    #cell is left
    elif(cell[1]==qpointposition[1] and cell[0]<qpointposition[0]):
        dqx = abs(qpointposition[2])
        dx = cell[0]+1
        dist = (dqx-dx)**2
        dist = math.sqrt(dist)
    #cell is right
    elif(cell[1]==qpointposition[1] and cell[0]>qpointposition[0]):
        dqx = abs(qpointposition[2])
        dx = cell[0]
        dist = (dqx-dx)**2
        dist = math.sqrt(dist)
    #cell is on top right
    elif(cell[1]>qpointposition[1] and cell[0]>qpointposition[0]):
        dqx = abs(qpointposition[2])
        dqy = abs(qpointposition[3])
        dx = cell[0]
        dy = cell[1]
        dist = (dqx-dx)**2 + (dqy-dy)**2
        dist = math.sqrt(dist)
    #cell is on top left
    elif(cell[1]>qpointposition[1] and cell[0]<qpointposition[0]):
        dqx = abs(qpointposition[2])
        dqy = abs(qpointposition[3])
        dx = cell[0]+1
        dy = cell[1]
        dist = (dqx-dx)**2 + (dqy-dy)**2
        dist = math.sqrt(dist)
    #cell is on bottom right
    elif(cell[1]<qpointposition[1] and cell[0]>qpointposition[0]):
        dqx = abs(qpointposition[2])
        dqy = abs(qpointposition[3])
        dx = cell[0]
        dy = cell[1]+1
        dist = (dqx-dx)**2 + (dqy-dy)**2
        dist = math.sqrt(dist)
    #cell is on bottom left
    elif(cell[1]<qpointposition[1] and cell[0]<qpointposition[0]):
        dqx = abs(qpointposition[2])
        dqy = abs(qpointposition[3])
        dx = cell[0]+1
        dy = cell[1]+1
        dist = (dqx-dx)**2 + (dqy-dy)**2
        dist = math.sqrt(dist)
    return dist

def minpointsdist(q1,q2,limitsarray):
    q1pointposition = getCellPos(q1[1],q1[2],limitsarray)
    q2pointposition = getCellPos(q2[1],q2[2],limitsarray)
    q1x = abs(q1pointposition[2])
    q1y = abs(q1pointposition[3])
    q2x = abs(q2pointposition[2])
    q2y = abs(q2pointposition[3])
    dist = (q1x-q2x)**2 + (q1y-q2y)**2
    dist = math.sqrt(dist)
    return dist

def idItem(item):
    if(len(item)==4):
        return "cell"
    elif(len(item)==3):
        return "point"

def sortQueue(queue):
    queue = sorted(queue, key=lambda distance: distance[-1])

def appendqueue(queue,item,point,limitsarray):
    if(idItem(item)=="cell"):
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
    sortQueue(queue)

def initQueue(queue,point,limitsarray,cellmatrix):
    pointPos = getCellPos(point[1],point[2],limitsarray)
    tempmindist = mindist(point,cellmatrix[0],limitsarray)
    tempcell = cellmatrix[0]
    for cell in cellmatrix:
        if(pointPos[0]==cell[0] and pointPos[1]==cell[1]):
            appendqueue(queue,cell,point,limitsarray)
        else:
            for cell in cellmatrix:
                if(mindist(point,cell,limitsarray)<tempmindist):
                    tempcell = cell



# def getNearestNeighbor(queue,point,limitsarray):
#     while True:
#         appendqueue(queue,)

def main():
    matrices = initMatrices()
    cellmatrix = matrices[0]
    pointsmatrix = matrices[1]
    limitsarray = matrices[2]
    matrices = []
    queue = []

    argv1 = pointsmatrix[0][1]
    argv2 = pointsmatrix[0][2]

    point = [-1,argv1,argv2]

    initQueue(queue,point,limitsarray,cellmatrix)

    # print cellmatrix[10]
    # print getCellPos(pointsmatrix[0][1],pointsmatrix[0][2],limitsarray)
    # print mindist(pointsmatrix[0],cellmatrix[10],limitsarray)
    # print limitsarray
if __name__ == "__main__":
    main()
