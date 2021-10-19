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

        self.stations_ids = list(self.graph.keys())
        self.not_visited = set(station for station in self.stations_ids) #keep track of stations that have not been visited yet
        self.predecessors = {} 
        self.distances = {station:float("inf") for station in self.stations_ids}
        self.station_names = [self.tubemap.stations[ident].name for ident in self.stations_ids]
    
    def name_to_id(self, station_name):

        name_to_id = {name:ident for (name,ident) in zip(self.station_names, self.station_ids)} #make dictionary that maps station names to their ids

        return name_to_id[station_name]
        
        
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
            self.distances[curr_station_id] = 0

        #if recursion ends --> starting station will be equal to end station and we can finally retrieve the path from the list of previous stations
        if start_station_name == end_station_name:
            pass

        neighbours_list = list(self.graph[self.name_to_id(start_station_name)].keys()) #make list of neighbours for current station

        #iterate over all neighbours and find distances
        for neighbour in neighbours_list:
            if neighbour in self.not_visited:
                neighbour_connections = self.graph[curr_station_id][neighbour]

                for connection in neighbour_connections:
                    curr_shortest_distance = self.distances[neighbour]
                    root_to_neighbour = self.distances[curr_station_id] + connection.time

                    if root_to_neighbour < curr_shortest_distance:
                        self.distances[neighbour] = root_to_neighbour
                        self.predecessors[neighbour] = curr_station_id
                    
        self.not_visited.remove(curr_station_id) #remove current station from 'not visited' stations set

        #find closest neighbour from current station using distances retrieved in for loop
        

        self.get_shortest_path(start_station_name, end_station_name)

        return []  # TODO


def test_shortest_path():
    from solution.tube.map import TubeMap
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
