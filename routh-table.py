import utility


# The actual usable screen size is (in pixel):
# WIDTH = 320
# HEIGHT = 222
# The number of lines and columns visible at the same time in the interpreter is (based on 'M'):
# MAX_LINE = 16  # Python font size = small
# MAX_COLUMN = 42  # Python font size = small
# MAX_LINE = 12  # Python font size = large
# MAX_COLUMN = 29  # Python font size = large

def routh(*args):
    degree = len(args)
    coef = list(args)
    table = []
    row0 = []
    row1 = []
    for i in range(degree):
        if i % 2 == 0:
            row0.append(coef[i])
        else:
            row1.append(coef[i])
    if degree % 2 != 0:
        row1.append(0)

    row0.append(0)
    row1.append(0)
    table.append(row0)
    table.append(row1)

    for i in range(degree-2):
        row = []
        zeroFirstColumn = False
        zeroRow = False
        zeroRowCount = 0
        for j in range(len(table[i])-1):
            b = - (table[i][0] * table[i+1][j+1] - table[i+1]
                   [0] * table[i][j+1]) / table[i+1][0]
            row.append(b)
            zeroRowCount += abs(b)
        row.append(0)
        table.append(row)

        if zeroRowCount == 0:
            zeroRow = True
            showTable(degree, table)
            print("Full row of zero\n")
            break

        if table[i+2][0] == 0:
            zeroFirstColumn = True
            showTable(degree, table)
            print("Zero in the 1st column\n")
            break

    if zeroFirstColumn:
        coef.reverse()
        table = []
        row0 = []
        row1 = []
        for i in range(degree):
            if i % 2 == 0:
                row0.append(coef[i])
            else:
                row1.append(coef[i])
        if degree % 2 != 0:
            row1.append(0)

        row0.append(0)
        row1.append(0)
        table.append(row0)
        table.append(row1)

        row = []
        # print(table)
        for i in range(degree-2):
            for j in range(len(table[i])-1):
                b = - (table[i][0] * table[i+1][j+1] - table[i+1]
                       [0] * table[i][j+1]) / table[i+1][0]
                row.append(b)
                zeroRowCount += abs(b)
            row.append(0)
            table.append(row)
            row = []

    # if zeroRow:
    #     print("Entire row of zeros")
        # TODO algorithm for the row of zero

    # print(table)
    showTable(degree, table)
    numberSignChanges = signChanges(table)
    utility.show(
        "Number of poles in the right-half plane: {:,.1g}".format(numberSignChanges))


def showTable(degree, table):
    for i in range(len(table)):
        rowNumbers = ""
        for j in range(len(table[i])-1):
            rowNumbers += "{: ,.2f} | ".format(table[i][j])
        print("s{:,.1g} | {}".format(degree-1-i, rowNumbers))


def signChanges(table):
    signChangeCount = 0
    previousNumber = table[0][0]
    previousSign = True
    if previousNumber > 0:
        previousSign = True
    else:
        previousNumber = False

    for i in range(len(table)-1):
        if table[i+1][0] > 0 and not previousSign:
            signChangeCount += 1
            previousSign = True
        elif table[i+1][0] < 0 and previousSign:
            signChangeCount += 1
            previousSign = False

        previousNumber = table[i+1][0]

    return signChangeCount

# menu = [
#     # "ie title: function(arguments)",
#     "Routh table (coefs from s^n to s^0): routh(coefs)",
# ]

# utility.printMenu("Routh table", menu)


if __name__ == "__main__":
    # routh(3, 2, 1) # no sign change
    # routh(3, -2, 1) # 2 sign change
    # routh(1, 2, 3, 6, 5, 3) # zero 1st column
    # routh(1, 4, 2, 8, 3) # zero 1st column
    # routh(1, 7, 6, 42, 8, 56) # zero row
    # routh(1, 1, 12, 22, 39, 59, 48, 38, 20) # zero row
    # routh(1, 1, -6, 0, -1, -1, 6) # zero row
    # routh(6, -1, -1, 0, -6, 1, 1) # zero row
    routh(1, 110, 3875, 43760, 500, 6000)
