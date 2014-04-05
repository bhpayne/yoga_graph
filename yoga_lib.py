import random
import networkx as nx
import matplotlib.pyplot as plt

def pose_properties(DG):
	DG.add_node(0,english_name="all fours")
	DG.node[0]["two_sided"]=False

	DG.add_node(1,english_name="cow")
	DG.node[1]["two_sided"]=False

	DG.add_node(2,english_name="cat")
	DG.node[2]["two_sided"]=False

	DG.add_node(3,english_name="child's pose")
	DG.node[3]["two_sided"]=False

	DG.add_node(4,english_name="downward dog")
	DG.node[4]["two_sided"]=False

	DG.add_node(5,english_name="dolphin")
	DG.node[5]["two_sided"]=False

	DG.add_node(6,english_name="lay on stomach")
	DG.node[6]["two_sided"]=False

	DG.add_node(7,english_name="bow pose")
	DG.node[7]["two_sided"]=False

	DG.add_node(8,english_name="one leg extended up")
	DG.node[8]["two_sided"]=True

	DG.add_node(9,english_name="both legs extended up")
	DG.node[9]["two_sided"]=False

	DG.add_node(10,english_name="supported shoulder stand")
	DG.node[10]["two_sided"]=False

	DG.add_node(11,english_name="plow pose")
	DG.node[11]["two_sided"]=False

	DG.add_node(12,english_name="ear pressure pose")
	DG.node[12]["two_sided"]=False

	DG.add_node(13,english_name="plank")
	DG.node[13]["two_sided"]=False

	DG.add_node(14,english_name="wild thing")
	DG.node[14]["two_sided"]=True

	DG.add_node(15,english_name="chaturanga")
	DG.node[15]["two_sided"]=False

	DG.add_node(16,english_name="side plank")
	DG.node[16]["two_sided"]=True

	DG.add_node(17,english_name="standing bend")
	DG.node[17]["two_sided"]=False

	DG.add_node(18,english_name="down dog, one leg raised")
	DG.node[18]["two_sided"]=True

	DG.add_node(19,english_name="flipped dog")
	DG.node[19]["two_sided"]=True

	DG.add_node(20,english_name="stand straight (mountain)")
	DG.node[20]["two_sided"]=False

	DG.add_node(21,english_name="happy camper")
	DG.node[21]["two_sided"]=True

	DG.add_node(22,english_name="tree pose")
	DG.node[22]["two_sided"]=True

	DG.add_node(23,english_name="warrior 3 (bent forward on one leg, arms extended forward")
	DG.node[23]["two_sided"]=True

	DG.add_node(24,english_name="warrior 1 (arms up)")
	DG.node[24]["two_sided"]=True

	DG.add_node(25,english_name="dancer pose")
	DG.node[25]["two_sided"]=True

	DG.add_node(26,english_name="standing splits")
	DG.node[26]["two_sided"]=True

	DG.add_node(27,english_name="chair pose")
	DG.node[27]["two_sided"]=False

	DG.add_node(28,english_name="wheel pose")
	DG.node[28]["two_sided"]=False

	DG.add_node(29,english_name="warrior 2 (arms out)")
	DG.node[29]["two_sided"]=True

	DG.add_node(30,english_name="peaceful warrior")
	DG.node[30]["two_sided"]=True

	DG.add_node(31,english_name="corpse pose")
	DG.node[31]["two_sided"]=False

	DG.add_node(32,english_name="happy baby; rock side to side")
	DG.node[32]["two_sided"]=False

	DG.add_node(33,english_name="on back, knees bent, feet on ground")
	DG.node[33]["two_sided"]=False

	DG.add_node(34,english_name="on back, knees bent, feet in air")
	DG.node[34]["two_sided"]=False

	DG.add_node(35,english_name="knees to one side, head to other")
	DG.node[35]["two_sided"]=True

	DG.add_node(36,english_name="staff pose")
	DG.node[36]["two_sided"]=False

	DG.add_node(37,english_name="pigeon pose")
	DG.node[37]["two_sided"]=True

	DG.add_node(38,english_name="one leg straight, one leg in")
	DG.node[38]["two_sided"]=True

	DG.add_node(39,english_name="compass pose")
	DG.node[39]["two_sided"]=True

	DG.add_node(40,english_name="rock bent leg")
	DG.node[40]["two_sided"]=True

	DG.add_node(41,english_name="kneeling on shins")
	DG.node[41]["two_sided"]=False

	DG.add_node(42,english_name="standing on shins")
	DG.node[42]["two_sided"]=False

	DG.add_node(43,english_name="camel pose")
	DG.node[43]["two_sided"]=False

	DG.add_node(44,english_name="crow")
	DG.node[44]["two_sided"]=False

	DG.add_node(45,english_name="squat, knees wide")
	DG.node[45]["two_sided"]=False

	DG.add_node(46,english_name="standing, legs apart")
	DG.node[46]["two_sided"]=False

	DG.add_node(47,english_name="upward dog")
	DG.node[47]["two_sided"]=False

	DG.add_node(48,english_name="one leg forward with knee bent")
	DG.node[48]["two_sided"]=False

	DG.add_node(49,english_name="half lotus")
	DG.node[49]["two_sided"]=True

	DG.add_node(50,english_name="full lotus")
	DG.node[50]["two_sided"]=True

	DG.add_node(51,english_name="embryo pose")
	DG.node[51]["two_sided"]=True

	DG.add_node(52,english_name="flying lotus")
	DG.node[52]["two_sided"]=True

	DG.add_node(53,english_name="floating staff pose")
	DG.node[53]["two_sided"]=False

	DG.add_node(54,english_name="crane")
	DG.node[54]["two_sided"]=False

	DG.add_node(55,english_name="one-legged crane")
	DG.node[55]["two_sided"]=True

	DG.add_node(56,english_name="wide legs, feet parallel")
	DG.node[56]["two_sided"]=False

	DG.add_node(57,english_name="bent over wide legs, parallel feet")
	DG.node[57]["two_sided"]=False

	DG.add_node(58,english_name="tripod head stand; legs extended")
	DG.node[58]["two_sided"]=False

	DG.add_node(59,english_name="arms to side")
	DG.node[59]["two_sided"]=True

	DG.add_node(60,english_name="both legs straight; front foot point forward; back foot flat, 45deg")
	DG.node[60]["two_sided"]=True

	DG.add_node(61,english_name="hinged forward at hips")
	DG.node[61]["two_sided"]=True

	DG.add_node(62,english_name="revolved triangle pose")
	DG.node[62]["hindi_name"]="Parivrtta Trikonasana"
	DG.node[62]["two_sided"]=True

	DG.add_node(63,english_name="extended side angle pose")
	DG.node[63]["two_sided"]=True

	DG.add_node(64,english_name="bind")
	DG.node[64]["two_sided"]=True

	DG.add_node(65,english_name="bird of paradise")
	DG.node[65]["two_sided"]=True

	DG.add_node(66,english_name="funky bird of paradise")
	DG.node[66]["two_sided"]=True

	DG.add_node(67,english_name="standing bend bound twist")
	DG.node[67]["two_sided"]=True

	DG.add_node(68,english_name="standing bend, legs apart")
	DG.node[68]["two_sided"]=False

	DG.add_node(69,english_name="tripod head stand; legs bent")
	DG.node[69]["two_sided"]=False

	DG.add_node(70,english_name="floating elephant trunk; one leg over arm")
	DG.node[70]["two_sided"]=True

	DG.add_node(71,english_name="eight angle pose")
	DG.node[71]["two_sided"]=True

	DG.add_node(72,english_name="flying pigeon")
	DG.node[72]["two_sided"]=True

	DG.add_node(73,english_name="peddle feet")
	DG.node[73]["two_sided"]=True

	return DG
    
