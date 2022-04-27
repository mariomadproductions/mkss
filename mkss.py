#!/usr/bin/env python3
import argparse
import os
from pathlib import Path

#from https://stackoverflow.com/a/30463972
def make_executable(path):
    mode = os.stat(path).st_mode
    mode |= (mode & 0o444) >> 2    # copy R bits to X
    os.chmod(path, mode)

def mkss(file_path,file_type,template_dict):
    with open(file_path, 'x') as file:
        file.write(template_dict[file_type])
    make_executable(file_path)

def get_template_dict(template_dir_path):
    template_dict = {}
    for file_path in template_dir_path.iterdir():
        with open(file_path, 'rt') as file:
            template_dict[file_path.name] = file.read()

    return template_dict
    
def main():
    template_dict = get_template_dict(Path(__file__).resolve().parent\
                                      .joinpath('templates'))

    file_types = list(template_dict.keys())
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--type', default='sh', choices=file_types)
    parser.add_argument('file')
    args = parser.parse_args()
    mkss(args.file,args.type,template_dict)

if __name__ == "__main__":
    main()
