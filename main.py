from skeleton import size
from mines import mine_area, area, mines

for mine_pos in mine_area:
    try:
        if mine_pos % size != 0 and (mine_pos + 1) % size != 0: 
            if type(area[mine_pos - size - 1]) == int and mine_pos - size - 1 >= 0:
                area[mine_pos - size - 1] += 1

            if type(area[mine_pos - size]) == int and mine_pos - size >= 0:
                area[mine_pos - size] += 1

            if type(area[mine_pos - size + 1]) == int and mine_pos - size + 1 >= 0:
                area[mine_pos - size + 1] += 1

            if type(area[mine_pos - 1]) == int:
                area[mine_pos - 1] += 1

            if type(area[mine_pos + 1]) == int:
                area[mine_pos + 1] += 1

            if type(area[mine_pos + size - 1]) == int:
                area[mine_pos + size - 1] += 1

            if type(area[mine_pos + size]) == int:
                area[mine_pos + size] += 1

            if type(area[mine_pos + size + 1]) == int:
                area[mine_pos + size + 1] += 1

        if mine_pos % size == 0:
            if type(area[mine_pos - size]) == int and mine_pos - size >= 0:
                area[mine_pos - size] += 1

            if type(area[mine_pos - size + 1]) == int and mine_pos - size + 1 >= 0:
                area[mine_pos - size + 1] += 1

            if type(area[mine_pos + 1]) == int:
                area[mine_pos + 1] += 1
            
            if type(area[mine_pos + size + 1]) == int:
                area[mine_pos + size + 1] += 1

            if type(area[mine_pos + size]) == int:
                area[mine_pos + size] += 1

        if (mine_pos + 1) % size == 0:
            if type(area[mine_pos - size - 1]) == int and mine_pos - size - 1 > 0:
                area[mine_pos - size - 1] += 1

            if type(area[mine_pos - size]) == int and mine_pos - size > 0:
                area[mine_pos - size] += 1

            if type(area[mine_pos - 1]) == int:
                area[mine_pos - 1] += 1

            if type(area[mine_pos + size - 1]) == int:
                area[mine_pos + size - 1] += 1
            
            if type(area[mine_pos + size]) == int:
                area[mine_pos + size] += 1

    except:
        pass

board, uncovered_board = [], []

for i in range(size):
    board.append(area[(i*size):(i*size + size)])
    uncovered_board.append(['*' for x in range(size)])

remaining_cells = -mines

for j in range(size):
    for k in range(size):
        print(uncovered_board[j][k], end = '    ')

        if uncovered_board[j][k] == '*':
            remaining_cells += 1

    print('\n')
print(board)
print('Remaining cells to uncover:', remaining_cells, '\n')

uncovered_cell = None

