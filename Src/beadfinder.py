from utils import *
import sys
import re
from blob import Blob
import numpy as np

class beadfinder:
    
    """
    A data type in ordert to identify blobs in a picture.
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
        
        marked = np.array(pic.width(), pic.height(), False)
  
        for i in range(pic.width()):
            for j in range(pic.height()):
                b = Blob()
                self.Blobfinder(pic, tau, i, j, marked, b)
                if b.mass() > 0:
                    self._blobs += [b]

    def Blobfinder(self, Pic, Tau, i, j, marked, b):  
        
        """
        Identifies a blob using depth-first search.
        """
        # picture (pic) 
        # luminance threshold (tau) 
        # pixel column (i)
        # pixel row (j)
        # 2D boolean matrix (marked)
        # the blob being identified (blob).
        

        # Base case: return if pixel (i, j) is out of bounds, or if it
        # is marked, or if its luminance is less than tau.
        
        if i >= Pic.width() or j >= Pic.height() or i < 0 or j < 0 \
           or marked[i][j] is True or luminance(Pic.get(i, j)) < Tau:
            return

       
        marked[i][j] = True  # Mark the pixel.
        b.add(i, j) # Add the pixel to blob.
        
        self.Blobfinder(Pic, Tau, i - 1, j, marked, b)
        self.Blobfinder(Pic, Tau, i + 1, j, marked, b)
        self.Blobfinder(Pic, Tau, i, j + 1, marked, b)
        self.Blobfinder(Pic, Tau, i, j - 1, marked, b)

    def getBeads(self, P):
        """
        Returns a list of all beads with >= P pixels.
        """

        Blob = []
        for i in self._blobs:
            if i.mass() >= P:
                Blob += [i]
        return Blob


"""
Takes an integer P, a float Tau, and the name of a JPG file as
command-line arguments; writes out all of the Beads with at least P
pixels; and then writes out all of the blobs (beads with at least 1 pixel).
"""

"""
Entry
"""
def writeln(x=''):
    """
    Write x and an end-of-line mark to standard output.
    """
    if sys.hexversion < 0x03000000:
        x = unicode(x)
        x = x.encode('utf-8')
    else:
        x = str(x)
    sys.stdout.write(x)
    sys.stdout.write('\n')
    sys.stdout.flush()


def _main():
    
    P = int(sys.argv[1])
    Tau = float(sys.argv[2])
    Pic = Picture(sys.argv[3])
    b = beadfinder(Pic, Tau)
    Beads = b.getBeads(P)
    
    for i in Beads:
        writeln(str(i))

if __name__ == '__main__':
    _main()
