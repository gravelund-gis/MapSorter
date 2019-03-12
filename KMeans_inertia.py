#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 7 12:03:53 2019

@author: Joakim Jörwall
"""
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


def find_likely_number_of_groups(data_array, kn):
	"""
	Finds the likely number of image groups (clusters) "k" among the input images.
	The most likely k to use for the sorting is located at the "knee" of the K-Means inertia graph,
	where the graph is flattening out (at the bottom). The lower the inertia, the tighter the groups
	will be. However, the trade-off will be more clusters. No data scaling is performed.
	:param data_array, kn:
	:return inertia plot, user input request:
	"""
	ks = range(1, kn + 1)
	inertias = []

	try:
		for k in ks:
			# Create a K-Means instance with k clusters: model
			model = KMeans(n_clusters=k)

			# Fit the model to the dataset
			model.fit(data_array)

			# Append the inertia to the list of inertias
			inertias.append(model.inertia_)
	except ValueError as e:
		print(e, "Cluster value must not be higher than the number of images to be analyzed.")
		pass

	# Plot ks vs. inertias
	plt.plot(ks, inertias, '-o')
	plt.xlabel('number of clusters, k')
	plt.ylabel('inertia')
	plt.xticks(ks)
	print("\nInspect the inertia plot shown and select a suitable 'k' value at the\n'knee', then close the plot and "
	      "enter the chosen integer value\nat the prompt (a value must be input!).\n")
	plt.show()

	return input("Enter your chosen value of 'k': ")
