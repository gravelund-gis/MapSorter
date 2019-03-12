# MapSorter v. 0.1
Initially created for the Swedish University of Agricultural Sciences (SLU) at Alnarp and Uppsala.
----------------
Developed using Python v. 3.6.2.

In addition to the standard libraries (NumPy, Matplotlib, etc.) it requires the following modules to be installed:

Pillow (to handle the .tiff image format)

scipy (to calculate RGB band stats)

scikit-learn (to perform clustering)

The program may be run by simply double-clicking the main file 'MapSorter.py' in a file browser (e.g. Windows Explorer) or console. Or, run it using any Python IDE of your choice (Idle, PyCharm, etc.).
-----------------

WHAT IT DOES:
Automatically discovers cluster patterns in remote sensing (or any other) RGB imagery sets using the K-Means unsupervised machine learning algorithm, based on specific image characteristics. Similar images are then sorted into distinctive subdirectories.

The initial aim is as an upstream aid in preparation for semi-automatic LU/LC classification of very large sets of current/historic map tiles, where tiles may differ from one another in terms of hue or colorization. However, it may conceivably also prove useful in change detection applications, e.g. for time series NDVI.

HOW IT WORKS:
Simply by specifying the RGB image directory at the prompt shown when the program has been started (or optionally by using a static (hardcoded) directory path), then:

- The RGB images are split into their constituent bands;
- Statistics are extracted on each band. Statistics currently calculated are the band distribution median, skew, and kurtosis;
- The K-Means inertia is calculated and plotted as a parameter tuning aid to the user, to determine a suitable number of clusters 'k' for the image set in question (the only additional input required from the user);
- K-Means clustering is performed based on the extracted statistics and the number of specified clusters;
- The clustering result is plotted for user inspection;
- The original RGB images are copied into separate subdirectories (0, 1, 2 ...) for each cluster.

If, upon inspection of the cluster plot, the number of clusters 'k' should be higher or lower to adequately account for the image set, simply delete the copy subdirectories, rerun the program and choose a different 'k'.

Additionally, the program may be used iteratively upon the individual subdirectories, to obtain even finer-grained clustering, if so desired.
