from tkinter import *
import random
import Algorithm

data = []

def show_explanation():
    display.delete("all")
    if algorithm.get() == 1:
        f = open("bubble_sort.txt", 'r')
    elif algorithm.get() == 2:
        f = open("insertion_sort.txt",'r')
    elif algorithm.get() == 3:
        f = open("quick_sort.txt")
    content = f.read()
    display.create_text(20,20,text=content,font="Arial 13 ",anchor=NW)
    root.update_idletasks()
    f.close()

def draw_columns(data, data_color):
    display.delete("all")
    drawing_height = 350
    drawing_width = 850
    column_width = drawing_width / (len(data))
    normalized_data = [i / max(data) for i in data]
    space = 5
    for i, height in enumerate(normalized_data):
        x0 = i * (column_width) + 25
        y0 = drawing_height - height * 340
        x1 = (i + 1) * (column_width) + 25
        y1 = drawing_height
        display.create_rectangle(x0 + 2, y0 + 5, x1, y1, fill=data_color[i])
        display.create_text(x0 + 10, y0, text=str(data[i]))
    root.update_idletasks()


def genrate():
    global data
    array_size = int(size_scale.get())
    sorting_speed = int(speed_scale.get())
    min_size = int(min_scale.get())
    max_size = int(max_scale.get())
    data = []
    for i in range(array_size):
        data.append(random.randrange(min_size, max_size + 1))
    draw_columns(data, ["cyan" for i in range(len(data))])


def start():
    global data
    if algorithm.get() == 1:
        Algorithm.Bubble_Sort(data, draw_columns, speed_scale.get())
    elif algorithm.get()==2:
        Algorithm.Insertion_Sort(data,draw_columns,speed_scale.get())
    elif algorithm.get() == 3:
        Algorithm.Quick_Sort(data, 0, len(data) - 1, draw_columns, speed_scale.get())
        draw_columns(data, ['lawn green' for i in range(len(data))])


root = Tk()
root.title("Group 8 CWP Course Project")
root.geometry("900x600")
root.maxsize(900, 600)
root.minsize(900, 600)

algorithm = IntVar()
algorithm.set(1)

Label(root, text="Visualization of Sorting Algorithm", font="Arial 15 bold").grid(row=0, column=0, pady=5)

Algorithm_frame = Frame(root)
Algorithm_frame.grid(row=1, column=0)

UI = Frame(root, height=190, width=900)
UI.grid(row=2, column=0)

display = Canvas(root, height=400, width=900)
display.grid(row=3, column=0)

Label(Algorithm_frame, text="Algorithm:", font="Arial").grid(row=0, column=0, pady=5)
Radiobutton(Algorithm_frame, text="Bubble Sort", variable=algorithm, value=1).grid(row=0, column=1)
Radiobutton(Algorithm_frame, text="Insertion Sort", variable=algorithm, value=2).grid(row=0, column=2)
Radiobutton(Algorithm_frame, text="Quick Sort", variable=algorithm, value=3).grid(row=0, column=3)

Label(UI, text="Size", font="Arial").grid(row=0, column=0, padx=25, pady=10)
size_scale = Scale(UI, from_=5, to=25, orient=HORIZONTAL)
size_scale.set(10)
size_scale.grid(row=0, column=1)

Label(UI, text="Speed", font="Arial").grid(row=0, column=3, padx=25, pady=10)
speed_scale = Scale(UI, from_=1, to=5, orient=HORIZONTAL)
speed_scale.set(1)
speed_scale.grid(row=0, column=4)

Label(UI, text="Min Value", font="Arial").grid(row=1, column=0, padx=25, pady=10)
min_scale = Scale(UI, from_=0, to=50, orient=HORIZONTAL)
min_scale.set(0)
min_scale.grid(row=1, column=1)

Label(UI, text="Max Value", font="Arial").grid(row=1, column=3, padx=25, pady=10)
max_scale = Scale(UI, from_=5, to=50, orient=HORIZONTAL)
max_scale.set(25)
max_scale.grid(row=1, column=4)

Button(UI, text="Generate", command=genrate).grid(row=2, column=1, pady=10)
Button(UI, text="Start", command=start).grid(row=2, column=2, pady=10)
Button(UI, text="Explanation",command=show_explanation).grid(row=2,column=3,pady=10)

root.mainloop()
