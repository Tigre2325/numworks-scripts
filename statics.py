import utility
import math


# The actual usable screen size is (in pixel):
# WIDTH = 320
# HEIGHT = 222
# The number of line and columns visible at the same time in the interpreter is (based on 'M'):
# MAX_LINE = 16  # Python font size = small
# MAX_COLUMN = 42  # Python font size = small
# MAX_LINE = 12  # Python font size = large
# MAX_COLUMN = 29  # Python font size = large


def lambdaDim(x, y, z=0):
    norm = math.sqrt(x**2 + y**2 + z**2)

    components = [x/norm, y/norm, z/norm]

    print("norm = {:,.6g}".format(norm))

    print("\u03BBx = {:,.6g}".format(components[0]))
    print("\u03BBy = {:,.6g}".format(components[1]))
    print("\u03BBz = {:,.6g}".format(components[2]))


menu = [
    # "line title: function(arguments)",
    "lambda vector (dimensions): lambdaDim(x, y, (z))",
]

utility.printMenu("Statics", menu)

lambdaDim(-0.78, 1.6)
