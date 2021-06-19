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

for this_indx in range(len(DG)):
    dic_for_this_node = DG.nodes(data=True)[this_indx][1]
    print("index: " + str(this_indx) + "; " + dic_for_this_node["english_name"])
    f = open(write_to_path + str(this_indx) + ".html", "w")
    f.write("<HTML>\n<HEAD>\n")
    f.write("<TITLE>yoga graph: " + dic_for_this_node["english_name"] + "</TITLE>")
    f.write(
        "</head>\n<BODY>\n\n<table border=\"1\" style='table-layout:fixed;width:100%'>\n"
    )
    f.write(
        '<TR width="50%">\n\t<TD>Current pose: <font size="'
        + large_font_size
        + '">'
        + dic_for_this_node["english_name"]
        + "</font> </TD>\n"
    )
    f.write("\t<TD>Adjacent poses: \n")
    list_of_edges_for_this_node = DG[this_indx].keys()
    for neighbor_indx in list_of_edges_for_this_node:
        dic_for_adjacent_node = DG.nodes(data=True)[neighbor_indx][1]
        f.write(
            '<a href="'
            + str(neighbor_indx)
            + '.html">'
            + dic_for_adjacent_node["english_name"]
            + "</a> | \n"
        )
    f.write("\n\t</TD>\n</TR>\n<TR>\n")
    f.write('\t<TD valign="top">\n')
    if dic_for_this_node["yogajournal_picture"] != "":
        f.write('\t<a href="' + dic_for_this_node["yogajournalurl"] + '">\n')
        f.write(
            '\t<img src="'
            + dic_for_this_node["yogajournal_picture"]
            + '" width="'
            + image_width
            + '"></a><BR>\n'
        )
        # f.write("\timage source: <a href=\""+dic_for_this_node['yogajournal_picture']+"\">"+dic_for_this_node['yogajournal_picture']+"</a><BR>\n")
        f.write(
            '\t<font size="'
            + small_font_size
            + '">source:  <a href="'
            + dic_for_this_node["yogajournalurl"]
            + '">Yoga Journal</a></font><BR>\n'
        )
    if dic_for_this_node["Dharma Mittra picture URL"] != "":
        f.write(
            '\t<BR>\n\t<img src="'
            + dic_for_this_node["Dharma Mittra picture URL"]
            + '" width="'
            + image_width
            + '"><BR>\n'
        )
        # f.write("\timage source: <a href=\""+dic_for_this_node['Dharma Mittra picture URL']+"\">"+dic_for_this_node['Dharma Mittra picture URL']+"</a><BR>\n")
        f.write(
            '\t<font size="'
            + small_font_size
            + '">source:  <a href="http://www.dharmayogacenter.com/resources/yoga-poses/view-all-yoga-poses-by-category/">dharmayogacenter.com</a></font><BR>\n'
        )
    f.write("\n\t</TD>\n\t<TD>\n")
    list_of_edges_for_this_node = DG[this_indx].keys()
    for neighbor_indx in list_of_edges_for_this_node:
        dic_for_adjacent_node = DG.nodes(data=True)[neighbor_indx][1]
        f.write("\t<P>\n")
        f.write(
            '\t<font size="'
            + large_font_size
            + '"><a href="'
            + str(neighbor_indx)
            + '.html">'
            + dic_for_adjacent_node["english_name"]
            + "</a></font><BR>\n"
        )
        if dic_for_adjacent_node["yogajournal_picture"] != "":
            f.write('\t<a href="' + str(neighbor_indx) + '.html">\n')
            f.write(
                '\t<img src="'
                + dic_for_adjacent_node["yogajournal_picture"]
                + '" width="'
                + image_width
                + '"></a><BR>\n'
            )
            # f.write("\timage source: <a href=\""+dic_for_adjacent_node['yogajournal_picture']+"\">"+dic_for_adjacent_node['yogajournal_picture']+"</a><BR>\n")
            f.write(
                '\t<font size="'
                + small_font_size
                + '">source:  <a href="'
                + dic_for_adjacent_node["yogajournalurl"]
                + '">Yoga Journal</a></font><BR>\n'
            )
        if dic_for_adjacent_node["Dharma Mittra picture URL"] != "":
            f.write('\t<a href="' + str(neighbor_indx) + '.html">\n')
            f.write(
                '\t<BR>\n\t<img src="'
                + dic_for_adjacent_node["Dharma Mittra picture URL"]
                + '" width="'
                + image_width
                + '"></a><BR>\n'
            )
            # f.write("\timage source: <a href=\""+dic_for_adjacent_node['Dharma Mittra picture URL']+"\">"+dic_for_adjacent_node['Dharma Mittra picture URL']+"</a><BR>\n")
            f.write(
                '\t<font size="'
                + small_font_size
                + '">source:  <a href="http://www.dharmayogacenter.com/resources/yoga-poses/view-all-yoga-poses-by-category/">dharmayogacenter.com</a></font><BR>\n'
            )
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
