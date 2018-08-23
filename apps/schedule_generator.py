"""
Script which manages the process of loading the data for the scheduling algorithm, and calls the
most general functions of the algorithm, such as schedule generation, perofrmance evaluation, and
optimization
"""
import csv, json
from node import Node
from schedule_app import Schedule_Algorithm

## List of directory and data files to fetch for class
PROJECT_ROOT_DATA_DIR = "data/"
ROUTES_FILE = "routes_shape.csv"
STOPS_FILE = "stops.csv"
BUSES_FILE = "buses.csv"
CONN_FILE = "connections.csv"
FREQ_FILE = "frequency.csv"
PRIORITY_FILE = "priority.csv"
SCHEDULE_FILE = "schedule.json"

class schedule_generator():
    """
    Class that provides methods to load data into class, and to call the scheduling algorithm

    Attributes:
        routes (list): Contains elements of type (list) that describe each route in the data file
        stops (list): Contains elements of type (list) that describe each stop in the data file
        buses (list): Contains elements of type (list) that describe the detail of every bus in the inventory
        connections (list): Contains elements of type (list) that describe each connection
        nodes (list): Contains elements of type (Node) that describe each set of connections generated
        frequency (list): Contains elements of type (list) that describe the trip frequency for each route
        priority (list): Contains elements of type (list) that prioritize each route in terms of importance
    """
    routes = []
    stops = []
    buses = []
    connections = []
    nodes = []
    frequency = []
    priority = []

    def __init__(self):
        self.loadRoutesData()
        self.loadStopsData()
        self.loadBusesData()
        self.loadConnData()
        self.loadFreqData()
        self.loadPriorityData()

        self.loadNodes()
        self.scheduleRoutes()
        self.saveSchedule()


    def scheduleRoutes(self):
        """
        Function which manages the data load for the algorithm, and calls algorithm functions to perform
        operations
        """
        self.algorithm = Schedule_Algorithm(self.routes, self.buses, self.nodes, self.frequency, self.priority)
        self.algorithm.arrangeRoutes()
        self.algorithm.generateSchedules("S")
        self.algorithm.evaluateNodeConnections(route="26.1")
        self.algorithm.optimizeNodeConnections()

    def saveSchedule(self):
        """
        Function which saves the currently scheduled data in JSON format to "schedule_output.json"
        """
        data = self.algorithm.routes_schedules
        with open("schedule_output.json","w") as f:
            json.dump(data, f, indent=True)
        

    def loadNodes(self):
        """
        Function which generates a node object for each stop with the same connection ID, by searching
        through each row of the data file, and initialize nodes with stops of the same connection ID.
        """
        ## Fetch information of node ID, name, route, stop ID, and time allowed for originating
        ## and departing connections
        conn_id_col = self.connections[0].index("conn_id")
        conn_name_col = self.connections[0].index("conn_name")
        shape_id_col = self.connections[0].index("shape_id")
        stop_id_col = self.connections[0].index("stop_id")
        conn_time_arr_col = self.connections[0].index("conn_time_arr")
        conn_time_dep_col = self.connections[0].index("conn_time_dep")
        ## Delete header row 
        del self.connections[0]


        ## Initialize each node by searching each row
        current_conn_id = self.connections[0][conn_id_col]
        current_conn_name = self.connections[0][conn_name_col]
        conn_stops = []
        for conn_row in self.connections:
            ## If current connection row ID does not match the previous ones, initialize node
            if conn_row[conn_id_col] != current_conn_id:
                current_node = Node(current_conn_id, current_conn_name, conn_stops)
                self.nodes.append(current_node)
                conn_stops = []
                current_conn_id = conn_row[conn_id_col]
                current_conn_name = conn_row[conn_name_col]
            conn_stops.append([conn_row[shape_id_col], conn_row[stop_id_col]])
        ## Generate last node from file
        current_node = Node(current_conn_id, current_conn_name, conn_stops)
        self.nodes.append(current_node)

    def loadRoutesData(self):
        """
        Function that loads each route information into self.routes
        """
        route_dir = "../" + PROJECT_ROOT_DATA_DIR + "/" + ROUTES_FILE
        with open(route_dir) as route_file:
            csvreader = csv.reader(route_file, delimiter=",", quotechar="|")
            for row in csvreader:
                self.routes.append(row)

    def loadStopsData(self):
        """
        Function that loads each stop information into self.stops
        """
        stops_dir = "../" + PROJECT_ROOT_DATA_DIR + "/" + STOPS_FILE
        with open(stops_dir) as stops_file:
            csvreader = csv.reader(stops_file, delimiter=",", quotechar="|")
            for row in csvreader:
                self.stops.append(row)

    def loadBusesData(self):
        """
        Function that loads each bus information in inventory into self.buses
        """
        buses_dir = "../" + PROJECT_ROOT_DATA_DIR + "/" + BUSES_FILE
        with open(buses_dir) as buses_file:
            csvreader = csv.reader(buses_file, delimiter=",", quotechar="|")
            for row in csvreader:
                self.buses.append(row)

    def loadConnData(self):
        """
        Function that loads each connection information into self.connections
        """
        conn_dir = "../" + PROJECT_ROOT_DATA_DIR + "/" + CONN_FILE
        with open(conn_dir) as conn_file:
            csvreader = csv.reader(conn_file, delimiter=",", quotechar="|")
            for row in csvreader:
                self.connections.append(row)

    def loadFreqData(self):
        """
        Function that loads each route's frequency information into self.frequency
        """
        freq_dir = "../" + PROJECT_ROOT_DATA_DIR + "/" + FREQ_FILE
        with open(freq_dir) as freq_file:
            csvreader = csv.reader(freq_file, delimiter=",", quotechar="|")
            for row in csvreader:
                self.frequency.append(row)

    def loadPriorityData(self):
        """
        Function that loads each priority information into self.priority
        """
        priority_dir = "../" + PROJECT_ROOT_DATA_DIR + "/" + PRIORITY_FILE
        with open(priority_dir) as priority_file:
            csvreader = csv.reader(priority_file, delimiter=",", quotechar="|")
            for row in csvreader:
                self.priority.append(row)

gen = schedule_generator()
