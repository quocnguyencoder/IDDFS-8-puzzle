# -*- coding: utf-8 -*-
"""
Created on Wed May  6 23:03:07 2020
@author: Quoc , Hoa , Phuong

n-Puzzle Using Iterative deepening depth-first search in Python
"""

"""
IDDFS code reference at: https://eddmann.com/posts/using-iterative-deepening-depth-first-search-in-python/?fbclid=IwAR1qwutR3vwLtclRi9fLM5k9bMG2A_E_LkJHj7q9GtgPxUScTaccSfVzTwg
"""

def id_dfs(puzzle, goal, get_moves):
    """
    Depth first search algorithms
    input: state, goal, frontier
    output: route
    """
    import itertools

    def dfs(route, depth):
        if depth == 0:
            return
        if route[-1] == goal:
            return route
        for move in get_moves(route[-1]):
            if move not in route: 
                next_route = dfs(route + [move], depth - 1)
                if next_route:
                    return next_route

    for depth in itertools.count(): 
        route = dfs([puzzle], depth)
        if route:
            return route
def SearchBlank(mang):
    """
    Find 0 position
    input: 2D list
    output: 0 position
    """
    import itertools
 
    mang = list(itertools.chain.from_iterable(mang)) 
    for i in range(0,len(mang)):
        if mang[i]==0:
            return i

def results(route):
    """
    Find a efficient route
    input:  route
    output: list move  ex: ['UP','DOWN','LEFT','RIGHT',...]
    """
    moves=[]
    move=[]
    index=SearchBlank(puzzle)
    for i in range(1,len(route)):
        mang=route[i]
        for j in range(0,len(state)):
            if SearchBlank(mang)==index+state[j]:
                moves.append(j)
                index=SearchBlank(mang)
    for k in range(len(moves)):
        move.append(possiblemove[moves[k]])
    return move

def num_moves(rows, cols): 
    def get_moves(subject):
        """
        append frontier
        input: parent node
        output: child nodes
        """
        moves = []

        zrow, zcol = next((r, c)
            for r, l in enumerate(subject)
                for c, v in enumerate(l) if v == 0)

        def swap(row, col):
            import copy
            s = copy.deepcopy(subject)
            s[zrow][zcol], s[row][col] = s[row][col], s[zrow][zcol]
            return s

        # north
        if zrow > 0:
            moves.append(swap(zrow - 1, zcol))
        # east
        if zcol < cols - 1:
            moves.append(swap(zrow, zcol + 1))
        # south
        if zrow < rows - 1:
            moves.append(swap(zrow + 1, zcol))
        # west
        if zcol > 0:
            moves.append(swap(zrow, zcol - 1))

        return moves
    return get_moves

# puzzle for testing
puzzle=[[3,1,2],[6,0,8],[7,5,4]]
#puzzle=[[1,2,0],[3,4,5],[6,7,8]]
#puzzle=[[1,4,0],[3,5,2],[6,7,8]]

goal=[[0,1,2],[3,4,5],[6,7,8]]
state=[-3,3,-1,1]
possiblemove=["UP","DOWN","LEFT","RIGHT"]
move = (results(id_dfs(puzzle, goal, num_moves(3, 3))))
solution = id_dfs(puzzle, goal, num_moves(3, 3))
#print('Moves: ',len(solution)) 


