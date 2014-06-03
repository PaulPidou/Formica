import tkinter as tk
 
window = tk.Tk()
rows = 128
cols = 128
cellSize = 8
canvas = tk.Canvas(window, width = cellSize*rows, height = cellSize*cols)

##  Draw grid  
for x in range(0, cellSize*rows, cellSize):
    canvas.create_line(x, 0, x, cellSize * rows)

for y in range(0, cellSize*cols, cellSize):
    canvas.create_line(0, y, cellSize * cols, y)
##

canvas.pack()
window.mainloop()
