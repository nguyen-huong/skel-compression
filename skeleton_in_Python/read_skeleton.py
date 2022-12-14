# from conf import args as args

import utils
# import cv2
import numpy as np


def read_skeleton(skel):

	#open the skeleton file
	file = open(skel, 'r')

	read_lines = []

	for line in file:
		#strip away the '\n' characters and split the values by the spaces.
	    read_lines.append(line.strip('\n').split(' '))

	num_of_frames = int(read_lines[0][0]) #get the number of frames


	skeleton_data = None

	skeleton_data = utils.no_subject(num_of_frames, read_lines) #read the information from the list

	return skeleton_data


if __name__=='__main__':
	data = read_skeleton(skel)


