# CO70053 - Python Programming - 2021 - Coursework 2

## Project Structure

```
Project folder/
├─ data/
│  ├─ london.json
├─ network/
│  ├─ path.py
│  ├─ graph.py
├─ tube/
│  ├─ components.py
│  ├─ map.py
├─ main.py
```

### `data/`

Contains the JSON file `london.json` describing the London tube map.

### `network/`

- `path.py` contains the `PathFinder` class, used to compute the shortest distance between two stations.


- `graph.py` contains the `NeighbourGraphBuilder` class, used to generate the abstract graph representing the tube map.
You can test its implementation via the command:
```bash
python -m network.graph
```

### `tube/`

- `components.py` contains the definitions of the following classes (_those classes are already implemented_):
  - `Station`
  - `Line`
  - `Connection`

- `map.py` contains the definition `TubeMap` class, used to read the data from a json file (for instance: `data/london.json`).
You can test its implementation via the command:
```bash
python -m tube.map
```

### `main.py`

Contains a test of the full pipeline:
1. Reading JSON file using the class `TubeMap`.
2. Generating associated graph by using `NeighbourGraphBuilder`.
3. Computing the shortest path between two stations using `PathFinder` and printing it.


