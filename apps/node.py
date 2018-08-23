"""
Model that represents a Node object. It represents a connection of 2 or more routes that a
passenger can take. The purpose of a Node is to allow the program to find the most effective
connections between every route. Provides functions to evaluate the connection time.

"""
from itertools import permutations
from datetime import datetime, time, timedelta
import csv

## Directory where all csv data files are located
PROJECT_ROOT_DATA_DIR = "data/"
STOPS_FILE = "stops.csv"

class Node():
    """
    Class that represents a node, a set of connections centered at one location.

    Attributes:
        node_id (str): Node id for identification
        node_name (str): Name that represents the location of the connection
        node_stops (list): elements of type (str) that identify each stop for each node
        connections (list): elements of type (tuple), with each element being a tuple containing
                            the two stops in each connection
        total_wait_time (int): Performance variable that represents the total wait time in seconds
                               for the sume of the connections

    """
    node_id = None
    node_name = None
    node_stops = []
    connections = []
    
    def __init__(self, node_id, node_name, node_stops):
        self.node_id = node_id
        self.node_name = node_name
        self.node_stops = node_stops

        self.generateConnections()

    def generateConnections(self):
        """
        Function that generates the connections for every stop in the node, and stores them
        in the attribute variable connections.
        """
        ## Generate a permutation of every stop pair, and store the converted list
        self.connections = list(permutations(self.node_stops, 2))

    def evaluateConnectionTime(self, trips, hour=None, route=None):
        """
        Function that searches through every trip that passes through the node, and for each
        trip, searches for the shortest connection to the other routes in the node. Stores the
        total wait time for each connection in te attribute variable total_wait_time
        
        Args:
            trips (dict): Dictionary containing the trips generated by the application    
        Returns:
            total_wait_time (int): Cumulative wait time for each connection during one day
        """
        print("Evaluating Node: {} - Route: {} - {}".format(self.node_id, route, self.node_name))
        
        ## Evaluate the connections for each separate connection
        total_wait_time = {}
        for connection in self.connections:
            ## Separate connection list element into obvious variable
            start_route, start_stop = connection[0]
            finish_route, finish_stop = connection[1]
            ## If a route is provided and the connection does not include that route, skip connection
            if (route is not None) and (route!=start_route and route!=finish_route):
                continue

            connection_string = start_route+"-"+finish_route
            total_wait_time[connection_string] = 0
            
            ## Search through each trip in the route that passes through node
            for start_trip_id in trips[start_route]:
                ## Time at which bus arrives at node stop
                start_time = datetime.strptime(trips[start_route][start_trip_id][start_stop], "%H:%M:%S")
                ## Cycle through each departure time of connecting route until the next bus
                ## is found for a connection
                for stop_trip_id in trips[finish_route]: 
                    stop_time = datetime.strptime(trips[finish_route][stop_trip_id][finish_stop], "%H:%M:%S")
                    if stop_time > start_time:
                        total_wait_time[connection_string]+=(stop_time - start_time).seconds
                        break
        return total_wait_time

                    
                    
                
            
        
            
          
        
        
        
        
        
                    
            
            
        
