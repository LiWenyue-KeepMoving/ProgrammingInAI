from tkinter import *
import tkinter.messagebox  
import numpy as np

#创建窗口
root = Tk()                                 
root.title("Gobang")              
w1 = Canvas(root, width = 600, height = 600, background = 'yellow')
w1.pack() #布局方式全局统一

for i in range(0, 15):
    w1.create_line(i * 40 + 20, 20, i * 40 + 20, 580)
    w1.create_line(20, i * 40 + 20, 580, i * 40 + 20)
w1.create_oval(135, 135, 145, 145,fill='black')
w1.create_oval(135, 455, 145, 465,fill='black')
w1.create_oval(465, 135, 455, 145,fill='black')
w1.create_oval(455, 455, 465, 465,fill='black')
w1.create_oval(295, 295, 305, 305,fill='black')

num = 0
ComColor = 1
A = np.full((15,15),0)
B = np.full((15,15),'')

#落子坐标及由此产生的局面估值
class PointAndValue: 
    x = -1
    y = -1
    value = 0

#局面估值函数
def evaluateBoard(color):
    global A, B
    myValue = 0
    f = [[-1, 0], [-1, 1], [0, 1], [1, 1]]
    for i in range(0, 15): 
        for j in range(0, 15):
            if B[i][j] != color:
                continue
            for z in range(0, 4):
                PieceBlock = 0
                noneNum = 0
                a, b = f[z][0], f[z][1]
                count = 0
                x, y = i, j
                ifinside = False
                if x - a >= 0 and y - b >= 0 and x - a < 15 and y - b < 15 and B[x - a][y - b] != color and B[x - a][y - b] != '': 
                    PieceBlock += 1         
                while True:
                     count += 1
                     if count == 5:
                         break
                     if x + a >= 0 and y + b >= 0 and x + a < 15 and y + b < 15:
                         ifinside = True
                     else:
                         ifinside = False
                     if ifinside and B[x + a][y + b] == B[i][j]:
                         [x, y] = np.array([x, y]) + np.array([a, b]) 
                     else:
                         if ifinside and B[x + a][y + b] != '':
                             [x, y] = np.array([x, y]) + np.array([a, b])
                             PieceBlock += 1
                             break
                         else:
                             if ifinside and B[x + a][y + b] == ''and x + a + a >= 0 and y + b + b >= 0 and x + a + a < 15 and y + b + b < 15 and B[x + a + a][y + b + b] == B[i][j] and noneNum == 0:
                                 [x, y] = np.array([x, y]) + np.array([a, b]) + np.array([a, b])
                                 noneNum += 1
                             else:
                                 break                       

                if count == 5 and noneNum == 0:
                    myValue += 10000000
                if count == 5 and noneNum == 1:
                    myValue += 50000

                if count == 4 and PieceBlock == 0 and noneNum == 0:
                    myValue += 100000
                if count == 4 and PieceBlock == 0 and noneNum == 1:
                    myValue += 80000
                if count == 4 and PieceBlock == 1 and noneNum == 0:
                    myValue += 50000
                if count == 4 and PieceBlock == 1 and noneNum == 1:
                    myValue += 10000
                if count == 4 and PieceBlock == 2 and noneNum == 0:
                    myValue += 4000
                if count == 4 and PieceBlock == 2 and noneNum == 1:
                    myValue += 2500

                if count == 3 and PieceBlock == 0 and noneNum == 0:
                    myValue += 60000
                if count == 3 and PieceBlock == 0 and noneNum == 1:
                    myValue += 9000
                if count == 3 and PieceBlock == 1 and noneNum == 0:
                    myValue += 9000
                if count == 3 and PieceBlock == 1 and noneNum == 1:
                    myValue += 5000
                if count == 3 and PieceBlock == 2 and noneNum == 0:
                    myValue += 3000
                if count == 3 and PieceBlock == 2 and noneNum == 1:
                    myValue += 2200

                if count == 2 and PieceBlock == 0 and noneNum == 0:
                    myValue += 1200              
                if count == 2 and PieceBlock == 1 and noneNum == 0:
                    myValue += 1000               
                if count == 2 and PieceBlock == 2 and noneNum == 0:
                    myValue += 800
    return myValue

#MAX-MIN搜索最佳局面点
def GetMaxValuePoint(left_step, now_color):
    global A, B
    most_valuable_point = PointAndValue()
    max_value = 0
    for i in range(4, 10):
        for j in range(4, 10):
            if B[i][j] != '':
                continue
            NewPoint = PointAndValue()
            NewPoint.x = i
            NewPoint.y = j
            B[i][j] = str(now_color)
            NewValue = evaluateBoard(str(now_color)) - evaluateBoard(str(3 - now_color))
            if NewValue >= 9000000:
                NewPoint.value = NewValue
                return NewPoint
            if left_step > 1:
                NextStepPoint = PointAndValue()
                NextStepPoint = GetMaxValuePoint(left_step - 1, 3 - now_color)
                NewValue = - NextStepPoint.value
            if most_valuable_point.x == -1 or NewValue > max_value:
                most_valuable_point = NewPoint
                max_value = NewValue
            B[i][j] = ''
    LastPossiblePoint = PointAndValue()
    LastPossiblePoint = most_valuable_point
    LastPossiblePoint.value = max_value
    return LastPossiblePoint
    
