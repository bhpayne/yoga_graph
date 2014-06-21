#!/usr/bin/env python
"""
Ben Payne
ben.is.located@gmail.com

Yoga graph

Use: 

This work is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License. 
To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/4.0/.
"""


import random
import networkx as nx
import matplotlib.pyplot as plt
import yoga_lib as ylib
import yoga_db as ydb

viewer='/Applications/Preview.app/Contents/MacOS/Preview'
#viewer='/Applications/Firefox.app/Contents/MacOS/firefox'
#viewer='/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome'

# initialize graph
DG=nx.DiGraph()

DG=ydb.pose_properties(DG)
DG=ydb.pose_transitions(DG)

# create visual graph
#yl.plot_graph_with_label(DG,'english_name')

entry_point_index=4
max_poses=4
delay=3 # seconds
field_val='english_name'
ylib.random_flow(DG,entry_point_index,max_poses,field_val,delay,viewer)
