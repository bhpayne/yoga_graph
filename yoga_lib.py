#!/usr/bin/env python
"""
Ben Payne
ben.is.located@gmail.com

Yoga graph

This is a library of functions used by the main YogaGraph program
This file contains no graph data

This work is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License. 
To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/4.0/.
"""

import networkx as nx # graph format
import matplotlib.pyplot as plt # for plotting graph
import random # for selecting next pose
import subprocess # launch picture viewer 
import time # for delaying next pose
import os
import signal # for keyboard input with timeout
import fnmatch # for matching file name of pictures
import yaml # used to read "config.input"

"""
def interrupted(signum, frame):
	"called when read times out"
	print 'interrupted!'
	signal.signal(signal.SIGALRM, interrupted)

def input(delay,signal):
	try:
		print 'You have '+str(delay)+' seconds to type in your stuff...'
		foo = raw_input()
		return foo
	except:
		# timeout
		print("timeout reached")
		signal.alarm(0)
		foo = "none"
		return foo
"""

def get_inputs(config_filename):
	# https://yaml-online-parser.appspot.com/
	input_stream=file(config_filename,'r')
	input_data=yaml.load(input_stream)
	viewer=input_data["viewer"]
	use_viewer=input_data["use_viewer"]
	directory_containing_pictures=input_data["directory_containing_pictures"]
	entry_point_index=input_data["entry_point_index"]
	max_poses=input_data["max_poses"]
	delay=input_data["delay"]
	field_value=input_data["field_value"]
	return viewer,use_viewer,directory_containing_pictures,entry_point_index,max_poses,delay,field_value

def plot_graph_nodes(DG):
	#nx.draw_random(DG)
	nx.draw_spring(DG)
	plt.show()

def plot_graph_with_labels(DG,label_str):
	labels={}
	for node_indx in DG.nodes():
		labels[node_indx] = DG.node[node_indx][label_str]

	pos = nx.spring_layout(DG) # other choices are circular, random, shell, spectral

	nx.draw_networkx_labels(DG,pos,labels,font_size=12)
	nx.draw_networkx_nodes(DG,pos)
	nx.draw_networkx_edges(DG,pos,width=1)

	plt.show() # matplotlib

def list_cycles(DG):
	print("cycles")
	print(nx.simple_cycles(DG))
	print(nx.cycle_basis(DG,0)) # not implemented for directed graphs

def launch_picture(picturename,delay,viewer_name):
	print("picture = "+picturename)
	viewer = subprocess.Popen([viewer_name, picturename])
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
# 			print(filename)
			list_of_files.append(filename)
# 	print(list_of_files)
	if (len(list_of_files)>0):
		foundpic=True
		picturename=random.choice(list_of_files)
	else:
		foundpic=False
		picturename=""
	return foundpic,picturename

# http://stackoverflow.com/questions/3471461/raw-input-and-timeout
# http://stackoverflow.com/questions/1335507/keyboard-input-with-timeout-in-python
def get_user_feedback(delay,difficulty):
	user_feedback_speed = raw_input('Currently '+str(delay)+' seconds. faster/slower? [f/s]: ')
	if (user_feedback_speed=="f"):
		delay=delay-1
	elif (user_feedback_speed=="s"):
		delay=delay+1
	user_feedback_difficulty = raw_input('Current max difficulty '+str(difficulty)+'. harder/easier? [h/e]: ')
	if (user_feedback_difficulty=="h"):
		difficulty=difficulty+1
	elif (user_feedback_difficulty=="e"):
		difficulty=difficulty-1
	return delay,difficulty

def random_flow(DG,entry_point_indx,max_poses,field_val,delay,viewer,use_viewer):
	pose_history=[] # all the poses
	symmetry_history=[] # left-right cycle
	print("number of poses: "+str(max_poses))
	print("delay: "+str(delay)+" seconds")
	if (use_viewer): print("launching pictures")
	else: print("not launching pictures")
	print("\nentry point: ")
	print(str(entry_point_indx)+" = "+DG.node[entry_point_indx][field_val])
	current_indx = entry_point_indx

	pose_count=1
	while(pose_count<max_poses):
# 		print(DG.node[current_indx])
		pose_history.append(current_indx)
		symmetry_history.append(current_indx)

		# display current pose picture
		if (use_viewer):
			print("finding pictures")
			[foundpicture,picturename]=find_picture(current_indx,delay,viewer)
			print("pic="+picturename)
			if foundpicture:
				launch_picture(picturename,delay,viewer)

		print("\a") # audible tone
# 		difficulty=1
# 		[delay,difficulty]=get_user_feedback(delay,difficulty)
		"""
		# set alarm
		signal.alarm(delay)
		s = input(delay,signal)
		# disable the alarm after success
		signal.alarm(0)
		print 'You typed', s
		"""
		time.sleep(delay)

		# list next pose choices
# 		print("choices:")
		choices=DG.successors(current_indx)
		#print(choices)
		"""
		for pose_indx in choices:
			if (DG.node[pose_indx]["two_sided"]==False):
				print("   "+str(pose_indx)+" = "+DG.node[pose_indx][field_val])
			else:
				print("   "+str(pose_indx)+" = "+DG.node[pose_indx][field_val]+", left side")
		"""
		new_indx=random.choice(DG.successors(current_indx))
		print("\nnext move:")
		print(str(new_indx)+" = "+DG.node[new_indx][field_val])
		if (DG.node[new_indx]["hindi_name"] != ""):
			print(DG.node[new_indx]["hindi_name"])
		if (DG.node[new_indx]["description"] != ""):
			print(DG.node[new_indx]["description"])
		
		current_indx=new_indx
		pose_count = pose_count+1

	return pose_history

def produce_graphml(DG,filename):
	nx.write_graphml(DG,filename)
	