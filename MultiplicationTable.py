row = 1
while row < 10:
    column = 1
    while column <= row:
        print("%d * %d = %2d  " % (column, row, row * column), end='')
        column += 1
    print()
    row += 1
