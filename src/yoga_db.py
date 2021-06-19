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
https://www.yogajournal.com/pose-finder/pose-finder/
http://www.yogajournal.com/poses/finder/browse_categories
https://www.yogajournal.com/poses/types/standing/
https://www.yogajournal.com/poses/anatomy/hips/
https://www.yogajournal.com/poses/anatomy/knees/
https://www.yogajournal.com/poses/types/


https://www.dharmayogacenter.com/resources/yoga-poses/

https://en.wikipedia.org/wiki/List_of_asanas

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
    DG.nodes[0]["asanas 608 page"] = ""
    DG.nodes[0]["asanas 608 english name"] = ""

    DG.add_node(1, english_name="cow")
    DG.nodes[1]["two_sided"] = False
    DG.nodes[1]["description"] = "on all fours, pull chest to floor and head up"
    DG.nodes[1]["yogajournalurl"] = "https://www.yogajournal.com/poses/types/backbends/cow-pose/"
    DG.nodes[1][
        "yogajournal_picture"
    ] = "https://www.yogajournal.com/wp-content/uploads/2007/08/3hp_288_02_bjk2.jpg?crop=535:301&width=1070&enable=upscale"
    DG.nodes[1]["hindi_name"] = "marjaryasana"
    DG.nodes[1]["comment"] = ""
    DG.nodes[1][
        "Dharma Mittra picture URL"
    ] = ""
    DG.nodes[1]["asanas_608_page"] = "373"
    DG.nodes[1]["asanas_608_english"] = "cat stretch pose B"

    DG.add_node(2, english_name="cat")
    DG.nodes[2]["two_sided"] = False
    DG.nodes[2]["description"] = "on all fours, pull chest to ceiling and head down"
    DG.nodes[2]["yogajournalurl"] = "https://www.yogajournal.com/poses/cat-pose/"
    DG.nodes[2][
        "yogajournal_picture"
    ] = "https://www.yogajournal.com/wp-content/uploads/2007/08/2hp_286_0574_bjk.jpg?crop=535:301&width=1070&enable=upscale"
    DG.nodes[2]["hindi_name"] = "marjaryasana"
    DG.nodes[2]["comment"] = ""
    DG.nodes[2][
        "Dharma Mittra picture URL"
    ] = ""
    DG.nodes[2]["asanas_608_page"] = "372"
    DG.nodes[2]["asanas_608_english"] = "cat stretch pose A"

    DG.add_node(3, english_name="child's pose")
    DG.nodes[3]["two_sided"] = False
    DG.nodes[3]["description"] = "arms stretched above head, face to ground. On shins"
    DG.nodes[3]["yogajournalurl"] = "http://www.yogajournal.com/poses/475"
    DG.nodes[3][
        "yogajournal_picture"
    ] = ""
    DG.nodes[3]["hindi_name"] = ""
    DG.nodes[3]["comment"] = ""
    DG.nodes[3]["Dharma Mittra picture URL"] = ""
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
    DG.nodes[4]["description"] = "feet and hands on floor, both shoulder width apart"
    DG.nodes[4]["asanas_608_page"] = ""
    DG.nodes[4]["asanas_608_english"] = ""

    DG.add_node(5, english_name="dolphin")
    DG.nodes[5]["two_sided"] = False
    DG.nodes[5]["description"] = "feet and forearms on floor"
    DG.nodes[5]["yogajournalurl"] = "https://www.yogajournal.com/practice/beginners/how-to/dolphin-pose/"
    DG.nodes[5][
        "yogajournal_picture"
    ] = "https://www.yogajournal.com/wp-content/uploads/2009/03/image-placeholder-title.jpg?width=730"
    DG.nodes[5]["hindi_name"] = ""
    DG.nodes[5]["comment"] = ""
    DG.nodes[5]["Dharma Mittra picture URL"] = ""
    DG.nodes[5]["asanas 608 page"] = ""
    DG.nodes[5]["asanas 608 english name"] = ""

    DG.add_node(6, english_name="lay on stomach")
    DG.nodes[6]["two_sided"] = False
    DG.nodes[6]["description"] = "whole body in contact with ground, arms by side"
    DG.nodes[6]["yogajournalurl"] = ""
    DG.nodes[6]["yogajournal_picture"] = ""
    DG.nodes[6]["hindi_name"] = "Makarasana"
    DG.nodes[6]["comment"] = ""
    DG.nodes[6]["Dharma Mittra picture URL"] = ""
    DG.nodes[6]["asanas 608 page"] = ""
    DG.nodes[6]["asanas 608 english name"] = ""

    DG.add_node(7, english_name="bow pose")
    DG.nodes[7]["two_sided"] = False
    DG.nodes[7]["description"] = ""
    DG.nodes[7]["yogajournalurl"] = "https://www.yogajournal.com/poses/types/backbends/bow-pose/"
    DG.nodes[7][
        "yogajournal_picture"
    ] = "https://www.yogajournal.com/wp-content/uploads/2007/08/3enneagram_289_1380_bjk.jpg?crop=535:301&width=1070&enable=upscale"
    DG.nodes[7]["hindi_name"] = ""
    DG.nodes[7]["comment"] = ""
    DG.nodes[7]["Dharma Mittra picture URL"] = ""
    DG.nodes[7]["asanas 608 page"] = ""
    DG.nodes[7]["asanas 608 english name"] = ""

    DG.add_node(8, english_name="laying on back, one leg extended up")
    DG.nodes[8]["two_sided"] = True
    DG.nodes[8]["description"] = ""
    DG.nodes[8]["yogajournalurl"] = ""
    DG.nodes[8]["yogajournal_picture"] = ""
    DG.nodes[8]["hindi_name"] = ""
    DG.nodes[8]["comment"] = ""
    DG.nodes[8]["Dharma Mittra picture URL"] = ""
    DG.nodes[8]["asanas 608 page"] = ""
    DG.nodes[8]["asanas 608 english name"] = ""

    DG.add_node(9, english_name="lying on back, both legs extended up")
    DG.nodes[9]["two_sided"] = False
    DG.nodes[9]["description"] = ""
    DG.nodes[9]["yogajournalurl"] = ""
    DG.nodes[9]["yogajournal_picture"] = ""
    DG.nodes[9]["hindi_name"] = ""
    DG.nodes[9]["comment"] = ""
    DG.nodes[9]["Dharma Mittra picture URL"] = ""
    DG.nodes[9]["asanas 608 page"] = ""
    DG.nodes[9]["asanas 608 english name"] = ""

    DG.add_node(10, english_name="supported shoulder stand")
    DG.nodes[10]["two_sided"] = False
    DG.nodes[10]["description"] = ""
    DG.nodes[10]["yogajournalurl"] = ""
    DG.nodes[10]["yogajournal_picture"] = ""
    DG.nodes[10]["hindi_name"] = "Sarvangasana"
    DG.nodes[10]["comment"] = ""
    DG.nodes[10]["Dharma Mittra picture URL"] = ""
    DG.nodes[10]["asanas_608_page"] = "226"
    DG.nodes[10]["asanas_608_english"] = "Shoulder Stand Pose"

    DG.add_node(11, english_name="plow pose")
    DG.nodes[11]["two_sided"] = False
    DG.nodes[11]["description"] = ""
    DG.nodes[11]["yogajournalurl"] = "https://www.yogajournal.com/poses/types/inversions/plow-pose/"
    DG.nodes[11][
        "yogajournal_picture"
    ] = "https://www.yogajournal.com/wp-content/uploads/2021/04/plow-pose.jpg?crop=535:301&width=1070&enable=upscale"
    DG.nodes[11]["hindi_name"] = "Halasana"
    DG.nodes[11]["comment"] = ""
    DG.nodes[11]["Dharma Mittra picture URL"] = ""
    DG.nodes[11]["asanas_608_page"] = "249"
    DG.nodes[11]["asanas_608_english"] = "Plough pose (variation)"

    DG.add_node(12, english_name="ear pressure pose")
    DG.nodes[12]["two_sided"] = False
    DG.nodes[12]["description"] = ""
    DG.nodes[12]["yogajournalurl"] = ""
    DG.nodes[12]["yogajournal_picture"] = ""
    DG.nodes[12]["hindi_name"] = ""
    DG.nodes[12]["comment"] = ""
    DG.nodes[12]["Dharma Mittra picture URL"] = ""
    DG.nodes[12]["asanas 608 page"] = ""
    DG.nodes[12]["asanas 608 english name"] = ""

    DG.add_node(13, english_name="plank")
    DG.nodes[13]["two_sided"] = False
    DG.nodes[13]["description"] = ""
    DG.nodes[13]["yogajournalurl"] = "http://www.yogajournal.com/pose/plank-pose/"
    DG.nodes[13][
        "yogajournal_picture"
    ] = "https://www.yogajournal.com/wp-content/uploads/2017/04/3editplankhp2_292_37428_cmyk.jpg?crop=535:301&width=1070&enable=upscale"
    DG.nodes[13]["hindi_name"] = ""
    DG.nodes[13]["comment"] = ""
    DG.nodes[13][
        "Dharma Mittra picture URL"
    ] = ""
    DG.nodes[13]["asanas 608 page"] = ""
    DG.nodes[13]["asanas 608 english name"] = ""

    DG.add_node(14, english_name="wild thing")
    DG.nodes[14]["two_sided"] = True
    DG.nodes[14]["description"] = ""
    DG.nodes[14]["yogajournalurl"] = ""
    DG.nodes[14]["yogajournal_picture"] = ""
    DG.nodes[14]["hindi_name"] = ""
    DG.nodes[14]["comment"] = ""
    DG.nodes[14]["Dharma Mittra picture URL"] = ""
    DG.nodes[14]["asanas 608 page"] = ""
    DG.nodes[14]["asanas 608 english name"] = ""

    DG.add_node(15, english_name="low pushup")
    DG.nodes[15]["two_sided"] = False
    DG.nodes[15]["hindi_name"] = "chaturanga"
    DG.nodes[15]["description"] = ""
    DG.nodes[15][
        "yogajournalurl"
    ] = "https://www.yogajournal.com/poses/types/strength/four-limbed-staff-pose/"
    DG.nodes[15][
        "yogajournal_picture"
    ] = "https://www.yogajournal.com/wp-content/uploads/2007/08/edit3chaturangahp2_292_37434_cmyk.jpg?crop=535:301&width=1070&enable=upscale"
    DG.nodes[15]["comment"] = ""
    DG.nodes[15]["Dharma Mittra picture URL"] = ""
    DG.nodes[15]["asanas 608 page"] = ""
    DG.nodes[15]["asanas 608 english name"] = ""

    DG.add_node(16, english_name="side plank")
    DG.nodes[16]["two_sided"] = True
    DG.nodes[16]["description"] = ""
    DG.nodes[16]["yogajournalurl"] = "http://www.yogajournal.com/pose/side-plank-pose/"
    DG.nodes[16][
        "yogajournal_picture"
    ] = ""
    DG.nodes[16]["hindi_name"] = ""
    DG.nodes[16]["comment"] = ""
    DG.nodes[16]["Dharma Mittra picture URL"] = ""
    DG.nodes[16]["asanas 608 page"] = ""
    DG.nodes[16]["asanas 608 english name"] = ""

    DG.add_node(17, english_name="standing bend, legs together")
    DG.nodes[17]["two_sided"] = False
    DG.nodes[17]["description"] = "legs together, face to knees"
    DG.nodes[17]["yogajournalurl"] = ""
    DG.nodes[17]["yogajournal_picture"] = ""
    DG.nodes[17]["hindi_name"] = ""
    DG.nodes[17]["comment"] = ""
    DG.nodes[17]["Dharma Mittra picture URL"] = ""
    DG.nodes[17]["asanas 608 page"] = ""
    DG.nodes[17]["asanas 608 english name"] = ""

    DG.add_node(18, english_name="down dog, one leg raised")
    DG.nodes[18]["two_sided"] = True
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
    DG.nodes[18]["asanas 608 page"] = ""
    DG.nodes[18]["asanas 608 english name"] = ""

    DG.add_node(19, english_name="flipped dog")
    DG.nodes[19]["two_sided"] = True
    DG.nodes[19]["description"] = ""
    DG.nodes[19]["yogajournalurl"] = ""
    DG.nodes[19]["yogajournal_picture"] = ""
    DG.nodes[19]["hindi_name"] = ""
    DG.nodes[19]["comment"] = ""
    DG.nodes[19]["Dharma Mittra picture URL"] = ""
    DG.nodes[19]["asanas 608 page"] = ""
    DG.nodes[19]["asanas 608 english name"] = ""

    DG.add_node(20, english_name="stand straight (mountain)")
    DG.nodes[20]["two_sided"] = False
    DG.nodes[20]["yogajournalurl"] = "http://www.yogajournal.com/poses/492"
    DG.nodes[20][
        "yogajournal_picture"
    ] = ""
    DG.nodes[20]["hindi_name"] = "Tadasana"
    DG.nodes[20]["description"] = "legs together, hands at side"
    DG.nodes[20]["comment"] = ""
    DG.nodes[20]["Dharma Mittra picture URL"] = ""
    DG.nodes[20]["asanas 608 page"] = ""
    DG.nodes[20]["asanas 608 english name"] = ""

    DG.add_node(21, english_name="happy camper")
    DG.nodes[21]["two_sided"] = True
    DG.nodes[21]["description"] = ""
    DG.nodes[21]["yogajournalurl"] = ""
    DG.nodes[21]["yogajournal_picture"] = ""
    DG.nodes[21]["hindi_name"] = ""
    DG.nodes[21]["comment"] = ""
    DG.nodes[21]["Dharma Mittra picture URL"] = ""
    DG.nodes[21]["asanas 608 page"] = ""
    DG.nodes[21]["asanas 608 english name"] = ""

    DG.add_node(22, english_name="tree pose")
    DG.nodes[22]["two_sided"] = True
    DG.nodes[22]["description"] = "arms up and straight, one leg bent with foot to thigh"
    DG.nodes[22]["yogajournalurl"] = "http://www.yogajournal.com/poses/496"
    DG.nodes[22][
        "yogajournal_picture"
    ] = ""
    DG.nodes[22]["hindi_name"] = "Vrksasana"
    DG.nodes[22]["comment"] = ""
    DG.nodes[22]["Dharma Mittra picture URL"] = ""
    DG.nodes[22]["asanas 608 page"] = ""
    DG.nodes[22]["asanas 608 english name"] = ""

    DG.add_node(23, english_name="warrior 3")
    DG.nodes[23]["two_sided"] = True
    DG.nodes[23]["description"] = "bent forward on one leg, arms extended forward"
    DG.nodes[23]["yogajournalurl"] = "http://www.yogajournal.com/poses/941"
    DG.nodes[23]["hindi_name"] = "Virabhadrasana III"
    DG.nodes[23][
        "yogajournal_picture"
    ] = ""
    DG.nodes[23]["comment"] = ""
    DG.nodes[23]["Dharma Mittra picture URL"] = ""
    DG.nodes[23]["asanas 608 page"] = ""
    DG.nodes[23]["asanas 608 english name"] = ""

    DG.add_node(24, english_name="warrior 1")
    DG.nodes[24]["two_sided"] = True
    DG.nodes[24]["description"] = "arms up"
    DG.nodes[24]["yogajournalurl"] = "http://www.yogajournal.com/poses/1708"
    DG.nodes[24]["yogajournal_picture"] = ""
    DG.nodes[24]["hindi_name"] = "Virabhadrasana I"
    DG.nodes[24]["comment"] = ""
    DG.nodes[24]["Dharma Mittra picture URL"] = ""
    DG.nodes[24]["asanas 608 page"] = ""
    DG.nodes[24]["asanas 608 english name"] = ""

    DG.add_node(25, english_name="dancer pose")
    DG.nodes[25]["two_sided"] = True
    DG.nodes[25]["description"] = ""
    DG.nodes[25]["yogajournalurl"] = "http://www.yogajournal.com/poses/936"
    DG.nodes[25]["yogajournal_picture"] = ""
    DG.nodes[25]["hindi_name"] = "Natarajasana"
    DG.nodes[25]["comment"] = ""
    DG.nodes[25]["Dharma Mittra picture URL"] = ""
    DG.nodes[25]["asanas 608 page"] = ""
    DG.nodes[25]["asanas 608 english name"] = ""

    DG.add_node(26, english_name="standing splits")
    DG.nodes[26]["two_sided"] = True
    DG.nodes[26]["description"] = ""
    DG.nodes[26]["yogajournalurl"] = "http://www.yogajournal.com/poses/2499"
    DG.nodes[26]["yogajournal_picture"] = ""
    DG.nodes[26]["hindi_name"] = "Urdhva Prasarita Eka Padasana"
    DG.nodes[26]["comment"] = ""
    DG.nodes[26]["Dharma Mittra picture URL"] = ""
    DG.nodes[26]["asanas 608 page"] = ""
    DG.nodes[26]["asanas 608 english name"] = ""

    DG.add_node(27, english_name="chair pose")
    DG.nodes[27]["two_sided"] = False
    DG.nodes[27]["description"] = ""
    DG.nodes[27]["yogajournalurl"] = "http://www.yogajournal.com/poses/493"
    DG.nodes[27][
        "yogajournal_picture"
    ] = ""
    DG.nodes[27]["hindi_name"] = "Utkatasana"
    DG.nodes[27]["comment"] = ""
    DG.nodes[27]["Dharma Mittra picture URL"] = ""
    DG.nodes[27]["asanas 608 page"] = ""
    DG.nodes[27]["asanas 608 english name"] = ""

    DG.add_node(28, english_name="wheel pose")
    DG.nodes[28]["two_sided"] = False
    DG.nodes[28]["description"] = ""
    DG.nodes[28]["yogajournalurl"] = "http://www.yogajournal.com/poses/473"
    DG.nodes[28][
        "yogajournal_picture"
    ] = ""
    DG.nodes[28]["hindi_name"] = "Urdhva Dhanurasana"
    DG.nodes[28]["comment"] = ""
    DG.nodes[28][
        "Dharma Mittra picture URL"
    ] = ""
    DG.nodes[28]["asanas 608 page"] = ""
    DG.nodes[28]["asanas 608 english name"] = ""

    DG.add_node(29, english_name="warrior 2")
    DG.nodes[29]["two_sided"] = True
    DG.nodes[29]["description"] = "arms out"
    DG.nodes[29]["yogajournalurl"] = "http://www.yogajournal.com/poses/495"
    DG.nodes[29][
        "yogajournal_picture"
    ] = "http://www.yogajournal.com/pose/warrior-ii-pose/"
    DG.nodes[29]["hindi_name"] = "Virabhadrasana II"
    DG.nodes[29]["comment"] = ""
    DG.nodes[29]["Dharma Mittra picture URL"] = ""
    DG.nodes[29]["asanas 608 page"] = ""
    DG.nodes[29]["asanas 608 english name"] = ""

    DG.add_node(30, english_name="peaceful warrior")
    DG.nodes[30]["two_sided"] = True
    DG.nodes[30]["description"] = ""
    DG.nodes[30]["yogajournalurl"] = ""
    DG.nodes[30]["yogajournal_picture"] = ""
    DG.nodes[30]["hindi_name"] = ""
    DG.nodes[30]["comment"] = ""
    DG.nodes[30]["Dharma Mittra picture URL"] = ""
    DG.nodes[30]["asanas 608 page"] = ""
    DG.nodes[30]["asanas 608 english name"] = ""

    DG.add_node(31, english_name="corpse pose")
    DG.nodes[31]["two_sided"] = False
    DG.nodes[31]["description"] = "laying on back"
    DG.nodes[31]["yogajournalurl"] = "http://www.yogajournal.com/pose/corpse-pose/"
    DG.nodes[31][
        "yogajournal_picture"
    ] = ""
    DG.nodes[31]["hindi_name"] = "shabasana"
    DG.nodes[31]["comment"] = ""
    DG.nodes[31]["Dharma Mittra picture URL"] = ""
    DG.nodes[31]["asanas 608 page"] = ""
    DG.nodes[31]["asanas 608 english name"] = ""

    DG.add_node(32, english_name="happy baby, rock side to side")
    DG.nodes[32]["two_sided"] = False
    DG.nodes[32]["description"] = "on back, feet up"
    DG.nodes[32]["yogajournalurl"] = "http://www.yogajournal.com/poses/2497"
    DG.nodes[32][
        "yogajournal_picture"
    ] = ""
    DG.nodes[32]["hindi_name"] = ""
    DG.nodes[32]["comment"] = ""
    DG.nodes[32]["Dharma Mittra picture URL"] = ""
    DG.nodes[32]["asanas 608 page"] = ""
    DG.nodes[32]["asanas 608 english name"] = ""

    DG.add_node(33, english_name="on back, knees bent, feet on ground")
    DG.nodes[33]["two_sided"] = False
    DG.nodes[33]["description"] = ""
    DG.nodes[33]["yogajournalurl"] = ""
    DG.nodes[33]["yogajournal_picture"] = ""
    DG.nodes[33]["hindi_name"] = ""
    DG.nodes[33]["comment"] = ""
    DG.nodes[33]["Dharma Mittra picture URL"] = ""
    DG.nodes[33]["asanas 608 page"] = ""
    DG.nodes[33]["asanas 608 english name"] = ""

    DG.add_node(34, english_name="on back, knees bent, feet in air")
    DG.nodes[34]["two_sided"] = False
    DG.nodes[34]["description"] = ""
    DG.nodes[34]["yogajournalurl"] = ""
    DG.nodes[34]["yogajournal_picture"] = ""
    DG.nodes[34]["hindi_name"] = ""
    DG.nodes[34]["comment"] = ""
    DG.nodes[34]["Dharma Mittra picture URL"] = ""
    DG.nodes[34]["asanas 608 page"] = ""
    DG.nodes[34]["asanas 608 english name"] = ""

    DG.add_node(35, english_name="knees to one side, head to other")
    DG.nodes[35]["two_sided"] = True
    DG.nodes[35]["description"] = ""
    DG.nodes[35]["yogajournalurl"] = ""
    DG.nodes[35]["yogajournal_picture"] = ""
    DG.nodes[35]["hindi_name"] = ""
    DG.nodes[35]["comment"] = ""
    DG.nodes[35]["Dharma Mittra picture URL"] = ""
    DG.nodes[35]["asanas 608 page"] = ""
    DG.nodes[35]["asanas 608 english name"] = ""

    DG.add_node(36, english_name="staff pose")
    DG.nodes[36]["two_sided"] = False
    DG.nodes[36]["description"] = ""
    DG.nodes[36]["yogajournalurl"] = ""
    DG.nodes[36]["yogajournal_picture"] = ""
    DG.nodes[36]["hindi_name"] = "paschimatanasana"
    DG.nodes[36]["comment"] = ""
    DG.nodes[36]["Dharma Mittra picture URL"] = ""
    DG.nodes[36]["asanas_608_page"] = "278"
    DG.nodes[36]["asanas_608_english"] = "back stretch pose (preparation)"

    DG.add_node(37, english_name="pigeon pose")
    DG.nodes[37]["two_sided"] = True
    DG.nodes[37]["description"] = ""
    DG.nodes[37]["yogajournalurl"] = ""
    DG.nodes[37]["yogajournal_picture"] = ""
    DG.nodes[37]["hindi_name"] = ""
    DG.nodes[37]["comment"] = ""
    DG.nodes[37]["Dharma Mittra picture URL"] = ""

    DG.add_node(38, english_name="one leg straight, one leg in")
    DG.nodes[38]["two_sided"] = True
    DG.nodes[38]["description"] = ""
    DG.nodes[38]["yogajournalurl"] = ""
    DG.nodes[38]["yogajournal_picture"] = ""
    DG.nodes[38]["hindi_name"] = ""
    DG.nodes[38]["comment"] = ""
    DG.nodes[38]["Dharma Mittra picture URL"] = ""

    DG.add_node(39, english_name="compass pose")
    DG.nodes[39]["two_sided"] = True
    DG.nodes[39]["description"] = ""
    DG.nodes[39]["yogajournalurl"] = ""
    DG.nodes[39]["yogajournal_picture"] = ""
    DG.nodes[39]["hindi_name"] = ""
    DG.nodes[39]["comment"] = ""
    DG.nodes[39]["Dharma Mittra picture URL"] = ""

    DG.add_node(40, english_name="rock bent leg")
    DG.nodes[40]["two_sided"] = True
    DG.nodes[40]["description"] = ""
    DG.nodes[40]["yogajournalurl"] = ""
    DG.nodes[40]["yogajournal_picture"] = ""
    DG.nodes[40]["hindi_name"] = ""
    DG.nodes[40]["comment"] = ""
    DG.nodes[40]["Dharma Mittra picture URL"] = ""
    DG.nodes[40]["asanas 608 page"] = ""
    DG.nodes[40]["asanas 608 english name"] = ""

    DG.add_node(41, english_name="kneeling on shins")
    DG.nodes[41]["two_sided"] = False
    DG.nodes[41]["description"] = ""
    DG.nodes[41]["yogajournalurl"] = ""
    DG.nodes[41]["yogajournal_picture"] = ""
    DG.nodes[41]["hindi_name"] = ""
    DG.nodes[41]["comment"] = ""
    DG.nodes[41]["Dharma Mittra picture URL"] = ""
    DG.nodes[41]["asanas 608 page"] = ""
    DG.nodes[41]["asanas 608 english name"] = ""

    DG.add_node(42, english_name="standing on shins")
    DG.nodes[42]["two_sided"] = False
    DG.nodes[42]["description"] = ""
    DG.nodes[42]["yogajournalurl"] = ""
    DG.nodes[42]["yogajournal_picture"] = ""
    DG.nodes[42]["hindi_name"] = ""
    DG.nodes[42]["comment"] = ""
    DG.nodes[42]["Dharma Mittra picture URL"] = ""
    DG.nodes[42]["asanas 608 page"] = ""
    DG.nodes[42]["asanas 608 english name"] = ""

    DG.add_node(43, english_name="camel pose")
    DG.nodes[43]["two_sided"] = False
    DG.nodes[43]["description"] = ""
    DG.nodes[43]["yogajournalurl"] = "http://www.yogajournal.com/poses/types/backbends/camel-pose/"
    DG.nodes[43][
        "yogajournal_picture"
    ] = "https://www.yogajournal.com/wp-content/uploads/2007/08/ccd03730.jpg?crop=535:301&width=1070&enable=upscale"
    DG.nodes[43]["hindi_name"] = ""
    DG.nodes[43]["comment"] = ""
    DG.nodes[43]["Dharma Mittra picture URL"] = ""
    DG.nodes[43]["asanas 608 page"] = ""
    DG.nodes[43]["asanas 608 english name"] = ""

    DG.add_node(44, english_name="crow")
    DG.nodes[44]["two_sided"] = False
    DG.nodes[44]["description"] = ""
    DG.nodes[44]["yogajournalurl"] = "http://www.yogajournal.com/pose/crane-pose/"
    DG.nodes[44][
        "yogajournal_picture"
    ] = ""
    DG.nodes[44]["hindi_name"] = ""
    DG.nodes[44]["comment"] = ""
    DG.nodes[44]["Dharma Mittra picture URL"] = ""
    DG.nodes[44]["asanas 608 page"] = ""
    DG.nodes[44]["asanas 608 english name"] = ""

    DG.add_node(45, english_name="squat, knees wide")
    DG.nodes[45]["two_sided"] = False
    DG.nodes[45]["description"] = ""
    DG.nodes[45]["yogajournalurl"] = ""
    DG.nodes[45]["yogajournal_picture"] = ""
    DG.nodes[45]["hindi_name"] = ""
    DG.nodes[45]["comment"] = ""
    DG.nodes[45]["Dharma Mittra picture URL"] = ""
    DG.nodes[45]["asanas 608 page"] = ""
    DG.nodes[45]["asanas 608 english name"] = ""

    DG.add_node(46, english_name="standing, legs apart")
    DG.nodes[46]["two_sided"] = False
    DG.nodes[46]["description"] = ""
    DG.nodes[46]["yogajournalurl"] = ""
    DG.nodes[46]["yogajournal_picture"] = ""
    DG.nodes[46]["hindi_name"] = ""
    DG.nodes[46]["comment"] = ""
    DG.nodes[46]["Dharma Mittra picture URL"] = ""
    DG.nodes[46]["asanas 608 page"] = ""
    DG.nodes[46]["asanas 608 english name"] = ""

    DG.add_node(47, english_name="upward dog")
    DG.nodes[47]["two_sided"] = False
    DG.nodes[47]["description"] = ""
    DG.nodes[47]["yogajournalurl"] = "http://www.yogajournal.com/poses/474"
    DG.nodes[47][
        "yogajournal_picture"
    ] = ""
    DG.nodes[47]["hindi_name"] = ""
    DG.nodes[47]["comment"] = ""
    DG.nodes[47][
        "Dharma Mittra picture URL"
    ] = ""
    DG.nodes[47]["asanas 608 page"] = ""
    DG.nodes[47]["asanas 608 english name"] = ""

    DG.add_node(48, english_name="one leg forward with knee bent")
    DG.nodes[48]["two_sided"] = False
    DG.nodes[48]["description"] = ""
    DG.nodes[48]["yogajournalurl"] = ""
    DG.nodes[48]["yogajournal_picture"] = ""
    DG.nodes[48]["hindi_name"] = ""
    DG.nodes[48]["comment"] = ""
    DG.nodes[48]["Dharma Mittra picture URL"] = ""
    DG.nodes[48]["asanas 608 page"] = ""
    DG.nodes[48]["asanas 608 english name"] = ""

    DG.add_node(49, english_name="half lotus")
    DG.nodes[49]["two_sided"] = True
    DG.nodes[49]["description"] = ""
    DG.nodes[49]["yogajournalurl"] = "http://www.yogajournal.com/pose/fire-log-pose/"
    DG.nodes[49][
        "yogajournal_picture"
    ] = ""
    DG.nodes[49]["hindi_name"] = "siddhasana"
    DG.nodes[49]["comment"] = ""
    DG.nodes[49][
        "Dharma Mittra picture URL"
    ] = ""
    DG.nodes[49]["asanas_608_page"] = "624"
    DG.nodes[49]["asanas_608_english"] = "accomplished pose"

    DG.add_node(50, english_name="full lotus")
    DG.nodes[50]["two_sided"] = True
    DG.nodes[50]["description"] = ""
    DG.nodes[50]["yogajournalurl"] = "http://www.yogajournal.com/poses/488"
    DG.nodes[50][
        "yogajournal_picture"
    ] = ""
    DG.nodes[50]["hindi_name"] = "padmasana"
    DG.nodes[50]["comment"] = ""
    DG.nodes[50]["Dharma Mittra picture URL"] = ""
    DG.nodes[50]["asanas_608_page"] = "626"
    DG.nodes[50]["asanas_608_english"] = "lotus pose"

    DG.add_node(51, english_name="embryo pose")
    DG.nodes[51]["two_sided"] = True
    DG.nodes[51]["description"] = ""
    DG.nodes[51]["yogajournalurl"] = ""
    DG.nodes[51]["yogajournal_picture"] = ""
    DG.nodes[51]["hindi_name"] = ""
    DG.nodes[51]["comment"] = ""
    DG.nodes[51]["Dharma Mittra picture URL"] = ""
    DG.nodes[51]["asanas_608_page"] = "243"
    DG.nodes[51]["asanas_608_english"] = "upward lotus pose"

    DG.add_node(52, english_name="flying lotus")
    DG.nodes[52]["two_sided"] = True
    DG.nodes[52]["description"] = ""
    DG.nodes[52]["yogajournalurl"] = ""
    DG.nodes[52]["yogajournal_picture"] = ""
    DG.nodes[52]["hindi_name"] = ""
    DG.nodes[52]["comment"] = ""
    DG.nodes[52]["Dharma Mittra picture URL"] = ""
    DG.nodes[52]["asanas 608 page"] = ""
    DG.nodes[52]["asanas 608 english name"] = ""

    DG.add_node(53, english_name="floating staff pose")
    DG.nodes[53]["two_sided"] = False
    DG.nodes[53]["description"] = ""
    DG.nodes[53]["yogajournalurl"] = ""
    DG.nodes[53]["yogajournal_picture"] = ""
    DG.nodes[53]["hindi_name"] = ""
    DG.nodes[53]["comment"] = ""
    DG.nodes[53]["Dharma Mittra picture URL"] = ""
    DG.nodes[53]["asanas 608 page"] = ""
    DG.nodes[53]["asanas 608 english name"] = ""

    DG.add_node(54, english_name="crane")
    DG.nodes[54]["two_sided"] = False
    DG.nodes[54]["description"] = ""
    DG.nodes[54]["yogajournalurl"] = ""
    DG.nodes[54]["yogajournal_picture"] = ""
    DG.nodes[54]["hindi_name"] = ""
    DG.nodes[54]["comment"] = ""
    DG.nodes[54]["Dharma Mittra picture URL"] = ""
    DG.nodes[54]["asanas 608 page"] = ""
    DG.nodes[54]["asanas 608 english name"] = ""

    DG.add_node(55, english_name="one-legged crane")
    DG.nodes[55]["two_sided"] = True
    DG.nodes[55]["description"] = ""
    DG.nodes[55]["yogajournalurl"] = ""
    DG.nodes[55]["yogajournal_picture"] = ""
    DG.nodes[55]["hindi_name"] = ""
    DG.nodes[55]["comment"] = ""
    DG.nodes[55]["Dharma Mittra picture URL"] = ""
    DG.nodes[55]["asanas 608 page"] = ""
    DG.nodes[55]["asanas 608 english name"] = ""

    DG.add_node(56, english_name="wide legs, feet parallel")
    DG.nodes[56]["two_sided"] = False
    DG.nodes[56]["description"] = ""
    DG.nodes[56]["yogajournalurl"] = ""
    DG.nodes[56]["yogajournal_picture"] = ""
    DG.nodes[56]["hindi_name"] = ""
    DG.nodes[56]["comment"] = ""
    DG.nodes[56]["Dharma Mittra picture URL"] = ""
    DG.nodes[56]["asanas 608 page"] = ""
    DG.nodes[56]["asanas 608 english name"] = ""

    DG.add_node(57, english_name="bent over wide legs, parallel feet")
    DG.nodes[57]["two_sided"] = False
    DG.nodes[57]["description"] = ""
    DG.nodes[57]["yogajournalurl"] = ""
    DG.nodes[57]["yogajournal_picture"] = ""
    DG.nodes[57]["hindi_name"] = ""
    DG.nodes[57]["comment"] = ""
    DG.nodes[57]["Dharma Mittra picture URL"] = ""
    DG.nodes[57]["asanas 608 page"] = ""
    DG.nodes[57]["asanas 608 english name"] = ""

    DG.add_node(
        58, english_name="tripod head stand, legs extended straight up, arms at 90deg"
    )
    DG.nodes[58]["two_sided"] = False
    DG.nodes[58]["description"] = "arms at 90deg"
    DG.nodes[58]["yogajournalurl"] = ""
    DG.nodes[58]["yogajournal_picture"] = ""
    DG.nodes[58]["hindi_name"] = "Salamba-Shirshasana"
    DG.nodes[58]["comment"] = ""
    DG.nodes[58]["Dharma Mittra picture URL"] = ""
    DG.nodes[58]["asanas_608_page"] = "181"
    DG.nodes[58]["asanas_608_english"] = "Supported Head Stand Pose"

    DG.add_node(59, english_name="arms to side")
    DG.nodes[59]["two_sided"] = True
    DG.nodes[59]["description"] = ""
    DG.nodes[59]["yogajournalurl"] = ""
    DG.nodes[59]["yogajournal_picture"] = ""
    DG.nodes[59]["hindi_name"] = ""
    DG.nodes[59]["comment"] = ""
    DG.nodes[59]["Dharma Mittra picture URL"] = ""
    DG.nodes[59]["asanas 608 page"] = ""
    DG.nodes[59]["asanas 608 english name"] = ""

    DG.add_node(
        60,
        english_name="both legs straight, front foot point forward, back foot flat at 45deg",
    )
    DG.nodes[60]["two_sided"] = True
    DG.nodes[60]["description"] = ""
    DG.nodes[60]["yogajournalurl"] = ""
    DG.nodes[60]["yogajournal_picture"] = ""
    DG.nodes[60]["hindi_name"] = ""
    DG.nodes[60]["comment"] = ""
    DG.nodes[60]["Dharma Mittra picture URL"] = ""
    DG.nodes[60]["asanas 608 page"] = ""
    DG.nodes[60]["asanas 608 english name"] = ""

    DG.add_node(61, english_name="standing hinged forward at hips")
    DG.nodes[61]["two_sided"] = True
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
    DG.nodes[62]["description"] = ""
    DG.nodes[62]["yogajournalurl"] = "https://www.yogajournal.com/poses/revolved-triangle-pose-2/"
    DG.nodes[62]["yogajournal_picture"] = "https://www.yogajournal.com/wp-content/uploads/2007/08/revolved-triangle-pose.jpg?crop=535:301&width=1070&enable=upscale"
    DG.nodes[62]["comment"] = ""
    DG.nodes[62]["Dharma Mittra picture URL"] = ""
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
    DG.nodes[63]["description"] = ""
    DG.nodes[63]["asanas_608_page"] = ""
    DG.nodes[63]["asanas_608_english"] = ""

    DG.add_node(64, english_name="bind")
    DG.nodes[64]["two_sided"] = True
    DG.nodes[64]["description"] = ""
    DG.nodes[64]["yogajournalurl"] = ""
    DG.nodes[64]["yogajournal_picture"] = ""
    DG.nodes[64]["hindi_name"] = ""
    DG.nodes[64]["comment"] = ""
    DG.nodes[64]["Dharma Mittra picture URL"] = ""
    DG.nodes[64]["asanas 608 page"] = ""
    DG.nodes[64]["asanas 608 english name"] = ""

    DG.add_node(65, english_name="bird of paradise")
    DG.nodes[65]["two_sided"] = True
    DG.nodes[65]["description"] = ""
    DG.nodes[65]["yogajournalurl"] = ""
    DG.nodes[65]["yogajournal_picture"] = ""
    DG.nodes[65]["hindi_name"] = ""
    DG.nodes[65]["comment"] = ""
    DG.nodes[65]["Dharma Mittra picture URL"] = ""
    DG.nodes[65]["asanas 608 page"] = ""
    DG.nodes[65]["asanas 608 english name"] = ""

    DG.add_node(66, english_name="funky bird of paradise")
    DG.nodes[66]["two_sided"] = True
    DG.nodes[66]["description"] = ""
    DG.nodes[66]["yogajournalurl"] = ""
    DG.nodes[66]["yogajournal_picture"] = ""
    DG.nodes[66]["hindi_name"] = ""
    DG.nodes[66]["comment"] = ""
    DG.nodes[66]["Dharma Mittra picture URL"] = ""
    DG.nodes[66]["asanas 608 page"] = ""
    DG.nodes[66]["asanas 608 english name"] = ""

    DG.add_node(67, english_name="standing bend bound twist")
    DG.nodes[67]["two_sided"] = True
    DG.nodes[67]["description"] = ""
    DG.nodes[67]["yogajournalurl"] = ""
    DG.nodes[67]["yogajournal_picture"] = ""
    DG.nodes[67]["hindi_name"] = ""
    DG.nodes[67]["comment"] = ""
    DG.nodes[67]["Dharma Mittra picture URL"] = ""
    DG.nodes[67]["asanas 608 page"] = ""
    DG.nodes[67]["asanas 608 english name"] = ""

    DG.add_node(68, english_name="standing bend, legs apart")
    DG.nodes[68]["two_sided"] = False
    DG.nodes[68]["description"] = ""
    DG.nodes[68]["yogajournalurl"] = ""
    DG.nodes[68]["yogajournal_picture"] = ""
    DG.nodes[68]["hindi_name"] = ""
    DG.nodes[68]["comment"] = ""
    DG.nodes[68]["Dharma Mittra picture URL"] = ""
    DG.nodes[68]["asanas 608 page"] = ""
    DG.nodes[68]["asanas 608 english name"] = ""

    DG.add_node(69, english_name="tripod head stand, legs bent, arms at 90deg")
    DG.nodes[69]["two_sided"] = False
    DG.nodes[69]["description"] = "arms at 90deg"
    DG.nodes[69]["yogajournalurl"] = ""
    DG.nodes[69]["yogajournal_picture"] = ""
    DG.nodes[69]["hindi_name"] = ""
    DG.nodes[69]["comment"] = ""
    DG.nodes[69]["Dharma Mittra picture URL"] = ""
    DG.nodes[69]["asanas 608 page"] = ""
    DG.nodes[69]["asanas 608 english name"] = ""

    DG.add_node(70, english_name="floating elephant trunk; one leg over arm")
    DG.nodes[70]["two_sided"] = True
    DG.nodes[70]["description"] = ""
    DG.nodes[70]["yogajournalurl"] = ""
    DG.nodes[70]["yogajournal_picture"] = ""
    DG.nodes[70]["hindi_name"] = ""
    DG.nodes[70]["comment"] = ""
    DG.nodes[70]["Dharma Mittra picture URL"] = ""
    DG.nodes[70]["asanas 608 page"] = ""
    DG.nodes[70]["asanas 608 english name"] = ""

    DG.add_node(71, english_name="eight angle pose")
    DG.nodes[71]["two_sided"] = True
    DG.nodes[71]["description"] = ""
    DG.nodes[71]["yogajournalurl"] = ""
    DG.nodes[71]["yogajournal_picture"] = ""
    DG.nodes[71]["hindi_name"] = ""
    DG.nodes[71]["comment"] = ""
    DG.nodes[71]["Dharma Mittra picture URL"] = ""
    DG.nodes[71]["asanas 608 page"] = ""
    DG.nodes[71]["asanas 608 english name"] = ""

    DG.add_node(72, english_name="flying pigeon")
    DG.nodes[72]["two_sided"] = True
    DG.nodes[72]["description"] = "shin on back triceps"
    DG.nodes[72]["yogajournalurl"] = ""
    DG.nodes[72]["yogajournal_picture"] = ""
    DG.nodes[72]["hindi_name"] = ""
    DG.nodes[72]["comment"] = ""
    DG.nodes[72]["Dharma Mittra picture URL"] = ""
    DG.nodes[72]["asanas 608 page"] = ""
    DG.nodes[72]["asanas 608 english name"] = ""

    DG.add_node(73, english_name="peddle feet")
    DG.nodes[73]["two_sided"] = True
    DG.nodes[73]["description"] = ""
    DG.nodes[73]["yogajournalurl"] = ""
    DG.nodes[73]["yogajournal_picture"] = ""
    DG.nodes[73]["hindi_name"] = ""
    DG.nodes[73]["comment"] = ""
    DG.nodes[73]["Dharma Mittra picture URL"] = ""
    DG.nodes[73]["asanas 608 page"] = ""
    DG.nodes[73]["asanas 608 english name"] = ""

    DG.add_node(74, english_name="tripod head stand, legs extended out, arms at 90deg")
    DG.nodes[74]["two_sided"] = False
    DG.nodes[74]["description"] = "arms at 90deg"
    DG.nodes[74]["yogajournalurl"] = ""
    DG.nodes[74]["yogajournal_picture"] = ""
    DG.nodes[74]["hindi_name"] = ""
    DG.nodes[74]["comment"] = ""
    DG.nodes[74]["Dharma Mittra picture URL"] = ""
    DG.nodes[74]["asanas 608 page"] = ""
    DG.nodes[74]["asanas 608 english name"] = ""

    DG.add_node(75, english_name="no-handed head stand")
    DG.nodes[75]["two_sided"] = False
    DG.nodes[75]["description"] = ""
    DG.nodes[75]["yogajournalurl"] = ""
    DG.nodes[75]["yogajournal_picture"] = ""
    DG.nodes[75]["hindi_name"] = ""
    DG.nodes[75]["comment"] = ""
    DG.nodes[75]["Dharma Mittra picture URL"] = ""
    DG.nodes[75]["asanas 608 page"] = ""
    DG.nodes[75]["asanas 608 english name"] = ""

    DG.add_node(76, english_name="inverted tripod")
    DG.nodes[76]["two_sided"] = False
    DG.nodes[76]["description"] = ""
    DG.nodes[76]["yogajournalurl"] = ""
    DG.nodes[76]["yogajournal_picture"] = ""
    DG.nodes[76]["hindi_name"] = "Niralamba-Shirshasana"
    DG.nodes[76]["comment"] = ""
    DG.nodes[76]["Dharma Mittra picture URL"] = ""
    DG.nodes[76]["asanas_608_page"] = "197"
    DG.nodes[76]["asanas_608_english"] = "Hands-free Head Stand Pose (Variation)"

    DG.add_node(77, english_name="seated wide-leg")
    DG.nodes[77]["two_sided"] = False
    DG.nodes[77]["description"] = ""
    DG.nodes[77]["yogajournalurl"] = ""
    DG.nodes[77]["yogajournal_picture"] = ""
    DG.nodes[77]["hindi_name"] = ""
    DG.nodes[77]["comment"] = ""
    DG.nodes[77]["Dharma Mittra picture URL"] = ""
    DG.nodes[77]["asanas 608 page"] = ""
    DG.nodes[77]["asanas 608 english name"] = ""

    DG.add_node(78, english_name="seated wide-leg, floating")
    DG.nodes[78]["two_sided"] = False
    DG.nodes[78]["description"] = ""
    DG.nodes[78]["yogajournalurl"] = ""
    DG.nodes[78]["yogajournal_picture"] = ""
    DG.nodes[78]["hindi_name"] = ""
    DG.nodes[78]["comment"] = ""
    DG.nodes[78]["Dharma Mittra picture URL"] = ""
    DG.nodes[78]["asanas 608 page"] = ""
    DG.nodes[78]["asanas 608 english name"] = ""

    DG.add_node(79, english_name="seated wide-leg, flying")
    DG.nodes[79]["two_sided"] = False
    DG.nodes[79]["description"] = ""
    DG.nodes[79]["yogajournalurl"] = ""
    DG.nodes[79]["yogajournal_picture"] = ""
    DG.nodes[79]["hindi_name"] = ""
    DG.nodes[79]["comment"] = ""
    DG.nodes[79]["Dharma Mittra picture URL"] = ""
    DG.nodes[79]["asanas 608 page"] = ""
    DG.nodes[79]["asanas 608 english name"] = ""

    DG.add_node(80, english_name="all fours, one arm extended")
    DG.nodes[80]["two_sided"] = True
    DG.nodes[80]["description"] = ""
    DG.nodes[80]["yogajournalurl"] = ""
    DG.nodes[80]["yogajournal_picture"] = ""
    DG.nodes[80]["hindi_name"] = ""
    DG.nodes[80]["comment"] = ""
    DG.nodes[80]["Dharma Mittra picture URL"] = ""
    DG.nodes[80]["asanas 608 page"] = ""
    DG.nodes[80]["asanas 608 english name"] = ""

    DG.add_node(81, english_name="all fours, one leg extended")
    DG.nodes[81]["two_sided"] = True
    DG.nodes[81]["description"] = ""
    DG.nodes[81]["yogajournalurl"] = ""
    DG.nodes[81]["yogajournal_picture"] = ""
    DG.nodes[81]["hindi_name"] = ""
    DG.nodes[81]["comment"] = ""
    DG.nodes[81]["Dharma Mittra picture URL"] = ""
    DG.nodes[81]["asanas 608 page"] = ""
    DG.nodes[81]["asanas 608 english name"] = ""

    DG.add_node(82, english_name="all fours, one arm extended, oppposite leg extended")
    DG.nodes[82]["two_sided"] = True
    DG.nodes[82]["description"] = ""
    DG.nodes[82]["yogajournalurl"] = ""
    DG.nodes[82]["yogajournal_picture"] = ""
    DG.nodes[82]["hindi_name"] = ""
    DG.nodes[82]["comment"] = ""
    DG.nodes[82]["Dharma Mittra picture URL"] = ""
    DG.nodes[82]["asanas 608 page"] = ""
    DG.nodes[82]["asanas 608 english name"] = ""

    DG.add_node(83, english_name="all fours, one arm extended, same side leg extended")
    DG.nodes[83]["two_sided"] = True
    DG.nodes[83]["description"] = ""
    DG.nodes[83]["yogajournalurl"] = ""
    DG.nodes[83]["yogajournal_picture"] = ""
    DG.nodes[83]["hindi_name"] = ""
    DG.nodes[83]["comment"] = ""
    DG.nodes[83]["Dharma Mittra picture URL"] = ""
    DG.nodes[83]["asanas 608 page"] = ""
    DG.nodes[83]["asanas 608 english name"] = ""

    DG.add_node(84, english_name="all fours, hips to one side")
    DG.nodes[84]["two_sided"] = True
    DG.nodes[84]["description"] = ""
    DG.nodes[84]["yogajournalurl"] = ""
    DG.nodes[84]["yogajournal_picture"] = ""
    DG.nodes[84]["hindi_name"] = ""
    DG.nodes[84]["comment"] = ""
    DG.nodes[84]["Dharma Mittra picture URL"] = ""
    DG.nodes[84]["asanas 608 page"] = ""
    DG.nodes[84]["asanas 608 english name"] = ""

    DG.add_node(85, english_name="forearm plank")
    DG.nodes[85]["two_sided"] = False
    DG.nodes[85]["description"] = ""
    DG.nodes[85]["yogajournalurl"] = ""
    DG.nodes[85]["yogajournal_picture"] = ""
    DG.nodes[85]["hindi_name"] = ""
    DG.nodes[85]["comment"] = ""
    DG.nodes[85]["Dharma Mittra picture URL"] = ""
    DG.nodes[85]["asanas 608 page"] = ""
    DG.nodes[85]["asanas 608 english name"] = ""

    DG.add_node(86, english_name="tripod head stand, legs bent, arms straight")
    DG.nodes[86]["two_sided"] = False
    DG.nodes[86]["description"] = ""
    DG.nodes[86]["yogajournalurl"] = ""
    DG.nodes[86]["yogajournal_picture"] = ""
    DG.nodes[86]["hindi_name"] = ""
    DG.nodes[86]["comment"] = ""
    DG.nodes[86]["Dharma Mittra picture URL"] = ""
    DG.nodes[86]["asanas 608 page"] = ""
    DG.nodes[86]["asanas 608 english name"] = ""

    DG.add_node(87, english_name="standing back bend")
    DG.nodes[87]["two_sided"] = False
    DG.nodes[87]["description"] = "feet together"
    DG.nodes[87]["yogajournalurl"] = ""
    DG.nodes[87]["yogajournal_picture"] = ""
    DG.nodes[87]["hindi_name"] = ""
    DG.nodes[87]["comment"] = ""
    DG.nodes[87]["Dharma Mittra picture URL"] = ""
    DG.nodes[87]["asanas 608 page"] = ""
    DG.nodes[87]["asanas 608 english name"] = ""

    DG.add_node(88, english_name="scorpion")
    DG.nodes[88]["two_sided"] = False
    DG.nodes[88]["description"] = ""
    DG.nodes[88]["yogajournalurl"] = ""
    DG.nodes[88]["yogajournal_picture"] = ""
    DG.nodes[88]["hindi_name"] = ""
    DG.nodes[88]["comment"] = ""
    DG.nodes[88]["Dharma Mittra picture URL"] = ""
    DG.nodes[88]["asanas 608 page"] = ""
    DG.nodes[88]["asanas 608 english name"] = ""

    DG.add_node(89, english_name="bird of paradise, bent forward, leg to side")
    DG.nodes[89]["two_sided"] = False
    DG.nodes[89]["description"] = ""
    DG.nodes[89]["yogajournalurl"] = ""
    DG.nodes[89]["yogajournal_picture"] = ""
    DG.nodes[89]["hindi_name"] = ""
    DG.nodes[89]["comment"] = ""
    DG.nodes[89]["Dharma Mittra picture URL"] = ""
    DG.nodes[89]["asanas 608 page"] = ""
    DG.nodes[89]["asanas 608 english name"] = ""

    DG.add_node(90, english_name="tripod head stand, legs straight, arms straight")
    DG.nodes[90]["two_sided"] = False
    DG.nodes[90]["description"] = ""
    DG.nodes[90]["yogajournalurl"] = ""
    DG.nodes[90]["yogajournal_picture"] = ""
    DG.nodes[90]["hindi_name"] = ""
    DG.nodes[90]["comment"] = ""
    DG.nodes[90]["Dharma Mittra picture URL"] = ""
    DG.nodes[90]["asanas 608 page"] = ""
    DG.nodes[90]["asanas 608 english name"] = ""

    DG.add_node(91, english_name="butterfly")
    DG.nodes[91]["two_sided"] = False
    DG.nodes[91]["description"] = ""
    DG.nodes[91]["yogajournalurl"] = "https://www.yogajournal.com/poses/types/seated-twists/bound-angle-pose-2/"
    DG.nodes[91]["yogajournal_picture"] = "https://www.yogajournal.com/wp-content/uploads/2007/08/bound-angle-pose-baddha-konasana.jpg?crop=535:301&width=1070&enable=upscale"
    DG.nodes[91]["hindi_name"] = ""
    DG.nodes[91]["comment"] = ""
    DG.nodes[91]["Dharma Mittra picture URL"] = ""
    DG.nodes[91]["asanas 608 page"] = ""
    DG.nodes[91]["asanas 608 english name"] = ""

    DG.add_node(92, english_name="hurdler")
    DG.nodes[92]["two_sided"] = False
    DG.nodes[92]["description"] = ""
    DG.nodes[92]["yogajournalurl"] = ""
    DG.nodes[92]["yogajournal_picture"] = ""
    DG.nodes[92]["hindi_name"] = ""
    DG.nodes[92]["comment"] = ""
    DG.nodes[92]["Dharma Mittra picture URL"] = ""
    DG.nodes[92]["asanas 608 page"] = ""
    DG.nodes[92]["asanas 608 english name"] = ""

    DG.add_node(93, english_name="bridge")
    DG.nodes[93]["two_sided"] = False
    DG.nodes[93]["description"] = ""
    DG.nodes[93]["yogajournalurl"] = "https://www.yogajournal.com/poses/bridge-pose/"
    DG.nodes[93][
        "yogajournal_picture"
    ] = "https://www.yogajournal.com/wp-content/uploads/2007/08/bridge-pose-giselle-mari.jpg?crop=535:301&width=1070&enable=upscale"
    DG.nodes[93]["hindi_name"] = "Sethu Bandha Sarvangasana"
    DG.nodes[93]["comment"] = ""
    DG.nodes[93]["Dharma Mittra picture URL"] = ""
    DG.nodes[93]["asanas 608 page"] = ""
    DG.nodes[93]["asanas 608 english name"] = ""

    DG.add_node(94, english_name="standing eagle")
    DG.nodes[94]["two_sided"] = False
    DG.nodes[94]["description"] = ""
    DG.nodes[94]["yogajournalurl"] = "http://www.yogajournal.com/poses/eagle-pose/"
    DG.nodes[94][
        "yogajournal_picture"
    ] = "https://www.yogajournal.com/wp-content/uploads/2007/08/eaglehp2_292_37370_cmyk.jpg?crop=535:301&width=1070&enable=upscale"
    DG.nodes[94]["hindi_name"] = ""
    DG.nodes[94]["comment"] = ""
    DG.nodes[94]["Dharma Mittra picture URL"] = ""
    DG.nodes[94]["asanas 608 page"] = ""
    DG.nodes[94]["asanas 608 english name"] = ""

    DG.add_node(95, english_name="seated forward fold")
    DG.nodes[95]["two_sided"] = False
    DG.nodes[95]["description"] = ""
    DG.nodes[95][
        "yogajournalurl"
    ] = "http://www.yogajournal.com/pose/seated-forward-bend/"
    DG.nodes[95][
        "yogajournal_picture"
    ] = ""
    DG.nodes[95]["hindi_name"] = ""
    DG.nodes[95]["comment"] = ""
    DG.nodes[95]["Dharma Mittra picture URL"] = ""
    DG.nodes[95]["asanas 608 page"] = ""
    DG.nodes[95]["asanas 608 english name"] = ""

    DG.add_node(96,english_name="extended puppy pose")
    DG.nodes[96]["two_sided"]=False
    DG.nodes[96]["description"]=""
    DG.nodes[96]["yogajournalurl"]="https://www.yogajournal.com/poses/extended-puppy-pose/"
    DG.nodes[96]["yogajournal_picture"]="https://www.yogajournal.com/wp-content/uploads/2007/08/3yp_287_6641_gn_bjk.jpg"
    DG.nodes[96]["hindi_name"]=""
    DG.nodes[96]["comment"]=""
    DG.nodes[96]["Dharma Mittra picture URL"]=""
    DG.nodes[96]["asanas 608 page"]=""
    DG.nodes[96]["asanas 608 english name"]=""

    DG.add_node(97,english_name="boat")
    DG.nodes[97]["two_sided"]=False
    DG.nodes[97]["description"]=""
    DG.nodes[97]["yogajournalurl"]="https://www.yogajournal.com/poses/types/core/full-boat-pose-2/"
    DG.nodes[97]["yogajournal_picture"]="https://www.yogajournal.com/wp-content/uploads/2007/08/editedboathp_292_8_bjk.jpg?crop=535:301&width=1070&enable=upscale"
    DG.nodes[97]["hindi_name"]=""
    DG.nodes[97]["comment"]=""
    DG.nodes[97]["Dharma Mittra picture URL"]=""
    DG.nodes[97]["asanas 608 page"]=""
    DG.nodes[97]["asanas 608 english name"]=""

    DG.add_node(98,english_name="standing forward fold")
    DG.nodes[98]["two_sided"]=False
    DG.nodes[98]["description"]=""
    DG.nodes[98]["yogajournalurl"]="https://www.yogajournal.com/poses/big-toe-pose/"
    DG.nodes[98]["yogajournal_picture"]="https://www.yogajournal.com/wp-content/uploads/2007/08/big-toe-pose.jpg?crop=535:301&width=1070&enable=upscale"
    DG.nodes[98]["hindi_name"]=""
    DG.nodes[98]["comment"]=""
    DG.nodes[98]["Dharma Mittra picture URL"]=""
    DG.nodes[98]["asanas 608 page"]=""
    DG.nodes[98]["asanas 608 english name"]=""

    DG.add_node(99,english_name="standing forward fold with straight back")
    DG.nodes[99]["two_sided"]=False
    DG.nodes[99]["description"]=""
    DG.nodes[99]["yogajournalurl"]=""
    DG.nodes[99]["yogajournal_picture"]=""
    DG.nodes[99]["hindi_name"]=""
    DG.nodes[99]["comment"]=""
    DG.nodes[99]["Dharma Mittra picture URL"]=""
    DG.nodes[99]["asanas 608 page"]=""
    DG.nodes[99]["asanas 608 english name"]=""

    DG.add_node(100,english_name="forearm wheel pose")
    DG.nodes[100]["two_sided"]=False
    DG.nodes[100]["description"]=""
    DG.nodes[100]["yogajournalurl"]=""
    DG.nodes[100]["yogajournal_picture"]=""
    DG.nodes[100]["hindi_name"]=""
    DG.nodes[100]["comment"]=""
    DG.nodes[100]["Dharma Mittra picture URL"]=""
    DG.nodes[100]["asanas 608 page"]=""
    DG.nodes[100]["asanas 608 english name"]=""

    DG.add_node(101,english_name="handstand")
    DG.nodes[101]["two_sided"]=False
    DG.nodes[101]["description"]=""
    DG.nodes[101]["yogajournalurl"]=""
    DG.nodes[101]["yogajournal_picture"]=""
    DG.nodes[101]["hindi_name"]=""
    DG.nodes[101]["comment"]=""
    DG.nodes[101]["Dharma Mittra picture URL"]=""
    DG.nodes[101]["asanas 608 page"]=""
    DG.nodes[101]["asanas 608 english name"]=""

    DG.add_node(102,english_name="")
    DG.nodes[102]["two_sided"]=False
    DG.nodes[102]["description"]=""
    DG.nodes[102]["yogajournalurl"]=""
    DG.nodes[102]["yogajournal_picture"]=""
    DG.nodes[102]["hindi_name"]=""
    DG.nodes[102]["comment"]=""
    DG.nodes[102]["Dharma Mittra picture URL"]=""
    DG.nodes[102]["asanas 608 page"]=""
    DG.nodes[102]["asanas 608 english name"]=""

    DG.add_node(103,english_name="")
    DG.nodes[103]["two_sided"]=False
    DG.nodes[103]["description"]=""
    DG.nodes[103]["yogajournalurl"]=""
    DG.nodes[103]["yogajournal_picture"]=""
    DG.nodes[103]["hindi_name"]=""
    DG.nodes[103]["comment"]=""
    DG.nodes[103]["Dharma Mittra picture URL"]=""
    DG.nodes[103]["asanas 608 page"]=""
    DG.nodes[103]["asanas 608 english name"]=""

    DG.add_node(104,english_name="")
    DG.nodes[104]["two_sided"]=False
    DG.nodes[104]["description"]=""
    DG.nodes[104]["yogajournalurl"]=""
    DG.nodes[104]["yogajournal_picture"]=""
    DG.nodes[104]["hindi_name"]=""
    DG.nodes[104]["comment"]=""
    DG.nodes[104]["Dharma Mittra picture URL"]=""
    DG.nodes[104]["asanas 608 page"]=""
    DG.nodes[104]["asanas 608 english name"]=""

    DG.add_node(105,english_name="")
    DG.nodes[105]["two_sided"]=False
    DG.nodes[105]["description"]=""
    DG.nodes[105]["yogajournalurl"]=""
    DG.nodes[105]["yogajournal_picture"]=""
    DG.nodes[105]["hindi_name"]=""
    DG.nodes[105]["comment"]=""
    DG.nodes[105]["Dharma Mittra picture URL"]=""
    DG.nodes[105]["asanas 608 page"]=""
    DG.nodes[105]["asanas 608 english name"]=""

    DG.add_node(106,english_name="")
    DG.nodes[106]["two_sided"]=False
    DG.nodes[106]["description"]=""
    DG.nodes[106]["yogajournalurl"]=""
    DG.nodes[106]["yogajournal_picture"]=""
    DG.nodes[106]["hindi_name"]=""
    DG.nodes[106]["comment"]=""
    DG.nodes[106]["Dharma Mittra picture URL"]=""
    DG.nodes[106]["asanas 608 page"]=""
    DG.nodes[106]["asanas 608 english name"]=""

    DG.add_node(107,english_name="")
    DG.nodes[107]["two_sided"]=False
    DG.nodes[107]["description"]=""
    DG.nodes[107]["yogajournalurl"]=""
    DG.nodes[107]["yogajournal_picture"]=""
    DG.nodes[107]["hindi_name"]=""
    DG.nodes[107]["comment"]=""
    DG.nodes[107]["Dharma Mittra picture URL"]=""
    DG.nodes[107]["asanas 608 page"]=""
    DG.nodes[107]["asanas 608 english name"]=""

    DG.add_node(108,english_name="")
    DG.nodes[108]["two_sided"]=False
    DG.nodes[108]["description"]=""
    DG.nodes[108]["yogajournalurl"]=""
    DG.nodes[108]["yogajournal_picture"]=""
    DG.nodes[108]["hindi_name"]=""
    DG.nodes[108]["comment"]=""
    DG.nodes[108]["Dharma Mittra picture URL"]=""
    DG.nodes[108]["asanas 608 page"]=""
    DG.nodes[108]["asanas 608 english name"]=""

    DG.add_node(109,english_name="")
    DG.nodes[109]["two_sided"]=False
    DG.nodes[109]["description"]=""
    DG.nodes[109]["yogajournalurl"]=""
    DG.nodes[109]["yogajournal_picture"]=""
    DG.nodes[109]["hindi_name"]=""
    DG.nodes[109]["comment"]=""
    DG.nodes[109]["Dharma Mittra picture URL"]=""
    DG.nodes[109]["asanas 608 page"]=""
    DG.nodes[109]["asanas 608 english name"]=""


    return DG