def callback(event):
    global num, A, B, ComColor

    for j in range (0,15):
        for i in range (0,15):
            if (event.x - 20 - 40 * i) ** 2 + (event.y - 20 - 40 * j) ** 2 <= 2 * 20 ** 2:
                break
        if (event.x - 20 - 40 * i) ** 2 + (event.y - 20 - 40 * j) ** 2 <= 2*20 ** 2:
            break
    if num % 2 == 0 and A[j][i] != 1:
        w1.create_oval(40*i+5, 40*j+5, 40*i+35, 40*j+35,fill='black')
        A[j][i] = 1
        B[j][i] = '1'
        num += 1
    if num % 2 != 0 and A[j][i] != 1 :
        w1.create_oval(40*i+5, 40*j+5, 40*i+35, 40*j+35,fill='white')
        A[j][i] = 1
        B[j][i] = '2'
        num += 1
    print(B)
    print()
    # 判断胜负
    f = [[-1, 0], [-1, 1], [0, 1], [1, 1]]
    for z in range(0, 4):
        a, b = f[z][0], f[z][1]
        count1, count2 = 0, 0
        x, y = j, i
        while B[x][y] == B[j][i]:
            count1 += 1
            if x + a >= 0 and y + b >= 0 and x + a < 15 and y + b < 15 and B[x + a][y + b] == B[j][i]:
                [x, y] = np.array([x, y]) + np.array([a, b])
            else:
                x, y = j, i
                break
        while B[x][y] == B[j][i]:
            count2 += 1
            if x - a < 15 and y - b < 15 and x - a >= 0 and y - b >= 0 and B[x - a][y - b] == B[j][i]:
                [x, y] = np.array([x, y]) - np.array([a, b])
            else:
                break
        if count1 + count2 == 6:
            if B[j][i] == '1':
                tkinter.messagebox.showinfo('asd','bw')
            else:
                tkinter.messagebox.showinfo('asd', 'ww')
    #搜索下一个子应落的位置
    if ComColor == 1:
        if num == 0:
            print("(7, 7)")
        else:
            if num == 2:
                flag = 0
                for m in range(4,10):
                    for n in range(4,10):
                        if (m >= 5 and m <= 9) or (n >= 5 and n <= 9) or A[m][n] == 1:
                            continue
                        print('advice for black: (', m, ' ', n, ')')
                        flag = 1
                        break
                    if flag == 1:
                        flag = 0
                        break
            else:
                if num % 2 == 0:
                    #极大极小搜索结果
                    ppoint = PointAndValue()
                    ppoint = GetMaxValuePoint(2, 1)
                    print("Here is stronger way for black: (", ppoint.x,' ', ppoint.y, ')')
                    #单层搜索结果
                    max_x = 0
                    max_y = 0
                    max_value = float("-inf")
                    for poi_x in range(0, 15):
                        for poi_y in range(0, 15):
                            if A[poi_x][poi_y] != 0:
                                continue
                            B[poi_x][poi_y] = '1'
                            now_value = evaluateBoard('1') - evaluateBoard('2')
                            if now_value > max_value:
                                max_x = poi_x
                                max_y = poi_y
                                max_value = now_value
                            B[poi_x][poi_y] = ''
                    print('advice for black: (', max_x, ' ', max_y, ')')
    if ComColor == 1:
        if num == 1:
            print("advice for white: (5, 9)")
        else:
            if num % 2 == 1:
                #极大极小搜索结果
                dpoint = PointAndValue()
                dpoint = GetMaxValuePoint(2, 1)
                print("Here is stronger way for white: (", dpoint.x,' ', dpoint.y, ')')
                #单层搜索结果
                max_x = 0
                max_y = 0
                max_value = float("-inf")
                for poi_x0 in range(0, 15):
                    for poi_y0 in range(0, 15):
                        if A[poi_x0][poi_y0] != 0:
                            continue
                        B[poi_x0][poi_y0] = '2'
                        now_value = evaluateBoard('2') - evaluateBoard('1')
                        if now_value > max_value:
                            max_x = poi_x0
                            max_y = poi_y0
                            max_value = now_value
                        B[poi_x0][poi_y0] = ''
                print('advice for white: (', max_x, ' ', max_y, ')')
               
w1.bind("<Button -1>",callback)
w1.pack()
def quit():
    root.quit()
#but = Button(root,text="q",width=10,height=1,command=quit,font=('黑体',15))
#but.pack()
mainloop()


