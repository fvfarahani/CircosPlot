# CircosPlot
Discover Circos plots—visualize data in circular layout, ideal for revealing intricate relationships.

Install Circos:
http://aidanquinn.net/blog/blog/2015/11/11/installing-circos-on-mac-osx/

At the end:<br>
export PATH=~/Applications/circos/current/bin:$PATH<br>
execute either ~/.bashrc or ~/.bash_profile

1. Go to the directory containing circos.conf<br>
2. Type in terminal: circos -conf circos.conf



------------------------------------------------
https://github.com/moshi4/pyCirclize













-----------------------------------------------------------
The Glasser 2016 HCP MMP 1.0 is not a volumetric atlas.  Another paper of ours explains why it isn't, and why any binary volumetric form of it should not be considered a faithful representation of the entire cortex:

https://www.pnas.org/doi/10.1073/pnas.1801582115

However, the insula is a subset of cortex that has relatively low cross-subject variability in human subjects, so a version restricted to that region may be reasonable to represent as a volume file, if necessary.  We do have a probabilistic volume version of the entire MMP 1.0 in MNINonLinear space (mainly for the purpose of showing how blurry volumetric methods make it), but we didn't compute the centers of gravity, because they aren't a faithful representation of a non-spherical parcel, and we didn't expect the centers of gravity to be a required part of any format:

https://balsa.wustl.edu/file/kN6l6

This version also takes partial-voxel membership into account:

https://balsa.wustl.edu/file/np6v7

Neither of these includes smoothing effects, so data that has been volumetrically smoothed will implicitly have substantially larger blurring and conflation than these probabilistic versions.
