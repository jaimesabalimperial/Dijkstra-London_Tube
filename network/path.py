import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from network.graph import NeighbourGraphBuilder

class PathFinder:
    """
    Task 3: Complete the definition of the PathFinder class by:
    - completing the definition of the __init__ method (if needed)
    - completing the "get_shortest_path" method (don't hesitate to divide your code into several sub-methods)
    """

    def __init__(self, tubemap):
        """
        Args:
            tubemap (TubeMap) : The TubeMap to use.
        """
        self.tubemap = tubemap

        graph_builder = NeighbourGraphBuilder()
        self.graph = graph_builder.build(self.tubemap)

        self.station_ids = list(self.graph.keys())
        self.start_station = None #keep starting station stored
        self.not_visited = [station for station in self.station_ids] #keep track of stations that have not been visited yet
        self.predecessors = {} 
        self.distances = {station:float("inf") for station in self.station_ids}
        self.station_names = [self.tubemap.stations[ident].name for ident in self.station_ids]
    
    def name_to_id(self, station_name):
        """"""
        name_to_id = {name:ident for (name,ident) in zip(self.station_names, self.station_ids)} #make dictionary that maps station names to their ids
        return name_to_id[station_name]
    
    def id_to_name(self, station_id):
        """"""
        id_to_name = {ident:name for (name,ident) in zip(self.station_names, self.station_ids)} #make dictionary that maps station names to their ids
        return id_to_name[station_id]
        
        
    def find_neighbour_distances(self, curr_station_id):
        """"""
        neighbours_list = list(self.graph[curr_station_id].keys()) #make list of neighbours for current station
        unvisited_neighbours = [neighbour for neighbour in neighbours_list if neighbour in self.not_visited] #retrieve neighbours that havent been visited
        
        #find distances from start station to neighbours and update predecessors dictionary
        for neighbour in unvisited_neighbours:
            neighbour_connections = self.graph[curr_station_id][neighbour]

            #retrieve shortest connection to neighbour station
            shortest_connection_time = float("inf")
            for connection in neighbour_connections:
                if connection.time < shortest_connection_time:
                    shortest_connection_time = connection.time
            
            #compare distances
            curr_shortest_distance = self.distances[neighbour]
            total_distance = self.distances[curr_station_id] + shortest_connection_time

            if total_distance < curr_shortest_distance:
                self.distances[neighbour] = total_distance
                self.predecessors[neighbour] = curr_station_id
            
        
                    
    def get_shortest_path(self, start_station_name, end_station_name):
        """ Find ONE shortest path (in terms of duration) from start_station_name to end_station_name.

        For instance, get_shortest_path('Stockwell', 'South Kensington') should return the list:
        [Station(245, Stockwell, {2}), 
         Station(272, Vauxhall, {1, 2}), 
         Station(198, Pimlico, {1}), 
         Station(273, Victoria, {1}), 
         Station(229, Sloane Square, {1}), 
         Station(236, South Kensington, {1})
        ]

        If start_station_name or end_station_name does not exist, return None.

        You can use the Dijkstra algorithm to find the shortest path from start_station_name to end_station_name.

        See here for more information: https://en.wikipedia.org/wiki/Dijkstra's_algorithm#Pseudocode

        Args:
            start_station_name (str): name of the starting station
            end_station_name (str): name of the ending station

        Returns:
            list[Station] : list of Station objects corresponding to ONE 
                shortest path from start_station_name to end_station_name.
                Returns None if start_station_name or end_station_name does not exist.
        """
        curr_station_id = self.name_to_id(start_station_name)

        if start_station_name not in self.station_names or end_station_name not in self.station_names: #check for invalid start and end station names
            return None

        #if it is first time function is called, initialise the distance for the starting station to 0 
        if len(self.not_visited) == len(self.station_ids): 
            self.start_station = curr_station_id
            self.distances[curr_station_id] = 0

        #if recursion ends --> starting station will be equal to end station and we can finally retrieve the shortest path from the list of predecessors
        if start_station_name == end_station_name:
            reversed_path = []
            finished = False
            while not finished:
                end_station_id = self.name_to_id(end_station_name)
                if end_station_id == self.start_station:
                    reversed_path.append(self.tubemap.stations[end_station_id])
                    finished = True
                else: 
                    reversed_path.append(self.tubemap.stations[end_station_id])
                    end_station_name = self.id_to_name(self.predecessors[end_station_id])
            return reversed_path[::-1]
            
        self.find_neighbour_distances(curr_station_id) #updates self.distance to reflect distances from new node (station)
        self.not_visited.remove(curr_station_id) #remove current station from 'not visited' stations set

        #find closest neighbour from current station using distances retrieved in for loop
        relevant_distances = {station:distance for (station, distance) in self.distances.items() if station in self.not_visited}
        closest_neighbour = min(relevant_distances, key=self.distances.get) 
        closest_neighbour_name = self.id_to_name(closest_neighbour)

        #use recursion to go through graph to find shortest path
        return self.get_shortest_path(closest_neighbour_name, end_station_name)


def test_shortest_path():
    from tube.map import TubeMap
    tubemap = TubeMap()
    tubemap.import_from_json("data/london.json")
    
    path_finder = PathFinder(tubemap)
    stations = path_finder.get_shortest_path("Covent Garden", "Green Park")
    print(stations)
    
    station_names = [station.name for station in stations]
    expected = ["Covent Garden", "Leicester Square", "Piccadilly Circus", 
                "Green Park"]
    assert station_names == expected


if __name__ == "__main__":
    test_shortest_path()
