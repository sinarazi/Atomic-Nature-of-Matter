# Atomic Nature of Matter

- The project of ```Princeton university```

<img src ="Img/Brownian.gif">

Check the website [here](https://introcs.cs.princeton.edu/java/assignments/atomic.html) so as to download the dataset. 

Re-affirm the atomic nature of matter by tracking the motion of particles undergoing Brownian motion, fitting this data to Einstein's model, and estimating Avogadro's number.

### Historical:
The atom was crucial to the development of physics and chemistry in the 20th century, yet until 1908, not everyone recognized the existence of atoms and molecules. Robert Brown, a botanist, used a microscope to study the erratic, random motion of particles in water-immersed wildflower pollen grains in 1827. Later, this motion would be referred to as a '''Brownian motion'''. The Brownian motion, according to Einstein's theory, was brought about by millions of tiny water molecules slamming into the bigger pollen grain particles.
Einstein developed a quantitative theory of Brownian motion in one of his "miraculous year" (1905) works in an effort to support the "presence of atoms of definite finite size." His theory gave researchers a way to count molecules using a regular microscope by

### The problem:
In this project, I will redo a version of Perrin's experiment. It is really simplified due to the fact that with modern video and computer technology, it is possible to accurately measure and track the motion of an immersed particle undergoing Brownian motion. The data was supplied by ```Princeton University``` and named as video microscopy data of polystyrene spheres ("beads") suspended in water, undergoing Brownian motion. The data is analyzed and determined how much each bead moves between observations. After being fitted to Einstein's model, it will estimate Avogadro's number.
  
### Particle identification:
The first challenge is to identify the beads amidst the noisy data. Each image is 640-by-480 pixels, and each pixel is represented by a Color object which needs to be converted to a luminance value ranging from 0.0 (black) to 255.0 (white). Whiter pixels correspond to beads (foreground) and blacker pixels to water (background). We break the problem into three pieces: (i) read in the picture, (ii) classify the pixels as foreground or background, and (iii) find the disc-shaped clumps of foreground pixels that constitute each bead.
Read in the image. Use the Picture data type from Section 3.1 to read in the image.
Classify the pixels as foreground or background. We use a simple, but effective, technique known as thresholding to separate the pixels into foreground and background components: all pixels with monochrome luminance values strictly below some threshold tau are considered background, and all others are considered foreground. The two pictures above illustrates the original frame (above left) and the same frame after thresholding (above right), using tau = 180.0. This value of tau results in an effective cut for the supplied data.
Find the blobs. A polystyrene bead is typically represented by a disc-like shape of at least some minimum number P (typically 25) of connected foreground pixels. A blob or connected component is a maximal set of connected foreground pixels, regardless of its shape or size. We will refer to any blob containing at least P pixels as a bead. The center-of-mass of a blob (or bead) is the average of the x- and y-coordinates of its constituent pixels.
Create a helper data type Blob that has the following API.


### How to run:

####
```
```
####
```
```
####
```
```
