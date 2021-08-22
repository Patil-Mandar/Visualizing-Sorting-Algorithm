import time


def Bubble_Sort(data, draw_columns, speed):
    for i in range(len(data)):
        for j in range(len(data) - 1 - i):
            draw_columns(data, ['maroon1' if x == j or x == j + 1 else 'cyan' for x in range(len(data))])
            time.sleep(0.5 / speed)
            if data[j + 1] < data[j]:

                data[j], data[j + 1] = data[j + 1], data[j]
                draw_columns(data, ['gray47' if x == j or x == j + 1 else 'cyan' for x in range(len(data))])
                time.sleep(1 / speed)
    draw_columns(data, ['lawn green' for i in range(len(data))])


def Insertion_Sort(data,draw_columns,speed):
    for i in range(1,len(data)):
        current = data[i]
        j=i-1
        while data[j]>current and j>=0:
            data[j+1]=data[j]
            j-=1
        data[j+1]=current
        draw_columns(data, ['lawn green' if x<=i else 'cyan' for x in range(len(data))])
        time.sleep(1 / speed)



def partition(data, head, tail, draw_columns, speed):
    time.sleep(0.2)
    i = head - 1
    pivot = data[tail]
    for j in range(head, tail):
        if data[j] < pivot:
            i += 1
            draw_columns(data, ['maroon1' if x == j or x == i else 'cyan' for x in range(len(data))])
            time.sleep(0.5 / speed)
            data[i], data[j] = data[j], data[i]
            draw_columns(data, ['maroon1' if x == j or x == i else 'cyan' for x in range(len(data))])
            time.sleep(1 / speed)
    draw_columns(data, ['maroon1' if x == tail or x == i + 1 else 'cyan' for x in range(len(data))])
    time.sleep(0.5 / speed)
    data[i + 1], data[tail] = data[tail], data[i + 1]
    draw_columns(data, ['maroon1' if x == tail or x == i + 1 else 'cyan' for x in range(len(data))])
    time.sleep(1 / speed)
    return i + 1


def Quick_Sort(data, head, tail, draw_columns, speed):
    if (head < tail):
        pivot = partition(data, head, tail, draw_columns, speed)
        Quick_Sort(data, head, pivot - 1, draw_columns, speed)
        Quick_Sort(data, pivot + 1, tail, draw_columns, speed)
