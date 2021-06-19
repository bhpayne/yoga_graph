yoga_graph
==========

tl;dr: graph of yoga poses and transition

installation
============

sudo pip install pyyaml

introduction
============

All styles of yoga feature poses and transitions between poses.
A style is often differentiated by the poses practiced, the speed of transition, and the length of holding the pose.

The poses from all styles of yoga form the superset contained in the database (yoga_db.py). The database includes the connections between poses. Thus, it is possible to construct a graph. This graph includes all styles of yoga.


jargon
======
A pose is any body position held for a length of time. A pose is a node on the graph
A transition is a body movement between poses. A transition is an edge on the graph
A flow is a sequence of poses and transitions.  

Relative Difficulty
===================
Poses are of varying difficulty, but the level of difficulty depends on the practitioner. Thus, determining pose difficulty is subjective
If you are in a pose, transitions to adjacent poses on the graph are of varying difficulty. Transitions are easier to compare
Each edge is assigned a numerical score (positive integer) to measure relative difficulty of the transition.

Example
=======
Suppose you are in plank. You can transition to low pushup, then to laying flat on stomach. Thus, plank, low pushup, and laying on stomach are nodes, connected by two edges (plant to low pushup, and low pushup to laying on stomach). 
It is not possbile to get from low pushup to happy camper directly without passing through a few other poses. Thus, no transition (edge on the graph) exists between "laying on stomach" and happy camper.


previous work
=============
Many yogis observe that there is a library of poses and document this. Examples include Dharma Mitra's poster of 908 poses and his book "608 Asanas". Various websites, such as www.yogajournal.com, catalog pictures of poses and their description. Books specific to a style of yoga document their flow or flows


format
======
Books are commonly linear in layout, which is a good format for describing a flow. A large highly connected graph is easier to explore in elecronic (maleable) format.  

Python is an easy to use and widely used language. 
The networkx package makes working with graphs straight forward


tasks
=====

- [ ] Include more poses
- [ ] Include more transitions
- [ ] Include difficulty rankings for transitions
- [ ] Verify existing graph entries
- [ ] document flows from various styles
- [ ] output different graph formats (i.e., for Yed, GraphML)
- [ ] save history to file -- pickle
- [ ] read in previous flow -- pickle
- [ ] replay previous flow
- [ ] graph: two sided paths (symmetry_history)
- [ ] is this similar to 
* <https://itunes.apple.com/us/app/down-dog-app-new-yoga-practice/id983693694>
* <http://seattleyoganews.com/down-dog-app-yoga/>
