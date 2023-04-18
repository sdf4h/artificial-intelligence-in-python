from tkinter import *
import string
import ctypes
def fgh():
 xAxis = string.ascii_lowercase[0:7]
 yAxis = range(0, 12)

 cells = {}


 def evaluateCell(cellId):
    content = cells[cellId][0].get()
    content = content.lower()

    label = cells[cellId][1]

    if content.startswith('='):
        for cell in cells:
            if cell in content.lower():
                content = content.replace(cell, str(evaluateCell(cell)))

        content = content[1:]
        try:
            content = eval(content)
        except:
            content = 'NAN'
        label['text'] = content
        return content

    else:
        label['text'] = content
        return content


 def updateAllCells():
    root.after(10, updateAllCells)

    for cell in cells:
        evaluateCell(cell)


 root = Tk()
 root.resizable(0, 0)
 root.title('Приложение для электронных таблиц')

 for y in yAxis:
    label = Label(root, text=y, width=5, background='white')
    label.grid(row=y + 1, column=0)

 for i, x in enumerate(xAxis):
    label = Label(root, text=x, width=35, background='white')
    label.grid(row=0, column=i + 1, sticky='n')

 for y in yAxis:
    for xcoor, x in enumerate(xAxis):
        id = f'{x}{y}'

        var = StringVar(root, '', id)

        e = Entry(root, textvariable=var, width=30)
        e.grid(row=y + 1, column=xcoor + 1)

        label = Label(root, text='', width=5)
        label.grid(row=y + 1, column=xcoor + 1, sticky='e')

        cells[id] = [var, label]

 updateAllCells()

 root.mainloop()
import cv2
def vcb():


 cap = cv2.VideoCapture(0)

 cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
 cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

 ret, frame = cap.read()
 cv2.imwrite('photo.png', frame)

 cap.release()