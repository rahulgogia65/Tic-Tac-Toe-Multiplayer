# write your code here
# cells = input("Enter cells: ")


# to convert cells into matrix
# count = 0
# for a in range(3, 0, -1):
#     for b in range(1, 4):
#         matrix[b - 1][a - 1] = cells[count]
#         count += 1


def print_board(cell):
    print("---------")
    print("|", cell[0][2], cell[1][2], cell[2][2], "|")
    print("|", cell[0][1], cell[1][1], cell[2][1], "|")
    print("|", cell[0][0], cell[1][0], cell[2][0], "|")
    print("---------")


def ask_coordinates(var):
    global matrix
    while True:
        try:
            x_coordinate, y_coordinate = input("Enter the coordinates: ").split()
        except ValueError:
            print('You should enter numbers!')
        else:
            if x_coordinate.isnumeric() and y_coordinate.isnumeric():
                if 0 < int(x_coordinate) < 4 and 0 < int(y_coordinate) < 4:
                    if matrix[int(x_coordinate) - 1][int(y_coordinate) - 1] != '_':
                        print("This cell is occupied! Choose another one!")
                    else:
                        matrix[int(x_coordinate) - 1][int(y_coordinate) - 1] = var
                        print_board(matrix)
                        break
                else:
                    print('Coordinates should be from 1 to 3!')
            else:
                print('You should enter numbers!')


def check_status(matrix):
    ret = False
    h1 = matrix[0][2] == matrix[1][2] == matrix[2][2]
    h2 = matrix[0][1] == matrix[1][1] == matrix[2][1]
    h3 = matrix[0][0] == matrix[1][0] == matrix[2][0]

    v1 = matrix[0][2] == matrix[0][1] == matrix[0][0]
    v2 = matrix[1][2] == matrix[1][1] == matrix[1][0]
    v3 = matrix[2][2] == matrix[2][1] == matrix[2][0]

    d1 = matrix[0][2] == matrix[1][1] == matrix[2][0]
    d2 = matrix[2][2] == matrix[1][1] == matrix[0][0]

    # lst = [h1, h2, h3, v1, v2, v3, d1, d2]
    # true_list = [a for a in lst if a]

    # x = [let for let in matrix if let == 'X']
    # o = [let for let in matrix if let == 'O']
    # imp = bool()

    # if len(true_list) > 1:
    #     print("Impossible")
    #     imp = True
    #
    # elif abs(len(x) - len(o)) >= 2:
    #     print("Impossible")
    #     imp = True

    if '_' in matrix[0] or '_' in matrix[1] or '_' in matrix[2]:
        if h1 and matrix[0][2] != '_':
            print(matrix[0][2] + " wins")
        elif h2 and matrix[0][1] != '_':
            print(matrix[0][1] + " wins")
        elif h3 and matrix[0][0] != '_':
            print(matrix[0][0] + " wins")
        elif v1 and matrix[0][2] != '_':
            print(matrix[0][2] + " wins")
        elif v2 and matrix[1][2] != '_':
            print(matrix[1][2] + " wins")
        elif v3 and matrix[2][2] != '_':
            print(matrix[2][2] + " wins")
        elif d1 and matrix[0][2] != '_':
            print(matrix[0][2] + " wins")
        elif d2 and matrix[2][2] != '_':
            print(matrix[2][2] + " wins")
        else:
            ret = True

    else:
        if h1 and matrix[0][2] != '_':
            print(matrix[0][2] + " wins")
        elif h2 and matrix[0][1] != '_':
            print(matrix[0][1] + " wins")
        elif h3 and matrix[0][0] != '_':
            print(matrix[0][0] + " wins")
        elif v1 and matrix[0][2] != '_':
            print(matrix[0][2] + " wins")
        elif v2 and matrix[1][2] != '_':
            print(matrix[1][2] + " wins")
        elif v3 and matrix[2][2] != '_':
            print(matrix[2][2] + " wins")
        elif d1 and matrix[0][2] != '_':
            print(matrix[0][2] + " wins")
        elif d2 and matrix[2][2] != '_':
            print(matrix[2][2] + " wins")
        else:
            print("Draw")

    return ret


matrix = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
print_board(matrix)
count = 1
while True:
    var = str()
    if count % 2:
        var = 'X'
    else:
        var = 'O'
    ask_coordinates(var)
    x = check_status(matrix)
    if not x:
        break
    count += 1
