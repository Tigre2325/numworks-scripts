import math
import utility

# The actual usable screen size is (in pixel):
# WIDTH = 320
# HEIGHT = 222
# The number of line and columns visible at the same time in the interpreter is (based on 'M'):
# MAX_LINE = 16  # Python font size = small
# MAX_COLUMN = 42  # Python font size = small
# MAX_LINE = 12  # Python font size = large
# MAX_COLUMN = 29  # Python font size = large


def roots(a, b, c):

    delta = b * b - 4 * a * c

    print("Discriminant = {:.6g}:".format(delta))

    if delta == 0:
        x = - b / (2 * a)
        print("x = {:.6g}".format(x))

    elif delta > 0:
        x1 = (-b - math.sqrt(delta)) / (2 * a)
        x2 = (-b + math.sqrt(delta)) / (2 * a)

        print("x1 = {:.6g}".format(x1))
        print("x2 = {:.6g}".format(x2))

    else:
        xRe = -b / (2 * a)
        xIm = math.sqrt(-delta) / (2 * a)

        print("x1 = {:.6g} - i{:.6g}".format(xRe, xIm))
        print("x2 = {:.6g} + i{:.6g}".format(xRe, xIm))


menu = [
    "compute discriminant and roots: roots(a, b, c)",
]
utility.printMenu("2nd degree polynomial", menu)
