from collections import deque
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 1, 0, 1, 1, 1],
    [1, 1, 0, 1, 1, 0, 1, 1, 1],
    [1, 1, 0, 0, 0, 0, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
]

start = (1,1)
end = (7,7)
directions = [(1,0),(-1,0),(0,1),(0,-1)]
queue = deque([start])
parents = {start:None}

while queue:
    current = queue.popleft()
    if current == end:
        path = []
        while current:
            path.append(current)
            current = parents[current]
        path.reverse()
        print(path)
        break
    for direction in directions:
        row,col = current[0]+direction[0],current[1]+direction[1]
        if 0 <= row < len(maze) and 0 <= col < len(maze[0]) and maze[row][col] == 0 and (row,col) not in parents:
            queue.append((row,col))
            parents[(row,col)] = current
else:
    print("Error")

    # maze = CreatMaze()
    # 初始化起点，终点，记录路径，走法，队列
    # start = (1,1)
    # end = (7,7)
    # parents = {start:None}
    # queue = deque([start])
    # directions = [(-1,0),(1,0),(0,-1),(0,1)]
    # while queue:
    #     current = queue.popleft()
    #     if current == end:
    #         path = []
    #         while current:
    #             path.append(current)
    #             current = parents[current]
    #         path.reverse()
    #         print(path)
    #         break
    #
    #     for direction in directions:
    #         row,col = current[0]+direction[0],current[1]+direction[1]
    #         if 0<=row<len(maze) and 0<=col<len(maze[0]) and maze[row][col]==0 and (row,col) not in parents:
    #             queue.append((row,col))
    #             parents[row,col] = current
    # else:
    #     print("Error")