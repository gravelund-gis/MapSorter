#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 7 12:03:53 2019

@author: Joakim Jörwall
"""
import os
from os import listdir
from os.path import isfile, join
import shutil


def make_image_list(directory):
	"""
	Creates a list of all the image files in the image directory; files ONLY
	:param directory:
	:return file list:
	"""
	only_files = [file for file in listdir(directory) if isfile(join(directory, file))]
	return only_files


def group_image(directory, image, group):
	"""
	Creates subdirectories and copies the images into them based on their assigned cluster
	:param directory, image, group:
	:return none:
	"""
	if os.path.exists(directory + "\\" + group):
		pass
	else:
		try:
			os.mkdir(directory + '\\' + group)
			print("Successfully created directory", group)
		except OSError:
			print("Creation of directory failed.")
	try:
		shutil.copy(str(directory + '\\' + image), str(directory + "\\" + group + "\\" + image))
	except OSError as OSe:
		print(OSe)
