#Sudoku solver!

#SAMPLE BOARDS TO PASS INTO THE CODE

#EASY
#123456789456789123789123456231645978645978231978231645312564897564897312897312564
#000456789456789123789123456231645978645078231978231645312564890004897312897312560
#231645978645078231978231645312564890004897312897312560000456789456789123789123456
#312564890004897312897312560000456789456789123789123456231645978645078231978231645
#000514200020706050004892000038160040090000687200080900002040005947000020060078430
#038160040090000687200080900002040005947000020060078430000514200020706050004892000
#002040005947000020060078430000514200020706050004892000038160040090000687200080900

#MEDIUM-HARD
#306009870040060203500002010207000000050000090000000601060200009409070060032600105
#210000006003100000600002903792800000100000005000001682807300004000008200300000057

#EVIL
#073005000000308604009001000010000005004060900700000030000800500205407000000900280
#010000005004060900700000030000800500205407000000900280073005000000308604009001000
#000800500205407000000900280073005000000308604009001000010000005004060900700000030
#800003010070201040020500007040002050002000004006700003400005200900000100030100080
#040002050002000004006700003400005200900000100030100080800003010070201040020500007
#400005200900000100030100080800003010070201040020500007040002050002000004006700003

#LITERALLY IMPOSSIBLE
#000400000000000000089123456231645978645078231978231645312564890004897312897312560
#231645978645078231978231645312564890004897312897312560000400000000000000089123456
#312564890004897312897312560000400000000000000089123456231645978645078231978231645
#000000000000000000000000000000000000000000000000000000000000000000000000000000000


class Cell:
    def __init__(self, row, column, box, value):
        self.row = row
        self.column = column
        self.box = box
        self.value = value

class Row:
    def __init__(self, row_number):
        self.row_number = row_number
        self.cells = []
    def add_cell(self, cell):
        self.cells.append(cell)

class Column:
    def __init__(self, col_number):
        self.col_number = col_number
        self.cells = []
    def add_cell(self, cell):
        self.cells.append(cell)

class Box:
    def __init__(self, box_number):
        self.box_number = box_number
        self.cells = []
    def add_cell(self, cell):
        self.cells.append(cell)

rows = []
columns = []
boxes = []

for x in range(9):
    rows.append(Row(x))
    columns.append(Column(x))
    boxes.append(Box(x))

box_labels = [0, 0, 0, 1, 1, 1, 2, 2, 2, 0, 0, 0, 1, 1, 1, 2, 2, 2, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 3, 3, 3, 4, 4, 4, 5, 5, 5, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 6, 6, 6, 7, 7, 7, 8, 8, 8, 6, 6, 6, 7, 7, 7, 8, 8, 8]

values = input("What are your 81 numbers? Type 0 if the cell is blank; otherwise type the number of the cell.  Just type 81 digits, no spaces or commas please.\n")
print("\nYour board is currently the following, where 0 refers to a blank cell:\n")
for x in range(9):
    print(values[(9*x)+0], values[(9*x)+1], values[(9*x)+2], " ", values[(9*x)+3], values[(9*x)+4], values[(9*x)+5], " ", values[(9*x)+6], values[(9*x)+7], values[(9*x)+8])
    if x % 3 == 2:
        print(" ")

#Create the Cells that will belong to the Rows, Columns, and Boxes

for x in range(81):
    row_index = x // 9
    column_index = x % 9
    box_index = box_labels[x]
    if int(values[x]) == 0:
        cell = Cell(x // 9, x % 9, box_labels[x], set([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    else:
        cell = Cell(x // 9, x % 9, box_labels[x], set([int(values[x])]))
    rows[row_index].add_cell(cell)
    columns[column_index].add_cell(cell)
    boxes[box_index].add_cell(cell)

#should_i_solve = input("Would you like me to solve this Sudoku now?   ")

cells_remaining = 0

def easy_test():
    global cells_remaining
    cells_remaining = 0
    for row in rows:
        for cell in row.cells:
            if len(cell.value) != 1:
                cells_remaining += 1
                for other_cell in row.cells:
                    if cell != other_cell:
                        if len(other_cell.value) == 1:
                            if list(other_cell.value)[0] in cell.value:
                                cell.value.remove(list(other_cell.value)[0])
                for other_cell in columns[cell.column].cells:
                     if cell != other_cell:
                        if len(other_cell.value) == 1:
                            if list(other_cell.value)[0] in cell.value:
                                cell.value.remove(list(other_cell.value)[0])
                for other_cell in boxes[cell.box].cells:
                    if cell != other_cell:
                        if len(other_cell.value) == 1:
                            if list(other_cell.value)[0] in cell.value:
                               cell.value.remove(list(other_cell.value)[0])
'''                               
DOES NOT WORK!!
def hard_test():
    global cells_remaining
    cells_remaining = 0
    for row in rows:
        for cell in row.cells:
            if len(cell.value) == 2:
                for other_cell in row.cells:
                    if cell != other_cell:
                        if other_cell.value == cell.value:
                            for other_other_cell in row.cells:
                                if cell != other_other_cell:
                                    if len(other_other_cell.value) > 2:
                                        if list(cell.value)[0] in other_other_cell.value:
                                            other_other_cell.value.remove(list(cell.value)[0])
                                    if len(other_other_cell.value) > 2:
                                        if list(cell.value)[1] in other_other_cell.value:
                                            other_other_cell.value.remove(list(cell.value)[1])       
'''

'''
DOES NOT WORK!!  This code is supposed to find the first cell that has 2 possibilities, pick one, and go from there.
def brute_force():
    global rows
    global columns
    global boxes
    rows2 = rows
    columns2 = columns
    boxes2 = boxes
    if len(rows2[0].cells[0].value) > 1:
        test_value = rows2[0].cells[0].value
        print(test_value)
        rows2[0].cells[0].value = set([list(test_value)[0]])
        for run_through in range(81):
            easy_test() #Need to run this on the new cells.  How to make new cells?
        for row in rows:
            for cell in row.cells:
                if row.cell.value == set():
                    row.cell.#....
'''

for run_through in range(81):
    easy_test()

if cells_remaining == 0:
    print("\nThat was easy!  Here is your final board!\n")
else:
    #for run_through in range(81):
    #    hard_test()
    #brute_force()
    for run_through in range(81):
        easy_test()
    if cells_remaining == 0:
        print("\nThat was hard!  Here is your final board!\n")
    else:
        print("\nI'm sorry, but I was unable to solve your board.\nThere are " + str(cells_remaining) + " cells remaining.\n")

#Change cell value to 0 for cells that are still unknown, so that the board can be printed.
for row in rows:
    for cell in row.cells:
        if len(cell.value) > 1:
            cell.value = set([0])

#Print the final board
for x in range(9):
    print(list(rows[x].cells[0].value)[0], list(rows[x].cells[1].value)[0], list(rows[x].cells[2].value)[0], " ", list(rows[x].cells[3].value)[0], list(rows[x].cells[4].value)[0], list(rows[x].cells[5].value)[0], " ", list(rows[x].cells[6].value)[0], list(rows[x].cells[7].value)[0], list(rows[x].cells[8].value)[0])
    if x % 3 == 2:
        print(" ")