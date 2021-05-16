
class Node:
    def __init__(self, parent, pos):
        self.parent = parent
        self.pos = pos
        self.level = int
        self.childs = []


class Search:
    def __init__(self, start):
        self.start = start
        start = [start[0]-1, start[1]-1]
        print(start)
        print(type(start))
        rightNear = self.findNeighbors(start)
        print("rightNear")
        print(rightNear)
        root = Node(None, start)
        root.level = 1
        pathList = self.treeGrow(rightNear, root)
        return pathList
    #set start node and grow

    def findNeighbors(self, ori):
        neighborlist = []
        x = ori[0];
        y = ori[1];
        if ((x - 1) >= 0 and (x - 1) < 8):
            neighborlist.append([x - 1,y])
        if ((y - 1) >= 0 and (y - 1) < 8):
            neighborlist.append([x, y - 1])
        if ((x + 1) < 8):
            neighborlist.append([x + 1, y])
        if ((y + 1) < 8):
            neighborlist.append([x, y + 1])
        return neighborlist
    #find the neighbors of the node on the gameboard

    def treeGrow(self, rightNear, node):
        childPos = self.findNextMove(node)
        if len(childPos) > 0:
            print("searching")
            childNodes = []
            for i in range(0,len(childPos)):
                child = childPos[i]
                childNode = Node(node, child)
                childNode.level = node.level + 1
                childNodes.append(childNode)
                self.treeGrow(rightNear, childNode)
            node.childs = childNodes
     #recursion

        else:
            if node.level == 64:    #the 64th step
                print("last=>" + str(node.level))
                lastPos = node.pos
                lastPosString = str(lastPos[0])+","+str(lastPos[1])
                print("lastPosString=>" + lastPosString)
                for j in range(0, len(rightNear)):
                    near = rightNear[j]
                    nearPos = str(near[0])+","+str(near[1])
                    print("nearPos=>" + nearPos)
                    if lastPosString == nearPos:    #the last step is next to the start
                        print("done:")
                        pathList = self.dumpTree(node)  #find the path
                        return pathList



    def dumpTree(self, node):
        pathList = []
        self.checkTreePathPos(pathList, node)
        return pathList
    #called when done

    def findNextMove(self, node):
        neighbors = []
        pathList = []
        self.checkTreePathPos(pathList, node)
        neighborList = self.findNeighbors(node.pos)
        for i in range(0, len(neighborList)):
            near = neighborList[i]
            pos = str(near[0])+","+str(near[1])
            noteExist = False
            for j in range(0, len(pathList)):
                path = pathList[j]
                pathString = str(path[0])+","+str(path[1])
                if pathString == pos:
                    noteExist = True
                    break
            if noteExist == False:
                neighbors.append(near)
                #if near isn't in the pathList, then append.
        return neighbors


    def checkTreePathPos(self, pathList, node):

        pathList.append(node.pos)
        if node.parent != None:
            self.checkTreePathPos(pathList, node.parent)
    #find the path from the start to the current node