#!/usr/bin/env python
"""
Ben Payne
ben.is.located@gmail.com

Yoga graph

This file contains two functions called by the main YogaGraph program:
-pose_properties: contains information about the pose
-pose_transitions: set of edges on the graph

This work is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License. 
To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/4.0/.
"""

"""
On individual pages per pose, YogaJournal lists some of the 
'Preparatory Poses' and 'Follow-up Poses'
This graph is intended as a more full enumeration of that graph

YogaJournal has a page for creating a sequence
http://www3.yogajournal.com/poses/sequence_builder
however, this page doesn't specify which poses are adjacent
"""

"""
reference sites:
http://www.yogajournal.com/poses/finder/browse_categories
http://www.yogajournal.com/pose-finder/

http://www.dharmayogacenter.com/resources/yoga-poses/yoga-poses-alphabetical/
http://www.dharmayogacenter.com/resources/yoga-poses/view-all-yoga-poses-by-category/

https://en.wikipedia.org/wiki/List_of_asanas

http://www.theyogaposes.com/
http://www.joythruyoga.com/list-of-yoga-poses.html
https://yoga.com/poses


"""

def pose_properties(DG):
	DG.add_node(0,english_name="table top")
	DG.node[0]["two_sided"]=False
	DG.node[0]["description"]="on all fours; hands, knees, and feet are shoulder width apart"
	DG.node[0]["yogajournalurl"]=""
	DG.node[0]["yogajournal_picture"]=""
	DG.node[0]["hindi_name"]=""
	DG.node[0]["comment"]=""
	DG.node[0]["Dharma Mittra picture URL"]=""
	DG.node[0]["asanas 608 page"]=""
	DG.node[0]["asanas 608 english name"]=""	

	DG.add_node(1,english_name="cow")
	DG.node[1]["two_sided"]=False
	DG.node[1]["description"]="on all fours, pull chest to floor and head up"
	DG.node[1]["yogajournalurl"]="http://www.yogajournal.com/poses/2467"
	DG.node[1]["yogajournal_picture"]="http://media.yogajournal.com/wp-content/uploads/CowPose.jpg"
	DG.node[1]["hindi_name"]="marjaryasana"
	DG.node[1]["comment"]=""
	DG.node[1]["Dharma Mittra picture URL"]="http://www.dharmayogacenter.com/wp-content/gallery/asana-reference/marjaryasana2.jpg"
	DG.node[1]["asanas_608_page"]="373"
	DG.node[1]["asanas_608_english"]="cat stretch pose B"	

	DG.add_node(2,english_name="cat")
	DG.node[2]["two_sided"]=False
	DG.node[2]["description"]="on all fours, pull chest to ceiling and head down"
	DG.node[2]["yogajournalurl"]="http://www.yogajournal.com/poses/2468"
	DG.node[2]["yogajournal_picture"]="http://media.yogajournal.com/wp-content/uploads/252_hp_move_03_4501.jpg"
	DG.node[2]["hindi_name"]="marjaryasana"
	DG.node[2]["comment"]=""
	DG.node[2]["Dharma Mittra picture URL"]="http://www.dharmayogacenter.com/wp-content/gallery/asana-reference/marjaryasana1.jpg"
	DG.node[2]["asanas_608_page"]="372"
	DG.node[2]["asanas_608_english"]="cat stretch pose A"	
	
	DG.add_node(3,english_name="child's pose")
	DG.node[3]["two_sided"]=False
	DG.node[3]["description"]="arms stretched above head, face to ground. On shins"
	DG.node[3]["yogajournalurl"]="http://www.yogajournal.com/poses/475"
	DG.node[3]["yogajournal_picture"]="http://media.yogajournal.com/wp-content/uploads/266_hp_side06_4501.jpg"
	DG.node[3]["hindi_name"]=""
	DG.node[3]["comment"]=""
	DG.node[3]["Dharma Mittra picture URL"]=""
	DG.node[3]["asanas 608 page"]=""
	DG.node[3]["asanas 608 english name"]=""	
	
	DG.add_node(4,english_name="downward dog")
	DG.node[4]["two_sided"]=False
	DG.node[4]["yogajournalurl"]="http://www.yogajournal.com/poses/491"
#	DG.node[4]["yogajournalurl"]="http://www.yogajournal.com/pose/downward-facing-dog/"
	DG.node[4]["yogajournal_picture"]="http://media.yogajournal.com/wp-content/uploads/266_hp_side12_450.jpg"
	DG.node[4]["hindi_name"]="Adho Mukha Svanasana"
	DG.node[4]["Dharma Mittra picture URL"]=""
	DG.node[4]["description"]="feet and hands on floor, both shoulder width apart"
	DG.node[4]["asanas_608_page"]=""
	DG.node[4]["asanas_608_english"]=""	

	DG.add_node(5,english_name="dolphin")
	DG.node[5]["two_sided"]=False
	DG.node[5]["description"]="feet and forearms on floor"
	DG.node[5]["yogajournalurl"]="http://www.yogajournal.com/poses/2462"
	DG.node[5]["yogajournal_picture"]="http://media.yogajournal.com/wp-content/uploads/newMATY_3_0056_FNL.jpg"
	DG.node[5]["hindi_name"]=""
	DG.node[5]["comment"]=""
	DG.node[5]["Dharma Mittra picture URL"]=""
	DG.node[5]["asanas 608 page"]=""
	DG.node[5]["asanas 608 english name"]=""	

	DG.add_node(6,english_name="lay on stomach")
	DG.node[6]["two_sided"]=False
	DG.node[6]["description"]="whole body in contact with ground, arms by side"
	DG.node[6]["yogajournalurl"]=""
	DG.node[6]["yogajournal_picture"]=""
	DG.node[6]["hindi_name"]="Makarasana"
	DG.node[6]["comment"]=""
	DG.node[6]["Dharma Mittra picture URL"]=""
	DG.node[6]["asanas 608 page"]=""
	DG.node[6]["asanas 608 english name"]=""	

	DG.add_node(7,english_name="bow pose")
	DG.node[7]["two_sided"]=False
	DG.node[7]["description"]=""
	DG.node[7]["yogajournalurl"]="http://www.yogajournal.com/poses/875"
	DG.node[7]["yogajournal_picture"]="http://media.yogajournal.com/wp-content/uploads/HP_260_10_FNL_4501.jpg"
	DG.node[7]["hindi_name"]=""
	DG.node[7]["comment"]=""
	DG.node[7]["Dharma Mittra picture URL"]=""
	DG.node[7]["asanas 608 page"]=""
	DG.node[7]["asanas 608 english name"]=""	

	DG.add_node(8,english_name="laying on back, one leg extended up")
	DG.node[8]["two_sided"]=True
	DG.node[8]["description"]=""
	DG.node[8]["yogajournalurl"]=""
	DG.node[8]["yogajournal_picture"]=""
	DG.node[8]["hindi_name"]=""
	DG.node[8]["comment"]=""
	DG.node[8]["Dharma Mittra picture URL"]=""
	DG.node[8]["asanas 608 page"]=""
	DG.node[8]["asanas 608 english name"]=""	

	DG.add_node(9,english_name="lying on back, both legs extended up")
	DG.node[9]["two_sided"]=False
	DG.node[9]["description"]=""
	DG.node[9]["yogajournalurl"]=""
	DG.node[9]["yogajournal_picture"]=""
	DG.node[9]["hindi_name"]=""
	DG.node[9]["comment"]=""
	DG.node[9]["Dharma Mittra picture URL"]=""
	DG.node[9]["asanas 608 page"]=""
	DG.node[9]["asanas 608 english name"]=""	

	DG.add_node(10,english_name="supported shoulder stand")
	DG.node[10]["two_sided"]=False
	DG.node[10]["description"]=""
	DG.node[10]["yogajournalurl"]=""
	DG.node[10]["yogajournal_picture"]=""
	DG.node[10]["hindi_name"]="Sarvangasana"
	DG.node[10]["comment"]=""
	DG.node[10]["Dharma Mittra picture URL"]=""
	DG.node[10]["asanas_608_page"]="226"
	DG.node[10]["asanas_608_english"]="Shoulder Stand Pose"	

	DG.add_node(11,english_name="plow pose")
	DG.node[11]["two_sided"]=False
	DG.node[11]["description"]=""
	DG.node[11]["yogajournalurl"]="http://www.yogajournal.com/poses/479"
	DG.node[11]["yogajournal_picture"]="http://media.yogajournal.com/wp-content/uploads/plowpose.jpg"
	DG.node[11]["hindi_name"]="Halasana"
	DG.node[11]["comment"]=""
	DG.node[11]["Dharma Mittra picture URL"]=""
	DG.node[11]["asanas_608_page"]="249"
	DG.node[11]["asanas_608_english"]="Plough pose (variation)"	

	DG.add_node(12,english_name="ear pressure pose")
	DG.node[12]["two_sided"]=False
	DG.node[12]["description"]=""
	DG.node[12]["yogajournalurl"]=""
	DG.node[12]["yogajournal_picture"]=""
	DG.node[12]["hindi_name"]=""
	DG.node[12]["comment"]=""
	DG.node[12]["Dharma Mittra picture URL"]=""
	DG.node[12]["asanas 608 page"]=""
	DG.node[12]["asanas 608 english name"]=""	

	DG.add_node(13,english_name="plank")
	DG.node[13]["two_sided"]=False
	DG.node[13]["description"]=""
