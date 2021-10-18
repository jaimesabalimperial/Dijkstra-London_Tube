class NeighbourGraphBuilder:
    """
    Task 2: Complete the definition of the TubeMap class by:
    - writing an __init__ method (if needed)
    - completing the "build" method below (don't hesitate to divide your code into several sub-methods, if needed)
    """

    def __init__(self):
        ...  # TODO

    def build(self, tubemap):
        """
        Builds a graph related to the Tube Map.

        ----------------------------------------------

        The returned graph should be a dictionary having the following form:
        {
            "id_station_A": {
                "id_neighbour_station_1": [
                                connection_1 (instance of Connection),
                                connection_2 (instance of Connection),
                                ...],

                "id_neighbour_station_2": [
                                connection_1 (instance of Connection),
                                connection_2 (instance of Connection),
                                ...],
                ...
            }

            "id_station_B": {
                ...
            }

            ...

        }

        ----------------------------------------------

        Also, for instance, knowing that the id the station "Hammersmith" is "110",
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
            tubemap (TubeMap) tube map serving as a reference for building the graph.

        Return:
            graph (Dict) as described above.

        Note:
            If the input data (tubemap) is invalid, the output should be None.
        """

        return dict()  # TODO


def test_graph():
    from tube.map import TubeMap
    tubemap = TubeMap()
    tubemap.import_from_json("data/london.json")

    graph_builder = NeighbourGraphBuilder()
    graph = graph_builder.build(tubemap)

    print(graph)


if __name__ == "__main__":
    test_graph()
