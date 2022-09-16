class Color:

    def __init__(self, r=0, g=0, b=0):
        """
        Construct self such that it has the given red (r),
        green (g), and blue (b) components.
        """
        self._r = r  # Red component
        self._g = g  # Green component
        self._b = b  # Blue component

    def getRed(self):
        return self._r


    def getGreen(self):
        """
        Return the green component of self.
        """
        return self._g


    def getBlue(self):
        return self._b


    def __str__(self):

        return '(' + str(self._r) + ', ' + str(self._g) + ', ' + \
            str(self._b) + ')'

# WHITE = Color(255, 255, 255)

def luminance(col):
    red   = col.getRed()
    green = col.getGreen()
    blue  = col.getBlue()
    return (.299 * red) + (.587 * green) + (.114 * blue)

print(luminance)



