import random
import networkx as nx
import matplotlib.pyplot as plt
import yoga_lib as yl

# initialize graph
DG=nx.DiGraph()

DG=yl.pose_properties(DG)
DG=yl.pose_transitions(DG)

yl.plot_graph_with_label(DG,'english_name')

#yl.random_flow(DG)
