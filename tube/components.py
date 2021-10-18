"""
WARNING: the following classes should remain unchanged!
"""


class Station:
    def __init__(self, id, name, zones):
        """
        Args:
            id (str)
            name (str)
            zones (Set[int])
        """
        self.id = id
        self.name = name
        self.zones = zones

    def __repr__(self):
        return f"Station({self.id}, {self.name})"


class Line:
    def __init__(self, id, name):
        """
        Args:
            id (str)
            name (str)
        """
        self.id = id
        self.name = name

    def __repr__(self):
        return f"Line({self.id}, {self.name})"


class Connection:
    def __init__(self, stations, line, time):
        """
        Args:
            stations (Set[Station])
            line (Line)
            time (int) time needed (in minutes) to transit from one station in "stations" to the other one (in minutes)
        """
        self.stations = stations
        self.line = line
        self.time = time

    def __repr__(self):
        return f"Connection({'<->'.join([station.name for station in self.stations])}, {self.line.name}, {self.time})"


if __name__ == '__main__':
    # Some examples of Station, Line and Connection
    station_1 = Station(id="131",
                        name="Some Name Station",
                        zones={1, 2})

    station_2 = Station(id="42",
                        name="Some Other Name Station",
                        zones={3})

    line = Line(id="2",
                name="Name Line")

    connection = Connection(stations={station_1, station_2},
                            line=line,
                            time=4)
