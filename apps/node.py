from itertools import permutations
from datetime import datetime, time, timedelta
import csv

PROJECT_ROOT_DATA_DIR = "data/"
STOPS_FILE = "stops.csv"

class Node():
    node_id = None
    node_name = None
    node_stops = []
    connections = []

    ## Performance variables
    total_wait_time = 0
    
    def __init__(self, node_id, node_name, node_stops):
        self.node_id = node_id
        self.node_name = node_name
        self.node_stops = node_stops
        
        self.generateConnections()

    def generateConnections(self):
        ## Method which generates a connection between every stops in the node
        self.connections = list(permutations(self.node_stops, 2))

    def evaluateConnectionTime(self, trips):
        ## Trip JSON structure: trips[route][trip_id][stop] : time
        print("Evaluating Node: {} --- {}".format(self.node_id, self.node_name))
        for connection in self.connections:
            start_stop = connection[0]
            finish_stop = connection[1]
            print(connection)
            for start_trip_id in trips[start_stop[0]]:
                start_time = trips[start_stop[0]][start_trip_id][start_stop[1]]
                start_time_formatted = datetime.strptime(start_time, "%H:%M:%S").time()
                ## Cycle through each departure time of end connection until the next connection
                ## is found
                for stop_trip_id in trips[finish_stop[0]]:
                    stop_time = trips[finish_stop[0]][stop_trip_id][finish_stop[1]]
                    stop_time_formatted = datetime.strptime(stop_time, "%H:%M:%S").time()
                    if stop_time_formatted > start_time_formatted:
                        ## TODO: Catch situations when wait time calculations result in 0
                        self.total_wait_time+=(stop_time_formatted.minute - start_time_formatted.minute)

                    
                    
                
            
        
            
          
        
        
        
        
        
                    
            
            
        
