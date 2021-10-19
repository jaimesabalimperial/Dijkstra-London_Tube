import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from tube.components import Station, Line, Connection
import json


class TubeMap:
    """
    Task 1: Complete the definition of the TubeMap class by:
    - completing the "import_from_json" method (don't hesitate to divide your code into several sub-methods, if needed)

    As a minimum, the TubeMap class must contain these three member attributes:
    - stations: a dictionary that indexes Station instances by their id (key=id, value=Station)
    - lines: a dictionary that indexes Line instances by their id (key=id, value=Line)
    - connections: a list of Connection instances for the tube map (list of Connections)
    """

    def __init__(self):
        self.stations = {}  # key: id, value: Station
        self.lines = {}  # key: id, value: Line
        self.connections = []  # list of Connections


    def import_from_json(self, filepath):
        """ Import tube map information from a JSON file.
        
        During that import, the `stations`, `lines` and `connections` attributes should be updated.

        You can use the `json` python package to easily load the JSON file at `filepath`

        Note: when the indicated zone is not an integer (for instance: 2.5), 
            it means that the station is in two zones at the same time. 
            For example, if the zone of a station is "2.5", 
            it means that station is in zones 2 and 3.

        Args:
            filepath (str) : relative or absolute path to the JSON file 
                containing all the information about the tube map graph to import

        Returns:
            None

        Note:
            If the filepath is invalid, no attribute should be updated, and no error should be raised.
        """
        try:
            with open(filepath) as file:
                data = json.load(file)

        except FileNotFoundError:
            return print("The filepath is invalid, none of the attributes of TubeMap() where updated.")
        
        #retrieve data for stations, lines and connections
        stations = data["stations"]
        lines = data["lines"]
        connections = data["connections"] 

        #make sets for the zones of each station and order them by their id's (keys) with Station() objects as their values
        for station in stations:
            station_zones = station["zone"]

            #check if station is in one or two zones and make a set
            if station_zones.isdigit():
                station_zones = set([int(station["zone"])])
            else: 
                station_zones = set([int(float(station["zone"])), int(float(station["zone"])+1)])

            self.stations[station["id"]] = Station(station["id"], station["name"], station_zones)

        #order lines by their id's (keys) and make Line() objects as their values
        for line in lines: 
            self.lines[line["line"]] = Line(line["line"], line["name"])

        #make set of stations for connections and append Connection() object to list
        for connection in connections:
            stations_set = set([self.stations[connection["station1"]], self.stations[connection["station2"]]])
            self.connections.append(Connection(stations_set, self.lines[connection["line"]], int(connection["time"])))


def test_import():
    tubemap = TubeMap()
    tubemap.import_from_json("data/london.json")
    
    # view one example Station
    print(tubemap.stations[list(tubemap.stations)[0]])
    
    # view one example Line
    print(tubemap.lines[list(tubemap.lines)[0]])
    
    # view the first Connection
    print(tubemap.connections[0])
    
    # view stations for the first Connection
    print([station for station in tubemap.connections[0].stations])


if __name__ == "__main__":
    test_import()
