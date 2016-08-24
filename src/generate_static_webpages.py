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

# write to 
# ../site/generated_pages

#list_of_nodes=DG.nodes()
#list_of_edges=DG.edges()	

# edges associated with node 0: 
# DG[0]

for this_indx in range(len(DG)):
	dic_for_this_node=DG.nodes(data=True)[this_indx][1]
	list_of_edges_for_this_node=DG[this_indx].keys()