while uncovered_cell != '#' or remaining_cells == 0:
    action = input('Select action (m - mark/unmark mine, u - uncover cell): ')

    if action == 'u':
        uncover_x = input(f'Select column to uncover (1-{size}): ')
        uncover_y = input(f'Select row to uncover (1-{size}): ')

        try:
            uncover_x = int(uncover_x) - 1
            uncover_y = int(uncover_y) - 1

            if uncover_x >= 0 and uncover_x < size and uncover_y >= 0 and uncover_y < size:
                uncovered_board[uncover_y][uncover_x] = board[uncover_y][uncover_x]
                
                uncovered_cell = board[uncover_y][uncover_x]
                
                if uncovered_cell == '#':
                    print('\n' + 'Game over' + '\n')

                    for j in range(size):
                        for k in range(size):
                            print(board[j][k], end = '    ')

                        print('\n')
                    
                    break

                else:
                    if board[uncover_y][uncover_x] == 0:
                        if uncover_x == 0 and uncover_y == 0:
                            uncovered_board[uncover_y][uncover_x + 1] = board[uncover_y][uncover_x + 1]
                            uncovered_board[uncover_y + 1][uncover_x + 1] = board[uncover_y + 1][uncover_x + 1]
                            uncovered_board[uncover_y + 1][uncover_x] = board[uncover_y + 1][uncover_x]
                        
                        elif uncover_x == (size - 1) and uncover_y == 0:
                            uncovered_board[uncover_y + 1][uncover_x] = board[uncover_y + 1][uncover_x]
                            uncovered_board[uncover_y + 1][uncover_x - 1] = board[uncover_y + 1][uncover_x - 1]
                            uncovered_board[uncover_y][uncover_x - 1] = board[uncover_y][uncover_x - 1]

                        elif uncover_x == 0 and uncover_y == (size - 1):
                            uncovered_board[uncover_y - 1][uncover_x] = board[uncover_y - 1][uncover_x]
                            uncovered_board[uncover_y - 1][uncover_x + 1] = board[uncover_y - 1][uncover_x + 1]
                            uncovered_board[uncover_y][uncover_x + 1] = board[uncover_y][uncover_x + 1]

                        elif uncover_x == (size - 1) and uncover_y == (size - 1):
                            uncovered_board[uncover_y][uncover_x - 1] = board[uncover_y][uncover_x - 1]
                            uncovered_board[uncover_y - 1][uncover_x - 1] = board[uncover_y - 1][uncover_x - 1]
                            uncovered_board[uncover_y - 1][uncover_x] = board[uncover_y - 1][uncover_x]
                    
                        elif uncover_x == 0:
                            uncovered_board[uncover_y - 1][uncover_x] = board[uncover_y - 1][uncover_x]
                            uncovered_board[uncover_y - 1][uncover_x + 1] = board[uncover_y - 1][uncover_x + 1]
                            uncovered_board[uncover_y][uncover_x + 1] = board[uncover_y][uncover_x + 1]
                            uncovered_board[uncover_y + 1][uncover_x + 1] = board[uncover_y + 1][uncover_x + 1]
                            uncovered_board[uncover_y + 1][uncover_x] = board[uncover_y + 1][uncover_x]
                        
                        
                        elif uncover_x == (size - 1):
                            uncovered_board[uncover_y + 1][uncover_x] = board[uncover_y + 1][uncover_x]
                            uncovered_board[uncover_y + 1][uncover_x - 1] = board[uncover_y + 1][uncover_x - 1]
                            uncovered_board[uncover_y][uncover_x - 1] = board[uncover_y][uncover_x - 1]
                            uncovered_board[uncover_y - 1][uncover_x - 1] = board[uncover_y - 1][uncover_x - 1]
                            uncovered_board[uncover_y - 1][uncover_x] = board[uncover_y - 1][uncover_x]

                        elif uncover_y == 0:
                            uncovered_board[uncover_y][uncover_x + 1] = board[uncover_y][uncover_x + 1]
                            uncovered_board[uncover_y + 1][uncover_x + 1] = board[uncover_y + 1][uncover_x + 1]
                            uncovered_board[uncover_y + 1][uncover_x] = board[uncover_y + 1][uncover_x]
                            uncovered_board[uncover_y + 1][uncover_x - 1] = board[uncover_y + 1][uncover_x - 1]
                            uncovered_board[uncover_y][uncover_x - 1] = board[uncover_y][uncover_x - 1]

                        elif uncover_y == (size - 1):
                            uncovered_board[uncover_y - 1][uncover_x] = board[uncover_y - 1][uncover_x]
                            uncovered_board[uncover_y - 1][uncover_x + 1] = board[uncover_y - 1][uncover_x + 1]
                            uncovered_board[uncover_y][uncover_x + 1] = board[uncover_y][uncover_x + 1]
                            uncovered_board[uncover_y][uncover_x - 1] = board[uncover_y][uncover_x - 1]
                            uncovered_board[uncover_y - 1][uncover_x - 1] = board[uncover_y - 1][uncover_x - 1]
                        
                        else:
                            uncovered_board[uncover_y - 1][uncover_x] = board[uncover_y - 1][uncover_x]
                            uncovered_board[uncover_y - 1][uncover_x + 1] = board[uncover_y - 1][uncover_x + 1]
                            uncovered_board[uncover_y][uncover_x + 1] = board[uncover_y][uncover_x + 1]
                            uncovered_board[uncover_y + 1][uncover_x + 1] = board[uncover_y + 1][uncover_x + 1]
                            uncovered_board[uncover_y + 1][uncover_x] = board[uncover_y + 1][uncover_x]
                            uncovered_board[uncover_y + 1][uncover_x - 1] = board[uncover_y + 1][uncover_x - 1]
                            uncovered_board[uncover_y][uncover_x - 1] = board[uncover_y][uncover_x - 1]
                            uncovered_board[uncover_y - 1][uncover_x - 1] = board[uncover_y - 1][uncover_x - 1]

                    remaining_cells = 0
                    
                    for j in range(size):
                        for k in range(size):
                            print(uncovered_board[j][k], end = '    ')

                            if uncovered_board[j][k] == '*' or uncovered_board[j][k] == 'M':
                                remaining_cells += 1

                        print('\n')

                    remaining_cells -= mines
                    if remaining_cells ==0:
                        break
                    else:
                        print('Remaining cells to uncover:', remaining_cells, '\n')
            
                action = None

            else:
                print('Invalid placement')

        except:
            print('Invalid input')

        
    if action == 'm':
        mark_x = input(f'Select column to mark/unmark (1-{size}): ')
        mark_y = input(f'Select row to mark/unmark (1-{size}): ')

        try:
            mark_x = int(mark_x) - 1
            mark_y = int(mark_y) - 1

            if mark_x >= 0 and mark_x < size and mark_y >= 0 and mark_y < size:
                if uncovered_board[mark_y][mark_x] != 'M':
                    uncovered_board[mark_y][mark_x] = 'M'

                else:
                    uncovered_board[mark_y][mark_x] = '*'

            for j in range(size):
                    for k in range(size):
                        print(uncovered_board[j][k], end = '    ')
                    print('\n')

            action = None            

        except:
            print('Invalid input')

if remaining_cells == 0:
    print('Congratulations! You won!' + '\n')