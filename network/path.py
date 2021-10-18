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
            tubemap (TubeMap)
        """
        # TODO

    def get_shortest_path(self, start_station_name, end_station_name):
        """
        Finds ONE shortest path (in terms of duration) from start_station to end_station.

        You can use the Dijkstra algorithm to find the fastest path from start_station to end_station

        for instance: get_shortest_path_between_stations('Stockwell', 'South Kensington') should return the list:
        ['Stockwell', 'Vauxhall', 'Pimlico', 'Victoria', 'Sloane Square', 'South Kensington']

        See here for more information: https://en.wikipedia.org/wiki/Dijkstra's_algorithm#Pseudocode

        If start_station or end_station does not exist, return None.

        Args:
            start_station_name (str): name of the starting station
            end_station_name (str): name of the ending station

        Returns:
            list[Station]  list of Station objects corresponding to ONE shortest path from start_station to end_station.
                            Return None if start_station or end_station does not exist
        """
        return []  # TODO
