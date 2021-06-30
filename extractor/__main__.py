import os
import argparse

from .extractor import get_worlds


WORLD_FOLDER = "/storage/emulated/0/games/com.mojang/minecraftWorlds"


def input_number(text, input_range):
    try:
        input_text = input(text)
    except EOFError:
        print()
        return input_number(text, input_range)

    if input_text.isdigit():
        number = int(input_text)
        if number not in input_range:
            print(f"{number} is out of range")
            return input_number(text, input_range)
        return number
    else:
        print(f"{input_text} is not a number")
        return input_number(text, input_range)


def selector(contents, text):
    for i, v in enumerate(contents):
        print(i, v.name)

    print(text)
    number = input_number(">>> ", range(len(contents)))
    return contents[number]


def save_structure(world, structure):
    namespace, name = structure.name.split(":")

    export_dir = f"{world.dir}/structures/"
    if namespace != "mystructure":
        export_dir += namespace
    
    os.makedirs(export_dir, exist_ok=True)
    with open(f"{export_dir}/{name}.mcstructure", "wb") as f:
        f.write(structure.data)
    
    print(f"{world.name} - {structure.name} Export Succeed\n")


def core(parser, args):
    try:
        world = selector(get_worlds(args.directory), "Select World\nexit with ctrl+c")
    except KeyboardInterrupt:
        return

    structures = world.get_structures()

    while True:
        try:
            structure = selector(structures, "Select Structure\nexit with ctrl+c")
            save_structure(world, structure)
        except KeyboardInterrupt:
            break


def parse_args():
    parser = argparse.ArgumentParser(prog="extractor", description="extract structure")
    parser.add_argument("directory", help="directory with world", nargs="?", default=WORLD_FOLDER)
    parser.set_defaults(func=core)

    return parser, parser.parse_args()


def main():
    parser, args = parse_args()
    args.func(parser, args)

main()
