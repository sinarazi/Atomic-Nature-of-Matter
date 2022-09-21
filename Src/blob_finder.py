from Lib import *
import sys
from Lib.picture import Picture
from blob import Blob


class BlobFinder:
    """
    A data type for identifying blobs in a picture.
    """

    def __init__(self, pic, tau):
        """
        Constructs a blob finder to find blobs in the picture pic, using
        a luminance threshold tau.
        """

        # Initialize an empty list for the blobs in pic.
        self._blobs = []

        # Create a 2D list of booleans called marked, having the same
        # dimensions as pic.
        marked = stdarray.create2D(pic.width(), pic.height(), False)

        # Enumerate the pixels of pic, and for each pixel (i, j):
        # 1. Create a Blob object called blob.
        # 2. Call _findBlob() with the right arguments.
        # 3. Add blob to _blobs if it has a non-zero mass.
        for i in range(pic.width()):
            for j in range(pic.height()):
                blob = Blob()
                self._findBlob(pic, tau, i, j, marked, blob)
                if blob.mass() > 0:
                    self._blobs += [blob]

    def _findBlob(self, pic, tau, i, j, marked, blob):
        """
        Identifies a blob using depth-first search. The parameters are
        the picture (pic), luminance threshold (tau), pixel column (i),
        pixel row (j), 2D boolean matrix (marked), and the blob being
        identified (blob).
        """

        # Base case: return if pixel (i, j) is out of bounds, or if it
        # is marked, or if its luminance is less than tau.
        if i >= pic.width() or j >= pic.height() or i < 0 or j < 0 \
           or marked[i][j] is True or luminance.luminance(pic.get(i, j)) < tau:
            return

        # Mark the pixel.
        marked[i][j] = True

        # Add the pixel to blob.
        blob.add(i, j)

        # Recursively call _findBlob() on the N, E, W, S pixels.
        self._findBlob(pic, tau, i - 1, j, marked, blob)
        self._findBlob(pic, tau, i + 1, j, marked, blob)
        self._findBlob(pic, tau, i, j + 1, marked, blob)
        self._findBlob(pic, tau, i, j - 1, marked, blob)

    def getBeads(self, P):
        """
        Returns a list of all beads with >= P pixels.
        """

        Blob = []
        for i in self._blobs:
            if i.mass() >= P:
                Blob += [i]
        return Blob

def writeFile(sth, location):
    open(str(location), "w").write("\n".join(str(i) for i in sth))

# Takes an integer P, a float tau, and the name of a JPEG file as
# command-line arguments; writes out all of the beads with at least P
# pixels; and then writes out all of the blobs (beads with at least 1 pixel).
def _main():
    P = int(sys.argv[1])
    tau = float(sys.argv[2])
    pic = Picture(sys.argv[3])
    b = BlobFinder(pic, tau)
    beads = b.getBeads(P)
    stdio.writeln(str(len(beads)) + ' Beads:')
    for i in beads:
        stdio.writeln(str(i))
    blobs = b.getBeads(1)
    stdio.writeln(str(len(blobs)) + ' Blobs:')
    for i in blobs:
        stdio.writeln(str(i))

if __name__ == '__main__':
    _main()

#python blob_finder.py 0 180.0 Dataset/run_1/frame00001.jpg