#!/usr/bin/env python3

import csv
import json
import sys


def read_stats(file):
    stats = {}
    with open(file, "r") as data:
        for line in csv.DictReader(data):
            enemy = line["Enemy Type"]
            line.pop("Enemy Type")

            updated_stat = {}
            for stat in line:
                if "turns" in stat:
                    effect = stat.replace("_turns", "")
                    updated_stat[effect] = {"Chance": line[effect], "Duration": line[stat]}
                elif "Area" in stat:
                    pass
                else:
                    updated_stat[stat] = line[stat]
            stats[enemy] = updated_stat
    return stats


def dict_to_string(enemy, stats):
    print(f"{enemy}:")
    for stat in stats:
        if stat == "Level":
            print("\n==Base Stats==")
        elif stat == "Run":
            print("\n==Special Statuses==")
        elif stat == "Normal":
            print("\n==Status Effects==")
        elif stat == "Neut":
            print("\n==Elemental Defense==")

        if isinstance(stats[stat], dict):
            print(f"{stat}:")
            for x in stats[stat]:
                print(f"    {x}: {stats[stat][x]}")
        else:
            print(f"{stat}: {stats[stat]}")


def main():
    stats = read_stats("stats.csv")
    try:
        stats = stats[sys.argv[1]]
    except:
        print(f"{sys.argv[1]} not found in enemy list")
        sys.exit(0)
    dict_to_string(sys.argv[1], stats)


if __name__ == "__main__":
    main()
