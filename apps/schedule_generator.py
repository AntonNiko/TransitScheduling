import csv, json
from node import Node
from schedule_app import Schedule_Algorithm

PROJECT_ROOT_DATA_DIR = "data/"
ROUTES_FILE = "routes_shape.csv"
STOPS_FILE = "stops.csv"
BUSES_FILE = "buses.csv"
CONN_FILE = "connections.csv"
FREQ_FILE = "frequency.csv"
PRIORITY_FILE = "priority.csv"
SCHEDULE_FILE = "schedule.json"

class schedule_generator():
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
        self.algorithm = Schedule_Algorithm(self.routes, self.buses, self.nodes, self.frequency, self.priority)
        self.algorithm.arrangeRoutes()
        self.algorithm.generateSchedules("S")
        self.algorithm.evaluateNodeConnections()

    def saveSchedule(self):
        data = self.algorithm.routes_schedules
        with open("schedule_output.json","w") as f:
            json.dump(data, f, indent=True)
        

    def loadNodes(self):
        conn_id_col = self.connections[0].index("conn_id")
        conn_name_col = self.connections[0].index("conn_name")
        shape_id_col = self.connections[0].index("shape_id")
        stop_id_col = self.connections[0].index("stop_id")
        conn_time_arr_col = self.connections[0].index("conn_time_arr")
        conn_time_dep_col = self.connections[0].index("conn_time_dep")
        del self.connections[0]

        current_conn_id = self.connections[0][conn_id_col]
        current_conn_name = self.connections[0][conn_name_col]
        conn_stops = []
        for conn_row in self.connections:
            if conn_row[conn_id_col] != current_conn_id:
                current_node = Node(current_conn_id, current_conn_name, conn_stops)
                self.nodes.append(current_node)
                conn_stops = []
                current_conn_id = conn_row[conn_id_col]
                current_conn_name = conn_row[conn_name_col]
            conn_stops.append([conn_row[shape_id_col], conn_row[stop_id_col]])
        ## Generate last node from file
        current_node = Node(current_conn_id, current_conn_name, conn_stops)

    def loadRoutesData(self):
        route_dir = "../" + PROJECT_ROOT_DATA_DIR + "/" + ROUTES_FILE
        with open(route_dir) as route_file:
            csvreader = csv.reader(route_file, delimiter=",", quotechar="|")
            for row in csvreader:
                self.routes.append(row)

    def loadStopsData(self):
        stops_dir = "../" + PROJECT_ROOT_DATA_DIR + "/" + STOPS_FILE
        with open(stops_dir) as stops_file:
            csvreader = csv.reader(stops_file, delimiter=",", quotechar="|")
            for row in csvreader:
                self.stops.append(row)

    def loadBusesData(self):
        buses_dir = "../" + PROJECT_ROOT_DATA_DIR + "/" + BUSES_FILE
        with open(buses_dir) as buses_file:
            csvreader = csv.reader(buses_file, delimiter=",", quotechar="|")
            for row in csvreader:
                self.buses.append(row)

    def loadConnData(self):
        conn_dir = "../" + PROJECT_ROOT_DATA_DIR + "/" + CONN_FILE
        with open(conn_dir) as conn_file:
            csvreader = csv.reader(conn_file, delimiter=",", quotechar="|")
            for row in csvreader:
                self.connections.append(row)

    def loadFreqData(self):
        freq_dir = "../" + PROJECT_ROOT_DATA_DIR + "/" + FREQ_FILE
        with open(freq_dir) as freq_file:
            csvreader = csv.reader(freq_file, delimiter=",", quotechar="|")
            for row in csvreader:
                self.frequency.append(row)

    def loadPriorityData(self):
        priority_dir = "../" + PROJECT_ROOT_DATA_DIR + "/" + PRIORITY_FILE
        with open(priority_dir) as priority_file:
            csvreader = csv.reader(priority_file, delimiter=",", quotechar="|")
            for row in csvreader:
                self.priority.append(row)

gen = schedule_generator()