"""
    DG.add_node(0,english_name="")
    DG.nodes[0]["two_sided"]=False
    DG.nodes[0]["description"]=""
    DG.nodes[0]["yogajournalurl"]=""
    DG.nodes[0]["yogajournal_picture"]=""
    DG.nodes[0]["hindi_name"]=""
    DG.nodes[0]["comment"]=""
    DG.nodes[0]["Dharma Mittra picture URL"]=""
    DG.nodes[0]["asanas 608 page"]=""
    DG.nodes[0]["asanas 608 english name"]=""

    DG.add_node(1,english_name="")
    DG.nodes[1]["two_sided"]=False
    DG.nodes[1]["description"]=""
    DG.nodes[1]["yogajournalurl"]=""
    DG.nodes[1]["yogajournal_picture"]=""
    DG.nodes[1]["hindi_name"]=""
    DG.nodes[1]["comment"]=""
    DG.nodes[1]["Dharma Mittra picture URL"]=""
    DG.nodes[1]["asanas 608 page"]=""
    DG.nodes[1]["asanas 608 english name"]=""

    DG.add_node(2,english_name="")
    DG.nodes[2]["two_sided"]=False
    DG.nodes[2]["description"]=""
    DG.nodes[2]["yogajournalurl"]=""
    DG.nodes[2]["yogajournal_picture"]=""
    DG.nodes[2]["hindi_name"]=""
    DG.nodes[2]["comment"]=""
    DG.nodes[2]["Dharma Mittra picture URL"]=""
    DG.nodes[2]["asanas 608 page"]=""
    DG.nodes[2]["asanas 608 english name"]=""

    DG.add_node(3,english_name="")
    DG.nodes[3]["two_sided"]=False
    DG.nodes[3]["description"]=""
    DG.nodes[3]["yogajournalurl"]=""
    DG.nodes[3]["yogajournal_picture"]=""
    DG.nodes[3]["hindi_name"]=""
    DG.nodes[3]["comment"]=""
    DG.nodes[3]["Dharma Mittra picture URL"]=""
    DG.nodes[3]["asanas 608 page"]=""
    DG.nodes[3]["asanas 608 english name"]=""

    DG.add_node(4,english_name="")
    DG.nodes[4]["two_sided"]=False
    DG.nodes[4]["description"]=""
    DG.nodes[4]["yogajournalurl"]=""
    DG.nodes[4]["yogajournal_picture"]=""
    DG.nodes[4]["hindi_name"]=""
    DG.nodes[4]["comment"]=""
    DG.nodes[4]["Dharma Mittra picture URL"]=""
    DG.nodes[4]["asanas 608 page"]=""
    DG.nodes[4]["asanas 608 english name"]=""

    DG.add_node(5,english_name="")
    DG.nodes[5]["two_sided"]=False
    DG.nodes[5]["description"]=""
    DG.nodes[5]["yogajournalurl"]=""
    DG.nodes[5]["yogajournal_picture"]=""
    DG.nodes[5]["hindi_name"]=""
    DG.nodes[5]["comment"]=""
    DG.nodes[5]["Dharma Mittra picture URL"]=""
    DG.nodes[5]["asanas 608 page"]=""
    DG.nodes[5]["asanas 608 english name"]=""

    DG.add_node(6,english_name="")
    DG.nodes[6]["two_sided"]=False
    DG.nodes[6]["description"]=""
    DG.nodes[6]["yogajournalurl"]=""
    DG.nodes[6]["yogajournal_picture"]=""
    DG.nodes[6]["hindi_name"]=""
    DG.nodes[6]["comment"]=""
    DG.nodes[6]["Dharma Mittra picture URL"]=""
    DG.nodes[6]["asanas 608 page"]=""
    DG.nodes[6]["asanas 608 english name"]=""

    DG.add_node(7,english_name="")
    DG.nodes[7]["two_sided"]=False
    DG.nodes[7]["description"]=""
    DG.nodes[7]["yogajournalurl"]=""
    DG.nodes[7]["yogajournal_picture"]=""
    DG.nodes[7]["hindi_name"]=""
    DG.nodes[7]["comment"]=""
    DG.nodes[7]["Dharma Mittra picture URL"]=""
    DG.nodes[7]["asanas 608 page"]=""
    DG.nodes[7]["asanas 608 english name"]=""

    DG.add_node(8,english_name="")
    DG.nodes[8]["two_sided"]=False
    DG.nodes[8]["description"]=""
    DG.nodes[8]["yogajournalurl"]=""
    DG.nodes[8]["yogajournal_picture"]=""
    DG.nodes[8]["hindi_name"]=""
    DG.nodes[8]["comment"]=""
    DG.nodes[8]["Dharma Mittra picture URL"]=""
    DG.nodes[8]["asanas 608 page"]=""
    DG.nodes[8]["asanas 608 english name"]=""

    DG.add_node(9,english_name="")
    DG.nodes[9]["two_sided"]=False
    DG.nodes[9]["description"]=""
    DG.nodes[9]["yogajournalurl"]=""
    DG.nodes[9]["yogajournal_picture"]=""
    DG.nodes[9]["hindi_name"]=""
    DG.nodes[9]["comment"]=""
    DG.nodes[9]["Dharma Mittra picture URL"]=""
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

    DG.add_weighted_edges_from([(5, 3, 1)])  # 5 = dolphin; 3 = child's pose
    DG.add_weighted_edges_from([(5, 4, 1)])  # 5 = dolphin; 4 = downward dog
    DG.add_weighted_edges_from([(5, 6, 1)])  # 5 = dolphin; 6 = lay on stomach
    DG.add_weighted_edges_from([(5, 85, 1)])  # 5 = dolphin; 13 = forearm plank

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
        [(20, 87, 1)]
    )  # 20 = stand straight (mountain); 87 = standing back bend
    DG.add_weighted_edges_from(
        [(20, 46, 1)]
    )  # 20 = stand straight (mountain); 46 = standing, legs apart

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

    DG.add_weighted_edges_from([(29, 24, 1)])  # 29 = warrior 2; 24 = warrior 1
    DG.add_weighted_edges_from([(29, 30, 1)])  # 29 = warrior 2; 30 =
    DG.add_weighted_edges_from([(29, 56, 1)])  # 29 = warrior 2; 56 =
    DG.add_weighted_edges_from([(29, 60, 1)])  # 29 = warrior 2; 60 =

    DG.add_weighted_edges_from([(30, 29, 1)])  # 30 = peaceful warrior; 29 = warrior

    DG.add_weighted_edges_from([(31, 8, 1)])  # 31 = corpse; 8 = one leg extended up
    DG.add_weighted_edges_from([(31, 9, 1)])  # 31 = corpse; 9 = both legs extended up
    DG.add_weighted_edges_from([(31, 32, 1)])  # 31 = corpse; 32 = happy baby
    DG.add_weighted_edges_from(
        [(31, 34, 1)]
    )  # 31 = corpse; 34 = on back, knees bent, feet in air
    DG.add_weighted_edges_from([(31, 36, 1)])  # 31 = corpse; 36 = staff
    DG.add_weighted_edges_from([(31, 45, 1)])  # 31 = corpse; 45 = squat, knees wide

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

    DG.add_weighted_edges_from([(51, 50, 1)])  # 51 = embryo pose; 50 = full lotus

    DG.add_weighted_edges_from([(52, 50, 1)])  # 52 = flying lotus; 50 = full lotus

    DG.add_weighted_edges_from([(53, 36, 1)])  # 53 = floating staff pose; 36 = staff

    DG.add_weighted_edges_from([(54, 45, 1)])  # 54 = crane; 45 = squat, knees wide
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

    #     DG.add_weighted_edges_from([(91,,1)])   # 91 = butterfly

    #     DG.add_weighted_edges_from([(92,,1)])  # 92 = hurdler

    return DG
