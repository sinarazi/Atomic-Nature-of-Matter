class Blob:
 
    # Eraeye Blob 

    def __init__(self):

        # Moarefi yek blobe khali

        self._P = 0  # tedade pixel ha
        self._x = 0.0  # x-coordinate markaze jerm
        self._y = 0.0  # y-coordinate markaze jerm

    def add(self, i, j):

        # ezafe kardan pixel(i, j) be blob b

        self._x = (self._x * self._P + i) / (self._P + 1)
        self._y = (self._y * self._P + j) / (self._P + 1)
        self._P += 1

    def mass(self):
        
        # returne tedade pixel haye afzode shode be in blob beEbarati return kardan jerm an

        return self._P

    def distanceTo(self, other):
        
        # fasele oglidosi mian markaze do blob

        x1 = self._x
        y1 = self._y
        x2 = other._x
        y2 = other._y

        dx = (x1 - x2) ** 2
        dy = (y1 - y2) ** 2
        d = (dx + dy) ** 0.5

        return d

    def __str__(self):

        # ijade yek baznemayee reshtei az blob

        return '%d (%.4f, %.4f)' % (self._P, self._x, self._y)
