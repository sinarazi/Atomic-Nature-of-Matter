import sys
import stdio
from beadfinder import beadfinder
from utils import *
#from Libraries import *
from argparse import ArgumentParser


""" Takes an integer min_pixels, a float Tau, a float Delta, and a sequence of JPG
filenames as command-line arguments; identifies the Beads in each JPG
image using BlobFinder; and writes out (one per line, formatted with 4
decimal places to the right of decimal point) the radial distance that
each bead moves from one frame to the next (assuming it is no more than
Delta). """


def main():
    # min_pixels = 25
    # Tau = 180.0
    # Delta = 25.0
    # bf = beadfinder(Picture('F:/My projects/Atomic-Nature-of-Matter/Dataset/frame00000.jpg'), Tau)
    # PrevBeads = bf.getBeads(min_pixels)
    # dataset = r'F:/My projects/Atomic-Nature-of-Matter/Dataset/'

    # for i in range(5, len(sys.argv)):
    #     bf = beadfinder(Picture(sys.argv[i]), Tau)
    #     CurrBeads = bf.getBeads(min_pixels)
    #     for currBead in CurrBeads:
    #         min_dist = float('inf')
    #         for prevBead in PrevBeads:
    #             d = currBead.distanceTo(prevBead)
    #             if d <= Delta and d < min_dist:
    #                 min_dist = d
    #         if min_dist != float('inf'):
    #             print('%.4f\n', min_dist)
    #     writeFile("beadtracker_output/output.txt")
    #     PrevBeads = CurrBeads
    ap = ArgumentParser()
    ap.add_argument('P')

    P = int(sys.argv[1])
    tau = float(sys.argv[2])
    delta = float(sys.argv[3])
    pic = Picture(sys.argv[4])
    prevBeads = beadfinder(pic, tau).getBeads(P)
    # for every frame:
    for i in (5, len(sys.argv)):
        currBeads = beadfinder(Picture(i), tau).getBeads(P)
        # for every bead in that frame:
        for currBead in range(len(currBeads)):
            # intialize shortest_dist with largest possible dimension:
            shortest_dist = max([pic.width(), pic.height()])
            # search for currBead closest to prevBead:
            for v in range(min([len(currBeads), len(prevBeads)])):
                d = prevBeads[v].distanceTo(currBeads[currBead])
                if d < shortest_dist:
                    shortest_dist = d
            # confirm that displacement is within delta:
            if shortest_dist <= delta:
                # if yes, then show the distance:
                stdio.writef('%.4f\n', shortest_dist)

        stdio.writeln()
        prevBeads = currBeads

if __name__ == '__main__':
    main()
