#The objects of this class will be the tetrominos
class Tetromino:
    
    #In the constructor we randomly generate a type for the tetromino (7 different types)
    #Then based on the type we declare the blocks of the tetromino (we store the blocks as a list of 2 coordinates) and the color of the tetromino
    #And we also declare a position value which has a base value of 1 
    def __init__(self):

        #generate type
        from random import randrange
        self.ttype = randrange(1,8) #enumeration of the tetromino types: 1:square, 2:long, 3:reverse L, 4: L, 5:reverse Z, 6:Z, 7:T

        #generate blocks in starting position (above the height of 19 which is the highest row of the grid) based on type, we store the blocks in a list
        self.blocks = []
        if self.ttype == 1:
            self.blocks.append([4,21])
            self.blocks.append([5,21])
            self.blocks.append([4,20])
            self.blocks.append([5,20])
            self.color = (255,255,0)
        elif self.ttype == 2:
            self.blocks.append([3,20])
            self.blocks.append([4,20])
            self.blocks.append([5,20])
            self.blocks.append([6,20])
            self.color = (173, 216, 230)
        elif self.ttype == 3:
            self.blocks.append([3,21])
            self.blocks.append([3,20])
            self.blocks.append([4,20])
            self.blocks.append([5,20])
            self.color = (0, 82, 255)
        elif self.ttype == 4:
            self.blocks.append([5,21])
            self.blocks.append([3,20])
            self.blocks.append([4,20])
            self.blocks.append([5,20])
            self.color = (255, 140, 0)
        elif self.ttype == 5:
            self.blocks.append([4,21])
            self.blocks.append([5,21])
            self.blocks.append([3,20])
            self.blocks.append([4,20])
            self.color = (0, 255, 0)
        elif self.ttype == 6:
            self.blocks.append([3,21])
            self.blocks.append([4,21])
            self.blocks.append([4,20])
            self.blocks.append([5,20])
            self.color = (255, 0, 0)
        elif self.ttype == 7:
            self.blocks.append([4,21])
            self.blocks.append([3,20])
            self.blocks.append([4,20])
            self.blocks.append([5,20])
            self.color = (102,51, 153)

        #declaring the base position of the tetromino (this parameter will be modified by rotation)
        self.position = 1 

    # one method for every possible movement of a tetromino:

    def move_down(self):
        #Subtracting one from the vertical coordinates of the blocks
        self.blocks = [ [x,y-1] for [x,y] in self.blocks]

    def move_right(self,fix_blocks,border):
        #Adding one to the horizontal coordinates, but only if the border and the fix blocks allow it 
        blocks = [[x+1,y] for [x,y] in self.blocks]
        is_out = False
        for i in blocks:
            if i in border.blocks or i in fix_blocks.blocks:
                is_out = True
        if is_out == False:
            self.blocks = blocks

    def move_left(self,fix_blocks,border):
        #Subtracting one from the horizontal coordinates, but only if the border and the fix blocks allow it 
        blocks = [ [x-1,y] for [x,y] in self.blocks]
        is_out = False
        for i in blocks:
            if i in border.blocks or i in fix_blocks.blocks:
                is_out = True
        if is_out == False:
            self.blocks = blocks

    def move_up(self):
        #Adding one to the vertical coordinates of the blocks
        self.blocks = [ [x,y+1] for [x,y] in self.blocks]

    #This method will send the tetromino down to the bottom and fix it
    def move_down_fixate(self,fix_blocks):
        while True:
            blocks=[[i,j+1]for i,j in self.blocks]
            fix = False
            for i in self.blocks:
                if i in fix_blocks.blocks:
                    fix = True
            if fix == True:
                break
            else:
                self.move_down()


    #One method for every rotation of every tetromino based on the nintendo rotation system

    #The basic method:
    def rotate_base(self):
        
        #the square tetromino does not rotate

        #rotation of the long tetromino (2 different position)
        if self.ttype == 2:
                if self.position == 1:
                    self.blocks[0][0] += 2
                    self.blocks[0][1] += 2
                    self.blocks[1][0] += 1
                    self.blocks[1][1] += 1
                    self.blocks[3][0] -= 1
                    self.blocks[3][1] -= 1
                    self.position = 2
                else:
                    self.blocks[0][0] -= 2
                    self.blocks[0][1] -= 2
                    self.blocks[1][0] -= 1
                    self.blocks[1][1] -= 1
                    self.blocks[3][0] += 1
                    self.blocks[3][1] += 1
                    self.position = 1

        #rotation of the reverse L tetromino (4 different position)
        if self.ttype == 3:
                if self.position == 1:
                    self.blocks[0][0] += 2
                    self.blocks[1][0] += 1
                    self.blocks[1][1] += 1
                    self.blocks[3][0] -= 1
                    self.blocks[3][1] -= 1
                    self.position = 2
                elif self.position == 2:
                    self.blocks[0][1] -= 2
                    self.blocks[1][0] += 1
                    self.blocks[1][1] -= 1
                    self.blocks[3][0] -= 1
                    self.blocks[3][1] += 1
                    self.position = 3
                elif self.position == 3:
                    self.blocks[0][0] -= 2
                    self.blocks[1][0] -= 1
                    self.blocks[1][1] -= 1
                    self.blocks[3][0] += 1
                    self.blocks[3][1] += 1
                    self.position = 4
                elif self.position == 4:
                    self.blocks[0][1] += 2
                    self.blocks[1][0] -= 1
                    self.blocks[1][1] += 1
                    self.blocks[3][0] += 1
                    self.blocks[3][1] -= 1
                    self.position = 1

        #rotation of the L tetromino (4 different position)
        if self.ttype == 4:
                if self.position == 1:
                    self.blocks[0][1] -= 2
                    self.blocks[1][0] += 1
                    self.blocks[1][1] += 1
                    self.blocks[3][0] -= 1
                    self.blocks[3][1] -= 1
                    self.position = 2
                elif self.position == 2:
                    self.blocks[0][0] -= 2
                    self.blocks[1][0] += 1
                    self.blocks[1][1] -= 1
                    self.blocks[3][0] -= 1
                    self.blocks[3][1] += 1
                    self.position = 3
                elif self.position == 3:
                    self.blocks[0][1] += 2
                    self.blocks[1][0] -= 1
                    self.blocks[1][1] -= 1
                    self.blocks[3][0] += 1
                    self.blocks[3][1] += 1
                    self.position = 4
                elif self.position == 4:
                    self.blocks[0][0] += 2
                    self.blocks[1][0] -= 1
                    self.blocks[1][1] += 1
                    self.blocks[3][0] += 1
                    self.blocks[3][1] -= 1
                    self.position = 1

        #rotation of the reverse Z tetromino (2 different position)
        if self.ttype == 5:
                if self.position == 1:
                    self.blocks[0][0] += 1
                    self.blocks[1][1] -= 1
                    self.blocks[2][0] += 1
                    self.blocks[2][1] += 2
                    self.blocks[3][1] += 1
                    self.position = 2
                elif self.position == 2:
                    self.blocks[0][0] -= 1
                    self.blocks[1][1] += 1
                    self.blocks[2][0] -= 1
                    self.blocks[2][1] -= 2
                    self.blocks[3][1] -= 1
                    self.position = 1
            
        #rotation of the Z tetromino (2 different position)
        if self.ttype == 6:
                if self.position == 1:
                    self.blocks[0][0] += 2
                    self.blocks[0][1] += 1
                    self.blocks[1][0] += 1
                    self.blocks[2][1] += 1
                    self.blocks[3][0] -= 1
                    self.position = 2
                elif self.position == 2:
                    self.blocks[0][0] -= 2
                    self.blocks[0][1] -= 1
                    self.blocks[1][0] -= 1
                    self.blocks[2][1] -= 1
                    self.blocks[3][0] += 1
                    self.position = 1

        #rotation of the T tetromino (4 different position)
        if self.ttype == 7:
                if self.position == 1:
                    self.blocks[0][0] += 1
                    self.blocks[0][1] -= 1
                    self.blocks[1][0] += 1
                    self.blocks[1][1] += 1
                    self.blocks[3][0] -= 1
                    self.blocks[3][1] -= 1
                    self.position = 2
                elif self.position == 2:
                    self.blocks[0][0] -= 1
                    self.blocks[0][1] -= 1
                    self.blocks[1][0] += 1
                    self.blocks[1][1] -= 1
                    self.blocks[3][0] -= 1
                    self.blocks[3][1] += 1
                    self.position = 3
                elif self.position == 3:
                    self.blocks[0][0] -= 1
                    self.blocks[0][1] += 1
                    self.blocks[1][0] -= 1
                    self.blocks[1][1] -= 1
                    self.blocks[3][0] += 1
                    self.blocks[3][1] += 1
                    self.position = 4
                elif self.position == 4:
                    self.blocks[0][0] += 1
                    self.blocks[0][1] += 1
                    self.blocks[1][0] -= 1
                    self.blocks[1][1] += 1
                    self.blocks[3][0] += 1
                    self.blocks[3][1] -= 1
                    self.position = 1
    
    #The final rotate method which rotates the tetromino but only if the border and the fix blocks allow it  
    def rotate(self,fix_blocks,border):
        self.rotate_base()
        for i in self.blocks:
            if i in border.blocks or i in fix_blocks.blocks:
                self.rotate_base()
                self.rotate_base()
                self.rotate_base()
                
    #A method which displays the tetromino on the grid based on the list of the blocks 
    def draw_tetromino(self,grid):
        for i in self.blocks:
            if i[1] < 20:
                grid.create_block(i[0],i[1],self.color)

