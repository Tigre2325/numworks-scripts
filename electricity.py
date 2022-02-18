import utility

# The actual usable screen size is (in pixel):
# WIDTH = 320
# HEIGHT = 222
# The number of line and columns visible at the same time in the interpreter is (based on 'M'):
# MAX_LINE = 16  # Python font size = small
# MAX_COLUMN = 42  # Python font size = small
# MAX_LINE = 12 # Python font size = large
# MAX_COLUMN = 29 # Python font size = large


def resistorsSeries(*args):
    REq = 0
    for val in args:
        REq += val

    print("The equivalent resistance is: ")
    print("R_eq = {:,.6g} \u03A9".format(REq))


def resistorsParallel(*args):
    REq = 0
    for val in args:
        REq += 1 / val
    REq = 1 / REq

    print("The equivalent resistance is: ")
    print("R_eq = {:,.6g} \u03A9".format(REq))


def capacitorsSeries(*args):
    CEq = 0
    for val in args:
        CEq += 1 / val
    CEq = 1 / CEq

    print("The equivalent capacitance is: ")
    print("C_eq = {:,.6g} C".format(CEq))


def capacitorsParallel(*args):
    CEq = 0
    for val in args:
        CEq += val

    print("The equivalent capacitance is: ")
    print("C_eq = {:,.6g} C".format(CEq))


menu = [
    "resistors in series: resistorsSeries(R1, R2, R3...)",
    "resistors in parallel: resistorsParallel(R1, R2, R3...)",
    "capacitors in series: capacitorsSeries(C1, C2, C3...)",
    "capacitors in parallel: capacitorsParallel(C1, C2, C3...)",
]
utility.printMenu("Electricity", menu)
