edtp - Elite: Dangerous Trade Planner
=====================================

Command-line tool for finding the best trade routes in Elite.


### Setup

```
$ python3 setup.py install
```


### Usage

```
Usage:
    edtp area  [-hpf] <system> [--range=<lys>]
    edtp route [-hf]  <system_from> <system_to> [--station_from=<name>] [--station_to=<name>]
    edtp pool  [-hf]  <system> <system>...
    edtp start [-hpf] <system> [--station=<name>] [--range=<lys>]
    edtp all [-hpf]
    edtp -h | --help

Commands:
    area  - Get the best trading routes in a radius around the given system
    route - Get the best trading routes between the two given systems
    pool  - Get the best trading routes in the given pool of systems
    start - Get the best trading routes that start in the given system (station)
    all   - Compare ALL trading routes between ALL stations (Expect this to run a while)

Options:
    system                Human-readable name of a system.
    system_from           "
    system_to             "
    -h --help             Show this help
    -p --permit           Include systems that require permits
    -f --force            Force a refresh of the cached trading data
    --range=<lys>         Maximum distance in lightyears [default: 50]
    --station=<name>      Human-readable name of a station.
    --station_from=<name> "
    --station_to=<name>   "
```
