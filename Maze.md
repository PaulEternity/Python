from collections import deque
import tkinter as tk
import numpy as np

def CreatMaze(row,col,obstacle_pos):
    maze = np.random.choice([0,1],size=(row,col),p = [1-obstacle_pos,obstacle_pos])
    maze[0,0] = 0
    maze[row-1,col-1] = 0
    return maze


def BFS(maze):
    rows,cols = maze.shape
    start = (0,0)
    end = (rows-1,cols-1)
    queue = deque([(start,[start])])
    visited = set()

    while queue:
        (x,y),path = queue.popleft()
        if (x,y) == end:
            return path
        if (x,y) in visited:
            continue
        visited.add((x,y))
        for (dx,dy) in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx,ny = x+dx,y+dy
            if 0<=nx<rows and 0<=ny<cols and maze[nx,ny] == 0:
                queue.append(((nx,ny),path+[(nx,ny)]))
    return None


def PrintMaze(canvas,maze,path = None):
    canvas.delete("all")
    rows,cols = maze.shape
    cell_size = 30
    for i in range(rows):
        for j in range(cols):
            x0,y0 = j*cell_size,i*cell_size
            x1,y1 = x0 + cell_size,y0+cell_size
            if path and (i,j) in path:
                canvas.create_rectangle(x0, y0, x1, y1, fill = "blue")
            elif maze[i, j] == 0:
                canvas.create_rectangle(x0, y0, x1, y1, fill = "white")
            else:
                canvas.create_rectangle(x0, y0, x1, y1, fill = "black")


def SolveMaze():
    rows = int(rows_entry.get())
    cols = int(cols_entry.get())
    ob = float(obstacle_prob.get())
    maze = CreatMaze(rows,cols,ob)
    path = BFS(maze)
    if path:
        PrintMaze(canvas,maze,path)
    else:
        result.config(text = "Error")



window = tk.Tk()
window.title("Maze")

tk.Label(window,text="行数：").pack()
rows_entry = tk.Entry(window)
rows_entry.pack()
tk.Label(window,text="列数：").pack()
cols_entry = tk.Entry(window)
cols_entry.pack()
tk.Label(window,text="障碍物概率: ").pack()
obstacle_prob = tk.Entry(window)
obstacle_prob.pack()
solve_button = tk.Button(window,text="输出迷宫",command=SolveMaze)
solve_button.pack()

canvas = tk.Canvas(window,width=300,height=300)
canvas.pack()
result = tk.Label(window,text="")
result.pack()

window.mainloop()