"""
Animation
Reference at: https://www.reddit.com/r/learnpython/comments/3sx8kg/trying_to_animate_an_array_in_matplotlib/cx1grsi/
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import itertools

# get intial_puzzle list for animation 
initial_puzzle = list(itertools.chain.from_iterable(puzzle))

# Create figure
fig, ax = plt.subplots()	

fig.suptitle('  8-Puzzle Problem ', fontsize = 20, fontweight='bold',color='darkblue')
ax.set_title('axes title')

# puzzle 3x3
puzzle = np.zeros((3,3))

# list of text value
text = [0,1,2,3,4,5,6,7,8]

index = 0
for i in range(3):
    for j in range (3):
        puzzle[i,j] = initial_puzzle[index]
        if initial_puzzle[index] == 0:
            zero_index = index
            zero_index_x = i
            zero_index_y = j
        # set number text in plot
        text[index] = plt.text(j,i,str(initial_puzzle[index]), horizontalalignment='center', verticalalignment='center', style='oblique',color='yellow', fontsize=30)
        index += 1

# x and y index of 0 using in animation    
static_zero_index_x = zero_index_x
static_zero_index_y = zero_index_y

# index of solution list
index_move = 0;

# index of 0 in animation
text_index = zero_index 

# flag variable 
beginning = 1

def animate(c):   
    global  zero_index_x ,zero_index_y ,index_move , beginning ,text_index
    if beginning == 1:
        time.sleep(1)
        # turn of flag to move
        beginning = 0
        # reset puzzle to initial state
        index = 0
        for i in range(3):
            for j in range (3):
                puzzle[i,j] = initial_puzzle[index]
                text[index].set_text(str(initial_puzzle[index]))
                index += 1
        
        ax.set_title('Initial state',color = 'orange', fontweight='bold')
        
    elif move[index_move]== 'UP':
        #swap puzzle
        puzzle[zero_index_x,zero_index_y] , puzzle[zero_index_x -1 ,zero_index_y] =  puzzle[zero_index_x -1 ,zero_index_y] , puzzle[zero_index_x,zero_index_y]
        #change index
        zero_index_x -= 1 
        index_move += 1
        #update text when moving
        text[text_index].set_text(str(int(puzzle[zero_index_x+1][zero_index_y])))
        text[text_index - 3].set_text(str(int(puzzle[zero_index_x][zero_index_y])))
        text_index -= 3
        # update tile
        ax.set_title('Solving ... ',color = 'orange', style='oblique')
        
    elif move[index_move]== 'DOWN':
        puzzle[zero_index_x,zero_index_y] , puzzle[zero_index_x +1 ,zero_index_y] =  puzzle[zero_index_x +1 ,zero_index_y] , puzzle[zero_index_x,zero_index_y]
        zero_index_x += 1 
        index_move += 1
        text[text_index].set_text(str(int(puzzle[zero_index_x-1][zero_index_y])))
        text[text_index + 3].set_text(str(int(puzzle[zero_index_x][zero_index_y])))
        text_index += 3
        ax.set_title('Solving ... ',color = 'orange', style='oblique')
        
    elif move[index_move]== 'LEFT':
        puzzle[zero_index_x,zero_index_y] , puzzle[zero_index_x ,zero_index_y -1] =  puzzle[zero_index_x ,zero_index_y - 1] , puzzle[zero_index_x,zero_index_y]
        zero_index_y -= 1 
        index_move += 1
        text[text_index].set_text(str(int(puzzle[zero_index_x][zero_index_y+1])))
        text[text_index - 1].set_text(str(int(puzzle[zero_index_x][zero_index_y])))
        text_index -= 1
        ax.set_title('Solving ... ',color = 'orange', style='oblique')
        
    elif move[index_move]== 'RIGHT':
        puzzle[zero_index_x,zero_index_y] , puzzle[zero_index_x ,zero_index_y +1] =  puzzle[zero_index_x ,zero_index_y +1] , puzzle[zero_index_x,zero_index_y]
        zero_index_y += 1 
        index_move += 1
        text[text_index].set_text(str(int(puzzle[zero_index_x][zero_index_y-1])))
        text[text_index + 1].set_text(str(int(puzzle[zero_index_x][zero_index_y])))
        text_index += 1
        ax.set_title('Solving ... ',color = 'orange', style='oblique')
        
    #print(puzzle)
    
    # animating move
    ax.imshow(puzzle, cmap=plt.cm.Blues, interpolation='nearest')
    
    # reset when finish
    if index_move == len(move):
        #update title
        ax.set_title('Goal state',color = 'orange', fontweight='bold')
        # reset all value
        zero_index_x = static_zero_index_x
        zero_index_y = static_zero_index_y 
        index_move = 0;
        beginning = 1
        text_index = zero_index
        #print("Reset")


plt.axis('off')
#plt.imshow(puzzle,cmap='binary')
ani = animation.FuncAnimation(fig, animate, interval=700)
plt.show();
