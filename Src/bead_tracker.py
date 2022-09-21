import stdio
import sys
from blob_finder import BlobFinder
from picture import Picture



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
    P = int(sys.argv[1])
    tau = float(sys.argv[2])
    delta = float(sys.argv[3])
    bf = BlobFinder(Picture(sys.argv[4]), tau)
    prevBeads = bf.getBeads(P)
    for i in range(5, len(sys.argv)):
        bf = BlobFinder(Picture(sys.argv[i]), tau)
        currBeads = bf.getBeads(P)
        for currBead in currBeads:
            min_dist = float('inf')
            for prevBead in prevBeads:
                d = currBead.distanceTo(prevBead)
                if d <= delta and d < min_dist:
                    min_dist = d
            if min_dist != float('inf'):
                stdio.writef('%.4f\n', min_dist)
        stdio.writeln()
        prevBeads = currBeads
        

if __name__ == '__main__':
    main()

#python bead_tracker.py 25 180.0 25.0 run_1/frame00001.jpg  run_1/frame00002.jpg