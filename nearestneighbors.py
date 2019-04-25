import sys,math
from windowquerie import scan,file_len,getCellPos,writeToFile,initMatrices

def mindist(q,cell,limitsarray):
    qpointposition = getCellPos(q[1],q[2],limitsarray)
    distance = (qpointposition[1]-cell[0])**2 + (qpointposition[2]-cell[1])**2
    distance = math.sqrt(distance)
    return distance

def main():
    matrices = initMatrices()
    cellmatrix = matrices[0]
    pointsmatrix = matrices[1]
    limitsarray = matrices[2]
    matrices = []
    # print cellmatrix[0]
    # print pointsmatrix[0]
    mindist(pointsmatrix[0],cellmatrix[0],limitsarray)

if __name__ == "__main__":
    main()