#	DG.node[13]["yogajournalurl"]="http://www.yogajournal.com/poses/470"
	DG.node[13]["yogajournalurl"]="http://www.yogajournal.com/pose/plank-pose/"
	DG.node[13]["yogajournal_picture"]="http://media.yogajournal.com/wp-content/uploads/244_hp_01_450.jpg"
	DG.node[13]["hindi_name"]=""
	DG.node[13]["comment"]=""
	DG.node[13]["Dharma Mittra picture URL"]="http://www.dharmayogacenter.com/wp-content/gallery/asana-reference/chaturanga-dandasana.jpg"
	DG.node[13]["asanas 608 page"]=""
	DG.node[13]["asanas 608 english name"]=""	

	DG.add_node(14,english_name="wild thing")
	DG.node[14]["two_sided"]=True
	DG.node[14]["description"]=""
	DG.node[14]["yogajournalurl"]=""
	DG.node[14]["yogajournal_picture"]=""
	DG.node[14]["hindi_name"]=""
	DG.node[14]["comment"]=""
	DG.node[14]["Dharma Mittra picture URL"]=""
	DG.node[14]["asanas 608 page"]=""
	DG.node[14]["asanas 608 english name"]=""	

	DG.add_node(15,english_name="low pushup")
	DG.node[15]["two_sided"]=False
	DG.node[15]["hindi_name"]="chaturanga"
	DG.node[15]["description"]=""
	DG.node[15]["yogajournalurl"]="http://www.yogajournal.com/pose/four-limbed-staff-pose/"
	DG.node[15]["yogajournal_picture"]="http://media.yogajournal.com/wp-content/uploads/chaturangafourlimbedstaff.jpg"
	DG.node[15]["comment"]=""
	DG.node[15]["Dharma Mittra picture URL"]=""
	DG.node[15]["asanas 608 page"]=""
	DG.node[15]["asanas 608 english name"]=""	

	DG.add_node(16,english_name="side plank")
	DG.node[16]["two_sided"]=True
	DG.node[16]["description"]=""
	DG.node[16]["yogajournalurl"]="http://www.yogajournal.com/pose/side-plank-pose/"
	DG.node[16]["yogajournal_picture"]="http://media.yogajournal.com/wp-content/uploads/SidePlankPose.jpg"
	DG.node[16]["hindi_name"]=""
	DG.node[16]["comment"]=""
	DG.node[16]["Dharma Mittra picture URL"]=""
	DG.node[16]["asanas 608 page"]=""
	DG.node[16]["asanas 608 english name"]=""	

	DG.add_node(17,english_name="standing bend, legs together")
	DG.node[17]["two_sided"]=False
	DG.node[17]["description"]="legs together, face to knees"
	DG.node[17]["yogajournalurl"]=""
	DG.node[17]["yogajournal_picture"]=""
	DG.node[17]["hindi_name"]=""
	DG.node[17]["comment"]=""
	DG.node[17]["Dharma Mittra picture URL"]=""
	DG.node[17]["asanas 608 page"]=""
	DG.node[17]["asanas 608 english name"]=""	

	DG.add_node(18,english_name="down dog, one leg raised")
	DG.node[18]["two_sided"]=True
	DG.node[18]["description"]=""
	DG.node[18]["yogajournalurl"]="http://www.yogajournal.com/article/beginners/one-legged-downward-facing-dog/"
	DG.node[18]["yogajournal_picture"]="http://media.yogajournal.com/wp-content/uploads/bas_234_opener_Sized2.jpg"
	DG.node[18]["hindi_name"]=""
	DG.node[18]["comment"]=""
	DG.node[18]["Dharma Mittra picture URL"]=""
	DG.node[18]["asanas 608 page"]=""
	DG.node[18]["asanas 608 english name"]=""	

	DG.add_node(19,english_name="flipped dog")
	DG.node[19]["two_sided"]=True
	DG.node[19]["description"]=""
	DG.node[19]["yogajournalurl"]=""
	DG.node[19]["yogajournal_picture"]=""
	DG.node[19]["hindi_name"]=""
	DG.node[19]["comment"]=""
	DG.node[19]["Dharma Mittra picture URL"]=""
	DG.node[19]["asanas 608 page"]=""
	DG.node[19]["asanas 608 english name"]=""	

	DG.add_node(20,english_name="stand straight (mountain)")
	DG.node[20]["two_sided"]=False
	DG.node[20]["yogajournalurl"]="http://www.yogajournal.com/poses/492"
	DG.node[20]["yogajournal_picture"]="http://media.yogajournal.com/wp-content/uploads/pract-well_trail_268_02_FNLTadasana.jpg"
	DG.node[20]["hindi_name"]="Tadasana"
	DG.node[20]["description"]="legs together, hands at side"
	DG.node[20]["comment"]=""
	DG.node[20]["Dharma Mittra picture URL"]=""
	DG.node[20]["asanas 608 page"]=""
	DG.node[20]["asanas 608 english name"]=""	

	DG.add_node(21,english_name="happy camper")
	DG.node[21]["two_sided"]=True
	DG.node[21]["description"]=""
	DG.node[21]["yogajournalurl"]=""
	DG.node[21]["yogajournal_picture"]=""
	DG.node[21]["hindi_name"]=""
	DG.node[21]["comment"]=""
	DG.node[21]["Dharma Mittra picture URL"]=""
	DG.node[21]["asanas 608 page"]=""
	DG.node[21]["asanas 608 english name"]=""	

	DG.add_node(22,english_name="tree pose")
	DG.node[22]["two_sided"]=True
	DG.node[22]["description"]="arms up and straight, one leg bent with foot to thigh"
	DG.node[22]["yogajournalurl"]="http://www.yogajournal.com/poses/496"
	DG.node[22]["yogajournal_picture"]="http://media.yogajournal.com/wp-content/uploads/yogapedia_270_01_450x450.jpg"
	DG.node[22]["hindi_name"]="Vrksasana"
	DG.node[22]["comment"]=""
	DG.node[22]["Dharma Mittra picture URL"]=""
	DG.node[22]["asanas 608 page"]=""
	DG.node[22]["asanas 608 english name"]=""	

	DG.add_node(23,english_name="warrior 3")
	DG.node[23]["two_sided"]=True
	DG.node[23]["description"]="bent forward on one leg, arms extended forward"
	DG.node[23]["yogajournalurl"]="http://www.yogajournal.com/poses/941"
	DG.node[23]["hindi_name"]="Virabhadrasana III"
	DG.node[23]["yogajournal_picture"]="http://media.yogajournal.com/wp-content/uploads/246_hp_13_450.jpg"
	DG.node[23]["comment"]=""
	DG.node[23]["Dharma Mittra picture URL"]=""
	DG.node[23]["asanas 608 page"]=""
	DG.node[23]["asanas 608 english name"]=""	

	DG.add_node(24,english_name="warrior 1")
	DG.node[24]["two_sided"]=True
	DG.node[24]["description"]="arms up"
	DG.node[24]["yogajournalurl"]="http://www.yogajournal.com/poses/1708"
	DG.node[24]["yogajournal_picture"]=""
	DG.node[24]["hindi_name"]="Virabhadrasana I"
	DG.node[24]["comment"]=""
	DG.node[24]["Dharma Mittra picture URL"]=""
	DG.node[24]["asanas 608 page"]=""
	DG.node[24]["asanas 608 english name"]=""	

	DG.add_node(25,english_name="dancer pose")
	DG.node[25]["two_sided"]=True
	DG.node[25]["description"]=""
	DG.node[25]["yogajournalurl"]="http://www.yogajournal.com/poses/936"
	DG.node[25]["yogajournal_picture"]=""
	DG.node[25]["hindi_name"]="Natarajasana"
	DG.node[25]["comment"]=""
	DG.node[25]["Dharma Mittra picture URL"]=""
	DG.node[25]["asanas 608 page"]=""
	DG.node[25]["asanas 608 english name"]=""	

	DG.add_node(26,english_name="standing splits")
	DG.node[26]["two_sided"]=True
	DG.node[26]["description"]=""
	DG.node[26]["yogajournalurl"]="http://www.yogajournal.com/poses/2499"
	DG.node[26]["yogajournal_picture"]=""
	DG.node[26]["hindi_name"]="Urdhva Prasarita Eka Padasana"
	DG.node[26]["comment"]=""
	DG.node[26]["Dharma Mittra picture URL"]=""
	DG.node[26]["asanas 608 page"]=""
	DG.node[26]["asanas 608 english name"]=""	

	DG.add_node(27,english_name="chair pose")
	DG.node[27]["two_sided"]=False
	DG.node[27]["description"]=""
	DG.node[27]["yogajournalurl"]="http://www.yogajournal.com/poses/493"
	DG.node[27]["yogajournal_picture"]="http://media.yogajournal.com/wp-content/uploads/HP_269_FNL_81135.jpg"
	DG.node[27]["hindi_name"]="Utkatasana"
	DG.node[27]["comment"]=""
	DG.node[27]["Dharma Mittra picture URL"]=""
	DG.node[27]["asanas 608 page"]=""
	DG.node[27]["asanas 608 english name"]=""	

	DG.add_node(28,english_name="wheel pose")
	DG.node[28]["two_sided"]=False
	DG.node[28]["description"]=""
	DG.node[28]["yogajournalurl"]="http://www.yogajournal.com/poses/473"
	DG.node[28]["yogajournal_picture"]="http://media.yogajournal.com/wp-content/uploads/258_HP_11_fnl_450.jpg"
	DG.node[28]["hindi_name"]="Urdhva Dhanurasana"
	DG.node[28]["comment"]=""
	DG.node[28]["Dharma Mittra picture URL"]="http://www.dharmayogacenter.com/wp-content/gallery/asana-reference/urdhva-dhamurasana3.jpg"
	DG.node[28]["asanas 608 page"]=""
	DG.node[28]["asanas 608 english name"]=""	

	DG.add_node(29,english_name="warrior 2")
	DG.node[29]["two_sided"]=True
	DG.node[29]["description"]="arms out"
	DG.node[29]["yogajournalurl"]="http://www.yogajournal.com/poses/495"
	DG.node[29]["yogajournal_picture"]="http://www.yogajournal.com/pose/warrior-ii-pose/"
	DG.node[29]["hindi_name"]="Virabhadrasana II"
	DG.node[29]["comment"]=""
	DG.node[29]["Dharma Mittra picture URL"]=""
	DG.node[29]["asanas 608 page"]=""
	DG.node[29]["asanas 608 english name"]=""	

	DG.add_node(30,english_name="peaceful warrior")
	DG.node[30]["two_sided"]=True
	DG.node[30]["description"]=""
	DG.node[30]["yogajournalurl"]=""
	DG.node[30]["yogajournal_picture"]=""
	DG.node[30]["hindi_name"]=""
	DG.node[30]["comment"]=""
	DG.node[30]["Dharma Mittra picture URL"]=""
	DG.node[30]["asanas 608 page"]=""
	DG.node[30]["asanas 608 english name"]=""	

	DG.add_node(31,english_name="corpse pose")
	DG.node[31]["two_sided"]=False
	DG.node[31]["description"]="laying on back"
	DG.node[31]["yogajournalurl"]="http://www.yogajournal.com/pose/corpse-pose/"
	DG.node[31]["yogajournal_picture"]="http://media.yogajournal.com/wp-content/uploads/CorpsePoseYoga.jpg"
	DG.node[31]["hindi_name"]="shabasana"
	DG.node[31]["comment"]=""
	DG.node[31]["Dharma Mittra picture URL"]=""
	DG.node[31]["asanas 608 page"]=""
	DG.node[31]["asanas 608 english name"]=""	

	DG.add_node(32,english_name="happy baby, rock side to side")
	DG.node[32]["two_sided"]=False
	DG.node[32]["description"]="on back, feet up"
	DG.node[32]["yogajournalurl"]="http://www.yogajournal.com/poses/2497"
	DG.node[32]["yogajournal_picture"]="http://media.yogajournal.com/wp-content/uploads/249_hp_groove_16_450.jpg"
	DG.node[32]["hindi_name"]=""
	DG.node[32]["comment"]=""
	DG.node[32]["Dharma Mittra picture URL"]=""
	DG.node[32]["asanas 608 page"]=""
	DG.node[32]["asanas 608 english name"]=""	

	DG.add_node(33,english_name="on back, knees bent, feet on ground")
	DG.node[33]["two_sided"]=False
	DG.node[33]["description"]=""
	DG.node[33]["yogajournalurl"]=""
	DG.node[33]["yogajournal_picture"]=""
	DG.node[33]["hindi_name"]=""
	DG.node[33]["comment"]=""
	DG.node[33]["Dharma Mittra picture URL"]=""
	DG.node[33]["asanas 608 page"]=""
	DG.node[33]["asanas 608 english name"]=""	

	DG.add_node(34,english_name="on back, knees bent, feet in air")
	DG.node[34]["two_sided"]=False
	DG.node[34]["description"]=""
	DG.node[34]["yogajournalurl"]=""
	DG.node[34]["yogajournal_picture"]=""
	DG.node[34]["hindi_name"]=""
	DG.node[34]["comment"]=""
	DG.node[34]["Dharma Mittra picture URL"]=""
	DG.node[34]["asanas 608 page"]=""
	DG.node[34]["asanas 608 english name"]=""	

	DG.add_node(35,english_name="knees to one side, head to other")
	DG.node[35]["two_sided"]=True
	DG.node[35]["description"]=""
	DG.node[35]["yogajournalurl"]=""
	DG.node[35]["yogajournal_picture"]=""
	DG.node[35]["hindi_name"]=""
	DG.node[35]["comment"]=""
	DG.node[35]["Dharma Mittra picture URL"]=""
	DG.node[35]["asanas 608 page"]=""
	DG.node[35]["asanas 608 english name"]=""	

	DG.add_node(36,english_name="staff pose")
	DG.node[36]["two_sided"]=False
	DG.node[36]["description"]=""
	DG.node[36]["yogajournalurl"]=""
	DG.node[36]["yogajournal_picture"]=""
	DG.node[36]["hindi_name"]="paschimatanasana"
	DG.node[36]["comment"]=""
	DG.node[36]["Dharma Mittra picture URL"]=""
	DG.node[36]["asanas_608_page"]="278"
	DG.node[36]["asanas_608_english"]="back stretch pose (preparation)"	

	DG.add_node(37,english_name="pigeon pose")
	DG.node[37]["two_sided"]=True
	DG.node[37]["description"]=""
	DG.node[37]["yogajournalurl"]=""
	DG.node[37]["yogajournal_picture"]=""
	DG.node[37]["hindi_name"]=""
	DG.node[37]["comment"]=""
	DG.node[37]["Dharma Mittra picture URL"]=""

	DG.add_node(38,english_name="one leg straight, one leg in")
	DG.node[38]["two_sided"]=True
	DG.node[38]["description"]=""
	DG.node[38]["yogajournalurl"]=""
	DG.node[38]["yogajournal_picture"]=""
	DG.node[38]["hindi_name"]=""
	DG.node[38]["comment"]=""
	DG.node[38]["Dharma Mittra picture URL"]=""

	DG.add_node(39,english_name="compass pose")
	DG.node[39]["two_sided"]=True
	DG.node[39]["description"]=""
	DG.node[39]["yogajournalurl"]=""
	DG.node[39]["yogajournal_picture"]=""
	DG.node[39]["hindi_name"]=""
	DG.node[39]["comment"]=""
	DG.node[39]["Dharma Mittra picture URL"]=""

	DG.add_node(40,english_name="rock bent leg")
	DG.node[40]["two_sided"]=True
	DG.node[40]["description"]=""
	DG.node[40]["yogajournalurl"]=""
	DG.node[40]["yogajournal_picture"]=""
	DG.node[40]["hindi_name"]=""
	DG.node[40]["comment"]=""
	DG.node[40]["Dharma Mittra picture URL"]=""
	DG.node[40]["asanas 608 page"]=""
	DG.node[40]["asanas 608 english name"]=""	

	DG.add_node(41,english_name="kneeling on shins")
	DG.node[41]["two_sided"]=False
	DG.node[41]["description"]=""
	DG.node[41]["yogajournalurl"]=""
	DG.node[41]["yogajournal_picture"]=""
	DG.node[41]["hindi_name"]=""
	DG.node[41]["comment"]=""
	DG.node[41]["Dharma Mittra picture URL"]=""
	DG.node[41]["asanas 608 page"]=""
	DG.node[41]["asanas 608 english name"]=""	

	DG.add_node(42,english_name="standing on shins")
	DG.node[42]["two_sided"]=False
	DG.node[42]["description"]=""
	DG.node[42]["yogajournalurl"]=""
	DG.node[42]["yogajournal_picture"]=""
	DG.node[42]["hindi_name"]=""
	DG.node[42]["comment"]=""
	DG.node[42]["Dharma Mittra picture URL"]=""
	DG.node[42]["asanas 608 page"]=""
	DG.node[42]["asanas 608 english name"]=""	

	DG.add_node(43,english_name="camel pose")
	DG.node[43]["two_sided"]=False
	DG.node[43]["description"]=""
	DG.node[43]["yogajournalurl"]="http://www.yogajournal.com/pose/camel-pose/"
	DG.node[43]["yogajournal_picture"]="http://media.yogajournal.com/wp-content/uploads/258_HP_10_fnl_4501.jpg"
	DG.node[43]["hindi_name"]=""
	DG.node[43]["comment"]=""
	DG.node[43]["Dharma Mittra picture URL"]=""
	DG.node[43]["asanas 608 page"]=""
	DG.node[43]["asanas 608 english name"]=""	

	DG.add_node(44,english_name="crow")
	DG.node[44]["two_sided"]=False
	DG.node[44]["description"]=""
	DG.node[44]["yogajournalurl"]="http://www.yogajournal.com/pose/crane-pose/"
	DG.node[44]["yogajournal_picture"]="http://media.yogajournal.com/wp-content/uploads/Crane-Crow-Pose1.jpg"
	DG.node[44]["hindi_name"]=""
	DG.node[44]["comment"]=""
	DG.node[44]["Dharma Mittra picture URL"]=""
	DG.node[44]["asanas 608 page"]=""
	DG.node[44]["asanas 608 english name"]=""	

	DG.add_node(45,english_name="squat, knees wide")
	DG.node[45]["two_sided"]=False
	DG.node[45]["description"]=""
	DG.node[45]["yogajournalurl"]=""
	DG.node[45]["yogajournal_picture"]=""
	DG.node[45]["hindi_name"]=""
	DG.node[45]["comment"]=""
	DG.node[45]["Dharma Mittra picture URL"]=""
	DG.node[45]["asanas 608 page"]=""
	DG.node[45]["asanas 608 english name"]=""	

	DG.add_node(46,english_name="standing, legs apart")
	DG.node[46]["two_sided"]=False
	DG.node[46]["description"]=""
	DG.node[46]["yogajournalurl"]=""
	DG.node[46]["yogajournal_picture"]=""
	DG.node[46]["hindi_name"]=""
	DG.node[46]["comment"]=""
	DG.node[46]["Dharma Mittra picture URL"]=""
	DG.node[46]["asanas 608 page"]=""
	DG.node[46]["asanas 608 english name"]=""	

	DG.add_node(47,english_name="upward dog")
	DG.node[47]["two_sided"]=False
	DG.node[47]["description"]=""
	DG.node[47]["yogajournalurl"]="http://www.yogajournal.com/poses/474"
	DG.node[47]["yogajournal_picture"]="http://media.yogajournal.com/wp-content/uploads/230_hp_07_fnl_450.jpg"
	DG.node[47]["hindi_name"]=""
	DG.node[47]["comment"]=""
	DG.node[47]["Dharma Mittra picture URL"]="http://www.dharmayogacenter.com/wp-content/gallery/asana-reference/urdhva-mukha-svanasana.jpg"
	DG.node[47]["asanas 608 page"]=""
	DG.node[47]["asanas 608 english name"]=""	

	DG.add_node(48,english_name="one leg forward with knee bent")
	DG.node[48]["two_sided"]=False
	DG.node[48]["description"]=""
	DG.node[48]["yogajournalurl"]=""
	DG.node[48]["yogajournal_picture"]=""
	DG.node[48]["hindi_name"]=""
	DG.node[48]["comment"]=""
	DG.node[48]["Dharma Mittra picture URL"]=""
	DG.node[48]["asanas 608 page"]=""
	DG.node[48]["asanas 608 english name"]=""	

	DG.add_node(49,english_name="half lotus")
	DG.node[49]["two_sided"]=True
	DG.node[49]["description"]=""
	DG.node[49]["yogajournalurl"]="http://www.yogajournal.com/pose/fire-log-pose/"
	DG.node[49]["yogajournal_picture"]="http://media.yogajournal.com/wp-content/uploads/firelogpose.jpg"
	DG.node[49]["hindi_name"]="siddhasana"
	DG.node[49]["comment"]=""
	DG.node[49]["Dharma Mittra picture URL"]="http://www.dharmayogacenter.com/wp-content/gallery/asana-reference/virasana3.jpg"
	DG.node[49]["asanas_608_page"]="624"
	DG.node[49]["asanas_608_english"]="accomplished pose"	

	DG.add_node(50,english_name="full lotus")
	DG.node[50]["two_sided"]=True
	DG.node[50]["description"]=""
	DG.node[50]["yogajournalurl"]="http://www.yogajournal.com/poses/488"
	DG.node[50]["yogajournal_picture"]="http://media.yogajournal.com/wp-content/uploads/lotuspose.jpg"
	DG.node[50]["hindi_name"]="padmasana"
	DG.node[50]["comment"]=""
	DG.node[50]["Dharma Mittra picture URL"]=""
	DG.node[50]["asanas_608_page"]="626"
	DG.node[50]["asanas_608_english"]="lotus pose"	

	DG.add_node(51,english_name="embryo pose")
	DG.node[51]["two_sided"]=True
	DG.node[51]["description"]=""
	DG.node[51]["yogajournalurl"]=""
	DG.node[51]["yogajournal_picture"]=""
	DG.node[51]["hindi_name"]=""
	DG.node[51]["comment"]=""
	DG.node[51]["Dharma Mittra picture URL"]=""
	DG.node[51]["asanas_608_page"]="243"
	DG.node[51]["asanas_608_english"]="upward lotus pose"	
	
	DG.add_node(52,english_name="flying lotus")
	DG.node[52]["two_sided"]=True
	DG.node[52]["description"]=""
	DG.node[52]["yogajournalurl"]=""
	DG.node[52]["yogajournal_picture"]=""
	DG.node[52]["hindi_name"]=""
	DG.node[52]["comment"]=""
	DG.node[52]["Dharma Mittra picture URL"]=""
	DG.node[52]["asanas 608 page"]=""
	DG.node[52]["asanas 608 english name"]=""	

	DG.add_node(53,english_name="floating staff pose")
	DG.node[53]["two_sided"]=False
	DG.node[53]["description"]=""
	DG.node[53]["yogajournalurl"]=""
	DG.node[53]["yogajournal_picture"]=""
	DG.node[53]["hindi_name"]=""
	DG.node[53]["comment"]=""
	DG.node[53]["Dharma Mittra picture URL"]=""
	DG.node[53]["asanas 608 page"]=""
	DG.node[53]["asanas 608 english name"]=""	

	DG.add_node(54,english_name="crane")
	DG.node[54]["two_sided"]=False
	DG.node[54]["description"]=""
	DG.node[54]["yogajournalurl"]=""
	DG.node[54]["yogajournal_picture"]=""
	DG.node[54]["hindi_name"]=""
	DG.node[54]["comment"]=""
	DG.node[54]["Dharma Mittra picture URL"]=""
	DG.node[54]["asanas 608 page"]=""
	DG.node[54]["asanas 608 english name"]=""	

	DG.add_node(55,english_name="one-legged crane")
	DG.node[55]["two_sided"]=True
	DG.node[55]["description"]=""
	DG.node[55]["yogajournalurl"]=""
	DG.node[55]["yogajournal_picture"]=""
	DG.node[55]["hindi_name"]=""
	DG.node[55]["comment"]=""
	DG.node[55]["Dharma Mittra picture URL"]=""
	DG.node[55]["asanas 608 page"]=""
	DG.node[55]["asanas 608 english name"]=""	

	DG.add_node(56,english_name="wide legs, feet parallel")
	DG.node[56]["two_sided"]=False
	DG.node[56]["description"]=""
	DG.node[56]["yogajournalurl"]=""
	DG.node[56]["yogajournal_picture"]=""
	DG.node[56]["hindi_name"]=""
	DG.node[56]["comment"]=""
	DG.node[56]["Dharma Mittra picture URL"]=""
	DG.node[56]["asanas 608 page"]=""
	DG.node[56]["asanas 608 english name"]=""	

	DG.add_node(57,english_name="bent over wide legs, parallel feet")
	DG.node[57]["two_sided"]=False
	DG.node[57]["description"]=""
	DG.node[57]["yogajournalurl"]=""
	DG.node[57]["yogajournal_picture"]=""
	DG.node[57]["hindi_name"]=""
	DG.node[57]["comment"]=""
	DG.node[57]["Dharma Mittra picture URL"]=""
	DG.node[57]["asanas 608 page"]=""
	DG.node[57]["asanas 608 english name"]=""	

	DG.add_node(58,english_name="tripod head stand, legs extended straight up, arms at 90deg")
	DG.node[58]["two_sided"]=False
	DG.node[58]["description"]="arms at 90deg"
	DG.node[58]["yogajournalurl"]=""
	DG.node[58]["yogajournal_picture"]=""
	DG.node[58]["hindi_name"]="Salamba-Shirshasana"
	DG.node[58]["comment"]=""
	DG.node[58]["Dharma Mittra picture URL"]=""
	DG.node[58]["asanas_608_page"]="181"
	DG.node[58]["asanas_608_english"]="Supported Head Stand Pose"	

	DG.add_node(59,english_name="arms to side")
	DG.node[59]["two_sided"]=True
	DG.node[59]["description"]=""
	DG.node[59]["yogajournalurl"]=""
	DG.node[59]["yogajournal_picture"]=""
	DG.node[59]["hindi_name"]=""
	DG.node[59]["comment"]=""
	DG.node[59]["Dharma Mittra picture URL"]=""
	DG.node[59]["asanas 608 page"]=""
	DG.node[59]["asanas 608 english name"]=""	

	DG.add_node(60,english_name="both legs straight, front foot point forward, back foot flat at 45deg")
	DG.node[60]["two_sided"]=True
	DG.node[60]["description"]=""
	DG.node[60]["yogajournalurl"]=""
	DG.node[60]["yogajournal_picture"]=""
	DG.node[60]["hindi_name"]=""
	DG.node[60]["comment"]=""
	DG.node[60]["Dharma Mittra picture URL"]=""
	DG.node[60]["asanas 608 page"]=""
	DG.node[60]["asanas 608 english name"]=""	

	DG.add_node(61,english_name="standing hinged forward at hips")
	DG.node[61]["two_sided"]=True
	DG.node[61]["description"]=""
	DG.node[61]["yogajournalurl"]=""
	DG.node[61]["yogajournal_picture"]=""
	DG.node[61]["hindi_name"]=""
	DG.node[61]["comment"]=""
	DG.node[61]["Dharma Mittra picture URL"]="http://www.dharmayogacenter.com/wp-content/gallery/asana-reference/uttanasana.jpg"
	DG.node[61]["asanas 608 page"]=""
	DG.node[61]["asanas 608 english name"]=""	

	DG.add_node(62,english_name="revolved triangle pose")
	DG.node[62]["hindi_name"]="Parivrtta Trikonasana"
	DG.node[62]["two_sided"]=True
	DG.node[62]["description"]=""
	DG.node[62]["yogajournalurl"]=""
	DG.node[62]["yogajournal_picture"]=""
	DG.node[62]["comment"]=""
	DG.node[62]["Dharma Mittra picture URL"]=""
	DG.node[62]["asanas 608 page"]=""
	DG.node[62]["asanas 608 english name"]=""	

	DG.add_node(63,english_name="extended side angle pose")
	DG.node[63]["two_sided"]=True
	DG.node[63]["yogajournalurl"]="http://www.yogajournal.com/poses/749"
	DG.node[63]["yogajournal_picture"]="http://media.yogajournal.com/wp-content/uploads/extendedsideanglepose.jpg"
	DG.node[63]["hindi_name"]="Utthita Parsvakonasana"
	DG.node[63]["comment"]=""
	DG.node[63]["Dharma Mittra picture URL"]=""
	DG.node[63]["description"]=""
	DG.node[63]["asanas_608_page"]=""
	DG.node[63]["asanas_608_english"]=""	

	DG.add_node(64,english_name="bind")
	DG.node[64]["two_sided"]=True
	DG.node[64]["description"]=""
	DG.node[64]["yogajournalurl"]=""
	DG.node[64]["yogajournal_picture"]=""
	DG.node[64]["hindi_name"]=""
	DG.node[64]["comment"]=""
	DG.node[64]["Dharma Mittra picture URL"]=""
	DG.node[64]["asanas 608 page"]=""
	DG.node[64]["asanas 608 english name"]=""	

	DG.add_node(65,english_name="bird of paradise")
	DG.node[65]["two_sided"]=True
	DG.node[65]["description"]=""
	DG.node[65]["yogajournalurl"]=""
	DG.node[65]["yogajournal_picture"]=""
	DG.node[65]["hindi_name"]=""
	DG.node[65]["comment"]=""
	DG.node[65]["Dharma Mittra picture URL"]=""
	DG.node[65]["asanas 608 page"]=""
	DG.node[65]["asanas 608 english name"]=""	

	DG.add_node(66,english_name="funky bird of paradise")
	DG.node[66]["two_sided"]=True
	DG.node[66]["description"]=""
	DG.node[66]["yogajournalurl"]=""
	DG.node[66]["yogajournal_picture"]=""
	DG.node[66]["hindi_name"]=""
	DG.node[66]["comment"]=""
	DG.node[66]["Dharma Mittra picture URL"]=""
	DG.node[66]["asanas 608 page"]=""
	DG.node[66]["asanas 608 english name"]=""	

	DG.add_node(67,english_name="standing bend bound twist")
	DG.node[67]["two_sided"]=True
	DG.node[67]["description"]=""
	DG.node[67]["yogajournalurl"]=""
	DG.node[67]["yogajournal_picture"]=""
	DG.node[67]["hindi_name"]=""
	DG.node[67]["comment"]=""
	DG.node[67]["Dharma Mittra picture URL"]=""
	DG.node[67]["asanas 608 page"]=""
	DG.node[67]["asanas 608 english name"]=""	

	DG.add_node(68,english_name="standing bend, legs apart")
	DG.node[68]["two_sided"]=False
	DG.node[68]["description"]=""
	DG.node[68]["yogajournalurl"]=""
	DG.node[68]["yogajournal_picture"]=""
	DG.node[68]["hindi_name"]=""
	DG.node[68]["comment"]=""
	DG.node[68]["Dharma Mittra picture URL"]=""
	DG.node[68]["asanas 608 page"]=""
	DG.node[68]["asanas 608 english name"]=""	

	DG.add_node(69,english_name="tripod head stand, legs bent, arms at 90deg")
	DG.node[69]["two_sided"]=False
	DG.node[69]["description"]="arms at 90deg"
	DG.node[69]["yogajournalurl"]=""
	DG.node[69]["yogajournal_picture"]=""
	DG.node[69]["hindi_name"]=""
	DG.node[69]["comment"]=""
	DG.node[69]["Dharma Mittra picture URL"]=""
	DG.node[69]["asanas 608 page"]=""
	DG.node[69]["asanas 608 english name"]=""	

	DG.add_node(70,english_name="floating elephant trunk; one leg over arm")
	DG.node[70]["two_sided"]=True
	DG.node[70]["description"]=""
	DG.node[70]["yogajournalurl"]=""
	DG.node[70]["yogajournal_picture"]=""
	DG.node[70]["hindi_name"]=""
	DG.node[70]["comment"]=""
	DG.node[70]["Dharma Mittra picture URL"]=""
	DG.node[70]["asanas 608 page"]=""
	DG.node[70]["asanas 608 english name"]=""	

	DG.add_node(71,english_name="eight angle pose")
	DG.node[71]["two_sided"]=True
	DG.node[71]["description"]=""
	DG.node[71]["yogajournalurl"]=""
	DG.node[71]["yogajournal_picture"]=""
	DG.node[71]["hindi_name"]=""
	DG.node[71]["comment"]=""
	DG.node[71]["Dharma Mittra picture URL"]=""
	DG.node[71]["asanas 608 page"]=""
	DG.node[71]["asanas 608 english name"]=""	

	DG.add_node(72,english_name="flying pigeon")
	DG.node[72]["two_sided"]=True
	DG.node[72]["description"]="shin on back triceps"
	DG.node[72]["yogajournalurl"]=""
	DG.node[72]["yogajournal_picture"]=""
	DG.node[72]["hindi_name"]=""
	DG.node[72]["comment"]=""
	DG.node[72]["Dharma Mittra picture URL"]=""
	DG.node[72]["asanas 608 page"]=""
	DG.node[72]["asanas 608 english name"]=""	

	DG.add_node(73,english_name="peddle feet")
	DG.node[73]["two_sided"]=True
	DG.node[73]["description"]=""
	DG.node[73]["yogajournalurl"]=""
	DG.node[73]["yogajournal_picture"]=""
	DG.node[73]["hindi_name"]=""
	DG.node[73]["comment"]=""
	DG.node[73]["Dharma Mittra picture URL"]=""
	DG.node[73]["asanas 608 page"]=""
	DG.node[73]["asanas 608 english name"]=""	

	DG.add_node(74,english_name="tripod head stand, legs extended out, arms at 90deg")
	DG.node[74]["two_sided"]=False
	DG.node[74]["description"]="arms at 90deg"
	DG.node[74]["yogajournalurl"]=""
	DG.node[74]["yogajournal_picture"]=""
	DG.node[74]["hindi_name"]=""
	DG.node[74]["comment"]=""
	DG.node[74]["Dharma Mittra picture URL"]=""
	DG.node[74]["asanas 608 page"]=""
	DG.node[74]["asanas 608 english name"]=""	

	DG.add_node(75,english_name="no-handed head stand")
	DG.node[75]["two_sided"]=False
	DG.node[75]["description"]=""
	DG.node[75]["yogajournalurl"]=""
	DG.node[75]["yogajournal_picture"]=""
	DG.node[75]["hindi_name"]=""
	DG.node[75]["comment"]=""
	DG.node[75]["Dharma Mittra picture URL"]=""
	DG.node[75]["asanas 608 page"]=""
	DG.node[75]["asanas 608 english name"]=""	

	DG.add_node(76,english_name="inverted tripod")
	DG.node[76]["two_sided"]=False
	DG.node[76]["description"]=""
	DG.node[76]["yogajournalurl"]=""
	DG.node[76]["yogajournal_picture"]=""
	DG.node[76]["hindi_name"]="Niralamba-Shirshasana"
	DG.node[76]["comment"]=""
	DG.node[76]["Dharma Mittra picture URL"]=""
	DG.node[76]["asanas_608_page"]="197"
	DG.node[76]["asanas_608_english"]="Hands-free Head Stand Pose (Variation)"	

	DG.add_node(77,english_name="seated wide-leg")
	DG.node[77]["two_sided"]=False
	DG.node[77]["description"]=""
	DG.node[77]["yogajournalurl"]=""
	DG.node[77]["yogajournal_picture"]=""
	DG.node[77]["hindi_name"]=""
	DG.node[77]["comment"]=""
	DG.node[77]["Dharma Mittra picture URL"]=""
	DG.node[77]["asanas 608 page"]=""
	DG.node[77]["asanas 608 english name"]=""	

	DG.add_node(78,english_name="seated wide-leg, floating")
	DG.node[78]["two_sided"]=False
	DG.node[78]["description"]=""
	DG.node[78]["yogajournalurl"]=""
	DG.node[78]["yogajournal_picture"]=""
	DG.node[78]["hindi_name"]=""
	DG.node[78]["comment"]=""
	DG.node[78]["Dharma Mittra picture URL"]=""
	DG.node[78]["asanas 608 page"]=""
	DG.node[78]["asanas 608 english name"]=""	

	DG.add_node(79,english_name="seated wide-leg, flying")
	DG.node[79]["two_sided"]=False
	DG.node[79]["description"]=""
	DG.node[79]["yogajournalurl"]=""
	DG.node[79]["yogajournal_picture"]=""
	DG.node[79]["hindi_name"]=""
	DG.node[79]["comment"]=""
	DG.node[79]["Dharma Mittra picture URL"]=""
	DG.node[79]["asanas 608 page"]=""
	DG.node[79]["asanas 608 english name"]=""	

	DG.add_node(80,english_name="all fours, one arm extended")
	DG.node[80]["two_sided"]=True
	DG.node[80]["description"]=""
	DG.node[80]["yogajournalurl"]=""
	DG.node[80]["yogajournal_picture"]=""
	DG.node[80]["hindi_name"]=""
	DG.node[80]["comment"]=""
	DG.node[80]["Dharma Mittra picture URL"]=""
	DG.node[80]["asanas 608 page"]=""
	DG.node[80]["asanas 608 english name"]=""	

	DG.add_node(81,english_name="all fours, one leg extended")
	DG.node[81]["two_sided"]=True
	DG.node[81]["description"]=""
	DG.node[81]["yogajournalurl"]=""
	DG.node[81]["yogajournal_picture"]=""
	DG.node[81]["hindi_name"]=""
	DG.node[81]["comment"]=""
	DG.node[81]["Dharma Mittra picture URL"]=""
	DG.node[81]["asanas 608 page"]=""
	DG.node[81]["asanas 608 english name"]=""	

	DG.add_node(82,english_name="all fours, one arm extended, oppposite leg extended")
	DG.node[82]["two_sided"]=True
	DG.node[82]["description"]=""
	DG.node[82]["yogajournalurl"]=""
	DG.node[82]["yogajournal_picture"]=""
	DG.node[82]["hindi_name"]=""
	DG.node[82]["comment"]=""
	DG.node[82]["Dharma Mittra picture URL"]=""
	DG.node[82]["asanas 608 page"]=""
	DG.node[82]["asanas 608 english name"]=""	

	DG.add_node(83,english_name="all fours, one arm extended, same side leg extended")
	DG.node[83]["two_sided"]=True
	DG.node[83]["description"]=""
	DG.node[83]["yogajournalurl"]=""
	DG.node[83]["yogajournal_picture"]=""
	DG.node[83]["hindi_name"]=""
	DG.node[83]["comment"]=""
	DG.node[83]["Dharma Mittra picture URL"]=""
	DG.node[83]["asanas 608 page"]=""
	DG.node[83]["asanas 608 english name"]=""	

	DG.add_node(84,english_name="all fours, hips to one side")
	DG.node[84]["two_sided"]=True
	DG.node[84]["description"]=""
	DG.node[84]["yogajournalurl"]=""
	DG.node[84]["yogajournal_picture"]=""
	DG.node[84]["hindi_name"]=""
	DG.node[84]["comment"]=""
	DG.node[84]["Dharma Mittra picture URL"]=""
	DG.node[84]["asanas 608 page"]=""
	DG.node[84]["asanas 608 english name"]=""	

	DG.add_node(85,english_name="forearm plank")
	DG.node[85]["two_sided"]=False
	DG.node[85]["description"]=""
	DG.node[85]["yogajournalurl"]=""
	DG.node[85]["yogajournal_picture"]=""
	DG.node[85]["hindi_name"]=""
	DG.node[85]["comment"]=""
	DG.node[85]["Dharma Mittra picture URL"]=""
	DG.node[85]["asanas 608 page"]=""
	DG.node[85]["asanas 608 english name"]=""	

	DG.add_node(86,english_name="tripod head stand, legs bent, arms straight")
	DG.node[86]["two_sided"]=False
	DG.node[86]["description"]=""
	DG.node[86]["yogajournalurl"]=""
	DG.node[86]["yogajournal_picture"]=""
	DG.node[86]["hindi_name"]=""
	DG.node[86]["comment"]=""
	DG.node[86]["Dharma Mittra picture URL"]=""
	DG.node[86]["asanas 608 page"]=""
	DG.node[86]["asanas 608 english name"]=""	

	DG.add_node(87,english_name="standing back bend")
	DG.node[87]["two_sided"]=False
	DG.node[87]["description"]="feet together"
	DG.node[87]["yogajournalurl"]=""
	DG.node[87]["yogajournal_picture"]=""
	DG.node[87]["hindi_name"]=""
	DG.node[87]["comment"]=""
	DG.node[87]["Dharma Mittra picture URL"]=""
	DG.node[87]["asanas 608 page"]=""
	DG.node[87]["asanas 608 english name"]=""	

	DG.add_node(88,english_name="scorpion")
	DG.node[88]["two_sided"]=False
	DG.node[88]["description"]=""
	DG.node[88]["yogajournalurl"]=""
	DG.node[88]["yogajournal_picture"]=""
	DG.node[88]["hindi_name"]=""
	DG.node[88]["comment"]=""
	DG.node[88]["Dharma Mittra picture URL"]=""
	DG.node[88]["asanas 608 page"]=""
	DG.node[88]["asanas 608 english name"]=""	

	DG.add_node(89,english_name="bird of paradise, bent forward, leg to side")
	DG.node[89]["two_sided"]=False
	DG.node[89]["description"]=""
	DG.node[89]["yogajournalurl"]=""
	DG.node[89]["yogajournal_picture"]=""
	DG.node[89]["hindi_name"]=""
	DG.node[89]["comment"]=""
	DG.node[89]["Dharma Mittra picture URL"]=""
	DG.node[89]["asanas 608 page"]=""
	DG.node[89]["asanas 608 english name"]=""	

	DG.add_node(90,english_name="tripod head stand, legs straight, arms straight")
	DG.node[90]["two_sided"]=False
	DG.node[90]["description"]=""
	DG.node[90]["yogajournalurl"]=""
	DG.node[90]["yogajournal_picture"]=""
	DG.node[90]["hindi_name"]=""
	DG.node[90]["comment"]=""
	DG.node[90]["Dharma Mittra picture URL"]=""
	DG.node[90]["asanas 608 page"]=""
	DG.node[90]["asanas 608 english name"]=""	

	DG.add_node(91,english_name="butterfly")
	DG.node[91]["two_sided"]=False
	DG.node[91]["description"]=""
	DG.node[91]["yogajournalurl"]=""
	DG.node[91]["yogajournal_picture"]=""
	DG.node[91]["hindi_name"]=""
	DG.node[91]["comment"]=""
	DG.node[91]["Dharma Mittra picture URL"]=""
	DG.node[91]["asanas 608 page"]=""
	DG.node[91]["asanas 608 english name"]=""	

	DG.add_node(92,english_name="hurdler")
	DG.node[92]["two_sided"]=False
	DG.node[92]["description"]=""
	DG.node[92]["yogajournalurl"]=""
	DG.node[92]["yogajournal_picture"]=""
	DG.node[92]["hindi_name"]=""
	DG.node[92]["comment"]=""
	DG.node[92]["Dharma Mittra picture URL"]=""
	DG.node[92]["asanas 608 page"]=""
	DG.node[92]["asanas 608 english name"]=""	

	DG.add_node(93,english_name="bridge")
	DG.node[93]["two_sided"]=False
	DG.node[93]["description"]=""
	DG.node[93]["yogajournalurl"]="http://www.yogajournal.com/pose/bridge-pose/"
	DG.node[93]["yogajournal_picture"]="http://media.yogajournal.com/wp-content/uploads/257_HP_13_fnl_4502.jpg"
	DG.node[93]["hindi_name"]=""
	DG.node[93]["comment"]=""
	DG.node[93]["Dharma Mittra picture URL"]=""
	DG.node[93]["asanas 608 page"]=""
	DG.node[93]["asanas 608 english name"]=""	

	DG.add_node(94,english_name="standing eagle")
	DG.node[94]["two_sided"]=False
	DG.node[94]["description"]=""
	DG.node[94]["yogajournalurl"]="http://www.yogajournal.com/pose/eagle-pose/"
	DG.node[94]["yogajournal_picture"]="http://media.yogajournal.com/wp-content/uploads/pract-well_trail_268_04_Eagle.jpg"
	DG.node[94]["hindi_name"]=""
	DG.node[94]["comment"]=""
	DG.node[94]["Dharma Mittra picture URL"]=""
	DG.node[94]["asanas 608 page"]=""
	DG.node[94]["asanas 608 english name"]=""	

	DG.add_node(95,english_name="seated forward fold")
	DG.node[95]["two_sided"]=False
	DG.node[95]["description"]=""
	DG.node[95]["yogajournalurl"]="http://www.yogajournal.com/pose/seated-forward-bend/"
	DG.node[95]["yogajournal_picture"]="http://media.yogajournal.com/wp-content/uploads/257_HP_12_fnl_4501.jpg"
	DG.node[95]["hindi_name"]=""
	DG.node[95]["comment"]=""
	DG.node[95]["Dharma Mittra picture URL"]=""
	DG.node[95]["asanas 608 page"]=""
	DG.node[95]["asanas 608 english name"]=""	

	return DG
