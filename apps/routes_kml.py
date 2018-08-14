"""
Script that loads the csv data for each route and outputs a KML file with waypoints that can be
loaded in Google Maps or Google Earth.
"""
import csv
import sys
import xml.etree.cElementTree as ET
from xml.dom import minidom

PROJECT_ROOT_DATA_DIR = "data/"
DATA_FILE = "routes_shape.csv"

def route_kml_generator(route):
    """
    Function that loads data for a route from data provided in constant variables, and outputs a KML
    into the same directory as this function, and can be loaded.

    Args:
        route (int): Route used to create KML file

    """
    directory = "../" + PROJECT_ROOT_DATA_DIR + "/" + DATA_FILE
    data = []
    ## Load data file contianing all route waypoints
    with open(directory) as routes_file:
        csvreader = csv.reader(routes_file, delimiter=",", quotechar="|")
        index = 0
        for row in csvreader:
            if index==0:
                headers = row
            ## Only add row if equals to route being generated
            shape_id = row[0].split(".")
            if shape_id[0]!=str(route):
                index+=1
                continue
            data.append(row)
            index+=1

    ## Store index of columns for csv file
    shape_id_col = headers.index("shape_id")
    shape_pt_lat_col = headers.index("shape_pt_lat")
    shape_pt_lon_col = headers.index("shape_pt_lon")
    shape_pt_sequence_col = headers.index("shape_pt_sequence")
    stop_id_col = headers.index("stop_id")

    ## Add each waypoint coordinate for route to coordinates_data
    coordinates_data = ""
    for row in data[1:]:
        coordinates_data+="{}, {}\n".format(row[shape_pt_lon_col], row[shape_pt_lat_col])

    ## Following KML file structure for each element
    kml = ET.Element("kml")
    doc = ET.SubElement(kml, "Document")

    ET.SubElement(doc, "name").text = "Paths"
    ET.SubElement(doc, "description").text = "Description"
    style = ET.SubElement(doc, "Style" ,id="yellowLineGreenPoly")
    line_style = ET.SubElement(style, "LineStyle")
    ET.SubElement(line_style, "color").text = "7f00ffff"
    ET.SubElement(line_style, "width").text = "4"
    poly_style = ET.SubElement(style, "PolyStyle")
    ET.SubElement(poly_style, "color").text = "7f00ff00"

    placemark = ET.SubElement(doc, "Placemark")
    ET.SubElement(placemark, "name").text = "Route {}".format(route)
    ET.SubElement(placemark, "description").text = "Transparent green..."
    ET.SubElement(placemark, "styleUrl").text = "#yellowLineGreenPoly"
    line_string = ET.SubElement(placemark, "LineString")
    ET.SubElement(line_string, "extrude").text = "1"
    ET.SubElement(line_string, "tessellate").text = "1"
    ET.SubElement(line_string, "altitudeMode").text = "clampToGround"
    ## Add route waypoints to file
    ET.SubElement(line_string, "coordinates").text = coordinates_data

    tree = ET.ElementTree(kml)
    tree.write("Route{}.kml".format(route))

if __name__ == "__main__":
    route_kml_generator(int(sys.argv[1]))
    
