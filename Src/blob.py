class Blob:
 
    def __init__(self):

        # generation of vacant blob
        self._P = 0    # The number of pixels
        self._x = 0.0  # x-coordinate mass center
        self._y = 0.0  # y-coordinate mass center


    def add(self, i, j):

        # adding pixel(i, j) to blob b
        self._x = (self._x * self._P + i) / (self._P + 1)
        self._y = (self._y * self._P + j) / (self._P + 1)
        self._P += 1


    def mass(self):
        
        # return the number of pixels which mass is important
        return self._P


    def distanceTo(self, other):  
        # euclidian distance of 2 blobs
        x1 = self._x
        y1 = self._y
        x2 = other._x
        y2 = other._y

        dx = (x1 - x2) ** 2
        dy = (y1 - y2) ** 2
        d = (dx + dy) ** 0.5

        return d


    def __str__(self):

        # generation of string of blobs
        return '%d (%.4f, %.4f)' % (self._P, self._x, self._y)
