#!/usr/bin/env python
"""
Ben Payne
ben.is.located@gmail.com

Yoga graph

Use:

This work is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License.
To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/4.0/.
"""

import os
import glob
import networkx as nx  # format for directed graph
import yoga_db as ydb  # nodes and edges of graph
import yoga_lib as ylib  # library of functions for acting on graph

DG = nx.DiGraph()  # initialize directed graph using networkx
DG = ydb.pose_properties(DG)  # load node properties
DG = ydb.pose_transitions(DG)  # load edges

image_width = "200"
small_font_size = "2"
large_font_size = "5"
# write to
write_to_path = "../site/generated_pages/"

# list_of_nodes=DG.nodes()
# list_of_edges=DG.edges()

# edges associated with node 0:
# DG[0]

def yoga_journal(dictionary: dict, image_width: str, small_font_size: str) -> str:
    str_to_write = ""
    if dictionary["yogajournal_picture"] != "":
        str_to_write+='\t<a href="' + dictionary["yogajournalurl"] + '">\n'
        str_to_write+='\t<img src="'        + dictionary["yogajournal_picture"]        + '" width="'        + image_width    + '"></a><BR>\n'
        str_to_write += '\t<font size="'+ small_font_size            + '">source:  <a href="'            + dictionary["yogajournalurl"]            + '">Yoga Journal</a></font><BR>\n'
    return str_to_write

def dharma_mittra(dictionary: dict, image_width: str, small_font_size: str):
    str_to_write = ""
    if dictionary["Dharma Mittra picture URL"] != "":
        str_to_write += '\t<BR>\n\t<img src="'+ dictionary["Dharma Mittra picture URL"]+ '" width="'+ image_width+ '"><BR>\n'
        str_to_write += '\t<font size="'+ small_font_size            + '">source:  <a href="http://www.dharmayogacenter.com/resources/yoga-poses/view-all-yoga-poses-by-category/">dharmayogacenter.com</a></font><BR>\n'
    return str_to_write

def local_images(pose_index_int: int, image_width: str, small_font_size: str):
    str_to_write = ""
    list_all_images = []
    list_all_images += glob.glob("../site/pose_pictures/*.jpg")
    list_all_images += glob.glob("../site/pose_pictures/*.png")
    for img in list_all_images:
        filename = img.split("/")[-1]
        if filename.startswith(str(pose_index_int)+"__"):
            str_to_write += "<P><img src=\""+img.replace("/site","")+"\" width=\""+image_width+"\"><BR/>\n"

            is_img = False
            if filename.endswith("jpg"):
                source_filename = filename = img.split("/")[-1].replace("jpg","source")
                is_img = True
            elif filename.endswith("png"):
                source_filename = filename = img.split("/")[-1].replace("png","source")
                is_img = True
            else:
                print(filename + " is not an image")
            if is_img:
                print(source_filename)
                if os.path.exists("../site/pose_pictures/"+source_filename):
                    with open("../site/pose_pictures/"+source_filename, "r") as file_handle:
                        file_content=file_handle.read()
                    print(file_content)
                    str_to_write += "<font size=\"" + small_font_size + "\"><a href=\""+file_content+"\">source</a></font></P>\n"
    return str_to_write

