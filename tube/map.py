class TubeMap:
    """
    Task 1: Complete the definition of the TubeMap class by:
    - completing the definition of the __init__ method (if needed)
    - completing the "import_from_json" method (don't hesitate to divide your code into several sub-methods, if needed)

    As a minimum, the TubeMap class should contain these three member attributes:
    - stations: a dictionary that indexes Station instances by their id (key=id, value=Station)
    - lines: a dictionary that indexes Line instances by their id (key=id, value=Line)
    - connections: a list of Connection instances for the tube map (list of Connections)
    """

    def __init__(self):
        self.stations = {}  # key: id, value: Station
        self.lines = {}  # key: id, value: Line
        self.connections = []  # list of Connections

    def import_from_json(self, filepath):
        """
        Import the tube map information from a JSON file.
        During that import, the `stations`, `lines` and `connections` attributes should be updated.

        You can use the `json` python package to easily load the JSON file at `file_path`

        Note: when the indicated zone is not an integer (for instance: 2.5), it means that
              the station is in two zones at the same time.
              For example, if the zone of a station is "2.5", it means that station is in zones 2 and 3.

        Args:
            filepath (str) relative or absolute path to the json file containing all the information about the
                           tube map graph to import

        Returns:
            None

        Note:
            If the filepath is invalid, no attribute should be updated, and no error should be raised.
        """

        # TODO


def test_import():
    tubemap = TubeMap()
    tubemap.import_from_json("data/london.json")
    print(tubemap.stations[list(tubemap.stations)[0]])
    print(tubemap.lines[list(tubemap.lines)[0]])
    print([str(station) for station in tubemap.connections[0].stations])


if __name__ == "__main__":
    test_import()
