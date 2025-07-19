import argparse

# python3 prog.py --help
# python3 prog.py write --help
# python3 prog.py addition --help
# python3 prog.py write -a 'patxie'
# python3 prog.py addition -a 20 -b 5


parser = argparse.ArgumentParser(prog="prog.py")
subparsers = parser.add_subparsers(dest="command", required=True)

write_parser = subparsers.add_parser("write", help="Write Something")
write_parser.add_argument("-a", type=str, help="String to write" , required=True)


addition_parser = subparsers.add_parser("addition", help="Add two numbers")
addition_parser.add_argument("-a", type=int, help="First Number" , required=True)
addition_parser.add_argument("-b", type=int, help="Second Number" , required=True)

args = parser.parse_args()

match args.command:
    case "write":
        print(f'I am writting {args.a}')

    case "addition":
        result = args.a + args.b
        print(f'The sum is: {result}')



#parser.add_argument("parse", type=int)
