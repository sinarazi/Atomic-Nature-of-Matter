
from utils import *
from utils import Picture
from blob import Blob
import os
import cv2
#import numpy as np




def create2D(rowCount, colCount, value=None):
    """
    Create and return a 2D array having rowCount rows and colCount
    columns, with each element initialized to value.
    """
    a = [None] * rowCount
    for row in range(rowCount):
        a[row] = [value] * colCount
    return a

class beadfinder:
    
    """
    A data type in ordert to identify blobs in a picture.
    """

    def __init__(self, pic, tau):
        
        """
        Constructs a blob finder to find blobs in the picture pic, using
        a luminance threshold tau.
        """

        self._blobs = [] # Initialize an empty list for the blobs in pic.    
       # marked = create2D(pic.width(), pic.height(), False) # the same dimension as pic
        # for i in range(pic.width()):
        #     for j in range(pic.height()):
        #         b = Blob()
        #         self.Blobfinder(pic, tau, i, j, marked, b)
        #         if b.mass() > 0:
        #             self._blobs += [b]
        row, col, _ = pic.shape
        marked = create2D(row, col, False)
        for i in range(row):
            for j in range(col):
                b = Blob()
                self.Blobfinder(pic, tau, i, j, marked, b)
                if b.mass() > 0:
                    self._blobs += [b]


    def Blobfinder(self, Pic, Tau, i, j, marked, b):  #  Identifies a blob using depth-first search.
        """
        picture (pic) 
        luminance threshold (tau) 
        pixel column (i)
        pixel row (j)
        2D boolean matrix (marked)
        the blob being identified (blob)
        """
        # Base case: return if pixel (i, j) is out of bounds, or if it
        # is marked, or if its luminance is less than tau.
        
        # if i >= Pic.width() or j >= Pic.height() or i < 0 or j < 0 \
        #    or marked[i][j] is True or luminance(Pic.get(i, j)) < Tau:
        #     return
        row, col, _ = Pic.shape
        if i >= row or j >= col or i < 0 or j < 0 \
           or marked[i][j] is True or luminance(Picture.get(i, j)) < Tau:
            return

       
        marked[i][j] = True  # Mark the pixel.
        b.add(i, j)          # Add the pixel to blob.
        
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


def writeFile(sth, location):
    open(str(location), "w").write("\n".join(str(i) for i in sth))


def createDataset(dataset, P, Tau):
    for dir1 in os.listdir(dataset):
        for file in os.listdir(os.path.join(dataset, dir1)):
            image_path= os.path.join(dataset, dir1,  file)
            Pic = Picture(image_path)
            b = beadfinder(Pic, Tau)
            Beads = b.getBeads(P)
            writeFile(Beads, "beadfinder_output/output.txt")

def _main():
    
    # P = 25
    # Tau = 180.0
    # dataset = r'F:/My projects/Atomic-Nature-of-Matter/Dataset/'
    # for i in os.listdir(dataset):
    #     Pic = Picture('frame00000.jpg')
    #     b = beadfinder(Pic, Tau)
    #     Beads = b.getBeads(P)
    #     writeFile(Beads, "beadfinder_output/output.txt")
    P = 25
    Tau = 180.0
    dataset = r'F:/My projects/Atomic-Nature-of-Matter/Dataset/'
    for i in os.listdir(dataset):
        Pic = cv2.imread(dataset + 'frame00000.jpg')
        b = beadfinder(Pic, Tau)
        Beads = b.getBeads(P)
        writeFile(Beads, "beadfinder_output/output.txt")
       

if __name__ == '__main__':
    _main()
