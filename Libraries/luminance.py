#-----------------------------------------------------------------------
# luminance.py
#-----------------------------------------------------------------------

import sys
import stdio
from color import Color

#-----------------------------------------------------------------------

# Return the luminance of Color c.

def luminance(c):
    red   = c.getRed()
    green = c.getGreen()
    blue  = c.getBlue()
    return (.299 * red) + (.587 * green) + (.114 * blue)

#-----------------------------------------------------------------------

# Return the grayscale equivalent of Color c. Use the luminance of c
# to compute its grayscale value.

def toGray(c):
    y = int(round(luminance(c)))
    return Color(y, y, y)

#-----------------------------------------------------------------------

# Return True if Color c1 is compatible with Color c2, and
# False otherwise.

def areCompatible(c1, c2):
    return abs(luminance(c1) - luminance(c2)) >= 128.0

#-----------------------------------------------------------------------

# Accept six RGB values defining two Colors as command-line arguments.
# Write True to the standard output stream if the two Colors are
# compatible, and False otherwise.

def main():
    r1 = int(sys.argv[1])
    g1 = int(sys.argv[2])
    b1 = int(sys.argv[3])
    r2 = int(sys.argv[4])
    g2 = int(sys.argv[5])
    b2 = int(sys.argv[6])
    c1 = Color(r1, g1, b1)
    c2 = Color(r2, g2, b2)
    stdio.writeln(areCompatible(c1, c2))

if __name__ == '__main__':
    main()

#-----------------------------------------------------------------------

# python luminance.py 232 232 232 0 0 0
# True

# python luminance.py 9 90 166 232 232 232
# True

# python luminance.py 9 90 166 0 0 0
# False

