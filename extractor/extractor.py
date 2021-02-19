from  collections import namedtuple
import pathlib
import re

import bedrock


STRUCTURE_KEY_REGEX = re.compile("structuretemplate_(.+:.+)")
Structure = namedtuple("Structure", "name, data")


class World:
    def __init__(self, dir):
        self.dir = dir

        with open(f"{dir}/levelname.txt") as f:
            self.name = f.read().strip()

    def get_structures(self):
        structures = []
        append = structures.append

        with bedrock.World(self.dir) as world:
            for k, v in world.iterKeys():
                structure_name = STRUCTURE_KEY_REGEX.search(k.decode("utf-8", "ignore"))
                if (structure_name):
                    append(Structure(structure_name[1], v))

        return structures

def get_worlds(dir):
    path = pathlib.Path(dir)
    worlds = []
    append = worlds.append

    for world in path.glob("**/levelname.txt"):
        append(World(world.parent))

    return worlds