'''
	DG.add_node(9,english_name="")
	DG.node[9]["two_sided"]=False
	DG.node[9]["description"]=""
	DG.node[9]["yogajournalurl"]=""
	DG.node[9]["yogajournal_picture"]=""
	DG.node[9]["hindi_name"]=""
	DG.node[9]["comment"]=""
	DG.node[9]["Dharma Mittra picture URL"]=""
	DG.node[9]["asanas 608 page"]=""
	DG.node[9]["asanas 608 english name"]=""	

	DG.add_node(9,english_name="")
	DG.node[9]["two_sided"]=False
	DG.node[9]["description"]=""
	DG.node[9]["yogajournalurl"]=""
	DG.node[9]["yogajournal_picture"]=""
	DG.node[9]["hindi_name"]=""
	DG.node[9]["comment"]=""
	DG.node[9]["Dharma Mittra picture URL"]=""
	DG.node[9]["asanas 608 page"]=""
	DG.node[9]["asanas 608 english name"]=""	
'''



    
def pose_transitions(DG):
	DG.add_weighted_edges_from([(0,2,1)])   # 0 = all fours; 2 = cat
	DG.add_weighted_edges_from([(0,1,1)])   # 0 = all fours; 1 = cow
	DG.add_weighted_edges_from([(0,3,1)])   # 0 = all fours; 3 = child's pose
	DG.add_weighted_edges_from([(0,4,2)])   # 0 = all fours; 4 = downward dog
	DG.add_weighted_edges_from([(0,6,1)])   # 0 = all fours; 6 = lay on stomach
	DG.add_weighted_edges_from([(0,13,2)])  # 0 = all fours; 13 = plank
	DG.add_weighted_edges_from([(0,80,2)])  # 0 = all fours; 80 = all fours, one arm extended
	DG.add_weighted_edges_from([(0,81,2)])  # 0 = all fours; 81 = all fours, one leg extended
	DG.add_weighted_edges_from([(0,82,3)])  # 0 = all fours; 82 = all fours, one arm extended, oppposite leg extended
	DG.add_weighted_edges_from([(0,83,4)])  # 0 = all fours; 83 = all fours, one arm extended, same side leg extended
	DG.add_weighted_edges_from([(0,84,1)])  # 0 = all fours; 84 = all fours, hips to one side

	DG.add_weighted_edges_from([(1,0,1)])   # 1 = cow; 0 = all fours
	DG.add_weighted_edges_from([(1,4,1)])   # 1 = cow; 4 = downward dog

	DG.add_weighted_edges_from([(2,0,1)])   # 2 = cat; 0 = all fours
	DG.add_weighted_edges_from([(2,4,1)])   # 2 = cat; 4 = downward dog

	DG.add_weighted_edges_from([(3,0,1)])   # 3 = child's pose; 0 = all fours
	DG.add_weighted_edges_from([(3,4,1)])   # 3 = child's pose; 4 = downward dog
	DG.add_weighted_edges_from([(3,5,1)])   # 3 = child's pose; 5 = dolphin
	DG.add_weighted_edges_from([(3,6,1)])   # 3 = child's pose; 6 = lay on stomach
	DG.add_weighted_edges_from([(3,41,1)])  # 3 = child's pose; 41 = kneeling on shins
	DG.add_weighted_edges_from([(3,42,1)])  # 3 = child's pose; 42 = standing on shins
	DG.add_weighted_edges_from([(3,59,1)])  # 3 = child's pose; 59 = arms to side

	DG.add_weighted_edges_from([(4,0,1)])   # 4 = downward dog; 0 = all fours
	DG.add_weighted_edges_from([(4,1,1)])   # 4 = downward dog; 1 = cow
	DG.add_weighted_edges_from([(4,2,1)])   # 4 = downward dog; 2 = cat
	DG.add_weighted_edges_from([(4,3,1)])   # 4 = downward dog; 3 = child's pose
	DG.add_weighted_edges_from([(4,13,1)])  # 4 = downward dog; 13 = plank
	DG.add_weighted_edges_from([(4,17,1)])  # 4 = downward dog; 17 = standing bend, legs together
	DG.add_weighted_edges_from([(4,18,1)])  # 4 = downward dog; 18 = downward dog, one leg raised
	DG.add_weighted_edges_from([(4,47,2)])  # 4 = downward dog; 47 = upward dog
	DG.add_weighted_edges_from([(4,68,1)])  # 4 = downward dog; 68 = standing bend, legs apart
	DG.add_weighted_edges_from([(4,73,1)])  # 4 = downward dog; 73 = peddle feet
	DG.add_weighted_edges_from([(4,76,5)])  # 4 = downward dog; 76 = inverted tripod

	DG.add_weighted_edges_from([(5,3,1)])   # 5 = dolphin; 3 = child's pose
	DG.add_weighted_edges_from([(5,4,1)])   # 5 = dolphin; 4 = downward dog
	DG.add_weighted_edges_from([(5,6,1)])   # 5 = dolphin; 6 = lay on stomach
	DG.add_weighted_edges_from([(5,85,1)])  # 5 = dolphin; 13 = forearm plank

	DG.add_weighted_edges_from([(6,0,1)])   # 6 = lay on stomach; 0 = all fours
	DG.add_weighted_edges_from([(6,3,1)])   # 6 = lay on stomach; 3 = child's pose
	DG.add_weighted_edges_from([(6,5,1)])   # 6 = lay on stomach; 5 = dolphin
	DG.add_weighted_edges_from([(6,7,1)])   # 6 = lay on stomach; 7 = bow pose

	DG.add_weighted_edges_from([(7,6,1)])   # 7 = bow pose; 6 = lay on stomach

	DG.add_weighted_edges_from([(8,9,1)])   # 8 = laying on back, one leg extended up; 9 = both legs extended up
	DG.add_weighted_edges_from([(8,31,1)])  # 8 = laying on back, one leg extended up; 31 = corpse

	DG.add_weighted_edges_from([(9,8,1)])   # 9 = both legs extended up; 8 = lying on back, one leg extended up
	DG.add_weighted_edges_from([(9,10,1)])  # 9 = both legs extended up; 10 = supported shoulder stand
	DG.add_weighted_edges_from([(9,31,1)])  # 9 = both legs extended up; 31 = corpse
	DG.add_weighted_edges_from([(9,32,1)])  # 9 = both legs extended up; 32 = happy baby

	DG.add_weighted_edges_from([(10,9,1)])   # 10 = supported shoulder stand; 9 = both legs extended up
	DG.add_weighted_edges_from([(10,11,1)])  # 10 = supported shoulder stand; 11 = plow
	DG.add_weighted_edges_from([(10,12,1)])  # 10 = supported shoulder stand; 12 = ear pressure

	DG.add_weighted_edges_from([(11,10,1)])   # 11 = plow; 10 = supported shoulder stand
	DG.add_weighted_edges_from([(11,12,1)])   # 11 = plow; 12 = ear pressure

	DG.add_weighted_edges_from([(12,10,1)])   # 12 = ear pressure; 10 = supported shoulder stand
	DG.add_weighted_edges_from([(12,11,1)])   # 12 = ear pressure; 11 = plow

	DG.add_weighted_edges_from([(13,0,1)])   # 13 = plank; 0 = all fours
	DG.add_weighted_edges_from([(13,4,1)])   # 13 = plank; 4 = downward dog
	DG.add_weighted_edges_from([(13,14,1)])  # 13 = plank; 14 = wild thing
	DG.add_weighted_edges_from([(13,15,1)])  # 13 = plank; 15 = low pushup
	DG.add_weighted_edges_from([(13,16,1)])  # 13 = plank; 16 = side plank
	DG.add_weighted_edges_from([(13,37,1)])  # 13 = plank; 37 = pigeon pose
	DG.add_weighted_edges_from([(13,44,1)])  # 13 = plank; 44 = crow
	DG.add_weighted_edges_from([(13,48,1)])  # 13 = plank; 48 = one leg forward with knee bent
	DG.add_weighted_edges_from([(13,85,1)])  # 13 = plank; 85 = forearm plank

	DG.add_weighted_edges_from([(14,13,1)])   # 14 = wild thing; 13 = plank
	DG.add_weighted_edges_from([(14,37,1)])   # 14 = wild thing; 37 = pigeon pose

	DG.add_weighted_edges_from([(15,13,1)])   # 15 = low pushup; 13 = plank
	DG.add_weighted_edges_from([(15,44,4)])   # 15 = low pushup; 44 = crow
	DG.add_weighted_edges_from([(15,47,1)])   # 15 = low pushup; 47 = upward dog

	DG.add_weighted_edges_from([(16,13,1)])   # 16 = side plank; 13 = plank

	DG.add_weighted_edges_from([(17,4,1)])   # 17 = standing bend, legs together; 4 = downward dog
	DG.add_weighted_edges_from([(17,20,1)])  # 17 = standing bend, legs together; 20 = stand straight (mountain)
	DG.add_weighted_edges_from([(17,68,1)])  # 17 = standing bend, legs together; 68 = standing bend, legs apart

	DG.add_weighted_edges_from([(18,4,1)])   # 18 = downward dog, one leg raised; 4 = downward dog
	DG.add_weighted_edges_from([(18,19,1)])  # 18 = downward dog, one leg raised; 19 = flipped dog

	DG.add_weighted_edges_from([(19,18,1)])   # 19 = flipped dog; 18 = downward dog, one leg raised
	DG.add_weighted_edges_from([(19,28,1)])   # 19 = flipped dog; 28 = wheel

	DG.add_weighted_edges_from([(20,17,1)])   # 20 = stand straight (mountain); 17 = standing bend, legs together
	DG.add_weighted_edges_from([(20,21,1)])   # 20 = stand straight (mountain); 21 = happy camper
	DG.add_weighted_edges_from([(20,23,1)])   # 20 = stand straight (mountain); 23 = warrior 3
	DG.add_weighted_edges_from([(20,24,1)])   # 20 = stand straight (mountain); 24 = warrior 1
	DG.add_weighted_edges_from([(20,27,1)])   # 20 = stand straight (mountain); 27 = chair
	DG.add_weighted_edges_from([(20,87,1)])   # 20 = stand straight (mountain); 87 = standing back bend
	DG.add_weighted_edges_from([(20,46,1)])   # 20 = stand straight (mountain); 46 = standing, legs apart

	DG.add_weighted_edges_from([(21,20,1)])   # 21 = happy camper; 20 = stand straight (mountain)
	DG.add_weighted_edges_from([(21,27,1)])   # 21 = happy camper; 27 = chair
	DG.add_weighted_edges_from([(21,72,1)])   # 21 = happy camper; 72 = flying pigeon

	DG.add_weighted_edges_from([(22,20,1)])   # 22 = tree pose; 20 = stand straight (mountain)
	DG.add_weighted_edges_from([(22,21,1)])   # 22 = tree pose; 21 = happy camper
	DG.add_weighted_edges_from([(22,23,1)])   # 22 = tree pose; 23 = warrior 3

	DG.add_weighted_edges_from([(23,20,1)])   # 23 = warrior 3; 20 = stand straight (mountain)
	DG.add_weighted_edges_from([(23,22,1)])   # 23 = warrior 3; 22 = tree pose
	DG.add_weighted_edges_from([(23,24,1)])   # 23 = warrior 3; 24 = warrior 1
	DG.add_weighted_edges_from([(23,25,1)])   # 23 = warrior 3; 25 = dancer pose
	DG.add_weighted_edges_from([(23,26,1)])   # 23 = warrior 3; 26 = standing splits
	DG.add_weighted_edges_from([(23,48,1)])   # 23 = warrior 3; 48 = one leg forward with knee bent

	DG.add_weighted_edges_from([(24,20,1)])   # 24 = warrior 1; 20 = stand straight (mountain)
	DG.add_weighted_edges_from([(24,23,1)])   # 24 = warrior 1; 23 = warrior 3
	DG.add_weighted_edges_from([(24,29,1)])   # 24 = warrior 1; 29 = warrior 2

	DG.add_weighted_edges_from([(25,23,1)])   # 25 = dancer pose; 23 = warrior 3

	DG.add_weighted_edges_from([(26,23,1)])   # 26 = standing splits; 23 = warrior 3

	DG.add_weighted_edges_from([(27,20,1)])   # 27 = chair; 20 = stand straight (mountain)
	DG.add_weighted_edges_from([(27,21,1)])   # 27 = chair; 21 = happy camper

	DG.add_weighted_edges_from([(28,19,1)])   # 28 = wheel; 19 = flipped dog
	DG.add_weighted_edges_from([(28,20,1)])   # 28 = wheel; 20 = stand straight (mountain)
	DG.add_weighted_edges_from([(28,31,1)])   # 28 = wheel; 31 = corpse

	DG.add_weighted_edges_from([(29,24,1)])   # 29 = warrior 2; 24 = warrior 1
	DG.add_weighted_edges_from([(29,30,1)])   # 29 = warrior 2; 30 = 
	DG.add_weighted_edges_from([(29,56,1)])   # 29 = warrior 2; 56 = 
	DG.add_weighted_edges_from([(29,60,1)])   # 29 = warrior 2; 60 = 

	DG.add_weighted_edges_from([(30,29,1)])   # 30 = peaceful warrior; 29 = warrior

	DG.add_weighted_edges_from([(31,8,1)])   # 31 = corpse; 8 = one leg extended up
	DG.add_weighted_edges_from([(31,9,1)])   # 31 = corpse; 9 = both legs extended up
	DG.add_weighted_edges_from([(31,32,1)])  # 31 = corpse; 32 = happy baby
	DG.add_weighted_edges_from([(31,34,1)])  # 31 = corpse; 34 = on back, knees bent, feet in air
	DG.add_weighted_edges_from([(31,36,1)])  # 31 = corpse; 36 = staff
	DG.add_weighted_edges_from([(31,45,1)])  # 31 = corpse; 45 = squat, knees wide

	DG.add_weighted_edges_from([(32,9,1)])    # 32 = happy baby; 9 = both legs extended up
	DG.add_weighted_edges_from([(32,31,1)])   # 32 = happy baby; 31 = corpse

	DG.add_weighted_edges_from([(33,34,1)])   # 33 = on back, knees bent, feet on ground; 34 = on back, knees bent, feet in air
	DG.add_weighted_edges_from([(33,35,1)])   # 33 = on back, knees bent, feet on ground; 35 = knees to one side, head to other

	DG.add_weighted_edges_from([(34,31,1)])   # 34 = on back, knees bent, feet in air; 31 = corpse
	DG.add_weighted_edges_from([(34,33,1)])   # 34 = on back, knees bent, feet in air; 33 = on back, knees bent, feet on ground
	DG.add_weighted_edges_from([(34,35,1)])   # 34 = on back, knees bent, feet in air; 35 = knees to one side, head to other

	DG.add_weighted_edges_from([(35,33,1)])   # 35 = knees to one side, head to other; 33 = on back, knees bent, feet on ground
	DG.add_weighted_edges_from([(35,34,1)])   # 35 = knees to one side, head to other; 34 = on back, knees bent, feet in air

	DG.add_weighted_edges_from([(36,31,1)])   # 36 = staff; 31 = corpse
	DG.add_weighted_edges_from([(36,38,1)])   # 36 = staff; 38 = one leg straight, one leg in
	DG.add_weighted_edges_from([(36,45,1)])   # 36 = staff; 45 = squat, knees wide
	DG.add_weighted_edges_from([(36,49,1)])   # 36 = staff; 49 = half lotus
	DG.add_weighted_edges_from([(36,53,1)])   # 36 = staff; 53 = 

	DG.add_weighted_edges_from([(37,13,1)])   # 37 = pigeon pose; 13 = plank
	DG.add_weighted_edges_from([(37,14,1)])   # 37 = pigeon pose; 14 = wild thing

	DG.add_weighted_edges_from([(38,36,1)])   # 38 = one leg straight, one leg in; 36 = staff
	DG.add_weighted_edges_from([(38,39,1)])   # 38 = one leg straight, one leg in; 39 = compass pose
	DG.add_weighted_edges_from([(38,40,1)])   # 38 = one leg straight, one leg in; 40 = rock bent leg

	DG.add_weighted_edges_from([(39,38,1)])   # 39 = compass pose; 38 = one leg straight, one leg in
	DG.add_weighted_edges_from([(39,40,1)])   # 39 = compass pose; 40 = rock bent leg

	DG.add_weighted_edges_from([(40,38,1)])   # 40 = rock bent leg; 38 = one leg straight, one leg in
	DG.add_weighted_edges_from([(40,70,1)])   # 40 = rock bent leg; 70 = floating elephant trunk; one leg over arm
	DG.add_weighted_edges_from([(40,39,1)])   # 40 = rock bent leg; 39 = compass pose

	DG.add_weighted_edges_from([(41,3,1)])   # 41 = kneeling on shins; 3 = child's pose
	DG.add_weighted_edges_from([(41,42,1)])  # 41 = kneeling on shins; 42 = standing on shins

	DG.add_weighted_edges_from([(42,3,1)])   # 42 = standing on shins; 3 = child's pose
	DG.add_weighted_edges_from([(42,41,1)])  # 42 = standing on shins; 41 = kneeling on shins
	DG.add_weighted_edges_from([(42,43,1)])  # 42 = standing on shins; 43 = camel pose

	DG.add_weighted_edges_from([(43,42,1)])   # 43 = camel pose; 42 = standing on shins

	DG.add_weighted_edges_from([(44,15,1)])   # 44 = crow; 15 = low pushup
	DG.add_weighted_edges_from([(44,45,1)])   # 44 = crow; 45 = squat, knees wide

	DG.add_weighted_edges_from([(45,31,1)])   # 45 = squat, knees wide; 31 = corpse
	DG.add_weighted_edges_from([(45,36,1)])   # 45 = squat, knees wide; 36 = staff
	DG.add_weighted_edges_from([(45,44,1)])   # 45 = squat, knees wide; 44 = crow
	DG.add_weighted_edges_from([(45,46,1)])   # 45 = squat, knees wide; 46 = standing, legs apart
	DG.add_weighted_edges_from([(45,54,1)])   # 45 = squat, knees wide; 54 = 
	DG.add_weighted_edges_from([(45,69,1)])   # 45 = squat, knees wide; 69 = 

	DG.add_weighted_edges_from([(46,45,1)])   # 46 = standing, legs apart; 45 = squat, knees wide
	DG.add_weighted_edges_from([(46,20,1)])   # 46 = standing, legs apart; 20 = stand straight (mountain)
	DG.add_weighted_edges_from([(46,68,1)])   # 46 = standing, legs apart; 68 = standing bend, legs apart

	DG.add_weighted_edges_from([(47,4,1)])    # 47 = upward dog; 4 = downward dog
	DG.add_weighted_edges_from([(47,15,1)])   # 47 = upward dog; 15 = low pushup

	DG.add_weighted_edges_from([(48,13,1)])   # 48 = one leg forward with knee bent; 13 = plank
	DG.add_weighted_edges_from([(48,23,1)])   # 48 = one leg forward with knee bent; 23 = warrior 3

	DG.add_weighted_edges_from([(49,36,1)])   # 49 = half lotus; 36 = staff
	DG.add_weighted_edges_from([(49,50,1)])   # 49 = half lotus; 50 = full lotus

	DG.add_weighted_edges_from([(50,49,1)])   # 50 = full lotus; 49 = half lotus
	DG.add_weighted_edges_from([(50,51,1)])   # 50 = full lotus; 51 = embryo pose
	DG.add_weighted_edges_from([(50,52,1)])   # 50 = full lotus; 52 = flying lotus

	DG.add_weighted_edges_from([(51,50,1)])   # 51 = embryo pose; 50 = full lotus

	DG.add_weighted_edges_from([(52,50,1)])   # 52 = flying lotus; 50 = full lotus

	DG.add_weighted_edges_from([(53,36,1)])   # 53 = floating staff pose; 36 = staff

	DG.add_weighted_edges_from([(54,45,1)])   # 54 = crane; 45 = squat, knees wide
	DG.add_weighted_edges_from([(54,55,1)])   # 54 = crane; 55 = 
	DG.add_weighted_edges_from([(54,69,1)])   # 54 = crane; 69 = tripod head stand, legs bent, arms at 90deg

	DG.add_weighted_edges_from([(55,54,1)])   # 55 = one-legged crane; 54 = crane

	DG.add_weighted_edges_from([(56,29,1)])   # 56 = wide legs, feet parallel; 29 = warrior 2
	DG.add_weighted_edges_from([(56,57,1)])   # 56 = wide legs, feet parallel; 57 = bent over wide legs, parallel feet

	DG.add_weighted_edges_from([(57,56,1)])   # 57 = bent over wide legs, parallel feet; 56 = wide legs, feet parallel
	DG.add_weighted_edges_from([(57,69,1)])   # 57 = bent over wide legs, parallel feet; 69 = tripod head stand, legs bent, arms at 90deg

	DG.add_weighted_edges_from([(58,69,1)])   # 58 = tripod head stand, legs extended straight up, arms at 90deg; 69 = tripod head stand, legs bent, arms at 90deg
	DG.add_weighted_edges_from([(58,74,1)])   # 58 = tripod head stand, legs extended straight up, arms at 90deg; 74 = tripod head stand, legs extended out, arms at 90deg
	DG.add_weighted_edges_from([(58,75,1)])   # 58 = tripod head stand, legs extended straight up, arms at 90deg; 75 = no-handed head stand

	DG.add_weighted_edges_from([(59,3,1)])   # 59 = arms to side; 3 = child's pose

	DG.add_weighted_edges_from([(60,29,1)])   # 60 = both legs straight, front foot point forward, back foot flat at 45deg; 29 = warrior 2
	DG.add_weighted_edges_from([(60,61,1)])   # 60 = both legs straight, front foot point forward, back foot flat at 45deg; 61 = hinged forward at hips; 60 = both legs straight, front foot point forward, back foot flat at 45deg
	DG.add_weighted_edges_from([(60,63,1)])   # 60 = both legs straight, front foot point forward, back foot flat at 45deg; 63 = extended side angle pose

	DG.add_weighted_edges_from([(61,60,1)])   # 61 = hinged forward at hips; 60 = both legs straight, front foot point forward, back foot flat at 45deg
	DG.add_weighted_edges_from([(61,62,1)])   # 61 = hinged forward at hips; 62 = revolved triangle pose

	DG.add_weighted_edges_from([(62,61,1)])   # 62 = revolved triangle pose; 61 = hinged forward at hips

	DG.add_weighted_edges_from([(63,60,1)])   # 63 = extended side angle pose; 60 = both legs straight, front foot point forward, back foot flat at 45deg
	DG.add_weighted_edges_from([(63,64,1)])   # 63 = extended side angle pose; 64 = bind

	DG.add_weighted_edges_from([(64,63,1)])   # 64 = bind; 63 = extended side angle pose
	DG.add_weighted_edges_from([(64,65,1)])   # 64 = bind; 65 = bird of paradise

	DG.add_weighted_edges_from([(65,64,1)])   # 65 = bird of paradise; 64 = bind
	DG.add_weighted_edges_from([(65,67,1)])   # 65 = bird of paradise; 67 = standing bend bound twist
	DG.add_weighted_edges_from([(65,89,1)])   # 65 = bird of paradise; 89 = bird of paradise, bent forward, leg to side

	DG.add_weighted_edges_from([(66,67,1)])   # 66 = funky bird of paradise; 67 = standing bend bound twist

	DG.add_weighted_edges_from([(67,65,1)])   # 67 = standing bend bound twist; 65 = bird of paradise
	DG.add_weighted_edges_from([(67,68,1)])   # 67 = standing bend bound twist; 68 = standing bend, legs apart

	DG.add_weighted_edges_from([(68,4,1)])   # 68 = standing bend, legs apart; 4 = downward dog
	DG.add_weighted_edges_from([(68,17,1)])  # 68 = standing bend, legs apart; 17 = standing bend, legs together
	DG.add_weighted_edges_from([(68,46,1)])  # 68 = standing bend, legs apart; 46 = standing, legs apart
	DG.add_weighted_edges_from([(68,67,1)])  # 68 = standing bend, legs apart; 67 = standing bend bound twist

	DG.add_weighted_edges_from([(69,45,1)])   # 69 = tripod head stand, legs bent, arms at 90deg; 45 = squat, knees wide
	DG.add_weighted_edges_from([(69,54,1)])   # 69 = tripod head stand, legs bent, arms at 90deg; 54 = 
	DG.add_weighted_edges_from([(69,57,1)])   # 69 = tripod head stand, legs bent, arms at 90deg; 57 = 
	DG.add_weighted_edges_from([(69,58,1)])   # 69 = tripod head stand, legs bent, arms at 90deg; 58 = tripod head stand, legs extended straight up, arms at 90deg
	DG.add_weighted_edges_from([(69,86,1)])   # 69 = tripod head stand, legs bent, arms at 90deg; 86 = tripod head stand, legs bent, arms straight

	DG.add_weighted_edges_from([(70,40,1)])   # 70 = floating elephant trunk; one leg over arm; 40 = rock bent leg
	DG.add_weighted_edges_from([(70,71,1)])   # 70 = floating elephant trunk; one leg over arm; 71 = eight angle pose

	DG.add_weighted_edges_from([(71,70,1)])   # 71 = eight angle pose; 70 = floating elephant trunk; one leg over arm

	DG.add_weighted_edges_from([(72,21,1)])   # 72 = flying pigeon; 21 = happy camper

	DG.add_weighted_edges_from([(73,4,1)])   # 73 = peddle feet; 4 = downward dog

	DG.add_weighted_edges_from([(74,58,1)])   # 74 = tripod head stand, legs extended out, arms at 90deg; 58 = tripod head stand, legs extended straight up, arms at 90deg

	DG.add_weighted_edges_from([(75,58,1)])   # 75 = no-handed head stand; 58 = tripod head stand, legs extended straight up, arms at 90deg

	DG.add_weighted_edges_from([(76,4,1)])   # 76 = inverted tripod; 4 = downward dog

	DG.add_weighted_edges_from([(77,78,1)])   # 77 = seated wide-leg; 78 = seated wide-leg, floating
	DG.add_weighted_edges_from([(77,79,1)])   # 77 = seated wide-leg; 79 = seated wide-leg, flying

	DG.add_weighted_edges_from([(78,77,1)])   # 78 = seated wide-leg, floating; 77 = seated wide-leg; 

	DG.add_weighted_edges_from([(79,77,1)])   # 79 = seated wide-leg, flying; 77 = seated wide-leg

	DG.add_weighted_edges_from([(80,0,2)])  # 80 = all fours, one arm extended; 0 = all fours
	
	DG.add_weighted_edges_from([(81,0,2)])  # 81 = all fours, one leg extended; 0 = all fours
	
	DG.add_weighted_edges_from([(82,0,3)])  # 82 = all fours, one arm extended, oppposite leg extended; 0 = all fours
	
	DG.add_weighted_edges_from([(83,0,4)])  # 83 = all fours, one arm extended, same side leg extended; 0 = all fours; 

	DG.add_weighted_edges_from([(84,0,1)])  # 84 = all fours, hips to one side; 0 = all fours

	DG.add_weighted_edges_from([(85,13,1)])  # 85 = forearm plank; 13 = plank

	DG.add_weighted_edges_from([(86,69,1)])   # 86 = tripod head stand, legs bent, arms straight; 69 = tripod head stand, legs bent, arms at 90deg
	DG.add_weighted_edges_from([(86,90,1)])   # 86 = tripod head stand, legs bent, arms straight; 90 = tripod head stand, legs straight, arms straight

	DG.add_weighted_edges_from([(87,20,1)])   # 87 = standing back bend; 20 = stand straight (mountain)

# 	DG.add_weighted_edges_from([(88,,1)])   # 88 = scorpion ; 

	DG.add_weighted_edges_from([(89,65,1)])   # 89 = bird of paradise, bent forward, leg to side; 65 = bird of paradise

	DG.add_weighted_edges_from([(90,86,1)])   # 90 = tripod head stand, legs straight, arms straight; 86 = tripod head stand, legs bent, arms straight

#	DG.add_weighted_edges_from([(91,,1)])   # 91 = butterfly

#	DG.add_weighted_edges_from([(92,,1)])  # 92 = hurdler

	
	return DG
