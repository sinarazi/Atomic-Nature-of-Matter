import sys
from beadfinder import beadfinder, writeFile
from utils import *


""" Takes an integer min_pixels, a float Tau, a float Delta, and a sequence of JPG
filenames as command-line arguments; identifies the Beads in each JPG
image using BlobFinder; and writes out (one per line, formatted with 4
decimal places to the right of decimal point) the radial distance that
each bead moves from one frame to the next (assuming it is no more than
Delta). """

"""
we have to add jpg files one by one in order to show output.
"""
def main():
    min_pixels = 25
    Tau = 180.0
    Delta = 25.0
    bf = beadfinder(Picture('F:/My projects/Atomic-Nature-of-Matter/Dataset/frame00000.jpg'), Tau)
    PrevBeads = bf.getBeads(min_pixels)

    for i in range(5, len(sys.argv)):
        bf = beadfinder(Picture(sys.argv[i]), Tau)
        CurrBeads = bf.getBeads(min_pixels)
        for currBead in CurrBeads:
            min_dist = float('inf')
            for prevBead in PrevBeads:
                d = currBead.distanceTo(prevBead)
                if d <= Delta and d < min_dist:
                    min_dist = d
            if min_dist != float('inf'):
                print('%.4f\n', min_dist)
        writeFile("beadtracker_output/output.txt")
        PrevBeads = CurrBeads

if __name__ == '__main__':
    main()
