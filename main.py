from network.path import PathFinder
from tube.map import TubeMap


def get_tubemap():
    """
    returning an initialised TubeMap object

    Returns:
        tube.map.TubeMap: Initialised TubeMap object
    """

    tubemap = TubeMap()
    tubemap.import_from_json("data/london.json")
    return tubemap


def main():
    tubemap = get_tubemap()

    path_finder = PathFinder(tubemap)

    # Examples of usage of the path_finder
    path_stations = path_finder.get_shortest_path('Stockwell', 'Ealing Broadway')
    path_stations_names = [
        station.name
        for station in path_stations
    ]
    print(path_stations_names)


if __name__ == '__main__':
    main()
