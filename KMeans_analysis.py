#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 7 12:03:53 2019

@author: Joakim Jörwall
"""
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import datetime


def cluster_analysis(data_array, k):
	"""
	Groups (clusters) the input images into "k" groups (user input for k is expected), based on K-Means clustering.
	Outputs a plot of the resulting clusters, including the cluster centers. No data scaling is performed.
	:param data_array, k:
	:return cluster plot, labels:
	"""
	# MODELING:
	# Create a K-Means instance with k clusters: model
	model = KMeans(n_clusters=int(k))

	# Fit the model to the dataset
	model.fit(data_array)

	# Determine the cluster labels of the dataset: labels
	labels = model.predict(data_array)

	# PLOTTING DATASET and MODEL CENTROIDS
	# Assign the columns: xs and ys
	xs = data_array[:, 0]
	ys = data_array[:, 1]

	# Assign the cluster centers: centroids
	centroids = model.cluster_centers_

	# Assign the columns of centroids: centroids_x, centroids_y
	centroids_x = centroids[:, 0]
	centroids_y = centroids[:, 1]

	# Make a scatter plot of xs and ys, using labels to define the colors
	plt.scatter(xs, ys, c=labels, alpha=0.5)

	# Make a scatter plot of centroids_x and centroids_y
	plt.scatter(centroids_x, centroids_y, marker='D', s=30)

	# Add a title showing current date/time
	plt.title(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

	print("\nInspect the cluster plot shown.\nWhen ready, close the plot and the images will be sorted\n"
	      "and copied into subdirectories.")
	plt.show()

	return labels
