import os
import sys
from .filetree import find_pyfiles
from .parse import parse_pyfile

def main():
    import argparse
    parser = argparse.ArgumentParser(description='python file object parser')
    parser.add_argument('path',type=str,help='the python path to parse')
    parser.add_argument('-o',dest='outfile',type=argparse.FileType('w'),default=sys.stdout,help='the file to write to')
    parser.add_argument('-r',dest='recursive',action='store_true',help='if path file search shold be recursive')
    parser_askgroup = parser.add_mutually_exclusive_group()
    parser_askgroup.add_argument('-a',dest='ask',action='store_const',default=0,const=2,help='ask to include files and search directories')
    parser_askgroup.add_argument('-ad',dest='ask',action='store_const',const=1,help='ask before searching files recursively')
    args = parser.parse_args()

    if not os.path.exists(args.path):
        print("'{}' does not exist".format(args.path))
        exit(1)

    if os.path.isdir(args.path):
        files = [*find_pyfiles(args.path,args.recursive,args.ask)]
        if len(files)==0:
            print("no .py files found in '{}'".format(args.path))
            exit(1)
        for f in files:
            parse_pyfile(f,args.outfile)
        exit(1)
    if not args.path.endswith('.py'):
        print("Only takes .py files and directories as input",file=sys.stderr)
        exit(1)
    parse_pyfile(args.path,args.outfile)

if __name__ == '__main__':
    main()
