#!/usr/bin/env python
"""
Ben Payne
ben.is.located@gmail.com

Yoga graph

Use:

This work is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License.
To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/4.0/.
"""

import networkx as nx  # format for directed graph
import yoga_db as ydb  # nodes and edges of graph
#import yoga_lib as ylib  # library of functions for acting on graph

DG = nx.DiGraph()  # initialize directed graph using networkx
DG = ydb.pose_properties(DG)  # load node properties
DG = ydb.pose_transitions(DG)  # load edges

nx.nx_agraph.write_dot(DG, "all_nodes.gv")

# see https://dreampuf.github.io/GraphvizOnline
# to plot the graphviz
