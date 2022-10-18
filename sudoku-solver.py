from random import randrange, shuffle
import random
numarr = [[0]*9 for i in range(9)]
# numarr=[[9,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,8,9],
#         [0,0,0,1,0,9,0,0,5],
#         [0,0,0,0,0,5,8,9,0],
#         [3,0,0,0,0,0,2,1,4],
#         [0,8,9,0,0,4,0,0,6],
#         [4,2,3,6,8,0,0,0,1],
#         [5,6,0,9,0,0,4,0,0],
#         [8,9,7,5,4,1,6,2,3]]
newarr = [1,2,3,4,5,6,7,8,9]
shuffle(newarr)
def checkRow(row,num):
    for col in range(9):
        if(numarr[row][col]==num):
            return False
    return True
def checkCol(col,num):
    for row in range(9):
        if(numarr[row][col]==num):
            return False
    return True
def checkSq(numarr,row,col,num):
    for i in range(int(row/3)*3,int(row/3)*3+3):
        for j in range(int(col/3)*3,int(col/3)*3+3):
            if(numarr[i][j]==num):
                return False
    return True
def checkValid(numarr,row,col,num):
    isRow = checkRow(row,num)
    isCol = checkCol(col,num)
    isBox = checkSq(numarr,row,col,num)
    if(isRow and isCol and isBox):
        return True
    return False

def genBoard(numarr):
    x=0

    for i in range(3):
        for j in range(3):
            num = randrange(15)
            if(num<10):
                numarr[i][j]=newarr[x]
                x+=1
    x=0
    shuffle(newarr)
    for i in range(3,6):
        for j in range(3,6):
            num = randrange(15)
            if(num<10):
                numarr[i][j]=newarr[x]
                x+=1
    x=0
    shuffle(newarr)
    for i in range(6,9):
        for j in range(6,9):
            num = randrange(15)
            if(num<10):
                numarr[i][j]=newarr[x]
                x+=1






    def checkBox(num):
        for row in range(3,6):
            for col in range(3):
                if(numarr[row][col]==num):
                    return False
        return True
    def checkBox1(num):
        for row in range(6,9):
            for col in range(3):
                if(numarr[row][col]==num):
                    return False
        return True
    def checkBox2(num):
        for row in range(6,9):
            for col in range(3,6):
                if(numarr[row][col]==num):
                    return False
        return True
    def checkBox3(num):
        for row in range(3,6):
            for col in range(6,9):
                if(numarr[row][col]==num):
                    return False
        return True
    def checkBox4(num):
        for row in range(3):
            for col in range(3,6):
                if(numarr[row][col]==num):
                    return False
        return True
    def checkBox5(num):
        for row in range(3):
            for col in range(6,9):
                if(numarr[row][col]==num):
                    return False
        return True
    row=3
    count=0
    while(row<6):
        col=0
        while (col<3):
            shuffle(newarr)
            num = newarr[0]
            isRow = checkRow(row,num)
            isCol = checkCol(col,num)
            isBox = checkBox(num)
            count+=1
            if(count>6):
                break
            if(isRow and isCol and isBox):
                numarr[row][col]=num
                col+=1
        if(count>6):
            break
        row+=1
    row=6
    count=0
    while(row<9):
        col=0
        while (col<3):
            shuffle(newarr)
            num = newarr[0]
            isRow = checkRow(row,num)
            isCol = checkCol(col,num)
            isBox = checkBox1(num)
            count+=1
            if(count>6):
                break
            if(isRow and isCol and isBox):
                numarr[row][col]=num
                col+=1
        if(count>6):
            break
        row+=1
    row=6
    count=0
    while(row<9):
        col=3
        while (col<6):
            shuffle(newarr)
            num = newarr[0]
            isRow = checkRow(row,num)
            isCol = checkCol(col,num)
            isBox = checkBox2(num)
        
            count+=1
            if(count>6):
                break
            if(isRow and isCol and isBox):
                numarr[row][col]=num
                col+=1
        if(count>6):
            break
        row+=1
    row=3
    count=0
    while(row<6):
        col=6
        while (col<9):
            shuffle(newarr)
            num = newarr[0]
            isRow = checkRow(row,num)
            isCol = checkCol(col,num)
            isBox = checkBox3(num)
        
            count+=1
            if(count>6):
                break
            if(isRow and isCol and isBox):
                numarr[row][col]=num
                col+=1
        if(count>6):
            break
        row+=1
    row=0
    count=0
    while(row<3):
        col=3
        while (col<6):
            shuffle(newarr)
            num = newarr[0]
            isRow = checkRow(row,num)
            isCol = checkCol(col,num)
            isBox = checkBox4(num)
            count+=1
            if(count>6):
                break
            if(isRow and isCol and isBox):
                numarr[row][col]=num
                col+=1
        if(count>6):
            break
        row+=1
    row=0
    count=0
    while(row<3):
        col=6
        while (col<9):
            shuffle(newarr)
            num = newarr[0]
            isRow = checkRow(row,num)
            isCol = checkCol(col,num)
            isBox = checkBox5(num)
            count+=1
            if(count>6):
                break
            if(isRow and isCol and isBox):
                numarr[row][col]=num
                col+=1
        if(count>6):
            break
        row+=1

def printBoard(numarr):

    for row in range(9):
        for col in range(9):
            if(col%3==0 ):
                print("\t", end="")
            print(numarr[row][col],end="")
        print("")
        if (row%3==2):
            print("\n")

def checkEmpty(numarr):
    for row in range(9):
        for col in range(9):
            if(numarr[row][col]==0):
                return (row,col)
    return None


def solve(numarr):
    empty = checkEmpty(numarr)
    if(empty==None):
        return True
    else:
        row,col = empty
    for i in range(1,10):
        if(checkValid(numarr,row,col,i)):
            numarr[row][col]=i
            if solve(numarr):
                return True

            numarr[row][col]=0
    return False
def genValidBoard(numarr):
    count=0
    while True:
        genBoard(numarr)
        printBoard(numarr)
        solve(numarr)
        printBoard(numarr)
        count+=1
        if(checkEmpty(numarr)==None or count>5):
            print("Sorry could not generate valid board")
            break
        

genValidBoard(numarr)     
# solve(numarr)
# printBoard(numarr)
# printBoard(numarr)
# solve(numarr)
# printBoard(numarr)
        
