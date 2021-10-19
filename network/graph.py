import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import json


class NeighbourGraphBuilder:
    """
    Task 2: Complete the definition of the NeighbourGraphBuilder class by:
    - completing the "build" method below (don't hesitate to divide your code into several sub-methods, if needed)
    """

    def __init__(self):
        pass

    def build(self, tubemap):
        """ Builds a graph encoding neighbouring connections between stations.

        ----------------------------------------------

        The returned graph should be a dictionary having the following form:
        {
            "station_A_id": {
                "neighbour_station_1_id": [
                                connection_1 (instance of Connection),
                                connection_2 (instance of Connection),
                                ...],

                "neighbour_station_2_id": [
                                connection_1 (instance of Connection),
                                connection_2 (instance of Connection),
                                ...],
                ...
            }

            "station_B_id": {
                ...
            }

            ...

        }

        ----------------------------------------------

        For instance, knowing that the id of "Hammersmith" station is "110",
        graph['110'] should be equal to:
        {
            '17': [
                Connection(Hammersmith<->Barons Court, District Line, 1),
                Connection(Hammersmith<->Barons Court, Piccadilly Line, 2)
                ],

            '209': [
                Connection(Hammersmith<->Ravenscourt Park, District Line, 2)
                ],

            '101': [
                Connection(Goldhawk Road<->Hammersmith, Hammersmith & City Line, 2)
                ],

            '265': [
                Connection(Hammersmith<->Turnham Green, Piccadilly Line, 2)
                ]
        }

        ----------------------------------------------

        Args:
            tubemap (TubeMap) : tube map serving as a reference for building the graph.

        Return:
            graph (dict) : as described above.

        Note:
            If the input data (tubemap) is invalid, the method should return an empty dict.

        """
        neighbour_graph = {}
        for station_id in list(tubemap.stations.keys()): #loop over all stations
            neighbour_graph[station_id] = {} #initialise dictionary

            for connection in tubemap.connections: #loop over all connections for every station
                connecting_stations_ids = [station.id for station in connection.stations] #identify the stations involved in each connection

                #if connection involves the station were interested in, add connection to list
                if station_id in connecting_stations_ids: 
                    connecting_stations_ids.remove(station_id)
                    neighbour_station = connecting_stations_ids[0]

                    #if neighbour station id already exists, just append, otherwise make list
                    if neighbour_station not in list(neighbour_graph[station_id].keys()): 
                        neighbour_graph[station_id][neighbour_station] = [connection]
                    else: 
                        neighbour_graph[station_id][neighbour_station].append(connection)


        return neighbour_graph


def test_graph():
    from tube.map import TubeMap

    tubemap = TubeMap()
    tubemap.import_from_json("../data/london.json")

    graph_builder = NeighbourGraphBuilder()
    graph = graph_builder.build(tubemap)

    print(graph)


if __name__ == "__main__":
    test_graph()
