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
https://commons.wikimedia.org/wiki/Category:Nina_Mel
https://en.wiktionary.org/wiki/User:BD2412/yoga_poses
https://en.wikipedia.org/wiki/List_of_asanas

https://www.yogajournal.com/pose-finder/pose-finder/
http://www.yogajournal.com/poses/finder/browse_categories
https://www.yogajournal.com/poses/types/standing/
https://www.yogajournal.com/poses/anatomy/hips/
https://www.yogajournal.com/poses/anatomy/knees/
https://www.yogajournal.com/poses/types/


https://www.dharmayogacenter.com/resources/yoga-poses/

http://www.theyogaposes.com/
http://www.joythruyoga.com/list-of-yoga-poses.html
https://yoga.com/poses

"""


def pose_properties(DG):
    """
    Graph nodes
    """
    DG.add_node(0, english_name="table top")
    DG.nodes[0]["two_sided"] = False
    DG.nodes[0][
        "description"
    ] = "on all fours; hands, knees, and feet are shoulder width apart"
    DG.nodes[0]["yogajournalurl"] = ""
    DG.nodes[0]["yogajournal_picture"] = ""
    DG.nodes[0]["hindi_name"] = ""
    DG.nodes[0]["comment"] = ""
    DG.nodes[0]["Dharma Mittra picture URL"] = ""
    DG.nodes[0]["wikipedia"] = ""
    DG.nodes[0]["asanas 608 page"] = ""
    DG.nodes[0]["asanas 608 english name"] = ""

    DG.add_node(1, english_name="cow")
    DG.nodes[1]["two_sided"] = False
    DG.nodes[1]["body areas"] = []
    DG.nodes[1]["description"] = "on all fours, pull chest to floor and head up"
    DG.nodes[1]["yogajournalurl"] = "https://www.yogajournal.com/poses/types/backbends/cow-pose/"
    DG.nodes[1][
        "yogajournal_picture"
    ] = "https://www.yogajournal.com/wp-content/uploads/2007/08/3hp_288_02_bjk2.jpg?crop=535:301&width=1070&enable=upscale"
    DG.nodes[1]["hindi_name"] = "marjaryasana OR Bitilasana"
    DG.nodes[1]["comment"] = ""
    DG.nodes[1][
        "Dharma Mittra picture URL"
    ] = ""
    DG.nodes[1]["wikipedia"] = ""
    DG.nodes[1]["asanas_608_page"] = "373"
    DG.nodes[1]["asanas_608_english"] = "cat stretch pose B"

    DG.add_node(2, english_name="cat")
    DG.nodes[2]["two_sided"] = False
    DG.nodes[2]["body areas"] = []
    DG.nodes[2]["description"] = "on all fours, pull chest to ceiling and head down"
    DG.nodes[2]["yogajournalurl"] = "https://www.yogajournal.com/poses/cat-pose/"
    DG.nodes[2][
        "yogajournal_picture"
    ] = "https://www.yogajournal.com/wp-content/uploads/2007/08/2hp_286_0574_bjk.jpg?crop=535:301&width=1070&enable=upscale"
    DG.nodes[2]["hindi_name"] = "marjaryasana OR Bidalasana"
    DG.nodes[2]["comment"] = ""
    DG.nodes[2][
        "Dharma Mittra picture URL"
    ] = ""
    DG.nodes[2]["wikipedia"] = ""
    DG.nodes[2]["asanas_608_page"] = "372"
    DG.nodes[2]["asanas_608_english"] = "cat stretch pose A"

    DG.add_node(3, english_name="child's pose")
    DG.nodes[3]["two_sided"] = False
    DG.nodes[3]["body areas"] = []
    DG.nodes[3]["description"] = "arms stretched above head, face to ground. On shins"
    DG.nodes[3]["yogajournalurl"] = "https://www.yogajournal.com/poses/child-s-pose/"
    DG.nodes[3][
        "yogajournal_picture"
    ] = "https://www.yogajournal.com/wp-content/uploads/2007/08/3yp_287_6604_gn_bjk.jpg?crop=535:301&width=1070&enable=upscale"
    DG.nodes[3]["hindi_name"] = "Balasana"
    DG.nodes[3]["comment"] = ""
    DG.nodes[3]["Dharma Mittra picture URL"] = ""
    DG.nodes[3]["wikipedia"] = "https://en.wikipedia.org/wiki/Balasana"
    DG.nodes[3]["asanas 608 page"] = ""
    DG.nodes[3]["asanas 608 english name"] = ""

    DG.add_node(4, english_name="downward dog")
    DG.nodes[4]["two_sided"] = False
    DG.nodes[4]["yogajournalurl"] = "http://www.yogajournal.com/poses/491"
    #     DG.nodes[4]["yogajournalurl"]="http://www.yogajournal.com/pose/downward-facing-dog/"
    DG.nodes[4][
        "yogajournal_picture"
    ] = ""
    DG.nodes[4]["hindi_name"] = "Adho Mukha Svanasana"
    DG.nodes[4]["Dharma Mittra picture URL"] = ""
    DG.nodes[4]["body areas"] = []
    DG.nodes[4]["description"] = "feet and hands on floor, both shoulder width apart"
    DG.nodes[4]["wikipedia"] = "https://en.wikipedia.org/wiki/Downward_Dog_Pose"
    DG.nodes[4]["asanas_608_page"] = ""
    DG.nodes[4]["asanas_608_english"] = ""

    DG.add_node(5, english_name="dolphin")
    DG.nodes[5]["two_sided"] = False
    DG.nodes[5]["body areas"] = []
    DG.nodes[5]["description"] = "feet and forearms on floor"
    DG.nodes[5]["yogajournalurl"] = "https://www.yogajournal.com/practice/beginners/how-to/dolphin-pose/"
    DG.nodes[5][
        "yogajournal_picture"
    ] = "https://www.yogajournal.com/wp-content/uploads/2009/03/image-placeholder-title.jpg?width=730"
    DG.nodes[5]["hindi_name"] = ""
    DG.nodes[5]["comment"] = ""
    DG.nodes[5]["Dharma Mittra picture URL"] = ""
    DG.nodes[5]["wikipedia"] = ""
    DG.nodes[5]["asanas 608 page"] = ""
    DG.nodes[5]["asanas 608 english name"] = ""

    DG.add_node(6, english_name="lay on stomach OR crocodile")
    DG.nodes[6]["two_sided"] = False
    DG.nodes[6]["body areas"] = []
    DG.nodes[6]["description"] = "whole body in contact with ground, arms by side"
    DG.nodes[6]["yogajournalurl"] = ""
    DG.nodes[6]["yogajournal_picture"] = ""
    DG.nodes[6]["hindi_name"] = "Makarasana"
    DG.nodes[6]["comment"] = ""
    DG.nodes[6]["Dharma Mittra picture URL"] = ""
    DG.nodes[6]["wikipedia"] = "https://en.wikipedia.org/wiki/Makarasana"
    DG.nodes[6]["asanas 608 page"] = ""
    DG.nodes[6]["asanas 608 english name"] = ""

    DG.add_node(7, english_name="bow")
    DG.nodes[7]["two_sided"] = False
    DG.nodes[7]["body areas"] = []
    DG.nodes[7]["description"] = ""
    DG.nodes[7]["yogajournalurl"] = "https://www.yogajournal.com/poses/types/backbends/bow-pose/"
    DG.nodes[7][
        "yogajournal_picture"
    ] = "https://www.yogajournal.com/wp-content/uploads/2007/08/3enneagram_289_1380_bjk.jpg?crop=535:301&width=1070&enable=upscale"
    DG.nodes[7]["hindi_name"] = "Dhanurasana"
    DG.nodes[7]["comment"] = ""
    DG.nodes[7]["Dharma Mittra picture URL"] = ""
    DG.nodes[7]["wikipedia"] = "https://en.wikipedia.org/wiki/Dhanurasana"
    DG.nodes[7]["asanas 608 page"] = ""
    DG.nodes[7]["asanas 608 english name"] = ""

    DG.add_node(8, english_name="laying on back, one leg extended up")
    DG.nodes[8]["two_sided"] = True
    DG.nodes[8]["body areas"] = []
    DG.nodes[8]["description"] = ""
    DG.nodes[8]["yogajournalurl"] = ""
    DG.nodes[8]["yogajournal_picture"] = ""
    DG.nodes[8]["hindi_name"] = ""
    DG.nodes[8]["comment"] = ""
    DG.nodes[8]["Dharma Mittra picture URL"] = ""
    DG.nodes[8]["wikipedia"] = ""
    DG.nodes[8]["asanas 608 page"] = ""
    DG.nodes[8]["asanas 608 english name"] = ""

    DG.add_node(9, english_name="lying on back, both legs extended up")
    DG.nodes[9]["two_sided"] = False
    DG.nodes[9]["body areas"] = []
    DG.nodes[9]["description"] = ""
    DG.nodes[9]["yogajournalurl"] = ""
    DG.nodes[9]["yogajournal_picture"] = ""
    DG.nodes[9]["hindi_name"] = ""
    DG.nodes[9]["comment"] = ""
    DG.nodes[9]["Dharma Mittra picture URL"] = ""
    DG.nodes[9]["wikipedia"] = ""
    DG.nodes[9]["asanas 608 page"] = ""
    DG.nodes[9]["asanas 608 english name"] = ""

    DG.add_node(10, english_name="supported shoulder stand")
    DG.nodes[10]["two_sided"] = False
    DG.nodes[10]["body areas"] = []
    DG.nodes[10]["description"] = ""
    DG.nodes[10]["yogajournalurl"] = "https://www.yogajournal.com/poses/supported-shoulderstand/"
    DG.nodes[10]["yogajournal_picture"] = "https://www.yogajournal.com/wp-content/uploads/2007/08/2anatomy_284_05_fnl.jpg?crop=535:301&width=1070&enable=upscale"
    DG.nodes[10]["hindi_name"] = "Sarvangasana"
    DG.nodes[10]["comment"] = ""
    DG.nodes[10]["Dharma Mittra picture URL"] = ""
    DG.nodes[10]["wikipedia"] = "https://en.wikipedia.org/wiki/Sarvangasana"
    DG.nodes[10]["asanas_608_page"] = "226"
    DG.nodes[10]["asanas_608_english"] = "Shoulder Stand Pose"

    DG.add_node(11, english_name="plow pose")
    DG.nodes[11]["two_sided"] = False
    DG.nodes[11]["body areas"] = []
    DG.nodes[11]["description"] = ""
    DG.nodes[11]["yogajournalurl"] = "https://www.yogajournal.com/poses/types/inversions/plow-pose/"
    DG.nodes[11][
        "yogajournal_picture"
    ] = "https://www.yogajournal.com/wp-content/uploads/2021/04/plow-pose.jpg?crop=535:301&width=1070&enable=upscale"
    DG.nodes[11]["hindi_name"] = "Halasana"
    DG.nodes[11]["comment"] = ""
    DG.nodes[11]["Dharma Mittra picture URL"] = ""
    DG.nodes[11]["wikipedia"] = "https://en.wikipedia.org/wiki/Halasana"
    DG.nodes[11]["asanas_608_page"] = "249"
    DG.nodes[11]["asanas_608_english"] = "Plough pose (variation)"

    DG.add_node(12, english_name="ear pressure pose")
    DG.nodes[12]["two_sided"] = False
    DG.nodes[12]["body areas"] = []
    DG.nodes[12]["description"] = ""
    DG.nodes[12]["yogajournalurl"] = ""
    DG.nodes[12]["yogajournal_picture"] = ""
    DG.nodes[12]["hindi_name"] = ""
    DG.nodes[12]["comment"] = ""
    DG.nodes[12]["Dharma Mittra picture URL"] = ""
    DG.nodes[12]["wikipedia"] = ""
    DG.nodes[12]["asanas 608 page"] = ""
    DG.nodes[12]["asanas 608 english name"] = ""

    DG.add_node(13, english_name="high plank")
    DG.nodes[13]["two_sided"] = False
    DG.nodes[13]["body areas"] = []
    DG.nodes[13]["description"] = ""
    DG.nodes[13]["yogajournalurl"] = "https://www.yogajournal.com/poses/types/strength/plank-pose/"
    DG.nodes[13][
        "yogajournal_picture"
    ] = "https://www.yogajournal.com/wp-content/uploads/2017/04/3editplankhp2_292_37428_cmyk.jpg?crop=535:301&width=1070&enable=upscale"
    DG.nodes[13]["hindi_name"] = "Kumbhakasana OR Phalakasana"
    DG.nodes[13]["comment"] = ""
    DG.nodes[13][
        "Dharma Mittra picture URL"
    ] = ""
    DG.nodes[13]["asanas 608 page"] = ""
    DG.nodes[13]["asanas 608 english name"] = ""

    DG.add_node(14, english_name="wild thing")
    DG.nodes[14]["two_sided"] = True
    DG.nodes[14]["body areas"] = []
    DG.nodes[14]["description"] = ""
    DG.nodes[14]["yogajournalurl"] = "https://www.yogajournal.com/poses/wild-thing/"
    DG.nodes[14]["yogajournal_picture"] = "https://www.yogajournal.com/wp-content/uploads/2009/08/2yp_283_0205_fnl.jpg?crop=535:301&width=1070&enable=upscale"
    DG.nodes[14]["hindi_name"] = "Camatkarasana"
    DG.nodes[14]["comment"] = ""
    DG.nodes[14]["Dharma Mittra picture URL"] = ""
    DG.nodes[14]["wikipedia"] = ""
    DG.nodes[14]["asanas 608 page"] = ""
    DG.nodes[14]["asanas 608 english name"] = ""

    DG.add_node(15, english_name="low plank")
    DG.nodes[15]["two_sided"] = False
    DG.nodes[15]["hindi_name"] = "chaturanga"
    DG.nodes[15]["body areas"] = []
    DG.nodes[15]["description"] = ""
    DG.nodes[15][
        "yogajournalurl"
    ] = "https://www.yogajournal.com/poses/types/strength/four-limbed-staff-pose/"
    DG.nodes[15][
        "yogajournal_picture"
    ] = "https://www.yogajournal.com/wp-content/uploads/2007/08/edit3chaturangahp2_292_37434_cmyk.jpg?crop=535:301&width=1070&enable=upscale"
    DG.nodes[15]["comment"] = ""
    DG.nodes[15]["Dharma Mittra picture URL"] = ""
    DG.nodes[15]["wikipedia"] = "https://en.wikipedia.org/wiki/Chaturanga_Dandasana"
    DG.nodes[15]["asanas 608 page"] = ""
    DG.nodes[15]["asanas 608 english name"] = ""

    DG.add_node(16, english_name="side plank, straight arm support, straight legs")
    DG.nodes[16]["two_sided"] = True
    DG.nodes[16]["body areas"] = []
    DG.nodes[16]["description"] = ""
    DG.nodes[16]["yogajournalurl"] = "https://www.yogajournal.com/poses/side-plank-pose/"
    DG.nodes[16][
        "yogajournal_picture"
    ] = "https://www.yogajournal.com/wp-content/uploads/2007/08/2hp_271_06_fnl.jpg?crop=535:301&width=1070&enable=upscale"
    DG.nodes[16]["hindi_name"] = "Utthita Vasisthasana"
    DG.nodes[16]["comment"] = ""
    DG.nodes[16]["Dharma Mittra picture URL"] = ""
    DG.nodes[16]["wikipedia"] = "https://en.wikipedia.org/wiki/Utthita_Vasisthasana"
    DG.nodes[16]["asanas 608 page"] = ""
    DG.nodes[16]["asanas 608 english name"] = ""

    DG.add_node(17, english_name="standing bend, legs together")
    DG.nodes[17]["two_sided"] = False
    DG.nodes[17]["body areas"] = []
    DG.nodes[17]["description"] = "legs together, face to knees"
    DG.nodes[17]["yogajournalurl"] = ""
    DG.nodes[17]["yogajournal_picture"] = ""
    DG.nodes[17]["hindi_name"] = ""
    DG.nodes[17]["comment"] = ""
    DG.nodes[17]["Dharma Mittra picture URL"] = ""
    DG.nodes[17]["wikipedia"] = ""
    DG.nodes[17]["asanas 608 page"] = ""
    DG.nodes[17]["asanas 608 english name"] = ""

    DG.add_node(18, english_name="down dog, one leg raised")
    DG.nodes[18]["two_sided"] = True
    DG.nodes[18]["body areas"] = []
    DG.nodes[18]["description"] = ""
    DG.nodes[18][
        "yogajournalurl"
    ] = "http://www.yogajournal.com/article/beginners/one-legged-downward-facing-dog/"
    DG.nodes[18][
        "yogajournal_picture"
    ] = ""
    DG.nodes[18]["hindi_name"] = ""
    DG.nodes[18]["comment"] = ""
    DG.nodes[18]["Dharma Mittra picture URL"] = ""
    DG.nodes[18]["wikipedia"] = ""
    DG.nodes[18]["asanas 608 page"] = ""
    DG.nodes[18]["asanas 608 english name"] = ""

    DG.add_node(19, english_name="flipped dog")
    DG.nodes[19]["two_sided"] = True
    DG.nodes[19]["body areas"] = []
    DG.nodes[19]["description"] = ""
    DG.nodes[19]["yogajournalurl"] = ""
    DG.nodes[19]["yogajournal_picture"] = ""
    DG.nodes[19]["hindi_name"] = ""
    DG.nodes[19]["comment"] = ""
    DG.nodes[19]["Dharma Mittra picture URL"] = ""
    DG.nodes[19]["wikipedia"] = ""
    DG.nodes[19]["asanas 608 page"] = ""
    DG.nodes[19]["asanas 608 english name"] = ""

    DG.add_node(20, english_name="stand straight (mountain)")
    DG.nodes[20]["two_sided"] = False
    DG.nodes[20]["yogajournalurl"] = "http://www.yogajournal.com/poses/492"
    DG.nodes[20][
        "yogajournal_picture"
    ] = ""
    DG.nodes[20]["hindi_name"] = "Tadasana"
    DG.nodes[20]["body areas"] = []
    DG.nodes[20]["description"] = "legs together, hands at side"
    DG.nodes[20]["comment"] = ""
    DG.nodes[20]["Dharma Mittra picture URL"] = ""
    DG.nodes[20]["wikipedia"] = "https://en.wikipedia.org/wiki/Tadasana"
    DG.nodes[20]["asanas 608 page"] = ""
    DG.nodes[20]["asanas 608 english name"] = ""

    DG.add_node(21, english_name="happy camper")
    DG.nodes[21]["two_sided"] = True
    DG.nodes[21]["body areas"] = []
    DG.nodes[21]["description"] = ""
    DG.nodes[21]["yogajournalurl"] = ""
    DG.nodes[21]["yogajournal_picture"] = ""
    DG.nodes[21]["hindi_name"] = ""
    DG.nodes[21]["comment"] = ""
    DG.nodes[21]["Dharma Mittra picture URL"] = ""
    DG.nodes[21]["wikipedia"] = ""
    DG.nodes[21]["asanas 608 page"] = ""
    DG.nodes[21]["asanas 608 english name"] = ""

    DG.add_node(22, english_name="tree pose")
    DG.nodes[22]["two_sided"] = True
    DG.nodes[22]["body areas"] = ["foot balance"]
    DG.nodes[22]["description"] = "arms up and straight, one leg bent with foot to thigh"
    DG.nodes[22]["yogajournalurl"] = "http://www.yogajournal.com/poses/496"
    DG.nodes[22][
        "yogajournal_picture"
    ] = ""
    DG.nodes[22]["hindi_name"] = "Vrksasana"
    DG.nodes[22]["comment"] = ""
    DG.nodes[22]["Dharma Mittra picture URL"] = ""
    DG.nodes[22]["wikipedia"] = "https://en.wikipedia.org/wiki/Vriksasana"
    DG.nodes[22]["asanas 608 page"] = ""
    DG.nodes[22]["asanas 608 english name"] = ""

    DG.add_node(23, english_name="warrior 3")
    DG.nodes[23]["two_sided"] = True
    DG.nodes[23]["body areas"] = []
    DG.nodes[23]["description"] = "bent forward on one leg, arms extended forward"
    DG.nodes[23]["yogajournalurl"] = "http://www.yogajournal.com/poses/941"
    DG.nodes[23]["hindi_name"] = "Virabhadrasana III"
    DG.nodes[23][
        "yogajournal_picture"
    ] = ""
    DG.nodes[23]["comment"] = ""
    DG.nodes[23]["Dharma Mittra picture URL"] = ""
    DG.nodes[23]["wikipedia"] = ""
    DG.nodes[23]["asanas 608 page"] = ""
    DG.nodes[23]["asanas 608 english name"] = ""

    DG.add_node(24, english_name="warrior 1")
    DG.nodes[24]["two_sided"] = True
    DG.nodes[24]["body areas"] = []
    DG.nodes[24]["description"] = "arms up"
    DG.nodes[24]["yogajournalurl"] = "https://www.yogajournal.com/poses/warrior-i-pose/"
    DG.nodes[24]["yogajournal_picture"] = "https://www.yogajournal.com/wp-content/uploads/2017/04/warrior-i-carrie-owerko.jpg?crop=535:301&width=1070&enable=upscale"
    DG.nodes[24]["hindi_name"] = "Virabhadrasana I"
    DG.nodes[24]["comment"] = ""
    DG.nodes[24]["Dharma Mittra picture URL"] = ""
    DG.nodes[24]["wikipedia"] = ""
    DG.nodes[24]["asanas 608 page"] = ""
    DG.nodes[24]["asanas 608 english name"] = ""

    DG.add_node(25, english_name="dancer pose")
    DG.nodes[25]["two_sided"] = True
    DG.nodes[25]["body areas"] = []
    DG.nodes[25]["description"] = ""
    DG.nodes[25]["yogajournalurl"] = ""
    DG.nodes[25]["yogajournal_picture"] = ""
    DG.nodes[25]["hindi_name"] = "Natarajasana"
    DG.nodes[25]["comment"] = ""
    DG.nodes[25]["Dharma Mittra picture URL"] = ""
    DG.nodes[25]["wikipedia"] = "https://en.wikipedia.org/wiki/Natarajasana"
    DG.nodes[25]["asanas 608 page"] = ""
    DG.nodes[25]["asanas 608 english name"] = ""

    DG.add_node(26, english_name="standing splits, inverted")
    DG.nodes[26]["two_sided"] = True
    DG.nodes[26]["body areas"] = ["foot balance"]
    DG.nodes[26]["description"] = ""
    DG.nodes[26]["yogajournalurl"] = ""
    DG.nodes[26]["yogajournal_picture"] = ""
    DG.nodes[26]["hindi_name"] = "Urdhva Prasarita Eka Padasana"
    DG.nodes[26]["comment"] = ""
    DG.nodes[26]["Dharma Mittra picture URL"] = ""
    DG.nodes[26]["wikipedia"] = ""
    DG.nodes[26]["asanas 608 page"] = ""
    DG.nodes[26]["asanas 608 english name"] = ""

    DG.add_node(27, english_name="chair pose")
    DG.nodes[27]["two_sided"] = False
    DG.nodes[27]["body areas"] = []
    DG.nodes[27]["description"] = ""
    DG.nodes[27]["yogajournalurl"] = "http://www.yogajournal.com/poses/493"
    DG.nodes[27][
        "yogajournal_picture"
    ] = ""
    DG.nodes[27]["hindi_name"] = "Utkatasana"
    DG.nodes[27]["comment"] = ""
    DG.nodes[27]["Dharma Mittra picture URL"] = ""
    DG.nodes[27]["wikipedia"] = "https://en.wikipedia.org/wiki/Utkatasana"
    DG.nodes[27]["asanas 608 page"] = ""
    DG.nodes[27]["asanas 608 english name"] = ""

    DG.add_node(28, english_name="wheel")
    DG.nodes[28]["two_sided"] = False
    DG.nodes[28]["body areas"] = []
    DG.nodes[28]["description"] = ""
    DG.nodes[28]["yogajournalurl"] = ""
    DG.nodes[28][
        "yogajournal_picture"
    ] = ""
    DG.nodes[28]["hindi_name"] = "Urdhva Dhanurasana OR Chakrasana"
    DG.nodes[28]["comment"] = ""
    DG.nodes[28][
        "Dharma Mittra picture URL"
    ] = ""
    DG.nodes[28]["wikipedia"] = "https://en.wikipedia.org/wiki/Chakrasana"
    DG.nodes[28]["asanas 608 page"] = ""
    DG.nodes[28]["asanas 608 english name"] = ""

    DG.add_node(29, english_name="warrior 2")
    DG.nodes[29]["two_sided"] = True
    DG.nodes[29]["body areas"] = []
    DG.nodes[29]["description"] = "arms out"
    DG.nodes[29]["yogajournalurl"] = "https://www.yogajournal.com/poses/warrior-ii-pose/"
    DG.nodes[29][
        "yogajournal_picture"
    ] = "https://www.yogajournal.com/wp-content/uploads/2007/08/32hp_291_1870_gn_bjk.jpg?crop=535:301&width=1070&enable=upscale"
    DG.nodes[29]["hindi_name"] = "Virabhadrasana II"
    DG.nodes[29]["comment"] = ""
    DG.nodes[29]["Dharma Mittra picture URL"] = ""
    DG.nodes[29]["wikipedia"] = ""
    DG.nodes[29]["asanas 608 page"] = ""
    DG.nodes[29]["asanas 608 english name"] = ""

    DG.add_node(30, english_name="peaceful warrior")
    DG.nodes[30]["two_sided"] = True
    DG.nodes[30]["body areas"] = []
    DG.nodes[30]["description"] = ""
    DG.nodes[30]["yogajournalurl"] = ""
    DG.nodes[30]["yogajournal_picture"] = ""
    DG.nodes[30]["hindi_name"] = ""
    DG.nodes[30]["comment"] = ""
    DG.nodes[30]["Dharma Mittra picture URL"] = ""
    DG.nodes[30]["wikipedia"] = ""
    DG.nodes[30]["asanas 608 page"] = ""
    DG.nodes[30]["asanas 608 english name"] = ""

    DG.add_node(31, english_name="corpse pose")
    DG.nodes[31]["two_sided"] = False
    DG.nodes[31]["body areas"] = []
    DG.nodes[31]["description"] = "laying on back"
    DG.nodes[31]["yogajournalurl"] = "https://www.yogajournal.com/practice/beginners/corpse-pose/"
    DG.nodes[31][
        "yogajournal_picture"
    ] = ""
    DG.nodes[31]["hindi_name"] = "Shavasana"
    DG.nodes[31]["comment"] = ""
    DG.nodes[31]["Dharma Mittra picture URL"] = ""
    DG.nodes[31]["wikipedia"] = "https://en.wikipedia.org/wiki/Shavasana"
    DG.nodes[31]["asanas 608 page"] = ""
    DG.nodes[31]["asanas 608 english name"] = ""

    DG.add_node(32, english_name="happy baby, rock side to side")
    DG.nodes[32]["two_sided"] = False
    DG.nodes[32]["body areas"] = []
    DG.nodes[32]["description"] = "on back, feet up"
    DG.nodes[32]["yogajournalurl"] = "http://www.yogajournal.com/poses/2497"
    DG.nodes[32][
        "yogajournal_picture"
    ] = ""
    DG.nodes[32]["hindi_name"] = ""
    DG.nodes[32]["comment"] = ""
    DG.nodes[32]["Dharma Mittra picture URL"] = ""
    DG.nodes[32]["wikipedia"] = ""
    DG.nodes[32]["asanas 608 page"] = ""
    DG.nodes[32]["asanas 608 english name"] = ""

    DG.add_node(33, english_name="on back, knees bent, feet on ground")
    DG.nodes[33]["two_sided"] = False
    DG.nodes[33]["body areas"] = []
    DG.nodes[33]["description"] = ""
    DG.nodes[33]["yogajournalurl"] = ""
    DG.nodes[33]["yogajournal_picture"] = ""
    DG.nodes[33]["hindi_name"] = ""
    DG.nodes[33]["comment"] = ""
    DG.nodes[33]["Dharma Mittra picture URL"] = ""
    DG.nodes[33]["wikipedia"] = ""
    DG.nodes[33]["asanas 608 page"] = ""
    DG.nodes[33]["asanas 608 english name"] = ""

    DG.add_node(34, english_name="on back, knees bent, feet in air")
    DG.nodes[34]["two_sided"] = False
    DG.nodes[34]["body areas"] = []
    DG.nodes[34]["description"] = ""
    DG.nodes[34]["yogajournalurl"] = ""
    DG.nodes[34]["yogajournal_picture"] = ""
    DG.nodes[34]["hindi_name"] = ""
    DG.nodes[34]["comment"] = ""
    DG.nodes[34]["Dharma Mittra picture URL"] = ""
    DG.nodes[34]["wikipedia"] = ""
    DG.nodes[34]["asanas 608 page"] = ""
    DG.nodes[34]["asanas 608 english name"] = ""

    DG.add_node(35, english_name="knees to one side, head to other")
    DG.nodes[35]["two_sided"] = True
    DG.nodes[35]["body areas"] = []
    DG.nodes[35]["description"] = ""
    DG.nodes[35]["yogajournalurl"] = ""
    DG.nodes[35]["yogajournal_picture"] = ""
    DG.nodes[35]["hindi_name"] = ""
    DG.nodes[35]["comment"] = ""
    DG.nodes[35]["Dharma Mittra picture URL"] = ""
    DG.nodes[35]["wikipedia"] = ""
    DG.nodes[35]["asanas 608 page"] = ""
    DG.nodes[35]["asanas 608 english name"] = ""

    DG.add_node(36, english_name="seated forward fold with straight legs")
    DG.nodes[36]["two_sided"] = False
    DG.nodes[36]["body areas"] = []
    DG.nodes[36]["description"] = ""
    DG.nodes[36]["yogajournalurl"] = ""
    DG.nodes[36]["yogajournal_picture"] = ""
    DG.nodes[36]["hindi_name"] = "paschimatanasana"
    DG.nodes[36]["comment"] = ""
    DG.nodes[36]["Dharma Mittra picture URL"] = ""
    DG.nodes[36]["wikipedia"] = ""
    DG.nodes[36]["asanas_608_page"] = "279"
    DG.nodes[36]["asanas_608_english"] = "back stretch pose"

    DG.add_node(37, english_name="pigeon pose")
    DG.nodes[37]["two_sided"] = True
    DG.nodes[37]["body areas"] = []
    DG.nodes[37]["description"] = ""
    DG.nodes[37]["yogajournalurl"] = ""
    DG.nodes[37]["yogajournal_picture"] = ""
    DG.nodes[37]["hindi_name"] = ""
    DG.nodes[37]["comment"] = ""
    DG.nodes[37]["Dharma Mittra picture URL"] = ""
    DG.nodes[37]["wikipedia"] = ""
    DG.nodes[37]["asanas_608_page"] = "278"
    DG.nodes[37]["asanas_608_english"] = "back stretch pose (preparation)"

    DG.add_node(38, english_name="one leg straight, one leg in")
    DG.nodes[38]["two_sided"] = True
    DG.nodes[38]["body areas"] = []
    DG.nodes[38]["description"] = ""
    DG.nodes[38]["yogajournalurl"] = ""
    DG.nodes[38]["yogajournal_picture"] = ""
    DG.nodes[38]["hindi_name"] = ""
    DG.nodes[38]["comment"] = ""
    DG.nodes[38]["Dharma Mittra picture URL"] = ""
    DG.nodes[38]["wikipedia"] = ""
    DG.nodes[38]["asanas_608_page"] = "278"
    DG.nodes[38]["asanas_608_english"] = "back stretch pose (preparation)"

    DG.add_node(39, english_name="compass pose")
    DG.nodes[39]["two_sided"] = True
    DG.nodes[39]["body areas"] = []
    DG.nodes[39]["description"] = ""
    DG.nodes[39]["yogajournalurl"] = ""
    DG.nodes[39]["yogajournal_picture"] = ""
    DG.nodes[39]["hindi_name"] = ""
    DG.nodes[39]["comment"] = ""
    DG.nodes[39]["Dharma Mittra picture URL"] = ""
    DG.nodes[39]["wikipedia"] = ""
    DG.nodes[39]["asanas_608_page"] = "278"
    DG.nodes[39]["asanas_608_english"] = "back stretch pose (preparation)"

    DG.add_node(40, english_name="rock bent leg")
    DG.nodes[40]["two_sided"] = True
    DG.nodes[40]["body areas"] = []
    DG.nodes[40]["description"] = ""
    DG.nodes[40]["yogajournalurl"] = ""
    DG.nodes[40]["yogajournal_picture"] = ""
    DG.nodes[40]["hindi_name"] = ""
    DG.nodes[40]["comment"] = ""
    DG.nodes[40]["Dharma Mittra picture URL"] = ""
    DG.nodes[40]["wikipedia"] = ""
    DG.nodes[40]["asanas 608 page"] = ""
    DG.nodes[40]["asanas 608 english name"] = ""

    DG.add_node(41, english_name="kneeling on shins OR thunderbolt OR Diamond")
    DG.nodes[41]["two_sided"] = False
    DG.nodes[41]["body areas"] = []
    DG.nodes[41]["description"] = ""
    DG.nodes[41]["yogajournalurl"] = ""
    DG.nodes[41]["yogajournal_picture"] = ""
    DG.nodes[41]["hindi_name"] = "Vajrasana"
    DG.nodes[41]["comment"] = ""
    DG.nodes[41]["Dharma Mittra picture URL"] = ""
    DG.nodes[41]["wikipedia"] = "https://en.wikipedia.org/wiki/Vajrasana_(yoga)"
    DG.nodes[41]["asanas 608 page"] = ""
    DG.nodes[41]["asanas 608 english name"] = ""

    DG.add_node(42, english_name="standing on shins")
    DG.nodes[42]["two_sided"] = False
    DG.nodes[42]["body areas"] = []
    DG.nodes[42]["description"] = ""
    DG.nodes[42]["yogajournalurl"] = ""
    DG.nodes[42]["yogajournal_picture"] = ""
    DG.nodes[42]["hindi_name"] = ""
    DG.nodes[42]["comment"] = ""
    DG.nodes[42]["Dharma Mittra picture URL"] = ""
    DG.nodes[42]["wikipedia"] = ""
    DG.nodes[42]["asanas 608 page"] = ""
    DG.nodes[42]["asanas 608 english name"] = ""

    DG.add_node(43, english_name="camel pose")
    DG.nodes[43]["two_sided"] = False
    DG.nodes[43]["body areas"] = []
    DG.nodes[43]["description"] = ""
    DG.nodes[43]["yogajournalurl"] = "http://www.yogajournal.com/poses/types/backbends/camel-pose/"
    DG.nodes[43][
        "yogajournal_picture"
    ] = "https://www.yogajournal.com/wp-content/uploads/2007/08/ccd03730.jpg?crop=535:301&width=1070&enable=upscale"
    DG.nodes[43]["hindi_name"] = ""
    DG.nodes[43]["comment"] = ""
    DG.nodes[43]["Dharma Mittra picture URL"] = ""
    DG.nodes[43]["wikipedia"] = "https://en.wikipedia.org/wiki/Ustrasana"
    DG.nodes[43]["asanas 608 page"] = ""
    DG.nodes[43]["asanas 608 english name"] = ""

    DG.add_node(44, english_name="crow")
    DG.nodes[44]["two_sided"] = False
    DG.nodes[44]["body areas"] = []
    DG.nodes[44]["description"] = ""
    DG.nodes[44]["yogajournalurl"] = ""
    DG.nodes[44][
        "yogajournal_picture"
    ] = ""
    DG.nodes[44]["hindi_name"] = "Kakasana"
    DG.nodes[44]["comment"] = ""
    DG.nodes[44]["Dharma Mittra picture URL"] = ""
    DG.nodes[44]["wikipedia"] = ""
    DG.nodes[44]["asanas 608 page"] = ""
    DG.nodes[44]["asanas 608 english name"] = ""

    DG.add_node(45, english_name="squat, knees wide OR garland")
    DG.nodes[45]["two_sided"] = False
    DG.nodes[45]["body areas"] = []
    DG.nodes[45]["description"] = ""
    DG.nodes[45]["yogajournalurl"] = "https://www.yogajournal.com/poses/types/standing/garland-pose/"
    DG.nodes[45]["yogajournal_picture"] = ""
    DG.nodes[45]["hindi_name"] = "Upavesasana"
    DG.nodes[45]["comment"] = ""
    DG.nodes[45]["Dharma Mittra picture URL"] = ""
    DG.nodes[45]["wikipedia"] = ""
    DG.nodes[45]["asanas 608 page"] = ""
    DG.nodes[45]["asanas 608 english name"] = ""

    DG.add_node(46, english_name="standing, legs apart")
    DG.nodes[46]["two_sided"] = False
    DG.nodes[46]["body areas"] = []
    DG.nodes[46]["description"] = ""
    DG.nodes[46]["yogajournalurl"] = ""
    DG.nodes[46]["yogajournal_picture"] = ""
    DG.nodes[46]["hindi_name"] = ""
    DG.nodes[46]["comment"] = ""
    DG.nodes[46]["Dharma Mittra picture URL"] = ""
    DG.nodes[46]["wikipedia"] = ""
    DG.nodes[46]["asanas 608 page"] = ""
    DG.nodes[46]["asanas 608 english name"] = ""

    DG.add_node(47, english_name="upward dog")
    DG.nodes[47]["two_sided"] = False
    DG.nodes[47]["body areas"] = []
    DG.nodes[47]["description"] = ""
    DG.nodes[47]["yogajournalurl"] = ""
    DG.nodes[47][
        "yogajournal_picture"
    ] = ""
    DG.nodes[47]["hindi_name"] = "Urdhva Mukha Shvanasana"
    DG.nodes[47]["comment"] = ""
    DG.nodes[47][
        "Dharma Mittra picture URL"
    ] = ""
    DG.nodes[47]["wikipedia"] = "https://en.wikipedia.org/wiki/Urdhva_Mukha_Shvanasana"
    DG.nodes[47]["asanas 608 page"] = ""
    DG.nodes[47]["asanas 608 english name"] = ""

    DG.add_node(48, english_name="seated with one leg straight forward one knee bent on ground")
    DG.nodes[48]["two_sided"] = True
    DG.nodes[48]["body areas"] = []
    DG.nodes[48]["description"] = ""
    DG.nodes[48]["yogajournalurl"] = ""
    DG.nodes[48]["yogajournal_picture"] = ""
    DG.nodes[48]["hindi_name"] = "Janusirsasana"
    DG.nodes[48]["comment"] = ""
    DG.nodes[48]["Dharma Mittra picture URL"] = ""
    DG.nodes[48]["wikipedia"] = "https://en.wikipedia.org/wiki/Janusirsasana"
    DG.nodes[48]["asanas 608 page"] = ""
    DG.nodes[48]["asanas 608 english name"] = ""

    DG.add_node(49, english_name="half lotus OR accomplished")
    DG.nodes[49]["two_sided"] = True
    DG.nodes[49]["body areas"] = []
    DG.nodes[49]["description"] = ""
    DG.nodes[49]["yogajournalurl"] = "https://www.yogajournal.com/poses/fire-log-pose/"
    DG.nodes[49][
        "yogajournal_picture"
    ] = "https://www.yogajournal.com/wp-content/uploads/2007/08/fire-log-pose-agnistambhasana.jpg?crop=535:301&width=1070&enable=upscale"
    DG.nodes[49]["hindi_name"] = "siddhasana"
    DG.nodes[49]["comment"] = ""
    DG.nodes[49][
        "Dharma Mittra picture URL"
    ] = ""
    DG.nodes[49]["wikipedia"] = "https://en.wikipedia.org/wiki/Siddhasana"
    DG.nodes[49]["asanas_608_page"] = "624"
    DG.nodes[49]["asanas_608_english"] = "accomplished pose"

    DG.add_node(50, english_name="seated full lotus")
    DG.nodes[50]["two_sided"] = True
    DG.nodes[50]["body areas"] = []
    DG.nodes[50]["description"] = ""
    DG.nodes[50]["yogajournalurl"] = "https://www.yogajournal.com/poses/types/seated-twists/lotus-pose/"
    DG.nodes[50][
        "yogajournal_picture"
    ] = "https://www.yogajournal.com/wp-content/uploads/2007/08/ccd04508.jpg?crop=535:301&width=1070&enable=upscale"
    DG.nodes[50]["hindi_name"] = "padmasana"
    DG.nodes[50]["comment"] = ""
    DG.nodes[50]["Dharma Mittra picture URL"] = ""
    DG.nodes[50]["wikipedia"] = "https://en.wikipedia.org/wiki/Lotus_position"
    DG.nodes[50]["asanas_608_page"] = "626"
    DG.nodes[50]["asanas_608_english"] = "lotus pose"

    DG.add_node(51, english_name="embryo pose")
    DG.nodes[51]["two_sided"] = True
    DG.nodes[51]["body areas"] = []
    DG.nodes[51]["description"] = ""
    DG.nodes[51]["yogajournalurl"] = ""
    DG.nodes[51]["yogajournal_picture"] = ""
    DG.nodes[51]["hindi_name"] = ""
    DG.nodes[51]["comment"] = ""
    DG.nodes[51]["Dharma Mittra picture URL"] = ""
    DG.nodes[51]["wikipedia"] = ""
    DG.nodes[51]["asanas_608_page"] = "243"
    DG.nodes[51]["asanas_608_english"] = "upward lotus pose"

    DG.add_node(52, english_name="flying lotus OR Lotus peacock")
    DG.nodes[52]["two_sided"] = True
    DG.nodes[52]["body areas"] = []
    DG.nodes[52]["description"] = "only hands on ground"
    DG.nodes[52]["yogajournalurl"] = ""
    DG.nodes[52]["yogajournal_picture"] = ""
    DG.nodes[52]["hindi_name"] = "Padma Mayurasana"
    DG.nodes[52]["comment"] = ""
    DG.nodes[52]["Dharma Mittra picture URL"] = ""
    DG.nodes[52]["wikipedia"] = ""
    DG.nodes[52]["asanas 608 page"] = ""
    DG.nodes[52]["asanas 608 english name"] = ""

    DG.add_node(53, english_name="floating staff pose")
    DG.nodes[53]["two_sided"] = False
    DG.nodes[53]["body areas"] = []
    DG.nodes[53]["description"] = ""
    DG.nodes[53]["yogajournalurl"] = ""
    DG.nodes[53]["yogajournal_picture"] = ""
    DG.nodes[53]["hindi_name"] = ""
    DG.nodes[53]["comment"] = ""
    DG.nodes[53]["Dharma Mittra picture URL"] = ""
    DG.nodes[53]["wikipedia"] = ""
    DG.nodes[53]["asanas 608 page"] = ""
    DG.nodes[53]["asanas 608 english name"] = ""

    DG.add_node(54, english_name="crane")
    DG.nodes[54]["two_sided"] = False
    DG.nodes[54]["body areas"] = []
    DG.nodes[54]["description"] = ""
    DG.nodes[54]["yogajournalurl"] = "https://www.yogajournal.com/poses/types/crane-pose/"
    DG.nodes[54]["yogajournal_picture"] = "https://www.yogajournal.com/wp-content/uploads/2007/08/editcrowhp_292_9_bjk.jpg?crop=535:301&width=1070&enable=upscale"
    DG.nodes[54]["hindi_name"] = "Bakasana"
    DG.nodes[54]["comment"] = ""
    DG.nodes[54]["Dharma Mittra picture URL"] = ""
    DG.nodes[54]["wikipedia"] = "https://en.wikipedia.org/wiki/Bakasana"
    DG.nodes[54]["asanas 608 page"] = ""
    DG.nodes[54]["asanas 608 english name"] = ""

    DG.add_node(55, english_name="one-legged crane")
    DG.nodes[55]["two_sided"] = True
    DG.nodes[55]["body areas"] = []
    DG.nodes[55]["description"] = ""
    DG.nodes[55]["yogajournalurl"] = ""
    DG.nodes[55]["yogajournal_picture"] = ""
    DG.nodes[55]["hindi_name"] = ""
    DG.nodes[55]["comment"] = ""
    DG.nodes[55]["Dharma Mittra picture URL"] = ""
    DG.nodes[55]["wikipedia"] = ""
    DG.nodes[55]["asanas 608 page"] = ""
    DG.nodes[55]["asanas 608 english name"] = ""

    DG.add_node(56, english_name="standing wide legs, feet parallel, torso upright")
    DG.nodes[56]["two_sided"] = False
    DG.nodes[56]["body areas"] = []
    DG.nodes[56]["description"] = ""
    DG.nodes[56]["yogajournalurl"] = ""
    DG.nodes[56]["yogajournal_picture"] = ""
    DG.nodes[56]["hindi_name"] = ""
    DG.nodes[56]["comment"] = ""
    DG.nodes[56]["Dharma Mittra picture URL"] = ""
    DG.nodes[56]["wikipedia"] = ""
    DG.nodes[56]["asanas 608 page"] = ""
    DG.nodes[56]["asanas 608 english name"] = ""

    DG.add_node(57, english_name="standing wide legs, torso bent over, parallel feet")
    DG.nodes[57]["two_sided"] = False
    DG.nodes[57]["body areas"] = []
    DG.nodes[57]["description"] = ""
    DG.nodes[57]["yogajournalurl"] = "https://www.yogajournal.com/poses/wide-legged-forward-bend/"
    DG.nodes[57]["yogajournal_picture"] = "https://www.yogajournal.com/wp-content/uploads/2007/08/3hp_289_6573_bjk.jpg?crop=535:301&width=1070&enable=upscale"
    DG.nodes[57]["hindi_name"] = "Prasarita Padottanasana I"
    DG.nodes[57]["comment"] = ""
    DG.nodes[57]["Dharma Mittra picture URL"] = ""
    DG.nodes[57]["wikipedia"] = "https://en.wikipedia.org/wiki/Prasarita_Padottanasana"
    DG.nodes[57]["asanas 608 page"] = ""
    DG.nodes[57]["asanas 608 english name"] = ""

    DG.add_node(
        58, english_name="tripod head stand, legs extended straight up, arms at 90deg"
    )
    DG.nodes[58]["two_sided"] = False
    DG.nodes[58]["body areas"] = []
    DG.nodes[58]["description"] = "arms at 90deg"
    DG.nodes[58]["yogajournalurl"] = ""
    DG.nodes[58]["yogajournal_picture"] = ""
    DG.nodes[58]["hindi_name"] = "Salamba-Shirshasana"
    DG.nodes[58]["comment"] = ""
    DG.nodes[58]["Dharma Mittra picture URL"] = ""
    DG.nodes[58]["wikipedia"] = ""
    DG.nodes[58]["asanas_608_page"] = "181"
    DG.nodes[58]["asanas_608_english"] = "Supported Head Stand Pose"

    DG.add_node(59, english_name="arms to side")
    DG.nodes[59]["two_sided"] = True
    DG.nodes[59]["body areas"] = []
    DG.nodes[59]["description"] = ""
    DG.nodes[59]["yogajournalurl"] = ""
    DG.nodes[59]["yogajournal_picture"] = ""
    DG.nodes[59]["hindi_name"] = ""
    DG.nodes[59]["comment"] = ""
    DG.nodes[59]["Dharma Mittra picture URL"] = ""
    DG.nodes[59]["wikipedia"] = ""
    DG.nodes[59]["asanas 608 page"] = ""
    DG.nodes[59]["asanas 608 english name"] = ""

    DG.add_node(
        60,
        english_name="both legs straight, front foot point forward, back foot flat at 45deg",
    )
    DG.nodes[60]["two_sided"] = True
    DG.nodes[60]["body areas"] = []
    DG.nodes[60]["description"] = ""
    DG.nodes[60]["yogajournalurl"] = ""
    DG.nodes[60]["yogajournal_picture"] = ""
    DG.nodes[60]["hindi_name"] = ""
    DG.nodes[60]["comment"] = ""
    DG.nodes[60]["Dharma Mittra picture URL"] = ""
    DG.nodes[60]["wikipedia"] = ""
    DG.nodes[60]["asanas 608 page"] = ""
    DG.nodes[60]["asanas 608 english name"] = ""

    DG.add_node(61, english_name="standing hinged forward at hips")
    DG.nodes[61]["two_sided"] = True
    DG.nodes[61]["body areas"] = []
    DG.nodes[61]["description"] = ""
    DG.nodes[61]["yogajournalurl"] = ""
    DG.nodes[61]["yogajournal_picture"] = ""
    DG.nodes[61]["hindi_name"] = ""
    DG.nodes[61]["comment"] = ""
    DG.nodes[61][
        "Dharma Mittra picture URL"
    ] = ""
    DG.nodes[61]["asanas 608 page"] = ""
    DG.nodes[61]["asanas 608 english name"] = ""

    DG.add_node(62, english_name="revolved triangle pose")
    DG.nodes[62]["hindi_name"] = "Parivrtta Trikonasana"
    DG.nodes[62]["two_sided"] = True
    DG.nodes[62]["body areas"] = []
    DG.nodes[62]["description"] = ""
    DG.nodes[62]["yogajournalurl"] = "https://www.yogajournal.com/poses/revolved-triangle-pose-2/"
    DG.nodes[62]["yogajournal_picture"] = "https://www.yogajournal.com/wp-content/uploads/2007/08/revolved-triangle-pose.jpg?crop=535:301&width=1070&enable=upscale"
    DG.nodes[62]["comment"] = ""
    DG.nodes[62]["Dharma Mittra picture URL"] = ""
    DG.nodes[62]["wikipedia"] = ""
    DG.nodes[62]["asanas 608 page"] = ""
    DG.nodes[62]["asanas 608 english name"] = ""

    DG.add_node(63, english_name="extended side angle pose")
    DG.nodes[63]["two_sided"] = True
    DG.nodes[63]["yogajournalurl"] = "https://www.yogajournal.com/poses/extended-side-angle-pose-2/"
    DG.nodes[63][
        "yogajournal_picture"
    ] = "https://www.yogajournal.com/wp-content/uploads/2007/08/2hp_291_1875_gn_bjk.jpg?crop=535:301&width=1070&enable=upscale"
    DG.nodes[63]["hindi_name"] = "Utthita Parsvakonasana"
    DG.nodes[63]["comment"] = ""
    DG.nodes[63]["Dharma Mittra picture URL"] = ""
    DG.nodes[63]["wikipedia"] = "https://en.wikipedia.org/wiki/Utthita_Parsvakonasana"
    DG.nodes[63]["body areas"] = []
    DG.nodes[63]["description"] = ""
    DG.nodes[63]["asanas_608_page"] = ""
    DG.nodes[63]["asanas_608_english"] = ""

    DG.add_node(64, english_name="bind")
    DG.nodes[64]["two_sided"] = True
    DG.nodes[64]["body areas"] = []
    DG.nodes[64]["description"] = ""
    DG.nodes[64]["yogajournalurl"] = ""
    DG.nodes[64]["yogajournal_picture"] = ""
    DG.nodes[64]["hindi_name"] = ""
    DG.nodes[64]["comment"] = ""
    DG.nodes[64]["Dharma Mittra picture URL"] = ""
    DG.nodes[64]["wikipedia"] = ""
    DG.nodes[64]["asanas 608 page"] = ""
    DG.nodes[64]["asanas 608 english name"] = ""

    DG.add_node(65, english_name="bird of paradise")
    DG.nodes[65]["two_sided"] = True
    DG.nodes[65]["body areas"] = []
    DG.nodes[65]["description"] = ""
    DG.nodes[65]["yogajournalurl"] = ""
    DG.nodes[65]["yogajournal_picture"] = ""
    DG.nodes[65]["hindi_name"] = ""
    DG.nodes[65]["comment"] = ""
    DG.nodes[65]["Dharma Mittra picture URL"] = ""
    DG.nodes[65]["wikipedia"] = ""
    DG.nodes[65]["asanas 608 page"] = ""
    DG.nodes[65]["asanas 608 english name"] = ""

    DG.add_node(66, english_name="funky bird of paradise")
    DG.nodes[66]["two_sided"] = True
    DG.nodes[66]["body areas"] = []
    DG.nodes[66]["description"] = ""
    DG.nodes[66]["yogajournalurl"] = ""
    DG.nodes[66]["yogajournal_picture"] = ""
    DG.nodes[66]["hindi_name"] = ""
    DG.nodes[66]["comment"] = ""
    DG.nodes[66]["Dharma Mittra picture URL"] = ""
    DG.nodes[66]["wikipedia"] = ""
    DG.nodes[66]["asanas 608 page"] = ""
    DG.nodes[66]["asanas 608 english name"] = ""

    DG.add_node(67, english_name="standing bend bound twist")
    DG.nodes[67]["two_sided"] = True
    DG.nodes[67]["body areas"] = []
    DG.nodes[67]["description"] = ""
    DG.nodes[67]["yogajournalurl"] = ""
    DG.nodes[67]["yogajournal_picture"] = ""
    DG.nodes[67]["hindi_name"] = ""
    DG.nodes[67]["comment"] = ""
    DG.nodes[67]["Dharma Mittra picture URL"] = ""
    DG.nodes[67]["wikipedia"] = ""
    DG.nodes[67]["asanas 608 page"] = ""
    DG.nodes[67]["asanas 608 english name"] = ""

    DG.add_node(68, english_name="standing bend, legs apart")
    DG.nodes[68]["two_sided"] = False
    DG.nodes[68]["body areas"] = []
    DG.nodes[68]["description"] = ""
    DG.nodes[68]["yogajournalurl"] = ""
    DG.nodes[68]["yogajournal_picture"] = ""
    DG.nodes[68]["hindi_name"] = ""
    DG.nodes[68]["comment"] = ""
    DG.nodes[68]["Dharma Mittra picture URL"] = ""
    DG.nodes[68]["wikipedia"] = ""
    DG.nodes[68]["asanas 608 page"] = ""
    DG.nodes[68]["asanas 608 english name"] = ""

    DG.add_node(69, english_name="tripod head stand, legs bent, arms at 90deg")
    DG.nodes[69]["two_sided"] = False
    DG.nodes[69]["body areas"] = []
    DG.nodes[69]["description"] = "arms at 90deg"
    DG.nodes[69]["yogajournalurl"] = ""
    DG.nodes[69]["yogajournal_picture"] = ""
    DG.nodes[69]["hindi_name"] = ""
    DG.nodes[69]["comment"] = ""
    DG.nodes[69]["Dharma Mittra picture URL"] = ""
    DG.nodes[69]["wikipedia"] = ""
    DG.nodes[69]["asanas 608 page"] = ""
    DG.nodes[69]["asanas 608 english name"] = ""

    DG.add_node(70, english_name="floating elephant trunk; one leg over arm")
    DG.nodes[70]["two_sided"] = True
    DG.nodes[70]["body areas"] = []
    DG.nodes[70]["description"] = ""
    DG.nodes[70]["yogajournalurl"] = ""
    DG.nodes[70]["yogajournal_picture"] = ""
    DG.nodes[70]["hindi_name"] = ""
    DG.nodes[70]["comment"] = ""
    DG.nodes[70]["Dharma Mittra picture URL"] = ""
    DG.nodes[70]["wikipedia"] = ""
    DG.nodes[70]["asanas 608 page"] = ""
    DG.nodes[70]["asanas 608 english name"] = ""

    DG.add_node(71, english_name="eight angle pose")
    DG.nodes[71]["two_sided"] = True
    DG.nodes[71]["body areas"] = []
    DG.nodes[71]["description"] = ""
    DG.nodes[71]["yogajournalurl"] = ""
    DG.nodes[71]["yogajournal_picture"] = ""
    DG.nodes[71]["hindi_name"] = ""
    DG.nodes[71]["comment"] = ""
    DG.nodes[71]["Dharma Mittra picture URL"] = ""
    DG.nodes[71]["wikipedia"] = ""
    DG.nodes[71]["asanas 608 page"] = ""
    DG.nodes[71]["asanas 608 english name"] = ""

    DG.add_node(72, english_name="flying pigeon, leg extended")
    DG.nodes[72]["two_sided"] = True
    DG.nodes[72]["body areas"] = []
    DG.nodes[72]["description"] = "hand balance; shin or knee on back triceps"
    DG.nodes[72]["yogajournalurl"] = ""
    DG.nodes[72]["yogajournal_picture"] = ""
    DG.nodes[72]["hindi_name"] = ""
    DG.nodes[72]["comment"] = ""
    DG.nodes[72]["Dharma Mittra picture URL"] = ""
    DG.nodes[72]["wikipedia"] = ""
    DG.nodes[72]["asanas 608 page"] = ""
    DG.nodes[72]["asanas 608 english name"] = ""

    DG.add_node(73, english_name="peddle feet")
    DG.nodes[73]["two_sided"] = True
    DG.nodes[73]["body areas"] = []
    DG.nodes[73]["description"] = ""
    DG.nodes[73]["yogajournalurl"] = ""
    DG.nodes[73]["yogajournal_picture"] = ""
    DG.nodes[73]["hindi_name"] = ""
    DG.nodes[73]["comment"] = ""
    DG.nodes[73]["Dharma Mittra picture URL"] = ""
    DG.nodes[73]["wikipedia"] = ""
    DG.nodes[73]["asanas 608 page"] = ""
    DG.nodes[73]["asanas 608 english name"] = ""

    DG.add_node(74, english_name="tripod head stand, legs extended out, arms at 90deg")
    DG.nodes[74]["two_sided"] = False
    DG.nodes[74]["body areas"] = []
    DG.nodes[74]["description"] = "arms at 90deg"
    DG.nodes[74]["yogajournalurl"] = ""
    DG.nodes[74]["yogajournal_picture"] = ""
    DG.nodes[74]["hindi_name"] = ""
    DG.nodes[74]["comment"] = ""
    DG.nodes[74]["Dharma Mittra picture URL"] = ""
    DG.nodes[74]["wikipedia"] = ""
    DG.nodes[74]["asanas 608 page"] = ""
    DG.nodes[74]["asanas 608 english name"] = ""

    DG.add_node(75, english_name="no-handed head stand")
    DG.nodes[75]["two_sided"] = False
    DG.nodes[75]["body areas"] = []
    DG.nodes[75]["description"] = ""
    DG.nodes[75]["yogajournalurl"] = ""
    DG.nodes[75]["yogajournal_picture"] = ""
    DG.nodes[75]["hindi_name"] = ""
    DG.nodes[75]["comment"] = ""
    DG.nodes[75]["Dharma Mittra picture URL"] = ""
    DG.nodes[75]["wikipedia"] = ""
    DG.nodes[75]["asanas 608 page"] = ""
    DG.nodes[75]["asanas 608 english name"] = ""

    DG.add_node(76, english_name="inverted tripod")
    DG.nodes[76]["two_sided"] = False
    DG.nodes[76]["body areas"] = []
    DG.nodes[76]["description"] = ""
    DG.nodes[76]["yogajournalurl"] = ""
    DG.nodes[76]["yogajournal_picture"] = ""
    DG.nodes[76]["hindi_name"] = "Niralamba-Shirshasana"
    DG.nodes[76]["comment"] = ""
    DG.nodes[76]["Dharma Mittra picture URL"] = ""
    DG.nodes[76]["wikipedia"] = ""
    DG.nodes[76]["asanas_608_page"] = "197"
    DG.nodes[76]["asanas_608_english"] = "Hands-free Head Stand Pose (Variation)"

    DG.add_node(77, english_name="seated wide-leg, back perpendicular to floor")
    DG.nodes[77]["two_sided"] = False
    DG.nodes[77]["body areas"] = []
    DG.nodes[77]["description"] = ""
    DG.nodes[77]["yogajournalurl"] = ""
    DG.nodes[77]["yogajournal_picture"] = ""
    DG.nodes[77]["hindi_name"] = ""
    DG.nodes[77]["comment"] = ""
    DG.nodes[77]["Dharma Mittra picture URL"] = ""
    DG.nodes[77]["wikipedia"] = ""
    DG.nodes[77]["asanas 608 page"] = ""
    DG.nodes[77]["asanas 608 english name"] = ""

    DG.add_node(78, english_name="seated wide-leg, floating")
    DG.nodes[78]["two_sided"] = False
    DG.nodes[78]["body areas"] = []
    DG.nodes[78]["description"] = "only hands are in contact with floor"
    DG.nodes[78]["yogajournalurl"] = ""
    DG.nodes[78]["yogajournal_picture"] = ""
    DG.nodes[78]["hindi_name"] = ""
    DG.nodes[78]["comment"] = ""
    DG.nodes[78]["Dharma Mittra picture URL"] = ""
    DG.nodes[78]["wikipedia"] = ""
    DG.nodes[78]["asanas 608 page"] = ""
    DG.nodes[78]["asanas 608 english name"] = ""

    DG.add_node(79, english_name="seated wide-leg, flying")
    DG.nodes[79]["two_sided"] = False
    DG.nodes[79]["body areas"] = []
    DG.nodes[79]["description"] = ""
    DG.nodes[79]["yogajournalurl"] = ""
    DG.nodes[79]["yogajournal_picture"] = ""
    DG.nodes[79]["hindi_name"] = ""
    DG.nodes[79]["comment"] = ""
    DG.nodes[79]["Dharma Mittra picture URL"] = ""
    DG.nodes[79]["wikipedia"] = ""
    DG.nodes[79]["asanas 608 page"] = ""
    DG.nodes[79]["asanas 608 english name"] = ""

    DG.add_node(80, english_name="all fours, one arm extended")
    DG.nodes[80]["two_sided"] = True
    DG.nodes[80]["body areas"] = []
    DG.nodes[80]["description"] = ""
    DG.nodes[80]["yogajournalurl"] = ""
    DG.nodes[80]["yogajournal_picture"] = ""
    DG.nodes[80]["hindi_name"] = ""
    DG.nodes[80]["comment"] = ""
    DG.nodes[80]["Dharma Mittra picture URL"] = ""
    DG.nodes[80]["wikipedia"] = ""
    DG.nodes[80]["asanas 608 page"] = ""
    DG.nodes[80]["asanas 608 english name"] = ""

    DG.add_node(81, english_name="all fours, one leg extended")
    DG.nodes[81]["two_sided"] = True
    DG.nodes[81]["body areas"] = []
    DG.nodes[81]["description"] = ""
    DG.nodes[81]["yogajournalurl"] = ""
    DG.nodes[81]["yogajournal_picture"] = ""
    DG.nodes[81]["hindi_name"] = ""
    DG.nodes[81]["comment"] = ""
    DG.nodes[81]["Dharma Mittra picture URL"] = ""
    DG.nodes[81]["wikipedia"] = ""
    DG.nodes[81]["asanas 608 page"] = ""
    DG.nodes[81]["asanas 608 english name"] = ""

    DG.add_node(82, english_name="all fours, one arm extended, oppposite leg extended")
    DG.nodes[82]["two_sided"] = True
    DG.nodes[82]["body areas"] = []
    DG.nodes[82]["description"] = ""
    DG.nodes[82]["yogajournalurl"] = ""
    DG.nodes[82]["yogajournal_picture"] = ""
    DG.nodes[82]["hindi_name"] = ""
    DG.nodes[82]["comment"] = ""
    DG.nodes[82]["Dharma Mittra picture URL"] = ""
    DG.nodes[82]["wikipedia"] = ""
    DG.nodes[82]["asanas 608 page"] = ""
    DG.nodes[82]["asanas 608 english name"] = ""

    DG.add_node(83, english_name="all fours, one arm extended, same side leg extended")
    DG.nodes[83]["two_sided"] = True
    DG.nodes[83]["body areas"] = []
    DG.nodes[83]["description"] = ""
    DG.nodes[83]["yogajournalurl"] = ""
    DG.nodes[83]["yogajournal_picture"] = ""
    DG.nodes[83]["hindi_name"] = ""
    DG.nodes[83]["comment"] = ""
    DG.nodes[83]["Dharma Mittra picture URL"] = ""
    DG.nodes[83]["wikipedia"] = ""
    DG.nodes[83]["asanas 608 page"] = ""
    DG.nodes[83]["asanas 608 english name"] = ""

    DG.add_node(84, english_name="all fours, hips to one side")
    DG.nodes[84]["two_sided"] = True
    DG.nodes[84]["body areas"] = []
    DG.nodes[84]["description"] = ""
    DG.nodes[84]["yogajournalurl"] = ""
    DG.nodes[84]["yogajournal_picture"] = ""
    DG.nodes[84]["hindi_name"] = ""
    DG.nodes[84]["comment"] = ""
    DG.nodes[84]["Dharma Mittra picture URL"] = ""
    DG.nodes[84]["wikipedia"] = ""
    DG.nodes[84]["asanas 608 page"] = ""
    DG.nodes[84]["asanas 608 english name"] = ""

    DG.add_node(85, english_name="forearm plank")
    DG.nodes[85]["two_sided"] = False
    DG.nodes[85]["body areas"] = []
    DG.nodes[85]["description"] = ""
    DG.nodes[85]["yogajournalurl"] = ""
    DG.nodes[85]["yogajournal_picture"] = ""
    DG.nodes[85]["hindi_name"] = ""
    DG.nodes[85]["comment"] = ""
    DG.nodes[85]["Dharma Mittra picture URL"] = ""
    DG.nodes[85]["wikipedia"] = ""
    DG.nodes[85]["asanas 608 page"] = ""
    DG.nodes[85]["asanas 608 english name"] = ""

    DG.add_node(86, english_name="tripod head stand, legs bent, arms straight")
    DG.nodes[86]["two_sided"] = False
    DG.nodes[86]["body areas"] = []
    DG.nodes[86]["description"] = ""
    DG.nodes[86]["yogajournalurl"] = ""
    DG.nodes[86]["yogajournal_picture"] = ""
    DG.nodes[86]["hindi_name"] = ""
    DG.nodes[86]["comment"] = ""
    DG.nodes[86]["Dharma Mittra picture URL"] = ""
    DG.nodes[86]["wikipedia"] = ""
    DG.nodes[86]["asanas 608 page"] = ""
    DG.nodes[86]["asanas 608 english name"] = ""

    DG.add_node(87, english_name="standing back bend")
    DG.nodes[87]["two_sided"] = False
    DG.nodes[87]["body areas"] = []
    DG.nodes[87]["description"] = "feet together"
    DG.nodes[87]["yogajournalurl"] = ""
    DG.nodes[87]["yogajournal_picture"] = ""
    DG.nodes[87]["hindi_name"] = ""
    DG.nodes[87]["comment"] = ""
    DG.nodes[87]["Dharma Mittra picture URL"] = ""
    DG.nodes[87]["wikipedia"] = ""
    DG.nodes[87]["asanas 608 page"] = ""
    DG.nodes[87]["asanas 608 english name"] = ""

    DG.add_node(88, english_name="scorpion")
    DG.nodes[88]["two_sided"] = False
    DG.nodes[88]["body areas"] = []
    DG.nodes[88]["description"] = ""
    DG.nodes[88]["yogajournalurl"] = ""
    DG.nodes[88]["yogajournal_picture"] = ""
    DG.nodes[88]["hindi_name"] = "Vrischikasana"
    DG.nodes[88]["comment"] = ""
    DG.nodes[88]["Dharma Mittra picture URL"] = ""
    DG.nodes[88]["wikipedia"] = "https://en.wikipedia.org/wiki/Vrischikasana"
    DG.nodes[88]["asanas 608 page"] = ""
    DG.nodes[88]["asanas 608 english name"] = ""

    DG.add_node(89, english_name="bird of paradise, bent forward, leg to side")
    DG.nodes[89]["two_sided"] = False
    DG.nodes[89]["body areas"] = []
    DG.nodes[89]["description"] = ""
    DG.nodes[89]["yogajournalurl"] = ""
    DG.nodes[89]["yogajournal_picture"] = ""
    DG.nodes[89]["hindi_name"] = ""
    DG.nodes[89]["comment"] = ""
    DG.nodes[89]["Dharma Mittra picture URL"] = ""
    DG.nodes[89]["wikipedia"] = ""
    DG.nodes[89]["asanas 608 page"] = ""
    DG.nodes[89]["asanas 608 english name"] = ""

    DG.add_node(90, english_name="tripod head stand, legs straight, arms straight")
    DG.nodes[90]["two_sided"] = False
    DG.nodes[90]["body areas"] = []
    DG.nodes[90]["description"] = ""
    DG.nodes[90]["yogajournalurl"] = ""
    DG.nodes[90]["yogajournal_picture"] = ""
    DG.nodes[90]["hindi_name"] = ""
    DG.nodes[90]["comment"] = ""
    DG.nodes[90]["Dharma Mittra picture URL"] = ""
    DG.nodes[90]["wikipedia"] = ""
    DG.nodes[90]["asanas 608 page"] = ""
    DG.nodes[90]["asanas 608 english name"] = ""

    DG.add_node(91, english_name="butterfly OR cobbler")
    DG.nodes[91]["two_sided"] = False
    DG.nodes[91]["body areas"] = []
    DG.nodes[91]["description"] = ""
    DG.nodes[91]["yogajournalurl"] = "https://www.yogajournal.com/poses/types/seated-twists/bound-angle-pose-2/"
    DG.nodes[91]["yogajournal_picture"] = "https://www.yogajournal.com/wp-content/uploads/2007/08/bound-angle-pose-baddha-konasana.jpg?crop=535:301&width=1070&enable=upscale"
    DG.nodes[91]["hindi_name"] = "Baddha Konasana"
    DG.nodes[91]["comment"] = ""
    DG.nodes[91]["Dharma Mittra picture URL"] = ""
    DG.nodes[91]["wikipedia"] = "https://en.wikipedia.org/wiki/Baddha_Konasana"
    DG.nodes[91]["asanas 608 page"] = ""
    DG.nodes[91]["asanas 608 english name"] = ""

    DG.add_node(92, english_name="hurdler")
    DG.nodes[92]["two_sided"] = False
    DG.nodes[92]["body areas"] = []
    DG.nodes[92]["description"] = ""
    DG.nodes[92]["yogajournalurl"] = ""
    DG.nodes[92]["yogajournal_picture"] = ""
    DG.nodes[92]["hindi_name"] = ""
    DG.nodes[92]["comment"] = ""
    DG.nodes[92]["Dharma Mittra picture URL"] = ""
    DG.nodes[92]["wikipedia"] = ""
    DG.nodes[92]["asanas 608 page"] = ""
    DG.nodes[92]["asanas 608 english name"] = ""

    DG.add_node(93, english_name="bridge")
    DG.nodes[93]["two_sided"] = False
    DG.nodes[93]["body areas"] = []
    DG.nodes[93]["description"] = ""
    DG.nodes[93]["yogajournalurl"] = "https://www.yogajournal.com/poses/bridge-pose/"
    DG.nodes[93][
        "yogajournal_picture"
    ] = "https://www.yogajournal.com/wp-content/uploads/2007/08/bridge-pose-giselle-mari.jpg?crop=535:301&width=1070&enable=upscale"
    DG.nodes[93]["hindi_name"] = "Sethu Bandha Sarvangasana"
    DG.nodes[93]["comment"] = ""
    DG.nodes[93]["Dharma Mittra picture URL"] = ""
    DG.nodes[93]["wikipedia"] = "https://en.wikipedia.org/wiki/Setu_Bandha_Sarvangasana"
    DG.nodes[93]["asanas 608 page"] = ""
    DG.nodes[93]["asanas 608 english name"] = ""

    DG.add_node(94, english_name="standing eagle")
    DG.nodes[94]["two_sided"] = False
    DG.nodes[94]["body areas"] = []
    DG.nodes[94]["description"] = ""
    DG.nodes[94]["yogajournalurl"] = "http://www.yogajournal.com/poses/eagle-pose/"
    DG.nodes[94][
        "yogajournal_picture"
    ] = "https://www.yogajournal.com/wp-content/uploads/2007/08/eaglehp2_292_37370_cmyk.jpg?crop=535:301&width=1070&enable=upscale"
    DG.nodes[94]["hindi_name"] = "Garudasana"
    DG.nodes[94]["comment"] = ""
    DG.nodes[94]["Dharma Mittra picture URL"] = ""
    DG.nodes[94]["wikipedia"] = "https://en.wikipedia.org/wiki/Garudasana"
    DG.nodes[94]["asanas 608 page"] = ""
    DG.nodes[94]["asanas 608 english name"] = ""

    DG.add_node(95, english_name="seated forward fold")
    DG.nodes[95]["two_sided"] = False
    DG.nodes[95]["body areas"] = []
    DG.nodes[95]["description"] = ""
    DG.nodes[95][
        "yogajournalurl"
    ] = "https://www.yogajournal.com/poses/seated-forward-bend/"
    DG.nodes[95][
        "yogajournal_picture"
    ] = "https://www.yogajournal.com/wp-content/uploads/2007/08/promoforwardfoldhp2_292_37503_cmyk.jpg?crop=535:301&width=1070&enable=upscale"
    DG.nodes[95]["hindi_name"] = "Paschimottanasana"
    DG.nodes[95]["comment"] = ""
    DG.nodes[95]["Dharma Mittra picture URL"] = ""
    DG.nodes[95]["wikipedia"] = "https://en.wikipedia.org/wiki/Paschimottanasana"
    DG.nodes[95]["asanas 608 page"] = ""
    DG.nodes[95]["asanas 608 english name"] = ""

    DG.add_node(96,english_name="extended puppy pose")
    DG.nodes[96]["two_sided"]=False
    DG.nodes[96]["body areas"] = []
    DG.nodes[96]["description"]=""
    DG.nodes[96]["yogajournalurl"]="https://www.yogajournal.com/poses/extended-puppy-pose/"
    DG.nodes[96]["yogajournal_picture"]="https://www.yogajournal.com/wp-content/uploads/2007/08/3yp_287_6641_gn_bjk.jpg"
    DG.nodes[96]["hindi_name"]=""
    DG.nodes[96]["counter asana"] = None
    DG.nodes[96]["comment"]=""
    DG.nodes[96]["Dharma Mittra picture URL"]=""
    DG.nodes[96]["asanas 608 page"]=""
    DG.nodes[96]["asanas 608 english name"]=""

    DG.add_node(97,english_name="boat")
    DG.nodes[97]["two_sided"]=False
    DG.nodes[97]["body areas"] = []
    DG.nodes[97]["description"]=""
    DG.nodes[97]["yogajournalurl"]="https://www.yogajournal.com/poses/types/core/full-boat-pose-2/"
    DG.nodes[97]["yogajournal_picture"]="https://www.yogajournal.com/wp-content/uploads/2007/08/editedboathp_292_8_bjk.jpg?crop=535:301&width=1070&enable=upscale"
    DG.nodes[97]["hindi_name"]="Navasana"
    DG.nodes[97]["counter asana"] = None
    DG.nodes[97]["comment"]=""
    DG.nodes[97]["Dharma Mittra picture URL"]=""
    DG.nodes[97]["wikipedia"] = "https://en.wikipedia.org/wiki/Navasana"
    DG.nodes[97]["asanas 608 page"]=""
    DG.nodes[97]["asanas 608 english name"]=""

    DG.add_node(98,english_name="standing forward fold")
    DG.nodes[98]["two_sided"]=False
    DG.nodes[98]["body areas"] = []
    DG.nodes[98]["description"]=""
    DG.nodes[98]["yogajournalurl"]="https://www.yogajournal.com/poses/big-toe-pose/"
    DG.nodes[98]["yogajournal_picture"]="https://www.yogajournal.com/wp-content/uploads/2007/08/big-toe-pose.jpg?crop=535:301&width=1070&enable=upscale"
    DG.nodes[98]["hindi_name"]="Uttanasana"
    DG.nodes[98]["counter asana"] = None
    DG.nodes[98]["comment"]=""
    DG.nodes[98]["Dharma Mittra picture URL"]=""
    DG.nodes[98]["wikipedia"] = "https://en.wikipedia.org/wiki/Uttanasana"
    DG.nodes[98]["asanas 608 page"]=""
    DG.nodes[98]["asanas 608 english name"]=""

    DG.add_node(99,english_name="standing forward fold with straight back")
    DG.nodes[99]["two_sided"]=False
    DG.nodes[99]["body areas"] = []
    DG.nodes[99]["description"]=""
    DG.nodes[99]["yogajournalurl"]="https://www.yogajournal.com/poses/standing-half-forward-bend/"
    DG.nodes[99]["yogajournal_picture"]="https://www.yogajournal.com/wp-content/uploads/2008/02/2hp_281_0176_bjk.jpg?crop=535:301&width=1070&enable=upscale"
    DG.nodes[99]["hindi_name"]=""
    DG.nodes[99]["counter asana"] = None
    DG.nodes[99]["comment"]=""
    DG.nodes[99]["Dharma Mittra picture URL"]=""
    DG.nodes[99]["asanas 608 page"]=""
    DG.nodes[99]["asanas 608 english name"]=""

    DG.add_node(100,english_name="forearm wheel")
    DG.nodes[100]["two_sided"]=False
    DG.nodes[100]["body areas"] = []
    DG.nodes[100]["description"]=""
    DG.nodes[100]["yogajournalurl"]=""
    DG.nodes[100]["yogajournal_picture"]=""
    DG.nodes[100]["hindi_name"]=""
    DG.nodes[100]["counter asana"] = None
    DG.nodes[100]["comment"]=""
    DG.nodes[100]["Dharma Mittra picture URL"]=""
    DG.nodes[100]["asanas 608 page"]=""
    DG.nodes[100]["asanas 608 english name"]=""

    DG.add_node(101,english_name="handstand, legs straight")
    DG.nodes[101]["two_sided"]=False
    DG.nodes[101]["body areas"] = []
    DG.nodes[101]["description"]=""
    DG.nodes[101]["yogajournalurl"]="https://www.yogajournal.com/poses/types/handstand/"
    DG.nodes[101]["yogajournal_picture"]="https://www.yogajournal.com/wp-content/uploads/2007/08/201506-yjmag-handstand-final.jpg?crop=535:301&width=1070&enable=upscale"
    DG.nodes[101]["hindi_name"]="Adho Mukha Vrikshasana"
    DG.nodes[101]["counter asana"] = None
    DG.nodes[101]["comment"]=""
    DG.nodes[101]["Dharma Mittra picture URL"]=""
    DG.nodes[101]["wikipedia"] = "https://en.wikipedia.org/wiki/Handstand"
    DG.nodes[101]["asanas 608 page"]=""
    DG.nodes[101]["asanas 608 english name"]=""

    DG.add_node(102,english_name="extended triangle")
    DG.nodes[102]["two_sided"]=True
    DG.nodes[102]["body areas"] = []
    DG.nodes[102]["description"]=""
    DG.nodes[102]["yogajournalurl"]="https://www.yogajournal.com/poses/extended-triangle-pose/"
    DG.nodes[102]["yogajournal_picture"]="https://www.yogajournal.com/wp-content/uploads/2007/08/2yp_285_1643_prf.jpg?crop=535:301&width=1070&enable=upscale"
    DG.nodes[102]["hindi_name"]="Trikonasana"
    DG.nodes[102]["counter asana"] = None
    DG.nodes[102]["comment"]=""
    DG.nodes[102]["Dharma Mittra picture URL"]=""
    DG.nodes[102]["wikipedia"] = "https://en.wikipedia.org/wiki/Trikonasana"
    DG.nodes[102]["asanas 608 page"]=""
    DG.nodes[102]["asanas 608 english name"]=""

    DG.add_node(103,english_name="half moon")
    DG.nodes[103]["two_sided"]=True
    DG.nodes[103]["body areas"] = []
    DG.nodes[103]["description"]=""
    DG.nodes[103]["yogajournalurl"]="https://www.yogajournal.com/poses/types/balancing/half-moon-pose-3/"
    DG.nodes[103]["yogajournal_picture"]="https://www.yogajournal.com/wp-content/uploads/2007/08/2hp_291_1860_gn_bjk.jpg?crop=535:301&width=1070&enable=upscale"
    DG.nodes[103]["hindi_name"]="Ardha chandrasana"
    DG.nodes[103]["counter asana"] = None
    DG.nodes[103]["comment"]=""
    DG.nodes[103]["Dharma Mittra picture URL"]=""
    DG.nodes[103]["wikipedia"] = "https://en.wikipedia.org/wiki/Ardha_chandrasana"
    DG.nodes[103]["asanas 608 page"]=""
    DG.nodes[103]["asanas 608 english name"]=""

    DG.add_node(104,english_name="Standing Big Toe Hold")
    DG.nodes[104]["two_sided"]=True
    DG.nodes[104]["body areas"] = []
    DG.nodes[104]["description"]=""
    DG.nodes[104]["yogajournalurl"]="https://www.yogajournal.com/poses/extended-hand-to-big-toe-pose/"
    DG.nodes[104]["yogajournal_picture"]="https://www.yogajournal.com/wp-content/uploads/2007/08/2yp_285_1542_prf.jpg?crop=535:301&width=1070&enable=upscale"
    DG.nodes[104]["hindi_name"]="Utthita Padangusthasana"
    DG.nodes[104]["counter asana"] = None
    DG.nodes[104]["comment"]=""
    DG.nodes[104]["Dharma Mittra picture URL"]=""
    DG.nodes[104]["wikipedia"] = "https://en.wikipedia.org/wiki/Utthita_Padangusthasana"
    DG.nodes[104]["asanas 608 page"]=""
    DG.nodes[104]["asanas 608 english name"]=""

    DG.add_node(105,english_name="Crescent Moon OR low lunge")
    DG.nodes[105]["two_sided"]=False
    DG.nodes[105]["body areas"] = []
    DG.nodes[105]["description"]=""
    DG.nodes[105]["yogajournalurl"]="https://www.yogajournal.com/poses/types/standing/low-lunge/"
    DG.nodes[105]["yogajournal_picture"]="https://www.yogajournal.com/wp-content/uploads/2008/05/3yp_287_6671_gn_bjk.jpg?crop=535:301&width=1070&enable=upscale"
    DG.nodes[105]["hindi_name"]=""
    DG.nodes[105]["counter asana"] = None
    DG.nodes[105]["comment"]=""
    DG.nodes[105]["Dharma Mittra picture URL"]=""
    DG.nodes[105]["wikipedia"] = "https://en.wikipedia.org/wiki/Anjaneyasana"
    DG.nodes[105]["asanas 608 page"]=""
    DG.nodes[105]["asanas 608 english name"]=""

    DG.add_node(106,english_name="tiger")
    DG.nodes[106]["two_sided"]=True
    DG.nodes[106]["body areas"] = []
    DG.nodes[106]["description"]="one leg is stretched out straight, and the knee of the stretched out leg may then be bent so the foot points straight up; the opposite hand may also be stretched out"
    DG.nodes[106]["yogajournalurl"]=""
    DG.nodes[106]["yogajournal_picture"]=""
    DG.nodes[106]["hindi_name"]=""
    DG.nodes[106]["counter asana"] = None
    DG.nodes[106]["comment"]=""
    DG.nodes[106]["Dharma Mittra picture URL"]=""
    DG.nodes[106]["wikipedia"] = ""
    DG.nodes[106]["asanas 608 page"]=""
    DG.nodes[106]["asanas 608 english name"]=""

    DG.add_node(107,english_name="cobra")
    DG.nodes[107]["two_sided"]=False
    DG.nodes[107]["body areas"] = []
    DG.nodes[107]["description"]=""
    DG.nodes[107]["yogajournalurl"]=""
    DG.nodes[107]["yogajournal_picture"]=""
    DG.nodes[107]["hindi_name"]="Bhujangasana"
    DG.nodes[107]["counter asana"] = None
    DG.nodes[107]["comment"]=""
    DG.nodes[107]["Dharma Mittra picture URL"]=""
    DG.nodes[107]["wikipedia"] = "https://en.wikipedia.org/wiki/Bhujangasana"
    DG.nodes[107]["asanas 608 page"]=""
    DG.nodes[107]["asanas 608 english name"]=""

    DG.add_node(108,english_name="One legged wheel")
    DG.nodes[108]["two_sided"]=True
    DG.nodes[108]["body areas"] = []
    DG.nodes[108]["description"]=""
    DG.nodes[108]["yogajournalurl"]=""
    DG.nodes[108]["yogajournal_picture"]=""
    DG.nodes[108]["hindi_name"]="Eka Pada Urdhva Dhanurasana"
    DG.nodes[108]["counter asana"] = None
    DG.nodes[108]["comment"]=""
    DG.nodes[108]["Dharma Mittra picture URL"]=""
    DG.nodes[108]["wikipedia"] = ""
    DG.nodes[108]["asanas 608 page"]=""
    DG.nodes[108]["asanas 608 english name"]=""

    DG.add_node(109,english_name="Inverted Staff")
    DG.nodes[109]["two_sided"]=False
    DG.nodes[109]["body areas"] = []
    DG.nodes[109]["description"]=""
    DG.nodes[109]["yogajournalurl"]=""
    DG.nodes[109]["yogajournal_picture"]=""
    DG.nodes[109]["hindi_name"]=""
    DG.nodes[109]["counter asana"] = None
    DG.nodes[109]["comment"]=""
    DG.nodes[109]["Dharma Mittra picture URL"]=""
    DG.nodes[109]["wikipedia"] = "https://en.wikipedia.org/wiki/Viparita_Dandasana"
    DG.nodes[109]["asanas 608 page"]=""
    DG.nodes[109]["asanas 608 english name"]=""

    DG.add_node(110,english_name="seated One-legged King Pigeon")
    DG.nodes[110]["two_sided"]=False
    DG.nodes[110]["body areas"] = []
    DG.nodes[110]["description"]=""
    DG.nodes[110]["yogajournalurl"]="https://www.yogajournal.com/poses/one-legged-king-pigeon-pose/"
    DG.nodes[110]["yogajournal_picture"]="https://www.yogajournal.com/wp-content/uploads/2007/08/king-pigeon.jpg?crop=535:301&width=1070&enable=upscale"
    DG.nodes[110]["hindi_name"]=""
    DG.nodes[110]["counter asana"] = None
    DG.nodes[110]["comment"]=""
    DG.nodes[110]["Dharma Mittra picture URL"]=""
    DG.nodes[110]["wikipedia"] = "https://en.wikipedia.org/wiki/Eka_Pada_Rajakapotasana"
    DG.nodes[110]["asanas 608 page"]=""
    DG.nodes[110]["asanas 608 english name"]=""

    DG.add_node(111,english_name="Eight-Angle Pose")
    DG.nodes[111]["two_sided"]=False
    DG.nodes[111]["body areas"] = []
    DG.nodes[111]["description"]=""
    DG.nodes[111]["yogajournalurl"]=""
    DG.nodes[111]["yogajournal_picture"]=""
    DG.nodes[111]["hindi_name"]="Astavakrasana"
    DG.nodes[111]["counter asana"] = None
    DG.nodes[111]["comment"]=""
    DG.nodes[111]["Dharma Mittra picture URL"]=""
    DG.nodes[111]["wikipedia"] = "https://en.wikipedia.org/wiki/Astavakrasana"
    DG.nodes[111]["asanas 608 page"]=""
    DG.nodes[111]["asanas 608 english name"]=""

    DG.add_node(112,english_name="cow face")
    DG.nodes[112]["two_sided"]=False
    DG.nodes[112]["body areas"] = []
    DG.nodes[112]["description"]=""
    DG.nodes[112]["yogajournalurl"]="https://www.yogajournal.com/poses/cow-face-pose/"
    DG.nodes[112]["yogajournal_picture"]="https://www.yogajournal.com/wp-content/uploads/2007/08/gomukhasana.jpg?crop=535:301&width=1070&enable=upscale"
    DG.nodes[112]["hindi_name"]="Gomukhasana"
    DG.nodes[112]["counter asana"] = None
    DG.nodes[112]["comment"]=""
    DG.nodes[112]["Dharma Mittra picture URL"]=""
    DG.nodes[112]["wikipedia"] = "https://en.wikipedia.org/wiki/Gomukhasana"
    DG.nodes[112]["asanas 608 page"]=""
    DG.nodes[112]["asanas 608 english name"]=""

    DG.add_node(113,english_name="rooster")
    DG.nodes[113]["two_sided"]=False
    DG.nodes[113]["body areas"] = []
    DG.nodes[113]["description"]=""
    DG.nodes[113]["yogajournalurl"]=""
    DG.nodes[113]["yogajournal_picture"]=""
    DG.nodes[113]["hindi_name"]="Kukkutasana"
    DG.nodes[113]["counter asana"] = None
    DG.nodes[113]["comment"]=""
    DG.nodes[113]["Dharma Mittra picture URL"]=""
    DG.nodes[113]["wikipedia"] = "https://en.wikipedia.org/wiki/Kukkutasana"
    DG.nodes[113]["asanas 608 page"]=""
    DG.nodes[113]["asanas 608 english name"]=""

    DG.add_node(114,english_name="fish")
    DG.nodes[114]["two_sided"]=False
    DG.nodes[114]["body areas"] = []
    DG.nodes[114]["description"]="https://www.yogajournal.com/poses/types/backbends/fish-pose/"
    DG.nodes[114]["yogajournalurl"]="https://www.yogajournal.com/wp-content/uploads/2007/08/32enneagram_289_1419_bjk.jpg?crop=535:301&width=1070&enable=upscale"
    DG.nodes[114]["yogajournal_picture"]=""
    DG.nodes[114]["hindi_name"]="Matsyasana"
    DG.nodes[114]["counter asana"] = 10
    DG.nodes[114]["comment"]=""
    DG.nodes[114]["Dharma Mittra picture URL"]=""
    DG.nodes[114]["wikipedia"] = "https://en.wikipedia.org/wiki/Matsyasana"
    DG.nodes[114]["asanas 608 page"]=""
    DG.nodes[114]["asanas 608 english name"]=""

    DG.add_node(115,english_name="Shoulder pressing posture")
    DG.nodes[115]["two_sided"]=False
    DG.nodes[115]["body areas"] = []
    DG.nodes[115]["description"]=""
    DG.nodes[115]["yogajournalurl"]=""
    DG.nodes[115]["yogajournal_picture"]=""
    DG.nodes[115]["hindi_name"]=""
    DG.nodes[115]["counter asana"] = None
    DG.nodes[115]["comment"]=""
    DG.nodes[115]["Dharma Mittra picture URL"]=""
    DG.nodes[115]["wikipedia"] = "https://en.wikipedia.org/wiki/Bhujapidasana"
    DG.nodes[115]["asanas 608 page"]=""
    DG.nodes[115]["asanas 608 english name"]=""

    DG.add_node(116,english_name="Embryo in Womb Pose")
    DG.nodes[116]["two_sided"]=True
    DG.nodes[116]["body areas"] = []
    DG.nodes[116]["description"]=""
    DG.nodes[116]["yogajournalurl"]=""
    DG.nodes[116]["yogajournal_picture"]=""
    DG.nodes[116]["hindi_name"]="Garbha Pindasana"
    DG.nodes[116]["counter asana"] = None
    DG.nodes[116]["comment"]=""
    DG.nodes[116]["Dharma Mittra picture URL"]=""
    DG.nodes[116]["wikipedia"] = "https://en.wikipedia.org/wiki/Garbha_Pindasana"
    DG.nodes[116]["asanas 608 page"]=""
    DG.nodes[116]["asanas 608 english name"]=""

    DG.add_node(117,english_name="Eka Pada Koundinyasana I")
    DG.nodes[117]["two_sided"]=True
    DG.nodes[117]["body areas"] = []
    DG.nodes[117]["description"]="lower leg on arm"
    DG.nodes[117]["yogajournalurl"]="https://www.yogajournal.com/poses/pose-dedicated-to-the-sage-koundinya-i/"
    DG.nodes[117]["yogajournal_picture"]="https://www.yogajournal.com/wp-content/uploads/2007/08/nov-14-yogapedia-eka-pada-koundinyasana-1.jpg?crop=535:301&width=1070&enable=upscale"
    DG.nodes[117]["hindi_name"]="Eka Pada Koundinyasana I"
    DG.nodes[117]["counter asana"] = None
    DG.nodes[117]["comment"]=""
    DG.nodes[117]["Dharma Mittra picture URL"]=""
    DG.nodes[117]["wikipedia"] = ""
    DG.nodes[117]["asanas 608 page"]=""
    DG.nodes[117]["asanas 608 english name"]=""

    DG.add_node(118,english_name="Eka Pada Koundinyasana II")
    DG.nodes[118]["two_sided"]=True
    DG.nodes[118]["body areas"] = []
    DG.nodes[118]["description"]="upper leg on arm"
    DG.nodes[118]["yogajournalurl"]=""
    DG.nodes[118]["yogajournal_picture"]=""
    DG.nodes[118]["hindi_name"]="Eka Pada Koundinyasana II"
    DG.nodes[118]["counter asana"] = None
    DG.nodes[118]["comment"]=""
    DG.nodes[118]["Dharma Mittra picture URL"]=""
    DG.nodes[118]["wikipedia"] = ""
    DG.nodes[118]["asanas 608 page"]=""
    DG.nodes[118]["asanas 608 english name"]=""

    DG.add_node(119,english_name="Eka Pada Galavasana")
    DG.nodes[119]["two_sided"]=False
    DG.nodes[119]["body areas"] = []
    DG.nodes[119]["description"]="foot hooked over elbow"
    DG.nodes[119]["yogajournalurl"]=""
    DG.nodes[119]["yogajournal_picture"]=""
    DG.nodes[119]["hindi_name"]="Eka Pada Galavasana"
    DG.nodes[119]["counter asana"] = None
    DG.nodes[119]["comment"]=""
    DG.nodes[119]["Dharma Mittra picture URL"]=""
    DG.nodes[119]["wikipedia"] = ""
    DG.nodes[119]["asanas 608 page"]=""
    DG.nodes[119]["asanas 608 english name"]=""

    DG.add_node(120,english_name="peacock")
    DG.nodes[120]["two_sided"]=False
    DG.nodes[120]["body areas"] = []
    DG.nodes[120]["description"]="body is straight. Hands on floor"
    DG.nodes[120]["yogajournalurl"]=""
    DG.nodes[120]["yogajournal_picture"]=""
    DG.nodes[120]["hindi_name"]="Mayurasana"
    DG.nodes[120]["counter asana"] = None
    DG.nodes[120]["comment"]=""
    DG.nodes[120]["Dharma Mittra picture URL"]=""
    DG.nodes[120]["wikipedia"] = "https://en.wikipedia.org/wiki/Mayurasana"
    DG.nodes[120]["asanas 608 page"]=""
    DG.nodes[120]["asanas 608 english name"]=""

    DG.add_node(121,english_name="firefly")
    DG.nodes[121]["two_sided"]=False
    DG.nodes[121]["body areas"] = []
    DG.nodes[121]["description"]=""
    DG.nodes[121]["yogajournalurl"]=""
    DG.nodes[121]["yogajournal_picture"]=""
    DG.nodes[121]["hindi_name"]="Tittibhasana"
    DG.nodes[121]["counter asana"] = None
    DG.nodes[121]["comment"]=""
    DG.nodes[121]["Dharma Mittra picture URL"]=""
    DG.nodes[121]["wikipedia"] = "https://en.wikipedia.org/wiki/Tittibhasana"
    DG.nodes[121]["asanas 608 page"]=""
    DG.nodes[121]["asanas 608 english name"]=""

    DG.add_node(122,english_name="Raised Lotus pose")
    DG.nodes[122]["two_sided"]=False
    DG.nodes[122]["body areas"] = []
    DG.nodes[122]["description"]=""
    DG.nodes[122]["yogajournalurl"]="https://www.yogajournal.com/poses/scale-pose/"
    DG.nodes[122]["yogajournal_picture"]="https://www.yogajournal.com/wp-content/uploads/2007/08/scale-pose.jpg?crop=535:301&width=1070&enable=upscale"
    DG.nodes[122]["hindi_name"]="Tolasana"
    DG.nodes[122]["counter asana"] = None
    DG.nodes[122]["comment"]=""
    DG.nodes[122]["Dharma Mittra picture URL"]=""
    DG.nodes[122]["wikipedia"] = "https://en.wikipedia.org/wiki/Tulasana"
    DG.nodes[122]["asanas 608 page"]=""
    DG.nodes[122]["asanas 608 english name"]=""

    DG.add_node(123,english_name="one arm handstand, legs straight")
    DG.nodes[123]["two_sided"]=False
    DG.nodes[123]["body areas"] = []
    DG.nodes[123]["description"]=""
    DG.nodes[123]["yogajournalurl"]=""
    DG.nodes[123]["yogajournal_picture"]=""
    DG.nodes[123]["hindi_name"]=""
    DG.nodes[123]["counter asana"] = None
    DG.nodes[123]["comment"]=""
    DG.nodes[123]["Dharma Mittra picture URL"]=""
    DG.nodes[123]["wikipedia"] = ""
    DG.nodes[123]["asanas 608 page"]=""
    DG.nodes[123]["asanas 608 english name"]=""

    DG.add_node(124,english_name="forearm headstand, legs straight up")
    DG.nodes[124]["two_sided"]=False
    DG.nodes[124]["body areas"] = []
    DG.nodes[124]["description"]=""
    DG.nodes[124]["yogajournalurl"]="https://www.yogajournal.com/poses/supported-headstand/"
    DG.nodes[124]["yogajournal_picture"]="https://www.yogajournal.com/wp-content/uploads/2007/08/rina_headstand-2.jpg?crop=535:301&width=1070&enable=upscale"
    DG.nodes[124]["hindi_name"]="Shirshasana"
    DG.nodes[124]["counter asana"] = None
    DG.nodes[124]["comment"]=""
    DG.nodes[124]["Dharma Mittra picture URL"]=""
    DG.nodes[124]["wikipedia"] = "https://en.wikipedia.org/wiki/Shirshasana"
    DG.nodes[124]["asanas 608 page"]=""
    DG.nodes[124]["asanas 608 english name"]=""

    DG.add_node(125,english_name="legs up the wall pose")
    DG.nodes[125]["two_sided"]=False
    DG.nodes[125]["body areas"] = []
    DG.nodes[125]["description"]="commonly a fully supported pose using a wall and sometimes a pile of blankets."
    DG.nodes[125]["yogajournalurl"]="https://www.yogajournal.com/poses/legs-up-the-wall-pose-2/"
    DG.nodes[125]["yogajournal_picture"]="https://www.yogajournal.com/wp-content/uploads/2007/08/leah-cullis-performs-legs-up-the-wall-pose.jpg?crop=535:301&width=1070&enable=upscale"
    DG.nodes[125]["hindi_name"]=""
    DG.nodes[125]["counter asana"] = None
    DG.nodes[125]["comment"]=""
    DG.nodes[125]["Dharma Mittra picture URL"]=""
    DG.nodes[125]["wikipedia"] = "https://en.wikipedia.org/wiki/Viparita_Karani"
    DG.nodes[125]["asanas 608 page"]=""
    DG.nodes[125]["asanas 608 english name"]=""

    DG.add_node(126,english_name="Side-Reclining Leg Lift")
    DG.nodes[126]["two_sided"]=True
    DG.nodes[126]["body areas"] = []
    DG.nodes[126]["description"]=""
    DG.nodes[126]["yogajournalurl"]=""
    DG.nodes[126]["yogajournal_picture"]=""
    DG.nodes[126]["hindi_name"]="Anantasana"
    DG.nodes[126]["counter asana"] = None
    DG.nodes[126]["comment"]=""
    DG.nodes[126]["Dharma Mittra picture URL"]=""
    DG.nodes[126]["wikipedia"] = "https://en.wikipedia.org/wiki/Anantasana"
    DG.nodes[126]["asanas 608 page"]=""
    DG.nodes[126]["asanas 608 english name"]=""

    DG.add_node(127,english_name="caterpillar")
    DG.nodes[127]["two_sided"]=False
    DG.nodes[127]["body areas"] = []
    DG.nodes[127]["description"]=""
    DG.nodes[127]["yogajournalurl"]=""
    DG.nodes[127]["yogajournal_picture"]=""
    DG.nodes[127]["hindi_name"]="Ashtanga Namaskara"
    DG.nodes[127]["counter asana"] = None
    DG.nodes[127]["comment"]=""
    DG.nodes[127]["Dharma Mittra picture URL"]=""
    DG.nodes[127]["wikipedia"] = "https://en.wikipedia.org/wiki/Ashtanga_Namaskara"
    DG.nodes[127]["asanas 608 page"]=""
    DG.nodes[127]["asanas 608 english name"]=""

    DG.add_node(128,english_name="formidable")
    DG.nodes[128]["two_sided"]=True
    DG.nodes[128]["body areas"] = []
    DG.nodes[128]["description"]=""
    DG.nodes[128]["yogajournalurl"]=""
    DG.nodes[128]["yogajournal_picture"]=""
    DG.nodes[128]["hindi_name"]="Bhairavasana"
    DG.nodes[128]["counter asana"] = None
    DG.nodes[128]["comment"]=""
    DG.nodes[128]["Dharma Mittra picture URL"]=""
    DG.nodes[128]["wikipedia"] = "https://en.wikipedia.org/wiki/Bhairavasana"
    DG.nodes[128]["asanas 608 page"]=""
    DG.nodes[128]["asanas 608 english name"]=""

    DG.add_node(129,english_name="frog")
    DG.nodes[129]["two_sided"]=False
    DG.nodes[129]["body areas"] = []
    DG.nodes[129]["description"]=""
    DG.nodes[129]["yogajournalurl"]=""
    DG.nodes[129]["yogajournal_picture"]=""
    DG.nodes[129]["hindi_name"]="Bhekasana"
    DG.nodes[129]["counter asana"] = None
    DG.nodes[129]["comment"]=""
    DG.nodes[129]["Dharma Mittra picture URL"]=""
    DG.nodes[129]["wikipedia"] = "https://en.wikipedia.org/wiki/Bhekasana"
    DG.nodes[129]["asanas 608 page"]=""
    DG.nodes[129]["asanas 608 english name"]=""

    DG.add_node(130,english_name="Feathered Peacock Pose, legs straight")
    DG.nodes[130]["two_sided"]=False
    DG.nodes[130]["body areas"] = []
    DG.nodes[130]["description"]="forearm balance similar to Vrischikasana, but the legs are straight, stretched up over the head, with the back less extremely arched"
    DG.nodes[130]["yogajournalurl"]="https://www.yogajournal.com/poses/feathered-peacock-pose/"
    DG.nodes[130]["yogajournal_picture"]="https://www.yogajournal.com/wp-content/uploads/2007/08/forearm-balance-clio-manuelian.jpg?crop=535:301&width=1070&enable=upscale"
    DG.nodes[130]["hindi_name"]="Pincha Mayurasana"
    DG.nodes[130]["counter asana"] = None
    DG.nodes[130]["comment"]=""
    DG.nodes[130]["Dharma Mittra picture URL"]=""
    DG.nodes[130]["wikipedia"] = ""
    DG.nodes[130]["asanas 608 page"]=""
    DG.nodes[130]["asanas 608 english name"]=""

    DG.add_node(131,english_name="Formidable Face pose")
    DG.nodes[131]["two_sided"]=False
    DG.nodes[131]["body areas"] = []
    DG.nodes[131]["description"]="similar to Pincha Mayurasana but with bent arms and only the hands on the ground; the back is lightly arched and the legs and feet point vertically upwards. It may be practised with a block under the shoulders"
    DG.nodes[131]["yogajournalurl"]=""
    DG.nodes[131]["yogajournal_picture"]=""
    DG.nodes[131]["hindi_name"]="Ganda Bherundasana"
    DG.nodes[131]["counter asana"] = None
    DG.nodes[131]["comment"]=""
    DG.nodes[131]["Dharma Mittra picture URL"]=""
    DG.nodes[131]["wikipedia"] = ""
    DG.nodes[131]["asanas 608 page"]=""
    DG.nodes[131]["asanas 608 english name"]=""

    DG.add_node(132,english_name="Feathered Peacock Pose, legs in lotus")
    DG.nodes[132]["two_sided"]=False
    DG.nodes[132]["body areas"] = []
    DG.nodes[132]["description"]=""
    DG.nodes[132]["yogajournalurl"]=""
    DG.nodes[132]["yogajournal_picture"]=""
    DG.nodes[132]["hindi_name"]="Pincha Mayurasana"
    DG.nodes[132]["counter asana"] = None
    DG.nodes[132]["comment"]=""
    DG.nodes[132]["Dharma Mittra picture URL"]=""
    DG.nodes[132]["wikipedia"] = ""
    DG.nodes[132]["asanas 608 page"]=""
    DG.nodes[132]["asanas 608 english name"]=""

    DG.add_node(133,english_name="Posture of Repose")
    DG.nodes[133]["two_sided"]=False
    DG.nodes[133]["body areas"] = []
    DG.nodes[133]["description"]="same as Pincha Mayurasana, but with only the elbows on the ground, the hands cradling the face, making it a difficult balance."
    DG.nodes[133]["yogajournalurl"]=""
    DG.nodes[133]["yogajournal_picture"]=""
    DG.nodes[133]["hindi_name"]="Sayanasana"
    DG.nodes[133]["counter asana"] = None
    DG.nodes[133]["comment"]=""
    DG.nodes[133]["Dharma Mittra picture URL"]=""
    DG.nodes[133]["wikipedia"] = ""
    DG.nodes[133]["yogapedia"] = "https://www.yogapedia.com/definition/9944/sayanasana"
    DG.nodes[133]["asanas 608 page"]=""
    DG.nodes[133]["asanas 608 english name"]=""

    DG.add_node(134,english_name="Yogic Sleep Pose")
    DG.nodes[134]["two_sided"]=False
    DG.nodes[134]["body areas"] = []
    DG.nodes[134]["description"]=""
    DG.nodes[134]["yogajournalurl"]=""
    DG.nodes[134]["yogajournal_picture"]=""
    DG.nodes[134]["hindi_name"]="Yoganidrasana"
    DG.nodes[134]["counter asana"] = None
    DG.nodes[134]["comment"]=""
    DG.nodes[134]["Dharma Mittra picture URL"]=""
    DG.nodes[134]["wikipedia"] = "https://en.wikipedia.org/wiki/Yoganidrasana"
    DG.nodes[134]["asanas 608 page"]=""
    DG.nodes[134]["asanas 608 english name"]=""

    DG.add_node(135,english_name="locust or grasshopper")
    DG.nodes[135]["two_sided"]=False
    DG.nodes[135]["body areas"] = ["lower back"]
    DG.nodes[135]["description"]=""
    DG.nodes[135]["yogajournalurl"]="https://www.yogajournal.com/poses/locust-pose/"
    DG.nodes[135]["yogajournal_picture"]="https://www.yogajournal.com/wp-content/uploads/2007/08/2anatomy_278_01_fnl.jpg?crop=535:301&width=1070&enable=upscale"
    DG.nodes[135]["hindi_name"]="Salabhasana"
    DG.nodes[135]["counter asana"] = None
    DG.nodes[135]["comment"]=""
    DG.nodes[135]["Dharma Mittra picture URL"]=""
    DG.nodes[135]["wikipedia"] = "https://en.wikipedia.org/wiki/Salabhasana"
    DG.nodes[135]["asanas 608 page"]=""
    DG.nodes[135]["asanas 608 english name"]=""

    DG.add_node(136,english_name="Wind-Relieving pose")
    DG.nodes[136]["two_sided"]=False
    DG.nodes[136]["body areas"] = []
    DG.nodes[136]["description"]=""
    DG.nodes[136]["yogajournalurl"]=""
    DG.nodes[136]["yogajournal_picture"]=""
    DG.nodes[136]["hindi_name"]="Pavanamuktasana"
    DG.nodes[136]["counter asana"] = None
    DG.nodes[136]["comment"]=""
    DG.nodes[136]["Dharma Mittra picture URL"]=""
    DG.nodes[136]["wikipedia"] = "https://en.wikipedia.org/wiki/Pavanamuktasana"
    DG.nodes[136]["asanas 608 page"]=""
    DG.nodes[136]["asanas 608 english name"]=""

    DG.add_node(137,english_name="Revolved Abdomen pose OR Belly twist OR Spinal twist")
    DG.nodes[137]["two_sided"]=False
    DG.nodes[137]["body areas"] = []
    DG.nodes[137]["description"]=""
    DG.nodes[137]["yogajournalurl"]=""
    DG.nodes[137]["yogajournal_picture"]=""
    DG.nodes[137]["hindi_name"]="Jathara Parivartanasana"
    DG.nodes[137]["counter asana"] = None
    DG.nodes[137]["comment"]=""
    DG.nodes[137]["Dharma Mittra picture URL"]=""
    DG.nodes[137]["wikipedia"] = "https://en.wikipedia.org/wiki/Jathara_Parivartanasana"
    DG.nodes[137]["asanas 608 page"]=""
    DG.nodes[137]["asanas 608 english name"]=""

    DG.add_node(138,english_name="Bharadvaja's twist 1")
    DG.nodes[138]["two_sided"]=True
    DG.nodes[138]["body areas"] = []
    DG.nodes[138]["description"]="basic form, with the legs as in Virasana (hero pose), one foot on the floor and the other ankle cradled in the arch of the foot below."
    DG.nodes[138]["yogajournalurl"]=""
    DG.nodes[138]["yogajournal_picture"]=""
    DG.nodes[138]["hindi_name"]="Bharadvajasana I"
    DG.nodes[138]["counter asana"] = None
    DG.nodes[138]["comment"]=""
    DG.nodes[138]["Dharma Mittra picture URL"]=""
    DG.nodes[138]["wikipedia"] = "https://en.wikipedia.org/wiki/Bharadvajasana"
    DG.nodes[138]["asanas 608 page"]=""
    DG.nodes[138]["asanas 608 english name"]=""

    DG.add_node(139,english_name="Bharadvaja's twist 2")
    DG.nodes[139]["two_sided"]=True
    DG.nodes[139]["body areas"] = []
    DG.nodes[139]["description"]="advanced form requiring high hip mobility; one leg is bent as in Padmasana (lotus position), while the other leg is bent as in Virasana."
    DG.nodes[139]["yogajournalurl"]=""
    DG.nodes[139]["yogajournal_picture"]=""
    DG.nodes[139]["hindi_name"]="Bharadvajasana II"
    DG.nodes[139]["counter asana"] = None
    DG.nodes[139]["comment"]=""
    DG.nodes[139]["Dharma Mittra picture URL"]=""
    DG.nodes[139]["wikipedia"] = "https://en.wikipedia.org/wiki/Bharadvajasana"
    DG.nodes[139]["asanas 608 page"]=""
    DG.nodes[139]["asanas 608 english name"]=""

    DG.add_node(140,english_name="pose of the sage Marichi")
    DG.nodes[140]["two_sided"]=True
    DG.nodes[140]["body areas"] = []
    DG.nodes[140]["description"]="A twist. One leg is stretched out straight ahead of the body, the other is bent with the sole of the foot on the floor and the knee up beside the body. The body is twisted towards the side with the straight leg, and the arms are clasped behind the back and around the raised knee. The body may then lean forwards until the nose and chin touch the straight leg"
    DG.nodes[140]["yogajournalurl"]="https://www.yogajournal.com/poses/marichi-s-pose/"
    DG.nodes[140]["yogajournal_picture"]="https://www.yogajournal.com/wp-content/uploads/2007/08/anat_276_01_fnl-marichyasana.jpg?crop=535:301&width=1070&enable=upscale"
    DG.nodes[140]["hindi_name"]="Marichyasana"
    DG.nodes[140]["counter asana"] = None
    DG.nodes[140]["comment"]=""
    DG.nodes[140]["Dharma Mittra picture URL"]=""
    DG.nodes[140]["wikipedia"] = "https://en.wikipedia.org/wiki/Marichyasana"
    DG.nodes[140]["asanas 608 page"]=""
    DG.nodes[140]["asanas 608 english name"]=""

    DG.add_node(141,english_name="Marichyasana III")
    DG.nodes[141]["two_sided"]=False
    DG.nodes[141]["body areas"] = []
    DG.nodes[141]["description"]="the leg on the ground is stretched out straight. The body is twisted towards the side with the bent leg, and again the arms are clasped behind the back and around the raised knee"
    DG.nodes[141]["yogajournalurl"]="https://www.yogajournal.com/poses/pose-dedicated-to-the-sage-marichi-i/"
    DG.nodes[141]["yogajournal_picture"]="https://www.yogajournal.com/wp-content/uploads/2007/08/mc_225_05-credit-marichyasana-i.jpg?crop=535:301&width=1070&enable=upscale"
    DG.nodes[141]["hindi_name"]="Marichyasana III"
    DG.nodes[141]["counter asana"] = None
    DG.nodes[141]["comment"]=""
    DG.nodes[141]["Dharma Mittra picture URL"]=""
    DG.nodes[141]["wikipedia"] = "https://en.wikipedia.org/wiki/Marichyasana"
    DG.nodes[141]["asanas 608 page"]=""
    DG.nodes[141]["asanas 608 english name"]=""

    DG.add_node(142,english_name="Lord of the Fishes Pose")
    DG.nodes[142]["two_sided"]=False
    DG.nodes[142]["body areas"] = []
    DG.nodes[142]["description"]=""
    DG.nodes[142]["yogajournalurl"]=""
    DG.nodes[142]["yogajournal_picture"]=""
    DG.nodes[142]["hindi_name"]="Matsyendrasana"
    DG.nodes[142]["counter asana"] = None
    DG.nodes[142]["comment"]=""
    DG.nodes[142]["Dharma Mittra picture URL"]=""
    DG.nodes[142]["wikipedia"] = "https://en.wikipedia.org/wiki/Matsyendrasana"
    DG.nodes[142]["asanas 608 page"]=""
    DG.nodes[142]["asanas 608 english name"]=""

    DG.add_node(143,english_name="noose")
    DG.nodes[143]["two_sided"]=True
    DG.nodes[143]["body areas"] = []
    DG.nodes[143]["description"]=""
    DG.nodes[143]["yogajournalurl"]="https://www.yogajournal.com/poses/noose-pose/"
    DG.nodes[143]["yogajournal_picture"]="https://www.yogajournal.com/wp-content/uploads/2007/08/noose-pose-pasasana.jpg?crop=535:301&width=1070&enable=upscale"
    DG.nodes[143]["hindi_name"]="Pasasana"
    DG.nodes[143]["counter asana"] = None
    DG.nodes[143]["comment"]=""
    DG.nodes[143]["Dharma Mittra picture URL"]=""
    DG.nodes[143]["wikipedia"] = "https://en.wikipedia.org/wiki/Pasasana"
    DG.nodes[143]["asanas 608 page"]=""
    DG.nodes[143]["asanas 608 english name"]=""

    DG.add_node(144,english_name="easy")
    DG.nodes[144]["two_sided"]=True
    DG.nodes[144]["body areas"] = []
    DG.nodes[144]["description"]=""
    DG.nodes[144]["yogajournalurl"]="https://www.yogajournal.com/poses/types/seated-twists/easy-pose-3/"
    DG.nodes[144]["yogajournal_picture"]="https://www.yogajournal.com/wp-content/uploads/2007/08/2hp_286_0507_bjk.jpg?crop=535:301&width=1070&enable=upscale"
    DG.nodes[144]["hindi_name"]="Sukhasana"
    DG.nodes[144]["counter asana"] = None
    DG.nodes[144]["comment"]=""
    DG.nodes[144]["Dharma Mittra picture URL"]=""
    DG.nodes[144]["wikipedia"] = "https://en.wikipedia.org/wiki/Sukhasana"
    DG.nodes[144]["asanas 608 page"]=""
    DG.nodes[144]["asanas 608 english name"]=""

    DG.add_node(145,english_name="lion")
    DG.nodes[145]["two_sided"]=False
    DG.nodes[145]["body areas"] = []
    DG.nodes[145]["description"]=""
    DG.nodes[145]["yogajournalurl"]=""
    DG.nodes[145]["yogajournal_picture"]=""
    DG.nodes[145]["hindi_name"]="Simhasana"
    DG.nodes[145]["counter asana"] = None
    DG.nodes[145]["comment"]=""
    DG.nodes[145]["Dharma Mittra picture URL"]=""
    DG.nodes[145]["wikipedia"] = "https://en.wikipedia.org/wiki/Simhasana"
    DG.nodes[145]["asanas 608 page"]=""
    DG.nodes[145]["asanas 608 english name"]=""

    DG.add_node(146,english_name="Archer OR Bow and Arrow OR Shooting Bow")
    DG.nodes[146]["two_sided"]=False
    DG.nodes[146]["body areas"] = []
    DG.nodes[146]["description"]="pulling the foot towards the ear from a seated position with the legs outstretched."
    DG.nodes[146]["yogajournalurl"]=""
    DG.nodes[146]["yogajournal_picture"]=""
    DG.nodes[146]["hindi_name"]="Akarna Dhanurasana"
    DG.nodes[146]["counter asana"] = None
    DG.nodes[146]["comment"]=""
    DG.nodes[146]["Dharma Mittra picture URL"]=""
    DG.nodes[146]["wikipedia"] = "https://en.wikipedia.org/wiki/Akarna_Dhanurasana"
    DG.nodes[146]["asanas 608 page"]=""
    DG.nodes[146]["asanas 608 english name"]=""

    DG.add_node(147,english_name="rabbit")
    DG.nodes[147]["two_sided"]=False
    DG.nodes[147]["body areas"] = []
    DG.nodes[147]["description"]=""
    DG.nodes[147]["yogajournalurl"]=""
    DG.nodes[147]["yogajournal_picture"]=""
    DG.nodes[147]["hindi_name"]="Shasangasana"
    DG.nodes[147]["counter asana"] = None
    DG.nodes[147]["comment"]=""
    DG.nodes[147]["Dharma Mittra picture URL"]=""
    DG.nodes[147]["wikipedia"] = "https://en.wikipedia.org/wiki/Balasana"
    DG.nodes[147]["asanas 608 page"]=""
    DG.nodes[147]["asanas 608 english name"]=""

    DG.add_node(148,english_name="staff pose OR back stretch pose")
    DG.nodes[148]["two_sided"]=False
    DG.nodes[148]["body areas"] = []
    DG.nodes[148]["description"]="legs straight, back upright"
    DG.nodes[148]["yogajournalurl"]=""
    DG.nodes[148]["yogajournal_picture"]=""
    DG.nodes[148]["hindi_name"]="Dandasana"
    DG.nodes[148]["counter asana"] = None
    DG.nodes[148]["comment"]=""
    DG.nodes[148]["Dharma Mittra picture URL"]=""
    DG.nodes[148]["wikipedia"] = "https://en.wikipedia.org/wiki/Dandasana"
    DG.nodes[148]["asanas 608 page"]="278"
    DG.nodes[148]["asanas 608 english name"]="back stretch pose"

    DG.add_node(149,english_name="monkey OR seated front splits")
    DG.nodes[149]["two_sided"]=True
    DG.nodes[149]["body areas"] = []
    DG.nodes[149]["description"]=""
    DG.nodes[149]["yogajournalurl"]="https://www.yogajournal.com/poses/monkey-pose/"
    DG.nodes[149]["yogajournal_picture"]="https://www.yogajournal.com/wp-content/uploads/2007/08/2compass-4.jpg?crop=535:301&width=1070&enable=upscale"
    DG.nodes[149]["hindi_name"]="Hanumanasana"
    DG.nodes[149]["counter asana"] = None
    DG.nodes[149]["comment"]=""
    DG.nodes[149]["Dharma Mittra picture URL"]=""
    DG.nodes[149]["wikipedia"] = "https://en.wikipedia.org/wiki/Hanumanasana"
    DG.nodes[149]["asanas 608 page"]=""
    DG.nodes[149]["asanas 608 english name"]=""

    DG.add_node(150,english_name="tortoise or turtle")
    DG.nodes[150]["two_sided"]=False
    DG.nodes[150]["body areas"] = []
    DG.nodes[150]["description"]=""
    DG.nodes[150]["yogajournalurl"]=""
    DG.nodes[150]["yogajournal_picture"]=""
    DG.nodes[150]["hindi_name"]="Kurmasana"
    DG.nodes[150]["counter asana"] = None
    DG.nodes[150]["comment"]=""
    DG.nodes[150]["Dharma Mittra picture URL"]=""
    DG.nodes[150]["wikipedia"] = "https://en.wikipedia.org/wiki/Kurmasana"
    DG.nodes[150]["asanas 608 page"]=""
    DG.nodes[150]["asanas 608 english name"]=""

    DG.add_node(151,english_name="Upside-Down Tortoise")
    DG.nodes[151]["two_sided"]=False
    DG.nodes[151]["body areas"] = []
    DG.nodes[151]["description"]=""
    DG.nodes[151]["yogajournalurl"]=""
    DG.nodes[151]["yogajournal_picture"]=""
    DG.nodes[151]["hindi_name"]="Uttana Kurmasana"
    DG.nodes[151]["counter asana"] = None
    DG.nodes[151]["comment"]=""
    DG.nodes[151]["Dharma Mittra picture URL"]=""
    DG.nodes[151]["wikipedia"] = "https://en.wikipedia.org/wiki/Kurmasana"
    DG.nodes[151]["asanas 608 page"]=""
    DG.nodes[151]["asanas 608 english name"]=""

    DG.add_node(152,english_name="seated side split")
    DG.nodes[152]["two_sided"]=False
    DG.nodes[152]["body areas"] = []
    DG.nodes[152]["description"]=""
    DG.nodes[152]["yogajournalurl"]=""
    DG.nodes[152]["yogajournal_picture"]=""
    DG.nodes[152]["hindi_name"]="Samakonasana"
    DG.nodes[152]["counter asana"] = None
    DG.nodes[152]["comment"]=""
    DG.nodes[152]["Dharma Mittra picture URL"]=""
    DG.nodes[152]["wikipedia"] = "https://en.wikipedia.org/wiki/Split_(gymnastics)"
    DG.nodes[152]["asanas 608 page"]=""
    DG.nodes[152]["asanas 608 english name"]=""

    DG.add_node(153,english_name="forearm stand, legs in full lotus")
    DG.nodes[153]["two_sided"]=True
    DG.nodes[153]["body areas"] = []
    DG.nodes[153]["description"]=""
    DG.nodes[153]["yogajournalurl"]=""
    DG.nodes[153]["yogajournal_picture"]=""
    DG.nodes[153]["hindi_name"]=""
    DG.nodes[153]["counter asana"] = None
    DG.nodes[153]["comment"]=""
    DG.nodes[153]["Dharma Mittra picture URL"]=""
    DG.nodes[153]["wikipedia"] = ""
    DG.nodes[153]["asanas 608 page"]=""
    DG.nodes[153]["asanas 608 english name"]=""

    DG.add_node(154,english_name="hero")
    DG.nodes[154]["two_sided"]=False
    DG.nodes[154]["body areas"] = []
    DG.nodes[154]["description"]=""
    DG.nodes[154]["yogajournalurl"]=""
    DG.nodes[154]["yogajournal_picture"]=""
    DG.nodes[154]["hindi_name"]="Virasana"
    DG.nodes[154]["counter asana"] = None
    DG.nodes[154]["comment"]=""
    DG.nodes[154]["Dharma Mittra picture URL"]=""
    DG.nodes[154]["wikipedia"] = "https://en.wikipedia.org/wiki/Virasana"
    DG.nodes[154]["asanas 608 page"]=""
    DG.nodes[154]["asanas 608 english name"]=""

    DG.add_node(155,english_name="seated wide-leg, torso forward bend")
    DG.nodes[155]["two_sided"]=False
    DG.nodes[155]["body areas"] = []
    DG.nodes[155]["description"]=""
    DG.nodes[155]["yogajournalurl"]=""
    DG.nodes[155]["yogajournal_picture"]=""
    DG.nodes[155]["hindi_name"]="Upavista Konasana"
    DG.nodes[155]["counter asana"] = None
    DG.nodes[155]["comment"]=""
    DG.nodes[155]["Dharma Mittra picture URL"]=""
    DG.nodes[155]["wikipedia"] = "https://en.wikipedia.org/wiki/Upavi%E1%B9%A3%E1%B9%ADa_Ko%E1%B9%87%C4%81sana"
    DG.nodes[155]["asanas 608 page"]=""
    DG.nodes[155]["asanas 608 english name"]=""

    DG.add_node(156,english_name="hand stand, legs in eagle")
    DG.nodes[156]["two_sided"]=True
    DG.nodes[156]["body areas"] = []
    DG.nodes[156]["description"]=""
    DG.nodes[156]["yogajournalurl"]=""
    DG.nodes[156]["yogajournal_picture"]=""
    DG.nodes[156]["hindi_name"]=""
    DG.nodes[156]["counter asana"] = None
    DG.nodes[156]["comment"]=""
    DG.nodes[156]["Dharma Mittra picture URL"]=""
    DG.nodes[156]["wikipedia"] = ""
    DG.nodes[156]["asanas 608 page"]=""
    DG.nodes[156]["asanas 608 english name"]=""

    DG.add_node(157,english_name="hand stand, legs in lotus")
    DG.nodes[157]["two_sided"]=False
    DG.nodes[157]["body areas"] = []
    DG.nodes[157]["description"]=""
    DG.nodes[157]["yogajournalurl"]=""
    DG.nodes[157]["yogajournal_picture"]=""
    DG.nodes[157]["hindi_name"]=""
    DG.nodes[157]["counter asana"] = None
    DG.nodes[157]["comment"]=""
    DG.nodes[157]["Dharma Mittra picture URL"]=""
    DG.nodes[157]["wikipedia"] = ""
    DG.nodes[157]["asanas 608 page"]=""
    DG.nodes[157]["asanas 608 english name"]=""

    DG.add_node(158,english_name="forearm stand, legs in side splits")
    DG.nodes[158]["two_sided"]=False
    DG.nodes[158]["body areas"] = []
    DG.nodes[158]["description"]=""
    DG.nodes[158]["yogajournalurl"]=""
    DG.nodes[158]["yogajournal_picture"]=""
    DG.nodes[158]["hindi_name"]=""
    DG.nodes[158]["counter asana"] = None
    DG.nodes[158]["comment"]=""
    DG.nodes[158]["Dharma Mittra picture URL"]=""
    DG.nodes[158]["wikipedia"] = ""
    DG.nodes[158]["asanas 608 page"]=""
    DG.nodes[158]["asanas 608 english name"]=""

    DG.add_node(159,english_name="forearm stand, legs in eagle")
    DG.nodes[159]["two_sided"]=False
    DG.nodes[159]["body areas"] = []
    DG.nodes[159]["description"]=""
    DG.nodes[159]["yogajournalurl"]=""
    DG.nodes[159]["yogajournal_picture"]=""
    DG.nodes[159]["hindi_name"]=""
    DG.nodes[159]["counter asana"] = None
    DG.nodes[159]["comment"]=""
    DG.nodes[159]["Dharma Mittra picture URL"]=""
    DG.nodes[159]["wikipedia"] = ""
    DG.nodes[159]["asanas 608 page"]=""
    DG.nodes[159]["asanas 608 english name"]=""

    DG.add_node(160,english_name="downward dog twist to grab one leg")
    DG.nodes[160]["two_sided"]=False
    DG.nodes[160]["body areas"] = []
    DG.nodes[160]["description"]=""
    DG.nodes[160]["yogajournalurl"]=""
    DG.nodes[160]["yogajournal_picture"]=""
    DG.nodes[160]["hindi_name"]=""
    DG.nodes[160]["counter asana"] = None
    DG.nodes[160]["comment"]=""
    DG.nodes[160]["Dharma Mittra picture URL"]=""
    DG.nodes[160]["wikipedia"] = ""
    DG.nodes[160]["asanas 608 page"]=""
    DG.nodes[160]["asanas 608 english name"]=""

    DG.add_node(161,english_name="side plank, straight arm supporting, straight leg up")
    DG.nodes[161]["two_sided"]=False
    DG.nodes[161]["body areas"] = []
    DG.nodes[161]["description"]=""
    DG.nodes[161]["yogajournalurl"]=""
    DG.nodes[161]["yogajournal_picture"]=""
    DG.nodes[161]["hindi_name"]="Vasisthasana B"
    DG.nodes[161]["counter asana"] = None
    DG.nodes[161]["comment"]=""
    DG.nodes[161]["Dharma Mittra picture URL"]=""
    DG.nodes[161]["wikipedia"] = ""
    DG.nodes[161]["asanas 608 page"]=""
    DG.nodes[161]["asanas 608 english name"]=""

    DG.add_node(162,english_name="side plank, forearm supporting, straight legs")
    DG.nodes[162]["two_sided"]=False
    DG.nodes[162]["body areas"] = []
    DG.nodes[162]["description"]=""
    DG.nodes[162]["yogajournalurl"]=""
    DG.nodes[162]["yogajournal_picture"]=""
    DG.nodes[162]["hindi_name"]=""
    DG.nodes[162]["counter asana"] = None
    DG.nodes[162]["comment"]=""
    DG.nodes[162]["Dharma Mittra picture URL"]=""
    DG.nodes[162]["wikipedia"] = ""
    DG.nodes[162]["asanas 608 page"]=""
    DG.nodes[162]["asanas 608 english name"]=""

    DG.add_node(163,english_name="cowherd")
    DG.nodes[163]["two_sided"]=False
    DG.nodes[163]["body areas"] = []
    DG.nodes[163]["description"]="seated pose with the soles of the feet pressed together and the knees on the ground with the heels are under the body."
    DG.nodes[163]["yogajournalurl"]=""
    DG.nodes[163]["yogajournal_picture"]=""
    DG.nodes[163]["hindi_name"]="Gorakshasana"
    DG.nodes[163]["counter asana"] = None
    DG.nodes[163]["comment"]=""
    DG.nodes[163]["Dharma Mittra picture URL"]=""
    DG.nodes[163]["wikipedia"] = "https://en.wikipedia.org/wiki/Gorakshasana"
    DG.nodes[163]["asanas 608 page"]=""
    DG.nodes[163]["asanas 608 english name"]=""

    DG.add_node(164,english_name="gate")
    DG.nodes[164]["two_sided"]=False
    DG.nodes[164]["body areas"] = []
    DG.nodes[164]["description"]=""
    DG.nodes[164]["yogajournalurl"]="https://www.yogajournal.com/poses/gate-pose-2/"
    DG.nodes[164]["yogajournal_picture"]="https://www.yogajournal.com/wp-content/uploads/2007/08/3hp_288_03_bjk2.jpg?crop=535:301&width=1070&enable=upscale"
    DG.nodes[164]["hindi_name"]="Parighasana"
    DG.nodes[164]["counter asana"] = None
    DG.nodes[164]["comment"]=""
    DG.nodes[164]["Dharma Mittra picture URL"]=""
    DG.nodes[164]["wikipedia"] = ""
    DG.nodes[164]["asanas 608 page"]=""
    DG.nodes[164]["asanas 608 english name"]=""

    DG.add_node(165,english_name="high lunge")
    DG.nodes[165]["two_sided"]=False
    DG.nodes[165]["body areas"] = []
    DG.nodes[165]["description"]=""
    DG.nodes[165]["yogajournalurl"]="https://www.yogajournal.com/poses/high-lunge-variation/"
    DG.nodes[165]["yogajournal_picture"]="https://www.yogajournal.com/wp-content/uploads/2008/04/3hp_288_07_bjk2.jpg?crop=535:301&width=1070&enable=upscale"
    DG.nodes[165]["hindi_name"]=""
    DG.nodes[165]["counter asana"] = None
    DG.nodes[165]["comment"]=""
    DG.nodes[165]["Dharma Mittra picture URL"]=""
    DG.nodes[165]["wikipedia"] = ""
    DG.nodes[165]["asanas 608 page"]=""
    DG.nodes[165]["asanas 608 english name"]=""

    DG.add_node(166,english_name="lord of the dance")
    DG.nodes[166]["two_sided"]=False
    DG.nodes[166]["body areas"] = []
    DG.nodes[166]["description"]=""
    DG.nodes[166]["yogajournalurl"]="https://www.yogajournal.com/poses/types/backbends/lord-of-the-dance-pose/"
    DG.nodes[166]["yogajournal_picture"]="https://www.yogajournal.com/wp-content/uploads/2007/08/3enneagram_289_1454_bjk.jpg?crop=535:301&width=1070&enable=upscale"
    DG.nodes[166]["hindi_name"]="Nataraja"
    DG.nodes[166]["counter asana"] = None
    DG.nodes[166]["comment"]="YogaJournal seems to be making fun of its audience with the introduction, 'want to, like, connect with cosmic energy?'"
    DG.nodes[166]["Dharma Mittra picture URL"]=""
    DG.nodes[166]["wikipedia"] = ""
    DG.nodes[166]["asanas 608 page"]=""
    DG.nodes[166]["asanas 608 english name"]=""

    DG.add_node(167,english_name="side stretch")
    DG.nodes[167]["two_sided"]=False
    DG.nodes[167]["body areas"] = []
    DG.nodes[167]["description"]=""
    DG.nodes[167]["yogajournalurl"]="https://www.yogajournal.com/poses/types/intense-side-stretch-pose/"
    DG.nodes[167]["yogajournal_picture"]="https://www.yogajournal.com/wp-content/uploads/2007/08/ccd04294.jpg?crop=535:301&width=1070&enable=upscale"
    DG.nodes[167]["hindi_name"]="Parsvottanasana"
    DG.nodes[167]["counter asana"] = None
    DG.nodes[167]["comment"]=""
    DG.nodes[167]["Dharma Mittra picture URL"]=""
    DG.nodes[167]["wikipedia"] = "https://en.wikipedia.org/wiki/Parshvottanasana"
    DG.nodes[167]["asanas 608 page"]=""
    DG.nodes[167]["asanas 608 english name"]=""

    DG.add_node(168,english_name="revolved side angle")
    DG.nodes[168]["two_sided"]=False
    DG.nodes[168]["body areas"] = []
    DG.nodes[168]["description"]=""
    DG.nodes[168]["yogajournalurl"]="https://www.yogajournal.com/poses/types/twists/revolved-side-angle-pose/"
    DG.nodes[168]["yogajournal_picture"]="https://www.yogajournal.com/wp-content/uploads/2007/08/revolved-side-angle-pose.jpg?crop=535:301&width=1070&enable=upscale"
    DG.nodes[168]["hindi_name"]=""
    DG.nodes[168]["counter asana"] = None
    DG.nodes[168]["comment"]=""
    DG.nodes[168]["Dharma Mittra picture URL"]=""
    DG.nodes[168]["wikipedia"] = ""
    DG.nodes[168]["asanas 608 page"]=""
    DG.nodes[168]["asanas 608 english name"]=""

    DG.add_node(169,english_name="heron")
    DG.nodes[169]["two_sided"]=False
    DG.nodes[169]["body areas"] = []
    DG.nodes[169]["description"]=""
    DG.nodes[169]["yogajournalurl"]="https://www.yogajournal.com/poses/heron-pose/"
    DG.nodes[169]["yogajournal_picture"]="https://www.yogajournal.com/wp-content/uploads/2007/08/heron-pose-instructions.jpg?crop=535:301&width=1070&enable=upscale"
    DG.nodes[169]["hindi_name"]="Krounchasana"
    DG.nodes[169]["counter asana"] = None
    DG.nodes[169]["comment"]=""
    DG.nodes[169]["Dharma Mittra picture URL"]=""
    DG.nodes[169]["wikipedia"] = "https://en.wikipedia.org/wiki/Kraunchasana"
    DG.nodes[169]["asanas 608 page"]=""
    DG.nodes[169]["asanas 608 english name"]=""

    DG.add_node(170,english_name="King Pigeon")
    DG.nodes[170]["two_sided"]=False
    DG.nodes[170]["body areas"] = []
    DG.nodes[170]["description"]="elbows and shins on floor"
    DG.nodes[170]["yogajournalurl"]="https://www.yogajournal.com/poses/king-pigeon-pose/"
    DG.nodes[170]["yogajournal_picture"]="https://www.yogajournal.com/wp-content/uploads/2007/08/2yogapedia_273_13_fnl.jpg?crop=535:301&width=1070&enable=upscale"
    DG.nodes[170]["hindi_name"]=""
    DG.nodes[170]["counter asana"] = None
    DG.nodes[170]["comment"]=""
    DG.nodes[170]["Dharma Mittra picture URL"]=""
    DG.nodes[170]["wikipedia"] = ""
    DG.nodes[170]["asanas 608 page"]=""
    DG.nodes[170]["asanas 608 english name"]=""

    DG.add_node(171,english_name="One-Legged King Pigeon Pose II")
    DG.nodes[171]["two_sided"]=False
    DG.nodes[171]["body areas"] = []
    DG.nodes[171]["description"]="foot and knee on ground"
    DG.nodes[171]["yogajournalurl"]="https://www.yogajournal.com/poses/one-legged-king-pigeon-pose-ii/"
    DG.nodes[171]["yogajournal_picture"]="https://www.yogajournal.com/wp-content/uploads/2008/05/carrie-owerko-one-legged-king-pigeon-pose-carrie-owerko.jpg?crop=535:301&width=1070&enable=upscale"
    DG.nodes[171]["hindi_name"]=""
    DG.nodes[171]["counter asana"] = None
    DG.nodes[171]["comment"]=""
    DG.nodes[171]["Dharma Mittra picture URL"]=""
    DG.nodes[171]["wikipedia"] = ""
    DG.nodes[171]["asanas 608 page"]=""
    DG.nodes[171]["asanas 608 english name"]=""

    DG.add_node(172,english_name="sphinx")
    DG.nodes[172]["two_sided"]=False
    DG.nodes[172]["body areas"] = ["lower back"]
    DG.nodes[172]["description"]=""
    DG.nodes[172]["yogajournalurl"]="https://www.yogajournal.com/poses/sphinx-pose/"
    DG.nodes[172]["yogajournal_picture"]="https://www.yogajournal.com/wp-content/uploads/2007/08/32anatomy_290_5169_bjk.jpg?crop=535:301&width=1070&enable=upscale"
    DG.nodes[172]["hindi_name"]=""
    DG.nodes[172]["counter asana"] = None
    DG.nodes[172]["comment"]=""
    DG.nodes[172]["Dharma Mittra picture URL"]=""
    DG.nodes[172]["wikipedia"] = ""
    DG.nodes[172]["asanas 608 page"]=""
    DG.nodes[172]["asanas 608 english name"]=""

    DG.add_node(173,english_name="Marichyasana II")
    DG.nodes[173]["two_sided"]=False
    DG.nodes[173]["body areas"] = []
    DG.nodes[173]["description"]=""
    DG.nodes[173]["yogajournalurl"]=""
    DG.nodes[173]["yogajournal_picture"]="https://www.yogajournal.com/wp-content/uploads/2013/08/image-placeholder-title-6.jpg?width=730"
    DG.nodes[173]["hindi_name"]="Marichyasana II"
    DG.nodes[173]["counter asana"] = None
    DG.nodes[173]["comment"]=""
    DG.nodes[173]["Dharma Mittra picture URL"]=""
    DG.nodes[173]["wikipedia"] = ""
    DG.nodes[173]["asanas 608 page"]=""
    DG.nodes[173]["asanas 608 english name"]=""

    DG.add_node(174,english_name="standing splits, upright")
    DG.nodes[174]["two_sided"]=False
    DG.nodes[174]["body areas"] = ["foot balance"]
    DG.nodes[174]["description"]=""
    DG.nodes[174]["yogajournalurl"]=""
    DG.nodes[174]["yogajournal_picture"]=""
    DG.nodes[174]["hindi_name"]=""
    DG.nodes[174]["counter asana"] = None
    DG.nodes[174]["comment"]=""
    DG.nodes[174]["Dharma Mittra picture URL"]=""
    DG.nodes[174]["wikipedia"] = ""
    DG.nodes[174]["asanas 608 page"]=""
    DG.nodes[174]["asanas 608 english name"]=""

    DG.add_node(175,english_name="side crow")
    DG.nodes[175]["two_sided"]=True
    DG.nodes[175]["body areas"] = ["hand balance"]
    DG.nodes[175]["description"]="both legs bent; one leg is on opposite tricep"
    DG.nodes[175]["yogajournalurl"]=""
    DG.nodes[175]["yogajournal_picture"]=""
    DG.nodes[175]["hindi_name"]=""
    DG.nodes[175]["counter asana"] = None
    DG.nodes[175]["comment"]=""
    DG.nodes[175]["Dharma Mittra picture URL"]=""
    DG.nodes[175]["wikipedia"] = ""
    DG.nodes[175]["asanas 608 page"]=""
    DG.nodes[175]["asanas 608 english name"]=""

    DG.add_node(176,english_name="lotus corpse")
    DG.nodes[176]["two_sided"]=True
    DG.nodes[176]["body areas"] = []
    DG.nodes[176]["description"]="back is on ground, legs in lotus"
    DG.nodes[176]["yogajournalurl"]=""
    DG.nodes[176]["yogajournal_picture"]=""
    DG.nodes[176]["hindi_name"]=""
    DG.nodes[176]["counter asana"] = None
    DG.nodes[176]["comment"]=""
    DG.nodes[176]["Dharma Mittra picture URL"]=""
    DG.nodes[176]["wikipedia"] = ""
    DG.nodes[176]["asanas 608 page"]=""
    DG.nodes[176]["asanas 608 english name"]=""

    DG.add_node(177,english_name="")
    DG.nodes[177]["two_sided"]=False
    DG.nodes[177]["body areas"] = []
    DG.nodes[177]["description"]=""
    DG.nodes[177]["yogajournalurl"]=""
    DG.nodes[177]["yogajournal_picture"]=""
    DG.nodes[177]["hindi_name"]=""
    DG.nodes[177]["counter asana"] = None
    DG.nodes[177]["comment"]=""
    DG.nodes[177]["Dharma Mittra picture URL"]=""
    DG.nodes[177]["wikipedia"] = ""
    DG.nodes[177]["asanas 608 page"]=""
    DG.nodes[177]["asanas 608 english name"]=""

    DG.add_node(178,english_name="")
    DG.nodes[178]["two_sided"]=False
    DG.nodes[178]["body areas"] = []
    DG.nodes[178]["description"]=""
    DG.nodes[178]["yogajournalurl"]=""
    DG.nodes[178]["yogajournal_picture"]=""
    DG.nodes[178]["hindi_name"]=""
    DG.nodes[178]["counter asana"] = None
    DG.nodes[178]["comment"]=""
    DG.nodes[178]["Dharma Mittra picture URL"]=""
    DG.nodes[178]["wikipedia"] = ""
    DG.nodes[178]["asanas 608 page"]=""
    DG.nodes[178]["asanas 608 english name"]=""

    DG.add_node(179,english_name="")
    DG.nodes[179]["two_sided"]=False
    DG.nodes[179]["body areas"] = []
    DG.nodes[179]["description"]=""
    DG.nodes[179]["yogajournalurl"]=""
    DG.nodes[179]["yogajournal_picture"]=""
    DG.nodes[179]["hindi_name"]=""
    DG.nodes[179]["counter asana"] = None
    DG.nodes[179]["comment"]=""
    DG.nodes[179]["Dharma Mittra picture URL"]=""
    DG.nodes[179]["wikipedia"] = ""
    DG.nodes[179]["asanas 608 page"]=""
    DG.nodes[179]["asanas 608 english name"]=""

    DG.add_node(180,english_name="")
    DG.nodes[180]["two_sided"]=False
    DG.nodes[180]["body areas"] = []
    DG.nodes[180]["description"]=""
    DG.nodes[180]["yogajournalurl"]=""
    DG.nodes[180]["yogajournal_picture"]=""
    DG.nodes[180]["hindi_name"]=""
    DG.nodes[180]["counter asana"] = None
    DG.nodes[180]["comment"]=""
    DG.nodes[180]["Dharma Mittra picture URL"]=""
    DG.nodes[180]["wikipedia"] = ""
    DG.nodes[180]["asanas 608 page"]=""
    DG.nodes[180]["asanas 608 english name"]=""

    DG.add_node(181,english_name="")
    DG.nodes[181]["two_sided"]=False
    DG.nodes[181]["body areas"] = []
    DG.nodes[181]["description"]=""
    DG.nodes[181]["yogajournalurl"]=""
    DG.nodes[181]["yogajournal_picture"]=""
    DG.nodes[181]["hindi_name"]=""
    DG.nodes[181]["counter asana"] = None
    DG.nodes[181]["comment"]=""
    DG.nodes[181]["Dharma Mittra picture URL"]=""
    DG.nodes[181]["wikipedia"] = ""
    DG.nodes[181]["asanas 608 page"]=""
    DG.nodes[181]["asanas 608 english name"]=""

    DG.add_node(182,english_name="")
    DG.nodes[182]["two_sided"]=False
    DG.nodes[182]["body areas"] = []
    DG.nodes[182]["description"]=""
    DG.nodes[182]["yogajournalurl"]=""
    DG.nodes[182]["yogajournal_picture"]=""
    DG.nodes[182]["hindi_name"]=""
    DG.nodes[182]["counter asana"] = None
    DG.nodes[182]["comment"]=""
    DG.nodes[182]["Dharma Mittra picture URL"]=""
    DG.nodes[182]["wikipedia"] = ""
    DG.nodes[182]["asanas 608 page"]=""
    DG.nodes[182]["asanas 608 english name"]=""

    DG.add_node(183,english_name="")
    DG.nodes[183]["two_sided"]=False
    DG.nodes[183]["body areas"] = []
    DG.nodes[183]["description"]=""
    DG.nodes[183]["yogajournalurl"]=""
    DG.nodes[183]["yogajournal_picture"]=""
    DG.nodes[183]["hindi_name"]=""
    DG.nodes[183]["counter asana"] = None
    DG.nodes[183]["comment"]=""
    DG.nodes[183]["Dharma Mittra picture URL"]=""
    DG.nodes[183]["wikipedia"] = ""
    DG.nodes[183]["asanas 608 page"]=""
    DG.nodes[183]["asanas 608 english name"]=""

    DG.add_node(184,english_name="")
    DG.nodes[184]["two_sided"]=False
    DG.nodes[184]["body areas"] = []
    DG.nodes[184]["description"]=""
    DG.nodes[184]["yogajournalurl"]=""
    DG.nodes[184]["yogajournal_picture"]=""
    DG.nodes[184]["hindi_name"]=""
    DG.nodes[184]["counter asana"] = None
    DG.nodes[184]["comment"]=""
    DG.nodes[184]["Dharma Mittra picture URL"]=""
    DG.nodes[184]["wikipedia"] = ""
    DG.nodes[184]["asanas 608 page"]=""
    DG.nodes[184]["asanas 608 english name"]=""

    DG.add_node(185,english_name="")
    DG.nodes[185]["two_sided"]=False
    DG.nodes[185]["body areas"] = []
    DG.nodes[185]["description"]=""
    DG.nodes[185]["yogajournalurl"]=""
    DG.nodes[185]["yogajournal_picture"]=""
    DG.nodes[185]["hindi_name"]=""
    DG.nodes[185]["counter asana"] = None
    DG.nodes[185]["comment"]=""
    DG.nodes[185]["Dharma Mittra picture URL"]=""
    DG.nodes[185]["wikipedia"] = ""
    DG.nodes[185]["asanas 608 page"]=""
    DG.nodes[185]["asanas 608 english name"]=""

    DG.add_node(186,english_name="")
    DG.nodes[186]["two_sided"]=False
    DG.nodes[186]["body areas"] = []
    DG.nodes[186]["description"]=""
    DG.nodes[186]["yogajournalurl"]=""
    DG.nodes[186]["yogajournal_picture"]=""
    DG.nodes[186]["hindi_name"]=""
    DG.nodes[186]["counter asana"] = None
    DG.nodes[186]["comment"]=""
    DG.nodes[186]["Dharma Mittra picture URL"]=""
    DG.nodes[186]["wikipedia"] = ""
    DG.nodes[186]["asanas 608 page"]=""
    DG.nodes[186]["asanas 608 english name"]=""

    DG.add_node(187,english_name="")
    DG.nodes[187]["two_sided"]=False
    DG.nodes[187]["body areas"] = []
    DG.nodes[187]["description"]=""
    DG.nodes[187]["yogajournalurl"]=""
    DG.nodes[187]["yogajournal_picture"]=""
    DG.nodes[187]["hindi_name"]=""
    DG.nodes[187]["counter asana"] = None
    DG.nodes[187]["comment"]=""
    DG.nodes[187]["Dharma Mittra picture URL"]=""
    DG.nodes[187]["wikipedia"] = ""
    DG.nodes[187]["asanas 608 page"]=""
    DG.nodes[187]["asanas 608 english name"]=""

    DG.add_node(188,english_name="")
    DG.nodes[188]["two_sided"]=False
    DG.nodes[188]["body areas"] = []
    DG.nodes[188]["description"]=""
    DG.nodes[188]["yogajournalurl"]=""
    DG.nodes[188]["yogajournal_picture"]=""
    DG.nodes[188]["hindi_name"]=""
    DG.nodes[188]["counter asana"] = None
    DG.nodes[188]["comment"]=""
    DG.nodes[188]["Dharma Mittra picture URL"]=""
    DG.nodes[188]["wikipedia"] = ""
    DG.nodes[188]["asanas 608 page"]=""
    DG.nodes[188]["asanas 608 english name"]=""

    DG.add_node(189,english_name="")
    DG.nodes[189]["two_sided"]=False
    DG.nodes[189]["body areas"] = []
    DG.nodes[189]["description"]=""
    DG.nodes[189]["yogajournalurl"]=""
    DG.nodes[189]["yogajournal_picture"]=""
    DG.nodes[189]["hindi_name"]=""
    DG.nodes[189]["counter asana"] = None
    DG.nodes[189]["comment"]=""
    DG.nodes[189]["Dharma Mittra picture URL"]=""
    DG.nodes[189]["wikipedia"] = ""
    DG.nodes[189]["asanas 608 page"]=""
    DG.nodes[189]["asanas 608 english name"]=""

    DG.add_node(190,english_name="")
    DG.nodes[190]["two_sided"]=False
    DG.nodes[190]["body areas"] = []
    DG.nodes[190]["description"]=""
    DG.nodes[190]["yogajournalurl"]=""
    DG.nodes[190]["yogajournal_picture"]=""
    DG.nodes[190]["hindi_name"]=""
    DG.nodes[190]["counter asana"] = None
    DG.nodes[190]["comment"]=""
    DG.nodes[190]["Dharma Mittra picture URL"]=""
    DG.nodes[190]["wikipedia"] = ""
    DG.nodes[190]["asanas 608 page"]=""
    DG.nodes[190]["asanas 608 english name"]=""

    DG.add_node(191,english_name="")
    DG.nodes[191]["two_sided"]=False
    DG.nodes[191]["body areas"] = []
    DG.nodes[191]["description"]=""
    DG.nodes[191]["yogajournalurl"]=""
    DG.nodes[191]["yogajournal_picture"]=""
    DG.nodes[191]["hindi_name"]=""
    DG.nodes[191]["counter asana"] = None
    DG.nodes[191]["comment"]=""
    DG.nodes[191]["Dharma Mittra picture URL"]=""
    DG.nodes[191]["wikipedia"] = ""
    DG.nodes[191]["asanas 608 page"]=""
    DG.nodes[191]["asanas 608 english name"]=""

    DG.add_node(192,english_name="")
    DG.nodes[192]["two_sided"]=False
    DG.nodes[192]["body areas"] = []
    DG.nodes[192]["description"]=""
    DG.nodes[192]["yogajournalurl"]=""
    DG.nodes[192]["yogajournal_picture"]=""
    DG.nodes[192]["hindi_name"]=""
    DG.nodes[192]["counter asana"] = None
    DG.nodes[192]["comment"]=""
    DG.nodes[192]["Dharma Mittra picture URL"]=""
    DG.nodes[192]["wikipedia"] = ""
    DG.nodes[192]["asanas 608 page"]=""
    DG.nodes[192]["asanas 608 english name"]=""

    DG.add_node(193,english_name="")
    DG.nodes[193]["two_sided"]=False
    DG.nodes[193]["body areas"] = []
    DG.nodes[193]["description"]=""
    DG.nodes[193]["yogajournalurl"]=""
    DG.nodes[193]["yogajournal_picture"]=""
    DG.nodes[193]["hindi_name"]=""
    DG.nodes[193]["counter asana"] = None
    DG.nodes[193]["comment"]=""
    DG.nodes[193]["Dharma Mittra picture URL"]=""
    DG.nodes[193]["wikipedia"] = ""
    DG.nodes[193]["asanas 608 page"]=""
    DG.nodes[193]["asanas 608 english name"]=""

    DG.add_node(194,english_name="")
    DG.nodes[194]["two_sided"]=False
    DG.nodes[194]["body areas"] = []
    DG.nodes[194]["description"]=""
    DG.nodes[194]["yogajournalurl"]=""
    DG.nodes[194]["yogajournal_picture"]=""
    DG.nodes[194]["hindi_name"]=""
    DG.nodes[194]["counter asana"] = None
    DG.nodes[194]["comment"]=""
    DG.nodes[194]["Dharma Mittra picture URL"]=""
    DG.nodes[194]["wikipedia"] = ""
    DG.nodes[194]["asanas 608 page"]=""
    DG.nodes[194]["asanas 608 english name"]=""

    DG.add_node(195,english_name="")
    DG.nodes[195]["two_sided"]=False
    DG.nodes[195]["body areas"] = []
    DG.nodes[195]["description"]=""
    DG.nodes[195]["yogajournalurl"]=""
    DG.nodes[195]["yogajournal_picture"]=""
    DG.nodes[195]["hindi_name"]=""
    DG.nodes[195]["counter asana"] = None
    DG.nodes[195]["comment"]=""
    DG.nodes[195]["Dharma Mittra picture URL"]=""
    DG.nodes[195]["wikipedia"] = ""
    DG.nodes[195]["asanas 608 page"]=""
    DG.nodes[195]["asanas 608 english name"]=""

    DG.add_node(196,english_name="")
    DG.nodes[196]["two_sided"]=False
    DG.nodes[196]["body areas"] = []
    DG.nodes[196]["description"]=""
    DG.nodes[196]["yogajournalurl"]=""
    DG.nodes[196]["yogajournal_picture"]=""
    DG.nodes[196]["hindi_name"]=""
    DG.nodes[196]["counter asana"] = None
    DG.nodes[196]["comment"]=""
    DG.nodes[196]["Dharma Mittra picture URL"]=""
    DG.nodes[196]["wikipedia"] = ""
    DG.nodes[196]["asanas 608 page"]=""
    DG.nodes[196]["asanas 608 english name"]=""

    DG.add_node(197,english_name="")
    DG.nodes[197]["two_sided"]=False
    DG.nodes[197]["body areas"] = []
    DG.nodes[197]["description"]=""
    DG.nodes[197]["yogajournalurl"]=""
    DG.nodes[197]["yogajournal_picture"]=""
    DG.nodes[197]["hindi_name"]=""
    DG.nodes[197]["counter asana"] = None
    DG.nodes[197]["comment"]=""
    DG.nodes[197]["Dharma Mittra picture URL"]=""
    DG.nodes[197]["wikipedia"] = ""
    DG.nodes[197]["asanas 608 page"]=""
    DG.nodes[197]["asanas 608 english name"]=""

    DG.add_node(198,english_name="")
    DG.nodes[198]["two_sided"]=False
    DG.nodes[198]["body areas"] = []
    DG.nodes[198]["description"]=""
    DG.nodes[198]["yogajournalurl"]=""
    DG.nodes[198]["yogajournal_picture"]=""
    DG.nodes[198]["hindi_name"]=""
    DG.nodes[198]["counter asana"] = None
    DG.nodes[198]["comment"]=""
    DG.nodes[198]["Dharma Mittra picture URL"]=""
    DG.nodes[198]["wikipedia"] = ""
    DG.nodes[198]["asanas 608 page"]=""
    DG.nodes[198]["asanas 608 english name"]=""

    DG.add_node(199,english_name="")
    DG.nodes[199]["two_sided"]=False
    DG.nodes[199]["body areas"] = []
    DG.nodes[199]["description"]=""
    DG.nodes[199]["yogajournalurl"]=""
    DG.nodes[199]["yogajournal_picture"]=""
    DG.nodes[199]["hindi_name"]=""
    DG.nodes[199]["counter asana"] = None
    DG.nodes[199]["comment"]=""
    DG.nodes[199]["Dharma Mittra picture URL"]=""
    DG.nodes[199]["wikipedia"] = ""
    DG.nodes[199]["asanas 608 page"]=""
    DG.nodes[199]["asanas 608 english name"]=""

    return DG


"""
    DG.add_node(0,english_name="")
    DG.nodes[0]["two_sided"]=False
    DG.nodes[0]["body areas"] = []
    DG.nodes[0]["description"]=""
    DG.nodes[0]["yogajournalurl"]=""
    DG.nodes[0]["yogajournal_picture"]=""
    DG.nodes[0]["hindi_name"]=""
    DG.nodes[0]["counter asana"] = None
    DG.nodes[0]["comment"]=""
    DG.nodes[0]["Dharma Mittra picture URL"]=""
    DG.nodes[0]["wikipedia"] = ""
    DG.nodes[0]["asanas 608 page"]=""
    DG.nodes[0]["asanas 608 english name"]=""

    DG.add_node(1,english_name="")
    DG.nodes[1]["two_sided"]=False
    DG.nodes[1]["body areas"] = []
    DG.nodes[1]["description"]=""
    DG.nodes[1]["yogajournalurl"]=""
    DG.nodes[1]["yogajournal_picture"]=""
    DG.nodes[1]["hindi_name"]=""
    DG.nodes[1]["counter asana"] = None
    DG.nodes[1]["comment"]=""
    DG.nodes[1]["Dharma Mittra picture URL"]=""
    DG.nodes[1]["wikipedia"] = ""
    DG.nodes[1]["asanas 608 page"]=""
    DG.nodes[1]["asanas 608 english name"]=""

    DG.add_node(2,english_name="")
    DG.nodes[2]["two_sided"]=False
    DG.nodes[2]["body areas"] = []
    DG.nodes[2]["description"]=""
    DG.nodes[2]["yogajournalurl"]=""
    DG.nodes[2]["yogajournal_picture"]=""
    DG.nodes[2]["hindi_name"]=""
    DG.nodes[2]["counter asana"] = None
    DG.nodes[2]["comment"]=""
    DG.nodes[2]["Dharma Mittra picture URL"]=""
    DG.nodes[2]["wikipedia"] = ""
    DG.nodes[2]["asanas 608 page"]=""
    DG.nodes[2]["asanas 608 english name"]=""

    DG.add_node(3,english_name="")
    DG.nodes[3]["two_sided"]=False
    DG.nodes[3]["body areas"] = []
    DG.nodes[3]["description"]=""
    DG.nodes[3]["yogajournalurl"]=""
    DG.nodes[3]["yogajournal_picture"]=""
    DG.nodes[3]["hindi_name"]=""
    DG.nodes[3]["counter asana"] = None
    DG.nodes[3]["comment"]=""
    DG.nodes[3]["Dharma Mittra picture URL"]=""
    DG.nodes[3]["wikipedia"] = ""
    DG.nodes[3]["asanas 608 page"]=""
    DG.nodes[3]["asanas 608 english name"]=""

    DG.add_node(4,english_name="")
    DG.nodes[4]["two_sided"]=False
    DG.nodes[4]["body areas"] = []
    DG.nodes[4]["description"]=""
    DG.nodes[4]["yogajournalurl"]=""
    DG.nodes[4]["yogajournal_picture"]=""
    DG.nodes[4]["hindi_name"]=""
    DG.nodes[4]["counter asana"] = None
    DG.nodes[4]["comment"]=""
    DG.nodes[4]["Dharma Mittra picture URL"]=""
    DG.nodes[4]["wikipedia"] = ""
    DG.nodes[4]["asanas 608 page"]=""
    DG.nodes[4]["asanas 608 english name"]=""

    DG.add_node(5,english_name="")
    DG.nodes[5]["two_sided"]=False
    DG.nodes[5]["body areas"] = []
    DG.nodes[5]["description"]=""
    DG.nodes[5]["yogajournalurl"]=""
    DG.nodes[5]["yogajournal_picture"]=""
    DG.nodes[5]["hindi_name"]=""
    DG.nodes[5]["counter asana"] = None
    DG.nodes[5]["comment"]=""
    DG.nodes[5]["Dharma Mittra picture URL"]=""
    DG.nodes[5]["wikipedia"] = ""
    DG.nodes[5]["asanas 608 page"]=""
    DG.nodes[5]["asanas 608 english name"]=""

    DG.add_node(6,english_name="")
    DG.nodes[6]["two_sided"]=False
    DG.nodes[6]["body areas"] = []
    DG.nodes[6]["description"]=""
    DG.nodes[6]["yogajournalurl"]=""
    DG.nodes[6]["yogajournal_picture"]=""
    DG.nodes[6]["hindi_name"]=""
    DG.nodes[6]["counter asana"] = None
    DG.nodes[6]["comment"]=""
    DG.nodes[6]["Dharma Mittra picture URL"]=""
    DG.nodes[6]["wikipedia"] = ""
    DG.nodes[6]["asanas 608 page"]=""
    DG.nodes[6]["asanas 608 english name"]=""

    DG.add_node(7,english_name="")
    DG.nodes[7]["two_sided"]=False
    DG.nodes[7]["body areas"] = []
    DG.nodes[7]["description"]=""
    DG.nodes[7]["yogajournalurl"]=""
    DG.nodes[7]["yogajournal_picture"]=""
    DG.nodes[7]["hindi_name"]=""
    DG.nodes[7]["counter asana"] = None
    DG.nodes[7]["comment"]=""
    DG.nodes[7]["Dharma Mittra picture URL"]=""
    DG.nodes[7]["wikipedia"] = ""
    DG.nodes[7]["asanas 608 page"]=""
    DG.nodes[7]["asanas 608 english name"]=""

    DG.add_node(8,english_name="")
    DG.nodes[8]["two_sided"]=False
    DG.nodes[8]["body areas"] = []
    DG.nodes[8]["description"]=""
    DG.nodes[8]["yogajournalurl"]=""
    DG.nodes[8]["yogajournal_picture"]=""
    DG.nodes[8]["hindi_name"]=""
    DG.nodes[8]["counter asana"] = None
    DG.nodes[8]["comment"]=""
    DG.nodes[8]["Dharma Mittra picture URL"]=""
    DG.nodes[8]["wikipedia"] = ""
    DG.nodes[8]["asanas 608 page"]=""
    DG.nodes[8]["asanas 608 english name"]=""

    DG.add_node(9,english_name="")
    DG.nodes[9]["two_sided"]=False
    DG.nodes[9]["body areas"] = []
    DG.nodes[9]["description"]=""
    DG.nodes[9]["yogajournalurl"]=""
    DG.nodes[9]["yogajournal_picture"]=""
    DG.nodes[9]["hindi_name"]=""
    DG.nodes[9]["counter asana"] = None
    DG.nodes[9]["comment"]=""
    DG.nodes[9]["Dharma Mittra picture URL"]=""
    DG.nodes[9]["wikipedia"] = ""
    DG.nodes[9]["asanas 608 page"]=""
    DG.nodes[9]["asanas 608 english name"]=""
