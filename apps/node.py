from itertools import combinations
import csv

PROJECT_ROOT_DATA_DIR = "data/"
STOPS_FILE = "stops.csv"

class Node():
    node_id = None
    node_name = None
    node_stops = []
    connections = {}
    
    def __init__(self, node_id, node_name, node_stops):
        self.node_id = node_id
        self.node_name = node_name
        self.node_stops = node_stops
        
        self.generateConnections()

    def generateConnections(self):
        ## Method which generates a connection between every stops in the node
        pair_combinations = list(combinations(self.node_stops, 2))
        for i in range(len(pair_combinations)):
            self.connections[i] = pair_combinations[i]
            
          
        
        
        
        
        
                    
            
            
        
