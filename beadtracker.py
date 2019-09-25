import stdio
import sys
from beadfinder import beadfinder
from picture import Picture


""" Takes an integer min_pixels, a float Tau, a float Delta, and a sequence of JPG
filenames as command-line arguments; identifies the Beads in each JPG
image using BlobFinder; and writes out (one per line, formatted with 4
decimal places to the right of decimal point) the radial distance that
each bead moves from one frame to the next (assuming it is no more than
Delta). """

"""
برای نمایش خروجی باید فایلهای jpg را به تک تک وارد نمود 
"""
def main():
    min_pixels = int(sys.argv[1])
    Tau = float(sys.argv[2]) # adade ashari
    Delta = float(sys.argv[3])
    bf = beadfinder(Picture(sys.argv[4]), Tau)
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
                stdio.writef('%.4f\n', min_dist)
        stdio.writeln()
        PrevBeads = CurrBeads

if __name__ == '__main__':
    main()
