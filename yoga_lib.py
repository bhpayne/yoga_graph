import random
import networkx as nx
import matplotlib.pyplot as plt
import subprocess
import time
import os
import fnmatch

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
# 	viewer.terminate()
# 	viewer.kill()
	# better:
	# osascript -e 'tell application "Preview" to quit'
	
# https://docs.python.org/2/library/fnmatch.html
def find_picture(current_indx,delay,viewer):
	for filename in os.listdir('.'):
		list_of_files=[]
		if fnmatch.fnmatch(filename, str(current_indx)+'__*'):
			list_of_files.append(filename)
		if (len(list_of_files)>0):
			picturename=random.choice(list_of_files)
			launch_picture(picturename,delay,viewer)


def random_flow(DG,entry_point_indx,max_poses,field_val,delay,viewer):
	print("number of poses: "+str(max_poses))
	print("entry point: ")
	print(str(entry_point_indx)+" = "+DG.node[entry_point_indx][field_val])
	current_indx = entry_point_indx
	pose_count=1
	while(pose_count<max_poses):
# 		print(DG.node[current_indx])	
		find_picture(current_indx,delay,viewer)

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

