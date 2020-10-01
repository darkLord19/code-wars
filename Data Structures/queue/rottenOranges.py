class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
def isDelim(cell):
        return cell.x == -1 and cell.y == -1 

def isValid(x, y, r, c):
        return x >=0 and y>=0 and x < r and y < c

def checkAll(arr, r, c):
    for i in range(r):
        for j in range(c):
            if arr[i][j] == 1:
                return True

    return False
def printQueue(queue):
    for i in range(len(queue)):
        print(queue[i].x, queue[i].y, end=', ')
    print()

def rotOranges(arr, r, c):
    queue = []
    temp = None
    ans = 0
    # store all the cells having rotten oranges in the first time frame

    for i in range(r):
        for j in range(c):
            if arr[i][j] == 2:
                print("*")
                queue.append(Cell(i, j))

    # add delimiter
    queue.append(Cell(-1, -1))

    # BFS

    while len(queue) != 0:
        flag = False
        # process all the rotten oranges in the current time frams
        while len(queue) != 0 and not isDelim(queue[0]):
            printQueue(queue)
            temp = queue[0]
            # check right adjacent cell if it can be rotten
            if isValid(temp.x, temp.y+1, r, c) and arr[temp.x][temp.y+1] == 1:
                # add time frame in the total answer if it's not added
                if not flag:
                    ans+=1
                    flag = True
                arr[temp.x][temp.y+1] = 2
                queue.append(Cell(temp.x, temp.y+1))

            # check left adjacent cell
            if isValid(temp.x, temp.y-1, r, c) and arr[temp.x][temp.y-1] == 1:
                # add time frame in the total answer if it's not added
                if not flag:
                    ans+=1
                    flag = True
                arr[temp.x][temp.y-1] = 2
                queue.append(Cell(temp.x, temp.y-1))

            # check top adjacent cell
            if isValid(temp.x-1, temp.y, r, c) and arr[temp.x-1][temp.y] == 1:
                # add time frame in the total answer if it's not added
                if not flag:
                    ans+=1
                    flag = True
                arr[temp.x-1][temp.y] = 2
                queue.append(Cell(temp.x-1, temp.y))

            # check bottom adjacent cell
            if isValid(temp.x+1, temp.y, r, c) and arr[temp.x+1][temp.y] == 1:
                # add time frame in the total answer if it's not added
                if not flag:
                    ans+=1
                    flag = True
                arr[temp.x+1][temp.y] = 2
                queue.append(Cell(temp.x+1, temp.y))

            queue.pop(0)

        # pop previous delimiter from the front
        queue.pop(0)
        
        if len(queue)!=0:
            # add new elimiter at the last
            queue.append(Cell(-1, -1))

    
    return -1 if checkAll(arr, r, c) else ans


arr = [
    [2,1,0,2,1],
    [1,0,1,2,1],
    [1,0,0,2,1]
]

print(rotOranges(arr, 3, 5))