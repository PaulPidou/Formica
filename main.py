import tkinter as tk

class Grid(Canvas):
 "Main graphic class"
 def __init__(self, rows=128, cols=128, cellSize=8):
  Canvas.__init__(self)
  self.rows, self.cols, self.cellSize = rows, cols, cellSize
  self.configure(width = self.cellSize*self.rows, height = self.cellSize*self.cols)
  self.drawGrid()
 
 def drawGrid(self):
  "Draw grid" 
  for x in range(0, self.cellSize*self.rows, self.cellSize):
   self.create_line(x, 0, x, self.cellSize * self.rows)
 
  for y in range(0, self.cellSize*self.cols, self.cellSize):
   self.create_line(0, y, self.cellSize * self.cols, y)


# Programme de test
if __name__ == '__main__':
    window = tk.Tk()
    gr = Grid(window)
    gr.pack()
    window.mainloop()
