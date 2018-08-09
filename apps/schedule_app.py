import numpy as np
import random
from datetime import datetime, time, timedelta

class Schedule_Algorithm():
    START_DAY_HOUR = 3 ## Hour of day to start scheduling bus routes
    ## TODO get index for MF, S, Z 
    routes_stops = {}
    routes_schedules = {}

    def __init__(self, routes, buses, nodes, frequency, priority):
        self.routes = routes
        self.buses = buses
        self.nodes = nodes
        self.frequency = frequency
        self.priority = priority


    def arrangeRoutes(self):
        del self.priority[0]
        for priority in self.priority:
            self.routes_stops[priority[0]] = [[route_point[4], route_point[5]] for route_point in self.routes
                                                  if route_point[0]==priority[0] and route_point[4]!=""]
            self.routes_schedules[priority[0]] = {}

        ## Cycle through each route and times
        priority_routes = self.priority
        self.routes_order = []
        for i in range(len(priority_routes)):
            priority_routes_loop = [int(priority[1]) for priority in priority_routes]
            priority_min_index = priority_routes_loop.index(min(priority_routes_loop))
            self.routes_order.append(self.priority[priority_min_index][0])
            del self.priority[priority_min_index]
        

    def generateSchedules(self, period="MF"):
        current_route = self.routes_order[0]
        ## Fetches row with frequencies of current route
        current_route_frequency = self.frequency[[route[0] for route in self.frequency].index(current_route)]
        ## Only keeps the elements of frequency that match the schedule period requested (MF/S/Z)
        header_start_index = self.frequency[0].index("{}00".format(period))
        header_fin_index = self.frequency[0].index("{}23".format(period))
        current_route_frequency = current_route_frequency[header_start_index:(header_fin_index+1)]
        current_route_frequency = current_route_frequency[self.START_DAY_HOUR:] + current_route_frequency[:self.START_DAY_HOUR]

        current_hour = self.START_DAY_HOUR
        count = 0
        trip_id_num = 0
        for current_hour_freq in current_route_frequency:
            if current_hour == 24:
                current_hour = 0
            freq_minutes = self.calculateFrequencyMinutes(int(current_hour_freq), 0)
            if freq_minutes is None:
                count+=1
                current_hour+=1
                continue
            for trip_minute in freq_minutes:
                ## Generate Trip ID with format: (27.10001) -- 0001 represents individual trip
                trip_id_num+=1
                trip_id = str("%s%04d"% (current_route, trip_id_num))
                ## With current trip ID, generate a trip, listing all the stop times for the route
                self.generateTrip(current_route, trip_id, current_hour, trip_minute)
            ## Break out of loop once after 24 hours past day start hour
            if count == 23:
                break
            count+=1
            current_hour+=1

    def generateTrip(self, current_route, trip_id, current_hour, trip_minute):
        self.routes_schedules[current_route][trip_id] = {}
        
        ## Generate time for first stop
        trip_time = datetime(2000, 1, 1, current_hour, trip_minute, 0)
        for route_stop in self.routes_stops[current_route]:
            trip_time+= timedelta(seconds=int(route_stop[1]))
            self.routes_schedules[current_route][trip_id][route_stop[0]] = str(trip_time.time())
        print(self.routes_schedules[current_route][trip_id])
            
    def calculateFrequencyMinutes(self, frequency, shift_min):
        if frequency > 60 or frequency < 1:
            return None

        minutes = []
        current_min = shift_min
        while current_min < 60:
            minutes.append(current_min)
            current_min+=frequency
        return minutes

        
            
        
            
        
         

        
                       
        
