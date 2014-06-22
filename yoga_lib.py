#!/usr/bin/env python
"""
Ben Payne
ben.is.located@gmail.com

Yoga graph

This is a library called by the main YogaGraph program

This work is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License. 
To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/4.0/.
"""

import networkx as nx # graph format
import matplotlib.pyplot as plt # for plotting graph
import random # for selecting next pose
import subprocess # launch picture viewer 
import time # for delaying next pose
import os
import fnmatch # for matching file name of pictures

def plot_graph_nodes(DG):
	#nx.draw_random(DG)
	nx.draw_spring(DG)
	plt.show()

def plot_graph_with_label(DG,label_str):
	labels={}
	for node_indx in DG.nodes():
		labels[node_indx] = DG.node[node_indx][label_str]

	pos = nx.spring_layout(DG) # other choices are circular, random, shell, spectral

	nx.draw_networkx_labels(DG,pos,labels,font_size=12)
	nx.draw_networkx_nodes(DG,pos)
	nx.draw_networkx_edges(DG,pos,width=1)

	plt.show()

def list_cycles(DG):
	print("cycles")
	print(nx.simple_cycles(DG))
	print(nx.cycle_basis(DG,0)) # not implemented for directed graphs

def launch_picture(picturename,delay,viewer):
	print("picture = "+picturename)
	viewer = subprocess.Popen([viewer, picturename])
	time.sleep(delay)
	viewer.terminate()
	viewer.kill()
	# better?
# 	osascript -e 'tell application "Preview" to quit'
	
# https://docs.python.org/2/library/fnmatch.html
def find_picture(current_indx,delay,viewer):
	list_of_files=[]
	for filename in os.listdir('pose_pictures'):
# 		print(filename)
		if fnmatch.fnmatch(filename, str(current_indx)+'__*'):
			print(filename)
			list_of_files.append(filename)
# 	print(list_of_files)
	if (len(list_of_files)>0):
		foundpic=True
		picturename=random.choice(list_of_files)
	else:
		foundpic=False
		picturename=""
	return foundpic,picturename

def random_flow(DG,entry_point_indx,max_poses,field_val,delay,viewer):
	print("number of poses: "+str(max_poses))
	print("entry point: ")
	print(str(entry_point_indx)+" = "+DG.node[entry_point_indx][field_val])
	current_indx = entry_point_indx
	pose_count=1
	while(pose_count<max_poses):
# 		print(DG.node[current_indx])

		# display current pose picture
# 		print("finding pictures")
		[foundpicture,picturename]=find_picture(current_indx,delay,viewer)
# 		print("pic="+picturename)
		if foundpicture:
			launch_picture(picturename,delay,viewer)

		# list next pose choices
		print("choices:")
		choices=DG.successors(current_indx)
		#print(choices)
		for pose_indx in choices:
			if (DG.node[pose_indx]["two_sided"]==False):
				print("   "+str(pose_indx)+" = "+DG.node[pose_indx][field_val])
			else:
				print("   "+str(pose_indx)+" = "+DG.node[pose_indx][field_val]+", left side")
		new_indx=random.choice(DG.successors(current_indx))
		print("next move:")
		print(str(new_indx)+" = "+DG.node[new_indx][field_val])
		
		current_indx=new_indx
		pose_count = pose_count+1