#An object of this class stores all the fix blocks in a list
class Fix_blocks():

    #In the constructor we store a row of blocks which is right below the grid
    def __init__(self):
        self.blocks = [[i,-1] for i in range(10)]

    #A method which takes a tetromino and checks if it had already touched the bottom or the fix blocks yet
    def check_tetromino(self,T):
        for i in T.blocks:
            if i in self.blocks:
                return True

    #A method which takes a tetromino and adds it to the fix blocks
    #Then uses other methods to search for full rows, deletes then and returns the number of deleted rows
    def add_tetromino(self,T):
        for j in T.blocks:
            self.blocks.append([j[0],j[1]+1])
        
        full_rows = self.check_rows()
        self.delete_rows(full_rows)
        return len(full_rows)

    #This method displays the fix blocks (in white)
    def draw_blocks(self,grid):
        for i in self.blocks:
            if i[1] != -1 :
                grid.create_block(i[0],i[1],(255,255,255))

    #This method checks the rows of the fix blocks and returns the full rows
    def check_rows(self):
        rows=[0 for i in range(20)]
        for j in range(20):
            for i in self.blocks:
                if i[1] == j:
                    rows[j] += 1
        full_rows = []
        for i in range(20):
            if rows[i] == 10:
                full_rows.append(i)
        return full_rows
        
    #This method deletes the given rows from the fix blocks
    def delete_rows(self,rows):
        for i in range(19,-1,-1):
            if i in rows:
                del_list = []
                lower_list = []
                for j in range(len(self.blocks)):
                    if self.blocks[j][1] == i:
                        del_list.append(self.blocks[j])
                    if self.blocks[j][1] > i:
                        lower_list.append(self.blocks[j])
                for j in del_list:
                    self.blocks.remove(j)
                for j in range(len(self.blocks)):
                    if self.blocks[j] in lower_list:
                        self.blocks[j][1] -= 1

#This is a simple class for storing the border coordinates of the grid
class Border():
    def __init__(self):
        self.blocks = []
        for i in range(40):
            self.blocks.append([-1,i])
            self.blocks.append([10,i])
        for i in range(10):
            self.blocks.append([i,-1])
    
    