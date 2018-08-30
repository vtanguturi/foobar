def findShortestPath(startx, starty, maze):
    w = len(maze[0])
    h = len(maze)
    visitedCount = [[None for i in range(w)] for i in range(h)]
    visitedCount[startx][starty] = 1
    possibleMoves = [[1,0],[-1,0],[0,-1],[0,1]]
    
    visited = [(startx, starty)]
    while visited:
        currx, curry = visited.pop(0)
        for move in possibleMoves :
          newx, newy = currx + move[0], curry + move[1]
          if newx in range(h) and newy in range(w):
            if visitedCount[newx][newy] is None:
                visitedCount[newx][newy] = visitedCount[currx][curry] + 1
                if maze[newx][newy] == 1 :
                  continue
                visited.append((newx, newy)) 
                  
    return visitedCount

def answer(maze):
  w = len(maze[0])
  h = len(maze)
  forPath = findShortestPath(0, 0, maze)
  backPath = findShortestPath(h-1, w-1, maze)

  ans = float('inf')
  for i in range(h):
      for j in range(w):
          if forPath[i][j] and backPath[i][j]:
              ans = min(forPath[i][j] + backPath[i][j] - 1, ans)
  return ans
