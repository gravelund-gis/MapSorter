#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 7 12:03:53 2019

@author: Joakim Jörwall
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
from file_handling import make_image_list


def descriptive_stats_image(image_array):
	"""
	Compute and present simple descriptive stats for an image distribution
	:param image_array:
	:return median, skew, kurtosis:
	"""
	dist = image_array

	# mean = np.mean(dist, axis=0)
	# std = np.std(dist, axis=0)
	# band_sum = np.sum(dist)

	median = np.median(dist, axis=0)
	skew = scipy.stats.skew(dist)
	kurtosis = scipy.stats.kurtosis(dist)

	return median, skew, kurtosis


def get_rgb_component_stats(rgb_image):
	"""
	Splits an RGB image into the 3 image bands (8 bit, 0-255) and calculates band statistics
	:param rgb_image:
	:return band median, skew, kurtosis:
	"""
	# Load the image into a 3-D array: image
	image_name = rgb_image
	image = plt.imread(image_name)

	# Extract 2-D arrays of the RGB channels: red, green, blue
	red, green, blue = image[:, :, 0], image[:, :, 1], image[:, :, 2]

	# Flatten the 2-D arrays of the RGB channels into 1-D
	red_pixels = red.flatten()
	blue_pixels = blue.flatten()
	green_pixels = green.flatten()

	r_median, r_skew, r_kurtosis = descriptive_stats_image(red_pixels)
	g_median, g_skew, g_kurtosis = descriptive_stats_image(green_pixels)
	b_median, b_skew, b_kurtosis = descriptive_stats_image(blue_pixels)

	return r_median, r_skew, r_kurtosis,\
	       g_median, g_skew, g_kurtosis,\
	       b_median, b_skew, b_kurtosis


def get_rgb_values(directory):
	"""
	Creates an ordered list of calculated image band statistics
	:param directory:
	:return rgb_values_list, image_list:
	"""
	image_list = make_image_list(directory)
	rgb_values_list = []

	for image in image_list:
		r_median, r_skew, r_kurtosis,\
		g_median, g_skew, g_kurtosis,\
		b_median, b_skew, b_kurtosis =\
			get_rgb_component_stats(directory + '\\' + image)

		image_rgb_list = [r_median,
		                  g_median,
		                  b_median,
		                  r_skew,
		                  g_skew,
		                  b_skew,
		                  r_kurtosis,
		                  g_kurtosis,
		                  b_kurtosis,
		                  ]

		rgb_values_list.append(image_rgb_list)

	return rgb_values_list, image_list
