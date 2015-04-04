#!/usr/bin/env python
"""
Ben Payne
ben.is.located@gmail.com

Yoga graph

Use: 

This work is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License. 
To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/4.0/.
"""

import networkx as nx # format for directed graph
import yoga_db as ydb # nodes and edges of graph
import yoga_lib as ylib # library of functions for acting on graph

DG=nx.DiGraph() # initialize directed graph using networkx
DG=ydb.pose_properties(DG) # load node properties
DG=ydb.pose_transitions(DG) # load edges

#ylib.plot_graph_nodes(DG) # generate visual graph using networkx
#ylib.plot_graph_with_labels(DG,'english_name') # generate visual graph, plot using matplotlib

[viewer,use_viewer,directory_containing_pictures,entry_point_index,max_poses,delay,field_value]=ylib.get_inputs("config.input")

# print(viewer)
# print(directory_containing_pictures)
# print(entry_point_index)
# print(max_poses)

pose_history=ylib.random_flow(DG,entry_point_index,max_poses,field_value,delay,viewer,use_viewer)

#filename="20140627.graphml"
#nx.write_graphml(DG,filename)