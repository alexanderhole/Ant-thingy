import tkinter as tk

root = tk.Tk()
gridCanvasSize = 1000
maxX = 20
maxY = 20
centre = int(20/2)
squareSize = int(gridCanvasSize/maxX)
root.geometry(str(gridCanvasSize) + "x" + str(gridCanvasSize))  # set starting size of window

cells = []
for x in range(0, maxX):
    xrow = []
    for y in range(0, maxY):   
        frame = tk.Frame(root, width=squareSize, height=squareSize,  borderwidth=4,relief="sunken")
        frame.grid(row=x, column=y)
        xrow.append(frame)
    
    cells.append(xrow)
        

image = tk.PhotoImage(file="ant.png").subsample(4,4)
img = tk.Label(root, image=image,width=squareSize, height=squareSize)
ant = [centre,centre,3, img]
# Create an object of tkinter ImageTk
img.grid(row=ant[0], column=ant[1])


cells[ant[0]][ant[1]].config(background="black")

def turnAnt(direction, background):
    if(background == "black"):
        direction = direction + 1
        if(direction > 4):
            direction = 1
    else:
        direction = direction - 1
        if(direction < 1):
            direction = 4
    return direction
def moveAntforward(ant):
    if(ant[2] == 1):
        if(ant[0] != 0):
            ant[0] = ant[0]-1
    if(ant[2] == 2):
        if(ant[1] != maxY):
            ant[1] = ant[1]+1
    if(ant[2] == 3):
        if(ant[0] != maxX):
            ant[0] = ant[0]+1
    if(ant[2] == 4):
        if(ant[1] != 0):
            ant[1] = ant[1]-1  
      
def redraw():

    img.grid(row=ant[0], column=ant[1])
    newdirection = turnAnt(ant[2], cells[ant[0]][ant[1]]["bg"])
    ant[2] = newdirection
    moveAntforward(ant)
    print(cells[ant[0]][ant[1]]["bg"])
    print(ant)
    if(cells[ant[0]][ant[1]]["bg"] == "black"):
        cells[ant[0]][ant[1]].config(background="white")
    else:
        cells[ant[0]][ant[1]].config(background="black")
    root.after(100,redraw)


root.after(500,redraw)
root.mainloop()