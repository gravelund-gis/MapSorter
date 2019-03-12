#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 7 12:03:53 2019

@author: Joakim Jörwall
"""
import time
import numpy as np
from KMeans_inertia import find_likely_number_of_groups
from KMeans_analysis import cluster_analysis
from file_handling import group_image
from stats import get_rgb_values


def map_sorter(directory_path):
	t0 = time.time()
	
	print("Extracting RGB band characteristics from images.\nThis may take a while...\n")

	rgb_values_list, image_list = get_rgb_values(directory_path)
	data_array = np.array(rgb_values_list)

	# K-MEANS INERTIAS:
	print("Input the maximum number of image groups/clusters, for graphing.\n"
	      "Note that this value must not be higher than the number of images\n"
	      "to be analyzed. The default is 10.\n")

	kn = int(input("Enter maximum number of groups: ") or "10")
	k = find_likely_number_of_groups(data_array, kn)

	# K-MEANS MODELING:
	# Create a K-Means instance with k clusters
	labels = cluster_analysis(data_array, k)

	# Create a new directory for each unique group and copy the images into the directories according
	# to its group:
	cluster_dict = dict(zip(image_list, labels))

	for key, value in cluster_dict.items():
		group_image(directory_path, key, str(value))

	delta_t = time.time() - t0
	print("\nDONE! in {} s".format(round(delta_t, 3)))


if __name__ == '__main__':
	try:
		directory_path_static = r'E:\SLU\Grouping\clustering\0'
		directory_path = str(input("\nEnter full path to image directory: \n") or directory_path_static)
		# NOTE: If a static image directory path is desired, enter it above and simply hit Enter when prompted.
		# Otherwise, enter the desired path when prompted.

		map_sorter(directory_path)
	except OSError as e:
		print(e, "No such directory exists. Check spelling and omit any quotes. Use double backslashes in path if "
		      "needed.")
