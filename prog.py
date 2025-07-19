import argparse
parser = argparse.ArgumentParser()

parser.add_argument("echo", help='Print out some stuff', type=str)
args = parser.parse_args()
print(f'Hello there {args.echo}')
