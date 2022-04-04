#!/usr/bin/env python3
import argparse
import os

TEMPLATE_DICT = {"sh": "#!/usr/bin/env bash\n",
                 "py": "#!/usr/bin/env python3\n"\
                       "import argparse\n\n"\
                       "def main():\n    "\
                       "parser = argparse.ArgumentParser()\n    "\
                       "args = parser.parse_args()"\
                       "\n\nif __name__ == '__main__':\n    main()\n"}

FILE_TYPES = list(TEMPLATE_DICT.keys())

#from https://stackoverflow.com/a/30463972
def make_executable(path):
    mode = os.stat(path).st_mode
    mode |= (mode & 0o444) >> 2    # copy R bits to X
    os.chmod(path, mode)

def mkss(file_path,file_type):

    with open(file_path, 'x') as file:
        file.write(TEMPLATE_DICT[file_type])

    make_executable(file_path)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--type', default='sh', choices=FILE_TYPES)
    parser.add_argument('file')
    args = parser.parse_args()
    mkss(args.file,args.type)

if __name__ == "__main__":
    main()