def pose_transitions(DG):
	DG.add_weighted_edges_from([(2,0,1)])
	DG.add_weighted_edges_from([(0,2,1)])

	DG.add_weighted_edges_from([(2,1,1)])
	DG.add_weighted_edges_from([(1,2,1)])

	DG.add_weighted_edges_from([(1,0,1)])
	DG.add_weighted_edges_from([(0,1,1)])

	DG.add_weighted_edges_from([(0,3,1)])
	DG.add_weighted_edges_from([(3,0,1)])

	DG.add_weighted_edges_from([(3,4,1)])
	DG.add_weighted_edges_from([(4,3,1)])

	DG.add_weighted_edges_from([(3,5,1)])
	DG.add_weighted_edges_from([(5,3,1)])

	DG.add_weighted_edges_from([(6,0,1)])
	DG.add_weighted_edges_from([(0,6,1)])

	DG.add_weighted_edges_from([(4,6,1)])
	DG.add_weighted_edges_from([(6,4,1)])

	DG.add_weighted_edges_from([(6,3,1)])
	DG.add_weighted_edges_from([(3,6,1)])

	DG.add_weighted_edges_from([(5,6,1)])
	DG.add_weighted_edges_from([(6,5,1)])

	DG.add_weighted_edges_from([(7,6,1)])
	DG.add_weighted_edges_from([(6,7,1)])

	DG.add_weighted_edges_from([(9,8,1)])
	DG.add_weighted_edges_from([(8,9,1)])

	DG.add_weighted_edges_from([(9,10,1)])
	DG.add_weighted_edges_from([(10,9,1)])

	DG.add_weighted_edges_from([(10,11,1)])
	DG.add_weighted_edges_from([(11,10,1)])

	DG.add_weighted_edges_from([(11,12,1)])
	DG.add_weighted_edges_from([(12,11,1)])

	DG.add_weighted_edges_from([(13,0,1)])
	DG.add_weighted_edges_from([(0,13,1)])

	DG.add_weighted_edges_from([(13,5,1)])
	DG.add_weighted_edges_from([(5,13,1)])

	DG.add_weighted_edges_from([(14,13,1)])
	DG.add_weighted_edges_from([(13,14,1)])

	DG.add_weighted_edges_from([(15,13,1)])
	DG.add_weighted_edges_from([(13,15,1)])

	DG.add_weighted_edges_from([(16,13,1)])
	DG.add_weighted_edges_from([(13,16,1)])

	DG.add_weighted_edges_from([(4,1,1)])
	DG.add_weighted_edges_from([(1,4,1)])

	DG.add_weighted_edges_from([(4,2,1)])
	DG.add_weighted_edges_from([(2,4,1)])

	DG.add_weighted_edges_from([(0,4,1)])
	DG.add_weighted_edges_from([(4,0,1)])

	DG.add_weighted_edges_from([(4,13,1)])
	DG.add_weighted_edges_from([(13,4,1)])

	DG.add_weighted_edges_from([(17,4,1)])
	DG.add_weighted_edges_from([(4,17,1)])

	DG.add_weighted_edges_from([(18,4,1)])
	DG.add_weighted_edges_from([(4,18,1)])

	DG.add_weighted_edges_from([(18,19,1)])
	DG.add_weighted_edges_from([(19,18,1)])

	DG.add_weighted_edges_from([(17,20,1)])
	DG.add_weighted_edges_from([(20,17,1)])

	DG.add_weighted_edges_from([(20,23,1)])
	DG.add_weighted_edges_from([(23,20,1)])

	DG.add_weighted_edges_from([(23,22,1)])
	DG.add_weighted_edges_from([(22,23,1)])

	DG.add_weighted_edges_from([(23,24,1)])
	DG.add_weighted_edges_from([(24,23,1)])

	DG.add_weighted_edges_from([(24,20,1)])
	DG.add_weighted_edges_from([(20,24,1)])

	DG.add_weighted_edges_from([(23,25,1)])
	DG.add_weighted_edges_from([(25,23,1)])

	DG.add_weighted_edges_from([(26,23,1)])
	DG.add_weighted_edges_from([(23,26,1)])

	DG.add_weighted_edges_from([(21,20,1)])
	DG.add_weighted_edges_from([(20,21,1)])

	DG.add_weighted_edges_from([(27,21,1)])
	DG.add_weighted_edges_from([(21,27,1)])

	DG.add_weighted_edges_from([(27,20,1)])
	DG.add_weighted_edges_from([(20,27,1)])

	DG.add_weighted_edges_from([(28,19,1)])
	DG.add_weighted_edges_from([(19,28,1)])

	DG.add_weighted_edges_from([(28,6,1)])
	DG.add_weighted_edges_from([(6,28,1)])

	DG.add_weighted_edges_from([(28,20,1)])
	DG.add_weighted_edges_from([(20,28,1)])

	DG.add_weighted_edges_from([(29,24,1)])
	DG.add_weighted_edges_from([(24,29,1)])

	DG.add_weighted_edges_from([(30,29,1)])
	DG.add_weighted_edges_from([(29,30,1)])

	DG.add_weighted_edges_from([(31,9,1)])
	DG.add_weighted_edges_from([(9,31,1)])

	DG.add_weighted_edges_from([(8,31,1)])
	DG.add_weighted_edges_from([(31,8,1)])

	DG.add_weighted_edges_from([(32,31,1)])
	DG.add_weighted_edges_from([(31,32,1)])

	DG.add_weighted_edges_from([(9,32,1)])
	DG.add_weighted_edges_from([(32,9,1)])

	DG.add_weighted_edges_from([(34,33,1)])
	DG.add_weighted_edges_from([(33,34,1)])

	DG.add_weighted_edges_from([(34,31,1)])
	DG.add_weighted_edges_from([(31,34,1)])

	DG.add_weighted_edges_from([(35,33,1)])
	DG.add_weighted_edges_from([(33,35,1)])

	DG.add_weighted_edges_from([(34,35,1)])
	DG.add_weighted_edges_from([(35,34,1)])

	DG.add_weighted_edges_from([(31,36,1)])
	DG.add_weighted_edges_from([(36,31,1)])

	DG.add_weighted_edges_from([(37,13,1)])
	DG.add_weighted_edges_from([(13,37,1)])

	DG.add_weighted_edges_from([(37,14,1)])
	DG.add_weighted_edges_from([(14,37,1)])

	DG.add_weighted_edges_from([(38,36,1)])
	DG.add_weighted_edges_from([(36,38,1)])

	DG.add_weighted_edges_from([(38,39,1)])
	DG.add_weighted_edges_from([(39,38,1)])

	DG.add_weighted_edges_from([(40,38,1)])
	DG.add_weighted_edges_from([(38,40,1)])

	DG.add_weighted_edges_from([(40,39,1)])
	DG.add_weighted_edges_from([(39,40,1)])

	DG.add_weighted_edges_from([(3,41,1)])
	DG.add_weighted_edges_from([(41,3,1)])

	DG.add_weighted_edges_from([(3,42,1)])
	DG.add_weighted_edges_from([(42,3,1)])

	DG.add_weighted_edges_from([(42,41,1)])
	DG.add_weighted_edges_from([(41,42,1)])

	DG.add_weighted_edges_from([(42,43,1)])
	DG.add_weighted_edges_from([(43,42,1)])

	DG.add_weighted_edges_from([(15,44,1)])
	DG.add_weighted_edges_from([(44,15,1)])

	DG.add_weighted_edges_from([(44,45,1)])
	DG.add_weighted_edges_from([(45,44,1)])

	DG.add_weighted_edges_from([(45,46,1)])
	DG.add_weighted_edges_from([(46,45,1)])

	DG.add_weighted_edges_from([(46,20,1)])
	DG.add_weighted_edges_from([(20,46,1)])

	DG.add_weighted_edges_from([(15,47,1)])
	DG.add_weighted_edges_from([(47,15,1)])

	DG.add_weighted_edges_from([(47,4,1)])
	DG.add_weighted_edges_from([(4,47,1)])

	DG.add_weighted_edges_from([(13,48,1)])
	DG.add_weighted_edges_from([(48,13,1)])

	DG.add_weighted_edges_from([(23,48,1)])
	DG.add_weighted_edges_from([(48,23,1)])

	DG.add_weighted_edges_from([(45,36,1)])
	DG.add_weighted_edges_from([(36,45,1)])

	DG.add_weighted_edges_from([(45,31,1)])
	DG.add_weighted_edges_from([(31,45,1)])

	DG.add_weighted_edges_from([(36,49,1)])
	DG.add_weighted_edges_from([(49,36,1)])

	DG.add_weighted_edges_from([(49,50,1)])
	DG.add_weighted_edges_from([(50,49,1)])

	DG.add_weighted_edges_from([(51,50,1)])
	DG.add_weighted_edges_from([(50,51,1)])

	DG.add_weighted_edges_from([(52,50,1)])
	DG.add_weighted_edges_from([(50,52,1)])

	DG.add_weighted_edges_from([(53,36,1)])
	DG.add_weighted_edges_from([(36,53,1)])

	DG.add_weighted_edges_from([(45,54,1)])
	DG.add_weighted_edges_from([(54,45,1)])

	DG.add_weighted_edges_from([(54,55,1)])
	DG.add_weighted_edges_from([(55,54,1)])

	DG.add_weighted_edges_from([(29,56,1)])
	DG.add_weighted_edges_from([(56,29,1)])

	DG.add_weighted_edges_from([(57,56,1)])
	DG.add_weighted_edges_from([(56,57,1)])

	DG.add_weighted_edges_from([(59,3,1)])
	DG.add_weighted_edges_from([(3,59,1)])

	DG.add_weighted_edges_from([(60,29,1)])
	DG.add_weighted_edges_from([(29,60,1)])

	DG.add_weighted_edges_from([(61,60,1)])
	DG.add_weighted_edges_from([(60,61,1)])

	DG.add_weighted_edges_from([(62,61,1)])
	DG.add_weighted_edges_from([(61,62,1)])

	DG.add_weighted_edges_from([(60,63,1)])
	DG.add_weighted_edges_from([(63,60,1)])

	DG.add_weighted_edges_from([(63,64,1)])
	DG.add_weighted_edges_from([(64,63,1)])

	DG.add_weighted_edges_from([(64,65,1)])
	DG.add_weighted_edges_from([(65,64,1)])

	DG.add_weighted_edges_from([(66,65,1)])
	DG.add_weighted_edges_from([(65,66,1)])

	DG.add_weighted_edges_from([(67,65,1)])
	DG.add_weighted_edges_from([(65,67,1)])

	DG.add_weighted_edges_from([(68,46,1)])
	DG.add_weighted_edges_from([(46,68,1)])

	DG.add_weighted_edges_from([(17,68,1)])
	DG.add_weighted_edges_from([(68,17,1)])

	DG.add_weighted_edges_from([(68,67,1)])
	DG.add_weighted_edges_from([(67,68,1)])

	DG.add_weighted_edges_from([(69,45,1)])
	DG.add_weighted_edges_from([(45,69,1)])

	DG.add_weighted_edges_from([(54,69,1)])
	DG.add_weighted_edges_from([(69,54,1)])

	DG.add_weighted_edges_from([(57,69,1)])
	DG.add_weighted_edges_from([(69,57,1)])

	DG.add_weighted_edges_from([(69,58,1)])
	DG.add_weighted_edges_from([(58,69,1)])

	DG.add_weighted_edges_from([(70,40,1)])
	DG.add_weighted_edges_from([(40,70,1)])

	DG.add_weighted_edges_from([(71,70,1)])
	DG.add_weighted_edges_from([(70,71,1)])

	DG.add_weighted_edges_from([(72,21,1)])
	DG.add_weighted_edges_from([(21,72,1)])

	DG.add_weighted_edges_from([(73,4,1)])
	DG.add_weighted_edges_from([(4,73,1)])

	DG.add_weighted_edges_from([(4,68,1)])
	DG.add_weighted_edges_from([(68,4,1)])

	DG.add_weighted_edges_from([(12,10,1)])
	DG.add_weighted_edges_from([(10,12,1)])



	return DG

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

def random_flow(DG):
	print("entry point: ")
	entry_point_indx=4
	print(DG.node[entry_point_indx])
	pose_count=1
	while(pose_count<10):
		print("choices:")
		choices=DG.successors(entry_point_indx)
		print(choices)
		for pose_indx in choices:
			print(DG.node[pose_indx])
		current_indx=random.choice(DG.successors(entry_point_indx))
		print("next move:")
		print(DG.node[current_indx])
		pose_count = pose_count+1