for pose_index_int in range(len(DG)):

    dic_for_this_node = DG.nodes(data=True)[pose_index_int]
    if dic_for_this_node["english_name"] == "":
        break

    print("        <LI><a href=\"site/generated_pages/" + str(pose_index_int) + ".html\">" + dic_for_this_node["english_name"]+"</a></LI>")
    with open(write_to_path + str(pose_index_int) + ".html", "w") as f:
        f.write("<HTML>\n<HEAD>\n")
        f.write('<!-- defines the default zoom for mobile devices -->\n')
        f.write('<meta name="viewport" content="width=device-width, initial-scale=1" />\n')
        f.write("<TITLE>yoga graph: " + dic_for_this_node["english_name"] + "</TITLE>")
        f.write(
            "</head>\n<BODY>\n\n<table border=\"1\" style='table-layout:fixed;width:100%'>\n"
        )

        # upper left corner -- just the pose name
        f.write(
            '<TR width="50%">\n\t<TD>Current pose: <font size="'
            + large_font_size
            + '">'
            + dic_for_this_node["english_name"]
            + "</font> </TD>\n"
        )
        f.write("\t<TD>Adjacent poses: \n")

        list_of_edges_for_this_node = list(DG[pose_index_int].keys())
        list_of_edges_for_this_node.sort() # same order each time

        # text list in upper right quadrant
        for adjacent_pose_indx in list_of_edges_for_this_node:
            dic_for_adjacent_node = DG.nodes(data=True)[adjacent_pose_indx]
            f.write(
                '<a href="'
                + str(adjacent_pose_indx)
                + '.html">'
                + dic_for_adjacent_node["english_name"]
                + "</a> | \n"
            )
        f.write("\n\t</TD>\n</TR>\n")

        # lower row
        f.write("<TR>\n")
        # lower left quadrant
        f.write('\t<TD valign="top">\n')

        if "hindi_name" in dic_for_this_node.keys():
            if dic_for_this_node["hindi_name"] != "":
                f.write(dic_for_this_node["hindi_name"]+"<BR/>\n")

        if "two_sided" in dic_for_this_node.keys():
            if dic_for_this_node["two_sided"]:
                f.write("Two sided\n")
            else:
                f.write("left-right symmetric<BR/>\n")

        if "description" in dic_for_this_node.keys():
            if dic_for_this_node["description"] != "":
                f.write("<P>"+dic_for_this_node["description"]+"</P>\n")

        if "wikipedia" in dic_for_this_node.keys():
            if dic_for_this_node["wikipedia"] != "":
                f.write("\t<a href=\""+dic_for_this_node["wikipedia"]+"\">"+
                        dic_for_this_node["wikipedia"]+"</a><BR/>\n")

        str_to_write = local_images(pose_index_int, image_width, small_font_size)
        f.write(str_to_write)

        str_to_write = yoga_journal(dic_for_this_node, image_width, small_font_size)
        f.write(str_to_write)

        str_to_write = dharma_mittra(dic_for_this_node, image_width, small_font_size)
        f.write(str_to_write)

        f.write("\n\t</TD>\n\t<TD>\n")

        if "asanas 608 page" in dic_for_this_node.keys():
            if dic_for_this_node["asanas 608 page"] != "":
                f.write("page "+dic_for_this_node["asanas 608 page"]+" in 608 Asanas<BR/>\n")

        # lower right quadrant
        for adjacent_pose_indx in list_of_edges_for_this_node:
            dic_for_adjacent_node = DG.nodes(data=True)[adjacent_pose_indx]
            f.write("\t<P>\n")
            f.write(
                '\t<font size="'
                + large_font_size
                + '"><a href="'
                + str(adjacent_pose_indx)
                + '.html">'
                + dic_for_adjacent_node["english_name"]
                + "</a></font><BR>\n"
            )

            str_to_write = local_images(adjacent_pose_indx, image_width, small_font_size)
            f.write(str_to_write)

            str_to_write = yoga_journal(dic_for_adjacent_node, image_width, small_font_size)
            f.write(str_to_write)

            str_to_write = dharma_mittra(dic_for_this_node, image_width, small_font_size)
            f.write(str_to_write)

            f.write("\t</P>\n\t<HR>\n")

        f.write("\t</TD>\n</TR>\n</table>\n")
        f.write("\t<P>&nbsp;</P>\n")
        f.write(
            '\t<center><a href="http://bhpayne.github.io/yoga_graph/">http://bhpayne.github.io/yoga_graph/</a></center><BR>\n'
        )
        f.write("\t<P>&nbsp;</P>\n")
        f.write("\t<P>&nbsp;</P>\n")
        f.write("\t<P>&nbsp;</P>\n")
        f.write("<center>Ben Payne<BR>\n")
        f.write("ben.is.located AT gmail</center>\n")
        f.write("</BODY>\n</HTML>")
        f.close()
