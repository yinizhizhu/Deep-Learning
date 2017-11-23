import argparse

parser = argparse.ArgumentParser()
parser.add_argument("echo")
parser.add_argument('x', type=int, help="the integer")
parser.add_argument('square', type=int, help='display a square of a given number')
parser.add_argument("-v", "--verbosity", type=int, default=1, choices=[0,1,2], help="increase output verbosity")
args = parser.parse_args()

print args

answer = args.square**2

print args.echo

if args.verbosity:
    print "verbosity turned on"

if args.verbosity == 2:
    print 'the square of {} equals {}'.format(args.square, answer)
elif args.verbosity == 1:
    print '{}^2 == {}'.format(args.square, answer)
else:
    print answer