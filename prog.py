import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="Verbose Mode On", action="store_true")
parser.add_argument("-d", "--depth", help="<n> directories to recurse", type=int, required=True)
args = parser.parse_args()

if args.verbose:
    print("verbose turned on")

match args.depth:
    case 1:
        print('Depth 1')
    case 2:
        print('Depth 1')
    case 3:
        print('Depth 1')
    case None:
        print('No Depth provided')
    case _:
        print('Depth out of range')
