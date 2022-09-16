import pygame
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

# -----------------------------------------------------------------------------

def luminance(col):
    red   = col.getRed()
    green = col.getGreen()
    blue  = col.getBlue()
    return (.299 * red) + (.587 * green) + (.114 * blue)


def toGray(col):
    y = int(round(luminance(col)))
    return Color(y, y, y)


# Return True if Color c1 is compatible with Color c2, and
def areEquivalant(col1, col2):
    return abs(luminance(col1) - luminance(col2)) >= 128.0

# -----------------------------------------------------------------------------
DEFAULT_WIDTH = 512
DEFAULT_HEIGHT = 512
class Picture:

    def __init__(self, arg1=None, arg2=None):

        if (arg1 is None) and (arg2 is None): # set W and H to 512 * 512
            maxWidth = DEFAULT_WIDTH
            maxHeight = DEFAULT_HEIGHT
            self._surface = pygame.Surface((maxWidth, maxHeight))
            self._surface.fill((0, 0, 0))

        elif (arg1 is not None) and (arg2 is None): # set W to other value, but H is 512
            dataset = "Atomic-Nature-of-Matter\Dataset"
            fileName = arg1
            try:
                self._surface = pygame.image.load(dataset + fileName)
            except pygame.error:
                raise IOError()

        elif (arg1 is not None) and (arg2 is not None): # set both W and H to othe values
            maxWidth = arg1
            maxHeight = arg2
            self._surface = pygame.Surface((maxWidth, maxHeight))
            self._surface.fill((0, 0, 0))

        else:
            raise ValueError()


    def save(self, f):
        """
        Save self to the file whose name is f.
        """
        pygame.image.save(self._surface, f)


    def width(self):
        """
        Return the width of self.
        """
        return self._surface.get_width()


    def height(self):
        """
        Return the height of self.
        """
        return self._surface.get_height()
 

    def get(self, x, y):
        """
        Return the color of self at location (x, y).
        """
        pygameColor = self._surface.get_at((x, y))
        return Color(pygameColor.r, pygameColor.g, pygameColor.b)


    def set(self, x, y, col):
        """
        Set the color of self at location (x, y) to col.
        """
        pygameColor = pygame.Color(col.getRed(), col.getGreen(),
           col.getBlue(), 0)
        self._surface.set_at((x, y), pygameColor)