"""


def pose_transitions(DG):
    """
    graph edges
    """
    DG.add_weighted_edges_from([(0, 2, 1)])  # 0 = all fours; 2 = cat
    DG.add_weighted_edges_from([(0, 1, 1)])  # 0 = all fours; 1 = cow
    DG.add_weighted_edges_from([(0, 3, 1)])  # 0 = all fours; 3 = child's pose
    DG.add_weighted_edges_from([(0, 4, 2)])  # 0 = all fours; 4 = downward dog
    DG.add_weighted_edges_from([(0, 6, 1)])  # 0 = all fours; 6 = lay on stomach
    DG.add_weighted_edges_from([(0, 13, 2)])  # 0 = all fours; 13 = plank
    DG.add_weighted_edges_from(
        [(0, 80, 2)]
    )  # 0 = all fours; 80 = all fours, one arm extended
    DG.add_weighted_edges_from(
        [(0, 81, 2)]
    )  # 0 = all fours; 81 = all fours, one leg extended
    DG.add_weighted_edges_from(
        [(0, 82, 3)]
    )  # 0 = all fours; 82 = all fours, one arm extended, oppposite leg extended
    DG.add_weighted_edges_from(
        [(0, 83, 4)]
    )  # 0 = all fours; 83 = all fours, one arm extended, same side leg extended
    DG.add_weighted_edges_from(
        [(0, 84, 1)]
    )  # 0 = all fours; 84 = all fours, hips to one side

    DG.add_weighted_edges_from([(1, 0, 1)])  # 1 = cow; 0 = all fours
    DG.add_weighted_edges_from([(1, 4, 1)])  # 1 = cow; 4 = downward dog

    DG.add_weighted_edges_from([(2, 0, 1)])  # 2 = cat; 0 = all fours
    DG.add_weighted_edges_from([(2, 4, 1)])  # 2 = cat; 4 = downward dog

    DG.add_weighted_edges_from([(3, 0, 1)])  # 3 = child's pose; 0 = all fours
    DG.add_weighted_edges_from([(3, 4, 1)])  # 3 = child's pose; 4 = downward dog
    DG.add_weighted_edges_from([(3, 5, 1)])  # 3 = child's pose; 5 = dolphin
    DG.add_weighted_edges_from([(3, 6, 1)])  # 3 = child's pose; 6 = lay on stomach
    DG.add_weighted_edges_from([(3, 41, 1)])  # 3 = child's pose; 41 = kneeling on shins
    DG.add_weighted_edges_from([(3, 42, 1)])  # 3 = child's pose; 42 = standing on shins
    DG.add_weighted_edges_from([(3, 59, 1)])  # 3 = child's pose; 59 = arms to side

    DG.add_weighted_edges_from([(4, 0, 1)])  # 4 = downward dog; 0 = all fours
    DG.add_weighted_edges_from([(4, 1, 1)])  # 4 = downward dog; 1 = cow
    DG.add_weighted_edges_from([(4, 2, 1)])  # 4 = downward dog; 2 = cat
    DG.add_weighted_edges_from([(4, 3, 1)])  # 4 = downward dog; 3 = child's pose
    DG.add_weighted_edges_from([(4, 13, 1)])  # 4 = downward dog; 13 = plank
    DG.add_weighted_edges_from(
        [(4, 17, 1)]
    )  # 4 = downward dog; 17 = standing bend, legs together
    DG.add_weighted_edges_from(
        [(4, 18, 1)]
    )  # 4 = downward dog; 18 = downward dog, one leg raised
    DG.add_weighted_edges_from([(4, 47, 2)])  # 4 = downward dog; 47 = upward dog
    DG.add_weighted_edges_from(
        [(4, 68, 1)]
    )  # 4 = downward dog; 68 = standing bend, legs apart
    DG.add_weighted_edges_from([(4, 73, 1)])  # 4 = downward dog; 73 = peddle feet
    DG.add_weighted_edges_from([(4, 76, 5)])  # 4 = downward dog; 76 = inverted tripod
    DG.add_weighted_edges_from([(4, 160, 5)])  # 4 = downward dog; 76 = inverted tripod

    DG.add_weighted_edges_from([(5, 3, 1)])  # 5 = dolphin; 3 = child's pose
    DG.add_weighted_edges_from([(5, 4, 1)])  # 5 = dolphin; 4 = downward dog
    DG.add_weighted_edges_from([(5, 6, 1)])  # 5 = dolphin; 6 = lay on stomach
    DG.add_weighted_edges_from([(5, 85, 1)])  # 5 = dolphin; 13 = forearm plank
    DG.add_weighted_edges_from([(5, 124, 1)])  # 5 = dolphin; 13 = forearm plank

    DG.add_weighted_edges_from([(6, 0, 1)])  # 6 = lay on stomach; 0 = all fours
    DG.add_weighted_edges_from([(6, 3, 1)])  # 6 = lay on stomach; 3 = child's pose
    DG.add_weighted_edges_from([(6, 5, 1)])  # 6 = lay on stomach; 5 = dolphin
    DG.add_weighted_edges_from([(6, 7, 1)])  # 6 = lay on stomach; 7 = bow pose

    DG.add_weighted_edges_from([(7, 6, 1)])  # 7 = bow pose; 6 = lay on stomach

    DG.add_weighted_edges_from(
        [(8, 9, 1)]
    )  # 8 = laying on back, one leg extended up; 9 = both legs extended up
    DG.add_weighted_edges_from(
        [(8, 31, 1)]
    )  # 8 = laying on back, one leg extended up; 31 = corpse

    DG.add_weighted_edges_from(
        [(9, 8, 1)]
    )  # 9 = both legs extended up; 8 = lying on back, one leg extended up
    DG.add_weighted_edges_from(
        [(9, 10, 1)]
    )  # 9 = both legs extended up; 10 = supported shoulder stand
    DG.add_weighted_edges_from([(9, 31, 1)])  # 9 = both legs extended up; 31 = corpse
    DG.add_weighted_edges_from(
        [(9, 32, 1)]
    )  # 9 = both legs extended up; 32 = happy baby

    DG.add_weighted_edges_from(
        [(10, 9, 1)]
    )  # 10 = supported shoulder stand; 9 = both legs extended up
    DG.add_weighted_edges_from(
        [(10, 11, 1)]
    )  # 10 = supported shoulder stand; 11 = plow
    DG.add_weighted_edges_from(
        [(10, 12, 1)]
    )  # 10 = supported shoulder stand; 12 = ear pressure

    DG.add_weighted_edges_from(
        [(11, 10, 1)]
    )  # 11 = plow; 10 = supported shoulder stand
    DG.add_weighted_edges_from([(11, 12, 1)])  # 11 = plow; 12 = ear pressure

    DG.add_weighted_edges_from(
        [(12, 10, 1)]
    )  # 12 = ear pressure; 10 = supported shoulder stand
    DG.add_weighted_edges_from([(12, 11, 1)])  # 12 = ear pressure; 11 = plow

    DG.add_weighted_edges_from([(13, 0, 1)])  # 13 = plank; 0 = all fours
    DG.add_weighted_edges_from([(13, 4, 1)])  # 13 = plank; 4 = downward dog
    DG.add_weighted_edges_from([(13, 14, 1)])  # 13 = plank; 14 = wild thing
    DG.add_weighted_edges_from([(13, 15, 1)])  # 13 = plank; 15 = low pushup
    DG.add_weighted_edges_from([(13, 16, 1)])  # 13 = plank; 16 = side plank
    DG.add_weighted_edges_from([(13, 37, 1)])  # 13 = plank; 37 = pigeon pose
    DG.add_weighted_edges_from([(13, 44, 1)])  # 13 = plank; 44 = crow
    DG.add_weighted_edges_from(
        [(13, 48, 1)]
    )  # 13 = plank; 48 = one leg forward with knee bent
    DG.add_weighted_edges_from([(13, 85, 1)])  # 13 = plank; 85 = forearm plank

    DG.add_weighted_edges_from([(14, 13, 1)])  # 14 = wild thing; 13 = plank
    DG.add_weighted_edges_from([(14, 37, 1)])  # 14 = wild thing; 37 = pigeon pose

    DG.add_weighted_edges_from([(15, 13, 1)])  # 15 = low pushup; 13 = plank
    DG.add_weighted_edges_from([(15, 44, 4)])  # 15 = low pushup; 44 = crow
    DG.add_weighted_edges_from([(15, 47, 1)])  # 15 = low pushup; 47 = upward dog

    DG.add_weighted_edges_from([(16, 13, 1)])  # 16 = side plank; 13 = plank

    DG.add_weighted_edges_from(
        [(17, 4, 1)]
    )  # 17 = standing bend, legs together; 4 = downward dog
    DG.add_weighted_edges_from(
        [(17, 20, 1)]
    )  # 17 = standing bend, legs together; 20 = stand straight (mountain)
    DG.add_weighted_edges_from(
        [(17, 68, 1)]
    )  # 17 = standing bend, legs together; 68 = standing bend, legs apart

    DG.add_weighted_edges_from(
        [(18, 4, 1)]
    )  # 18 = downward dog, one leg raised; 4 = downward dog
    DG.add_weighted_edges_from(
        [(18, 19, 1)]
    )  # 18 = downward dog, one leg raised; 19 = flipped dog

    DG.add_weighted_edges_from(
        [(19, 18, 1)]
    )  # 19 = flipped dog; 18 = downward dog, one leg raised
    DG.add_weighted_edges_from([(19, 28, 1)])  # 19 = flipped dog; 28 = wheel

    DG.add_weighted_edges_from(
        [(20, 17, 1)]
    )  # 20 = stand straight (mountain); 17 = standing bend, legs together
    DG.add_weighted_edges_from(
        [(20, 21, 1)]
    )  # 20 = stand straight (mountain); 21 = happy camper
    DG.add_weighted_edges_from(
        [(20, 23, 1)]
    )  # 20 = stand straight (mountain); 23 = warrior 3
    DG.add_weighted_edges_from(
        [(20, 24, 1)]
    )  # 20 = stand straight (mountain); 24 = warrior 1
    DG.add_weighted_edges_from(
        [(20, 27, 1)]
    )  # 20 = stand straight (mountain); 27 = chair
    DG.add_weighted_edges_from(
        [(20, 28, 1)]
    )  # 20 = stand straight (mountain); 28 = wheel
    DG.add_weighted_edges_from(
        [(20, 87, 1)]
    )  # 20 = stand straight (mountain); 87 = standing back bend
    DG.add_weighted_edges_from(
        [(20, 46, 1)]
    )  # 20 = stand straight (mountain); 46 = standing, legs apart
    DG.add_weighted_edges_from(
        [(20, 94, 1)]
    )  # 20 = stand straight (mountain); 94 =
    DG.add_weighted_edges_from(
        [(20, 98, 1)]
    )  # 20 = stand straight (mountain); 98 =


    DG.add_weighted_edges_from(
        [(21, 20, 1)]
    )  # 21 = happy camper; 20 = stand straight (mountain)
    DG.add_weighted_edges_from([(21, 27, 1)])  # 21 = happy camper; 27 = chair
    DG.add_weighted_edges_from([(21, 72, 1)])  # 21 = happy camper; 72 = flying pigeon

    DG.add_weighted_edges_from(
        [(22, 20, 1)]
    )  # 22 = tree pose; 20 = stand straight (mountain)
    DG.add_weighted_edges_from([(22, 21, 1)])  # 22 = tree pose; 21 = happy camper
    DG.add_weighted_edges_from([(22, 23, 1)])  # 22 = tree pose; 23 = warrior 3

    DG.add_weighted_edges_from(
        [(23, 20, 1)]
    )  # 23 = warrior 3; 20 = stand straight (mountain)
    DG.add_weighted_edges_from([(23, 22, 1)])  # 23 = warrior 3; 22 = tree pose
    DG.add_weighted_edges_from([(23, 24, 1)])  # 23 = warrior 3; 24 = warrior 1
    DG.add_weighted_edges_from([(23, 25, 1)])  # 23 = warrior 3; 25 = dancer pose
    DG.add_weighted_edges_from([(23, 26, 1)])  # 23 = warrior 3; 26 = standing splits
    DG.add_weighted_edges_from(
        [(23, 48, 1)]
    )  # 23 = warrior 3; 48 = one leg forward with knee bent

    DG.add_weighted_edges_from(
        [(24, 20, 1)]
    )  # 24 = warrior 1; 20 = stand straight (mountain)
    DG.add_weighted_edges_from([(24, 23, 1)])  # 24 = warrior 1; 23 = warrior 3
    DG.add_weighted_edges_from([(24, 29, 1)])  # 24 = warrior 1; 29 = warrior 2

    DG.add_weighted_edges_from([(25, 23, 1)])  # 25 = dancer pose; 23 = warrior 3

    DG.add_weighted_edges_from([(26, 23, 1)])  # 26 = standing splits; 23 = warrior 3

    DG.add_weighted_edges_from(
        [(27, 20, 1)]
    )  # 27 = chair; 20 = stand straight (mountain)
    DG.add_weighted_edges_from([(27, 21, 1)])  # 27 = chair; 21 = happy camper

    DG.add_weighted_edges_from([(28, 19, 1)])  # 28 = wheel; 19 = flipped dog
    DG.add_weighted_edges_from(
        [(28, 20, 1)]
    )  # 28 = wheel; 20 = stand straight (mountain)
    DG.add_weighted_edges_from([(28, 31, 1)])  # 28 = wheel; 31 = corpse
    DG.add_weighted_edges_from([(28, 100, 1)])  # 28 = wheel;
    DG.add_weighted_edges_from([(28, 108, 1)])  # 28 = wheel;

    DG.add_weighted_edges_from([(29, 24, 1)])  # 29 = warrior 2; 24 = warrior 1
    DG.add_weighted_edges_from([(29, 30, 1)])  # 29 = warrior 2; 30 =
    DG.add_weighted_edges_from([(29, 56, 1)])  # 29 = warrior 2; 56 =
    DG.add_weighted_edges_from([(29, 60, 1)])  # 29 = warrior 2; 60 =

    DG.add_weighted_edges_from([(30, 29, 1)])  # 30 = peaceful warrior; 29 = warrior

    DG.add_weighted_edges_from([(31, 8, 1)])  # 31 = corpse; 8 = one leg extended up
    DG.add_weighted_edges_from([(31, 9, 1)])  # 31 = corpse; 9 = both legs extended up
    DG.add_weighted_edges_from([(31, 28, 1)])  # 31 = corpse; 28 = wheel
    DG.add_weighted_edges_from([(31, 32, 1)])  # 31 = corpse; 32 = happy baby
    DG.add_weighted_edges_from(
        [(31, 34, 1)]
    )  # 31 = corpse; 34 = on back, knees bent, feet in air
    DG.add_weighted_edges_from([(31, 36, 1)])  # 31 = corpse; 36 = staff
    DG.add_weighted_edges_from([(31, 45, 1)])  # 31 = corpse; 45 = squat, knees wide
    DG.add_weighted_edges_from([(31, 97, 1)])  # 31 = corpse; 97 = boat
    DG.add_weighted_edges_from([(31, 136, 1)])  # 31 = corpse;
    DG.add_weighted_edges_from([(31, 137, 1)])  # 31 = corpse;
    DG.add_weighted_edges_from([(31, 148, 1)])  # 31 = corpse;
    DG.add_weighted_edges_from([(31, 172, 1)])  # 31 = corpse; 172 = sphinx

    DG.add_weighted_edges_from(
        [(32, 9, 1)]
    )  # 32 = happy baby; 9 = both legs extended up
    DG.add_weighted_edges_from([(32, 31, 1)])  # 32 = happy baby; 31 = corpse

    DG.add_weighted_edges_from(
        [(33, 34, 1)]
    )  # 33 = on back, knees bent, feet on ground; 34 = on back, knees bent, feet in air
    DG.add_weighted_edges_from(
        [(33, 35, 1)]
    )  # 33 = on back, knees bent, feet on ground; 35 = knees to one side, head to other

    DG.add_weighted_edges_from(
        [(34, 31, 1)]
    )  # 34 = on back, knees bent, feet in air; 31 = corpse
    DG.add_weighted_edges_from(
        [(34, 33, 1)]
    )  # 34 = on back, knees bent, feet in air; 33 = on back, knees bent, feet on ground
    DG.add_weighted_edges_from(
        [(34, 35, 1)]
    )  # 34 = on back, knees bent, feet in air; 35 = knees to one side, head to other

    DG.add_weighted_edges_from(
        [(35, 33, 1)]
    )  # 35 = knees to one side, head to other; 33 = on back, knees bent, feet on ground
    DG.add_weighted_edges_from(
        [(35, 34, 1)]
    )  # 35 = knees to one side, head to other; 34 = on back, knees bent, feet in air

    DG.add_weighted_edges_from([(36, 31, 1)])  # 36 = staff; 31 = corpse
    DG.add_weighted_edges_from(
        [(36, 38, 1)]
    )  # 36 = staff; 38 = one leg straight, one leg in
    DG.add_weighted_edges_from([(36, 45, 1)])  # 36 = staff; 45 = squat, knees wide
    DG.add_weighted_edges_from([(36, 49, 1)])  # 36 = staff; 49 = half lotus
    DG.add_weighted_edges_from([(36, 53, 1)])  # 36 = staff; 53 =

    DG.add_weighted_edges_from([(37, 13, 1)])  # 37 = pigeon pose; 13 = plank
    DG.add_weighted_edges_from([(37, 14, 1)])  # 37 = pigeon pose; 14 = wild thing

    DG.add_weighted_edges_from(
        [(38, 36, 1)]
    )  # 38 = one leg straight, one leg in; 36 = staff
    DG.add_weighted_edges_from(
        [(38, 39, 1)]
    )  # 38 = one leg straight, one leg in; 39 = compass pose
    DG.add_weighted_edges_from(
        [(38, 40, 1)]
    )  # 38 = one leg straight, one leg in; 40 = rock bent leg

    DG.add_weighted_edges_from(
        [(39, 38, 1)]
    )  # 39 = compass pose; 38 = one leg straight, one leg in
    DG.add_weighted_edges_from([(39, 40, 1)])  # 39 = compass pose; 40 = rock bent leg

    DG.add_weighted_edges_from(
        [(40, 38, 1)]
    )  # 40 = rock bent leg; 38 = one leg straight, one leg in
    DG.add_weighted_edges_from(
        [(40, 70, 1)]
    )  # 40 = rock bent leg; 70 = floating elephant trunk; one leg over arm
    DG.add_weighted_edges_from([(40, 39, 1)])  # 40 = rock bent leg; 39 = compass pose

    DG.add_weighted_edges_from([(41, 3, 1)])  # 41 = kneeling on shins; 3 = child's pose
    DG.add_weighted_edges_from(
        [(41, 42, 1)]
    )  # 41 = kneeling on shins; 42 = standing on shins

    DG.add_weighted_edges_from([(42, 3, 1)])  # 42 = standing on shins; 3 = child's pose
    DG.add_weighted_edges_from(
        [(42, 41, 1)]
    )  # 42 = standing on shins; 41 = kneeling on shins
    DG.add_weighted_edges_from([(42, 43, 1)])  # 42 = standing on shins; 43 = camel pose

    DG.add_weighted_edges_from([(43, 42, 1)])  # 43 = camel pose; 42 = standing on shins

    DG.add_weighted_edges_from([(44, 15, 1)])  # 44 = crow; 15 = low pushup
    DG.add_weighted_edges_from([(44, 45, 1)])  # 44 = crow; 45 = squat, knees wide
    DG.add_weighted_edges_from([(44, 54, 1)])

    DG.add_weighted_edges_from([(45, 31, 1)])  # 45 = squat, knees wide; 31 = corpse
    DG.add_weighted_edges_from([(45, 36, 1)])  # 45 = squat, knees wide; 36 = staff
    DG.add_weighted_edges_from([(45, 44, 1)])  # 45 = squat, knees wide; 44 = crow
    DG.add_weighted_edges_from(
        [(45, 46, 1)]
    )  # 45 = squat, knees wide; 46 = standing, legs apart
    DG.add_weighted_edges_from([(45, 54, 1)])  # 45 = squat, knees wide; 54 =
    DG.add_weighted_edges_from([(45, 69, 1)])  # 45 = squat, knees wide; 69 =

    DG.add_weighted_edges_from(
        [(46, 45, 1)]
    )  # 46 = standing, legs apart; 45 = squat, knees wide
    DG.add_weighted_edges_from(
        [(46, 20, 1)]
    )  # 46 = standing, legs apart; 20 = stand straight (mountain)
    DG.add_weighted_edges_from(
        [(46, 68, 1)]
    )  # 46 = standing, legs apart; 68 = standing bend, legs apart

    DG.add_weighted_edges_from([(47, 4, 1)])  # 47 = upward dog; 4 = downward dog
    DG.add_weighted_edges_from([(47, 15, 1)])  # 47 = upward dog; 15 = low pushup

    DG.add_weighted_edges_from(
        [(48, 13, 1)]
    )  # 48 = one leg forward with knee bent; 13 = plank
    DG.add_weighted_edges_from(
        [(48, 23, 1)]
    )  # 48 = one leg forward with knee bent; 23 = warrior 3

    DG.add_weighted_edges_from([(49, 36, 1)])  # 49 = half lotus; 36 = staff
    DG.add_weighted_edges_from([(49, 50, 1)])  # 49 = half lotus; 50 = full lotus

    DG.add_weighted_edges_from([(50, 49, 1)])  # 50 = full lotus; 49 = half lotus
    DG.add_weighted_edges_from([(50, 51, 1)])  # 50 = full lotus; 51 = embryo pose
    DG.add_weighted_edges_from([(50, 52, 1)])  # 50 = full lotus; 52 = flying lotus
    DG.add_weighted_edges_from([(50, 122, 1)])  # 50 = full lotus;

    DG.add_weighted_edges_from([(51, 50, 1)])  # 51 = embryo pose; 50 = full lotus

    DG.add_weighted_edges_from([(52, 50, 1)])  # 52 = flying lotus; 50 = full lotus

    DG.add_weighted_edges_from([(53, 36, 1)])  # 53 = floating staff pose; 36 = staff

    DG.add_weighted_edges_from([(54, 45, 1)])  # 54 = crane; 45 = squat, knees wide
    DG.add_weighted_edges_from([(54, 44, 1)])
    DG.add_weighted_edges_from([(54, 55, 1)])  # 54 = crane; 55 =
    DG.add_weighted_edges_from(
        [(54, 69, 1)]
    )  # 54 = crane; 69 = tripod head stand, legs bent, arms at 90deg

    DG.add_weighted_edges_from([(55, 54, 1)])  # 55 = one-legged crane; 54 = crane

    DG.add_weighted_edges_from(
        [(56, 29, 1)]
    )  # 56 = wide legs, feet parallel; 29 = warrior 2
    DG.add_weighted_edges_from(
        [(56, 57, 1)]
    )  # 56 = wide legs, feet parallel; 57 = bent over wide legs, parallel feet

    DG.add_weighted_edges_from(
        [(57, 56, 1)]
    )  # 57 = bent over wide legs, parallel feet; 56 = wide legs, feet parallel
    DG.add_weighted_edges_from(
        [(57, 69, 1)]
    )  # 57 = bent over wide legs, parallel feet; 69 = tripod head stand, legs bent, arms at 90deg

    DG.add_weighted_edges_from(
        [(58, 69, 1)]
    )  # 58 = tripod head stand, legs extended straight up, arms at 90deg; 69 = tripod head stand, legs bent, arms at 90deg
    DG.add_weighted_edges_from(
        [(58, 74, 1)]
    )  # 58 = tripod head stand, legs extended straight up, arms at 90deg; 74 = tripod head stand, legs extended out, arms at 90deg
    DG.add_weighted_edges_from(
        [(58, 75, 1)]
    )  # 58 = tripod head stand, legs extended straight up, arms at 90deg; 75 = no-handed head stand

    DG.add_weighted_edges_from([(59, 3, 1)])  # 59 = arms to side; 3 = child's pose

    DG.add_weighted_edges_from(
        [(60, 29, 1)]
    )  # 60 = both legs straight, front foot point forward, back foot flat at 45deg; 29 = warrior 2
    DG.add_weighted_edges_from(
        [(60, 61, 1)]
    )  # 60 = both legs straight, front foot point forward, back foot flat at 45deg; 61 = hinged forward at hips; 60 = both legs straight, front foot point forward, back foot flat at 45deg
    DG.add_weighted_edges_from(
        [(60, 63, 1)]
    )  # 60 = both legs straight, front foot point forward, back foot flat at 45deg; 63 = extended side angle pose

    DG.add_weighted_edges_from(
        [(61, 60, 1)]
    )  # 61 = hinged forward at hips; 60 = both legs straight, front foot point forward, back foot flat at 45deg
    DG.add_weighted_edges_from(
        [(61, 62, 1)]
    )  # 61 = hinged forward at hips; 62 = revolved triangle pose

    DG.add_weighted_edges_from(
        [(62, 61, 1)]
    )  # 62 = revolved triangle pose; 61 = hinged forward at hips

    DG.add_weighted_edges_from(
        [(63, 60, 1)]
    )  # 63 = extended side angle pose; 60 = both legs straight, front foot point forward, back foot flat at 45deg
    DG.add_weighted_edges_from(
        [(63, 64, 1)]
    )  # 63 = extended side angle pose; 64 = bind

    DG.add_weighted_edges_from(
        [(64, 63, 1)]
    )  # 64 = bind; 63 = extended side angle pose
    DG.add_weighted_edges_from([(64, 65, 1)])  # 64 = bind; 65 = bird of paradise

    DG.add_weighted_edges_from([(65, 64, 1)])  # 65 = bird of paradise; 64 = bind
    DG.add_weighted_edges_from(
        [(65, 67, 1)]
    )  # 65 = bird of paradise; 67 = standing bend bound twist
    DG.add_weighted_edges_from(
        [(65, 89, 1)]
    )  # 65 = bird of paradise; 89 = bird of paradise, bent forward, leg to side

    DG.add_weighted_edges_from(
        [(66, 67, 1)]
    )  # 66 = funky bird of paradise; 67 = standing bend bound twist

    DG.add_weighted_edges_from(
        [(67, 65, 1)]
    )  # 67 = standing bend bound twist; 65 = bird of paradise
    DG.add_weighted_edges_from(
        [(67, 68, 1)]
    )  # 67 = standing bend bound twist; 68 = standing bend, legs apart

    DG.add_weighted_edges_from(
        [(68, 4, 1)]
    )  # 68 = standing bend, legs apart; 4 = downward dog
    DG.add_weighted_edges_from(
        [(68, 17, 1)]
    )  # 68 = standing bend, legs apart; 17 = standing bend, legs together
    DG.add_weighted_edges_from(
        [(68, 46, 1)]
    )  # 68 = standing bend, legs apart; 46 = standing, legs apart
    DG.add_weighted_edges_from(
        [(68, 67, 1)]
    )  # 68 = standing bend, legs apart; 67 = standing bend bound twist

    DG.add_weighted_edges_from(
        [(69, 45, 1)]
    )  # 69 = tripod head stand, legs bent, arms at 90deg; 45 = squat, knees wide
    DG.add_weighted_edges_from(
        [(69, 54, 1)]
    )  # 69 = tripod head stand, legs bent, arms at 90deg; 54 =
    DG.add_weighted_edges_from(
        [(69, 57, 1)]
    )  # 69 = tripod head stand, legs bent, arms at 90deg; 57 =
    DG.add_weighted_edges_from(
        [(69, 58, 1)]
    )  # 69 = tripod head stand, legs bent, arms at 90deg; 58 = tripod head stand, legs extended straight up, arms at 90deg
    DG.add_weighted_edges_from(
        [(69, 86, 1)]
    )  # 69 = tripod head stand, legs bent, arms at 90deg; 86 = tripod head stand, legs bent, arms straight

    DG.add_weighted_edges_from(
        [(70, 40, 1)]
    )  # 70 = floating elephant trunk; one leg over arm; 40 = rock bent leg
    DG.add_weighted_edges_from(
        [(70, 71, 1)]
    )  # 70 = floating elephant trunk; one leg over arm; 71 = eight angle pose

    DG.add_weighted_edges_from(
        [(71, 70, 1)]
    )  # 71 = eight angle pose; 70 = floating elephant trunk; one leg over arm

    DG.add_weighted_edges_from([(72, 21, 1)])  # 72 = flying pigeon; 21 = happy camper

    DG.add_weighted_edges_from([(73, 4, 1)])  # 73 = peddle feet; 4 = downward dog

    DG.add_weighted_edges_from(
        [(74, 58, 1)]
    )  # 74 = tripod head stand, legs extended out, arms at 90deg; 58 = tripod head stand, legs extended straight up, arms at 90deg

    DG.add_weighted_edges_from(
        [(75, 58, 1)]
    )  # 75 = no-handed head stand; 58 = tripod head stand, legs extended straight up, arms at 90deg

    DG.add_weighted_edges_from([(76, 4, 1)])  # 76 = inverted tripod; 4 = downward dog

    DG.add_weighted_edges_from(
        [(77, 78, 1)]
    )  # 77 = seated wide-leg; 78 = seated wide-leg, floating
    DG.add_weighted_edges_from(
        [(77, 79, 1)]
    )  # 77 = seated wide-leg; 79 = seated wide-leg, flying
    DG.add_weighted_edges_from(
        [(77, 155, 1)])
    DG.add_weighted_edges_from(
        [(77, 91, 1)]) # 91 = "butterfly OR cobbler"
    DG.add_weighted_edges_from(
        [(77, 148, 1)])

    DG.add_weighted_edges_from(
        [(78, 77, 1)]
    )  # 78 = seated wide-leg, floating; 77 = seated wide-leg;

    DG.add_weighted_edges_from(
        [(79, 77, 1)]
    )  # 79 = seated wide-leg, flying; 77 = seated wide-leg

    DG.add_weighted_edges_from(
        [(80, 0, 2)]
    )  # 80 = all fours, one arm extended; 0 = all fours

    DG.add_weighted_edges_from(
        [(81, 0, 2)]
    )  # 81 = all fours, one leg extended; 0 = all fours

    DG.add_weighted_edges_from(
        [(82, 0, 3)]
    )  # 82 = all fours, one arm extended, oppposite leg extended; 0 = all fours

    DG.add_weighted_edges_from(
        [(83, 0, 4)]
    )  # 83 = all fours, one arm extended, same side leg extended; 0 = all fours;

    DG.add_weighted_edges_from(
        [(84, 0, 1)]
    )  # 84 = all fours, hips to one side; 0 = all fours

    DG.add_weighted_edges_from([(85, 13, 1)])  # 85 = forearm plank; 13 = plank

    DG.add_weighted_edges_from(
        [(86, 69, 1)]
    )  # 86 = tripod head stand, legs bent, arms straight; 69 = tripod head stand, legs bent, arms at 90deg
    DG.add_weighted_edges_from(
        [(86, 90, 1)]
    )  # 86 = tripod head stand, legs bent, arms straight; 90 = tripod head stand, legs straight, arms straight

    DG.add_weighted_edges_from(
        [(87, 20, 1)]
    )  # 87 = standing back bend; 20 = stand straight (mountain)

    #     DG.add_weighted_edges_from([(88,,1)])   # 88 = scorpion ;

    DG.add_weighted_edges_from(
        [(89, 65, 1)]
    )  # 89 = bird of paradise, bent forward, leg to side; 65 = bird of paradise

    DG.add_weighted_edges_from(
        [(90, 86, 1)]
    )  # 90 = tripod head stand, legs straight, arms straight; 86 = tripod head stand, legs bent, arms straight

    #DG.add_weighted_edges_from([(91,,1)])   # 91 = butterfly
    DG.add_weighted_edges_from([(91,148,1)])   # 91 = butterfly
    #DG.add_weighted_edges_from([(92,,1)])  # 92 = hurdler
    DG.add_weighted_edges_from([(98,99,1)])  #
    DG.add_weighted_edges_from([(99,98,1)])  #

    #DG.add_weighted_edges_from([(100,,1)]) # 100 = ;
    #DG.add_weighted_edges_from([(101,,1)]) # 101 = ;
    #DG.add_weighted_edges_from([(102,,1)]) # 102 = ;
    #DG.add_weighted_edges_from([(103,,1)]) # 103 = ;
    #DG.add_weighted_edges_from([(104,,1)]) # 104 = ;
    #DG.add_weighted_edges_from([(105,,1)]) # 105 = ;
    #DG.add_weighted_edges_from([(106,,1)]) # 106 = ;
    #DG.add_weighted_edges_from([(107,,1)]) # 107 = ;
    #DG.add_weighted_edges_from([(108,,1)]) # 108 = ;
    #DG.add_weighted_edges_from([(109,,1)]) # 109 = ;
    #DG.add_weighted_edges_from([(110,,1)]) # 110 = ;
    #DG.add_weighted_edges_from([(111,,1)]) # 111 = ;
    #DG.add_weighted_edges_from([(112,,1)]) # 112 = ;
    #DG.add_weighted_edges_from([(113,,1)]) # 113 = ;
    #DG.add_weighted_edges_from([(114,,1)]) # 114 = ;
    #DG.add_weighted_edges_from([(115,,1)]) # 115 = ;
    #DG.add_weighted_edges_from([(116,,1)]) # 116 = ;
    #DG.add_weighted_edges_from([(117,,1)]) # 117 = ;
    #DG.add_weighted_edges_from([(118,,1)]) # 118 = ;
    #DG.add_weighted_edges_from([(119,,1)]) # 119 = ;
    #DG.add_weighted_edges_from([(120,,1)]) # 120 = ;
    #DG.add_weighted_edges_from([(121,,1)]) # 121 = ;
    #DG.add_weighted_edges_from([(122,,1)]) # 122 = ;
    DG.add_weighted_edges_from([(122,50,1)]) # 122 = ;
    #DG.add_weighted_edges_from([(123,,1)]) # 123 = ;
    DG.add_weighted_edges_from([(124,5,1)]) # 124 = ;
    DG.add_weighted_edges_from([(124,153,1)]) # 124 = ;
    DG.add_weighted_edges_from([(124,158,1)]) # 124 = ;
    DG.add_weighted_edges_from([(124,159,1)]) # 124 = ;
    #DG.add_weighted_edges_from([(125,,1)]) # 125 = ;
    #DG.add_weighted_edges_from([(126,,1)]) # 126 = ;
    #DG.add_weighted_edges_from([(127,,1)]) # 127 = ;
    #DG.add_weighted_edges_from([(128,,1)]) # 128 = ;
    #DG.add_weighted_edges_from([(129,,1)]) # 129 = ;
    #DG.add_weighted_edges_from([(130,,1)]) # 130 = ;
    #DG.add_weighted_edges_from([(131,,1)]) # 131 = ;
    #DG.add_weighted_edges_from([(132,,1)]) # 132 = ;
    #DG.add_weighted_edges_from([(133,,1)]) # 133 = ;
    #DG.add_weighted_edges_from([(134,,1)]) # 134 = ;
    DG.add_weighted_edges_from([(135,172,1)]) # 135 = ;
    DG.add_weighted_edges_from([(136,31,1)]) # 136 = ;
    #DG.add_weighted_edges_from([(136,,1)]) # 136 = ;
    #DG.add_weighted_edges_from([(137,,1)]) # 137 = ;
    DG.add_weighted_edges_from([(137,31,1)]) # 137 = ;
    #DG.add_weighted_edges_from([(138,,1)]) # 138 = ;
    #DG.add_weighted_edges_from([(139,,1)]) # 139 = ;
    #DG.add_weighted_edges_from([(140,,1)]) # 140 = ;
    #DG.add_weighted_edges_from([(141,,1)]) # 141 = ;
    #DG.add_weighted_edges_from([(142,,1)]) # 142 = ;
    #DG.add_weighted_edges_from([(143,,1)]) # 143 = ;
    #DG.add_weighted_edges_from([(144,,1)]) # 144 = ;
    #DG.add_weighted_edges_from([(145,,1)]) # 145 = ;
    #DG.add_weighted_edges_from([(146,,1)]) # 146 = ;
    #DG.add_weighted_edges_from([(147,,1)]) # 147 = ;
    DG.add_weighted_edges_from([(148,31,1)]) # 148 = ;
    DG.add_weighted_edges_from([(148,77,1)]) # 148 = ;
    DG.add_weighted_edges_from([(148,91,1)]) # 148 = ;
    #DG.add_weighted_edges_from([(149,,1)]) # 149 = ;
    #DG.add_weighted_edges_from([(150,,1)]) # 150 = ;
    #DG.add_weighted_edges_from([(151,,1)]) # 151 = ;
    #DG.add_weighted_edges_from([(152,,1)]) # 152 = ;
    DG.add_weighted_edges_from([(153,124,1)]) # 153 = ;
    DG.add_weighted_edges_from([(153,158,1)]) # 153 = ;
    DG.add_weighted_edges_from([(153,159,1)]) # 153 = ;
    #DG.add_weighted_edges_from([(154,,1)]) # 154 = ;
    DG.add_weighted_edges_from([(155,77,1)])
    #DG.add_weighted_edges_from([(155,,1)]) # 155 = ;
    #DG.add_weighted_edges_from([(156,,1)]) # 156 = ;
    #DG.add_weighted_edges_from([(157,,1)]) # 157 = ;
    DG.add_weighted_edges_from([(158,124,1)]) # 158 = ;
    DG.add_weighted_edges_from([(158,153,1)]) # 158 = ;
    DG.add_weighted_edges_from([(158,159,1)]) # 158 = ;
    DG.add_weighted_edges_from([(159,124,1)]) # 159 = ;
    DG.add_weighted_edges_from([(159,153,1)]) # 159 = ;
    DG.add_weighted_edges_from([(159,158,1)]) # 159 = ;
    DG.add_weighted_edges_from([(160,4,1)]) # 160 = ;
    #DG.add_weighted_edges_from([(161,,1)]) # 161 = ;
    #DG.add_weighted_edges_from([(162,,1)]) # 162 = ;
    #DG.add_weighted_edges_from([(163,,1)]) # 163 = ;
    #DG.add_weighted_edges_from([(164,,1)]) # 164 = ;
    #DG.add_weighted_edges_from([(165,,1)]) # 165 = ;
    #DG.add_weighted_edges_from([(166,,1)]) # 166 = ;
    #DG.add_weighted_edges_from([(167,,1)]) # 167 = ;
    #DG.add_weighted_edges_from([(168,,1)]) # 168 = ;
    #DG.add_weighted_edges_from([(169,,1)]) # 169 = ;
    #DG.add_weighted_edges_from([(170,,1)]) # 170 = ;
    #DG.add_weighted_edges_from([(171,,1)]) # 171 = ;
    DG.add_weighted_edges_from([(172,31,1)]) # 172 = ;
    DG.add_weighted_edges_from([(172,135,1)]) # 172 = ;
    #DG.add_weighted_edges_from([(173,,1)]) # 173 = ;
    #DG.add_weighted_edges_from([(174,,1)]) # 174 = ;
    #DG.add_weighted_edges_from([(175,,1)]) # 175 = ;
    #DG.add_weighted_edges_from([(176,,1)]) # 176 = ;
    #DG.add_weighted_edges_from([(177,,1)]) # 177 = ;
    #DG.add_weighted_edges_from([(178,,1)]) # 178 = ;
    #DG.add_weighted_edges_from([(179,,1)]) # 179 = ;
    #DG.add_weighted_edges_from([(180,,1)]) # 180 = ;
    #DG.add_weighted_edges_from([(181,,1)]) # 181 = ;
    #DG.add_weighted_edges_from([(182,,1)]) # 182 = ;
    #DG.add_weighted_edges_from([(183,,1)]) # 183 = ;
    #DG.add_weighted_edges_from([(184,,1)]) # 184 = ;
    #DG.add_weighted_edges_from([(185,,1)]) # 185 = ;
    #DG.add_weighted_edges_from([(186,,1)]) # 186 = ;
    #DG.add_weighted_edges_from([(187,,1)]) # 187 = ;
    #DG.add_weighted_edges_from([(188,,1)]) # 188 = ;
    #DG.add_weighted_edges_from([(189,,1)]) # 189 = ;
    #DG.add_weighted_edges_from([(190,,1)]) # 190 = ;
    #DG.add_weighted_edges_from([(191,,1)]) # 191 = ;
    #DG.add_weighted_edges_from([(192,,1)]) # 192 = ;
    #DG.add_weighted_edges_from([(193,,1)]) # 193 = ;
    #DG.add_weighted_edges_from([(194,,1)]) # 194 = ;
    #DG.add_weighted_edges_from([(195,,1)]) # 195 = ;
    #DG.add_weighted_edges_from([(196,,1)]) # 196 = ;
    #DG.add_weighted_edges_from([(197,,1)]) # 197 = ;
    #DG.add_weighted_edges_from([(198,,1)]) # 198 = ;
    #DG.add_weighted_edges_from([(199,,1)]) # 199 = ;
    #DG.add_weighted_edges_from([(200,,1)]) # 200 = ;


    return DG
