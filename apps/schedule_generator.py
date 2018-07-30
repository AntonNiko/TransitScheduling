import csv

PROJECT_ROOT_DATA_DIR = "data/"
ROUTES_FILE = "routes_shape.csv"
STOPS_FILE = "stops.csv"
BUSES_FILE = "buses.csv"
CONN_FILE = "connections.csv"
FREQ_FILE = "frequency.csv"
PRIORITY_FILE = "priority.csv"

class schedule_generator():
    routes = []
    stops = []
    buses = []
    connections = []
    frequency = []
    priority = []

    def __init__(self):
        self.loadRoutesData()
        self.loadStopsData()
        self.loadBusesData()
        self.loadConnData()
        self.loadFreqData()
    

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
