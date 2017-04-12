def getMin(n1, n2):
    if(n1 > n2):
        return n2
    else:
        return n1


def getMax(n1, n2):
    if(n1 > n2):
        return n1
    else:
        return n2


def segmentRectIntersect(xMin, xMax, yMin, yMax, x1, y1, x2, y2):
    

    if(x1 != x2 and y1 !=y2):
        return -1
    else:
        xLow = getMin(x1,x2)
        xHigh = getMax(x1,x2)
        yLow = getMin(y1,y2)
        yHigh = getMax(y1,y2)
    
    
    if(xLow == xHigh):

        if(xLow > xMax and xLow < xMax) :
            
            return 0

        elif(yLow > yMax and yHigh < yMin):
            
            return 0
        elif((yHigh > yMax and yLow < yMax) or (yLow < yMin and yHigh > yMax)):
            
            return 1

        else:
            
            return 2


    

    if(yLow == yHigh):
        if(yLow > yMax and yLow <yMax):
            
            return 0
        elif(xLow > xMax and xHigh < xMax):
            
            return 0
        elif((xHigh > xMax and xLow < xMax) or xLow < xMin and xHigh > xMax):
            return 1
            
        else:
            
            return 2


    

def rectRectIntersect(xMin1, xMax1, yMin1, yMax1, xMin2, xMax2, yMin2, yMax2):
    numbPoints = 0

    numbPoints = numbPoints + segmentRectIntersect(xMin1, xMax1, yMin1, yMax1, xMin2, yMax2, xMax2, yMax2)
    print numbPoints

    numbPoints = numbPoints + segmentRectIntersect(xMin1, xMax1, yMin1, yMax1, xMin2, yMin2, xMax2, yMin2)
    print numbPoints
    numbPoints = numbPoints + segmentRectIntersect(xMin1, xMax1, yMin1, yMax1, xMax2, yMin2, xMax2, yMax2)
    print numbPoints
    numbPoints = numbPoints + segmentRectIntersect(xMin1, xMax1, yMin1, yMax1, xMin2, yMin2, xMin2, yMax2)
    print numbPoints
    return numbPoints

def runProgram():
    r1x1 = input("Please enter a the x and y coordinate of a vertex of rectangle 1: ")
    r1y1 = input()

    r1x2 = input("Please enter a the x and y coordinate of the opposite vertex of rectangle 1: ")
    r1y2 = input()

    r2x1 = input("Please enter a the x and y coordinate of a vertex of rectangle 2: ")
    r2y1 = input()

    r2x2 = input("Please enter a the x and y coordinate of the opposite vertex of rectangle 2: ")
    r2y2 = input()
    


    xMin1 = getMin(r1x1,r1x2)
    xMax1 = getMax(r1x1,r1x2)
    yMin1 = getMin(r1y1,r1y2)
    yMax1 = getMax(r1y1,r1y2)
    xMin2 = getMin(r2x1,r2x2)
    xMax2 = getMax(r2x1,r2x2)
    yMin2 = getMin(r2y1,r2y2)
    yMax2 = getMax(r2y1,r2y2)

    
    numbIntersections = rectRectIntersect(xMin1, xMax1, yMin1, yMax1, xMin2, xMax2, yMin2, yMax2)

    print "The number of intersections of the two rectangles is: ", numbIntersections
    
