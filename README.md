# Atomic Nature of Matter

- The project of Princeton university

![Python-Project.gif](https://user-images.githubusercontent.com/45029937/79608759-cc920880-810a-11ea-85e1-d71ce40c98b3.gif)

Check the website [here](https://introcs.cs.princeton.edu/java/assignments/atomic.html). 

Re-affirm the atomic nature of matter by tracking the motion of particles undergoing Brownian motion, fitting this data to Einstein's model, and estimating Avogadro's number.

### Historical:
The atom played an integral role in 20th century physics and chemistry, but prior to 1908, the reality of atoms and molecules was not universally accepted. In 1827, the botanist Robert Brown observed the random erratic motion of particles found in wildflower pollen grains immersed in water using a microscope. This motion would later become known as ```Brownian motion```. Einstein hypothesized that this Brownian motion was the result of millions of tiny water molecules colliding with the larger pollen grain particles.
 In one of his "miraculous year" (1905) papers, Einstein formulated a quantitative theory of Brownian motion in an attempt to justify the "existence of atoms of definite finite size." His theory provided experimentalists with a method to count molecules with an ordinary microscope by observing their collective effect on a larger immersed particle. In 1908 Jean Baptiste Perrin used the recently invented ultramicroscope to experimentally validate Einstein's kinetic theory of Brownian motion, thereby providing the first direct evidence supporting the atomic nature of matter. His experiment also provided one of the earliest estimates of Avogadro's number. For this work, Perrin won the 1926 Nobel Prize in physics.

### The problem:
In this project, I will redo a version of Perrin's experiment. It is really simplified due to the fact that with modern video and computer technology, it is possible to accurately measure and track the motion of an immersed particle undergoing Brownian motion. The data was supplied by ```Princeton University``` and named as video microscopy data of polystyrene spheres ("beads") suspended in water, undergoing Brownian motion. The data is analyzed and determined how much each bead moves between observations. After being fitted to Einstein's model, it will estimate Avogadro's number.
  
### Particle identification:
The first challenge is to identify the beads amidst the noisy data. Each image is 640-by-480 pixels, and each pixel is represented by a Color object which needs to be converted to a luminance value ranging from 0.0 (black) to 255.0 (white). Whiter pixels correspond to beads (foreground) and blacker pixels to water (background). We break the problem into three pieces: (i) read in the picture, (ii) classify the pixels as foreground or background, and (iii) find the disc-shaped clumps of foreground pixels that constitute each bead.
Read in the image. Use the Picture data type from Section 3.1 to read in the image.
Classify the pixels as foreground or background. We use a simple, but effective, technique known as thresholding to separate the pixels into foreground and background components: all pixels with monochrome luminance values strictly below some threshold tau are considered background, and all others are considered foreground. The two pictures above illustrates the original frame (above left) and the same frame after thresholding (above right), using tau = 180.0. This value of tau results in an effective cut for the supplied data.
Find the blobs. A polystyrene bead is typically represented by a disc-like shape of at least some minimum number P (typically 25) of connected foreground pixels. A blob or connected component is a maximal set of connected foreground pixels, regardless of its shape or size. We will refer to any blob containing at least P pixels as a bead. The center-of-mass of a blob (or bead) is the average of the x- and y-coordinates of its constituent pixels.
Create a helper data type Blob that has the following API.
Create a helper data type Blob that has the following API.

#### public class Blob:

```
Blob()                    // construct an empty blob
add(int i, int j)    // add a pixel (i, j) to the blob
mass()                // return number of pixels added = its mass
distanceTo(Blob b) // return distance between centers of masses of this blob and b
toString()         // return string containing this blob's mass and center of mass
                                 // format center-of-mass coordinates with 4 digits to right
                                 // of decimal point
```

#### public class BlobFinder :

```
// find all blobs in the picture using the luminance threshold tau
def BlobFinder(Picture picture, double tau)

// return the number of beads with >= P pixels
def countBeads(int P)

// return all beads with >= P pixels
def Blob[] getBeads(int P)
```
