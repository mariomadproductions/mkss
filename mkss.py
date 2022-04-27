#!/usr/bin/env python3
import argparse
import os

#from https://stackoverflow.com/a/30463972
def make_executable(path):
    mode = os.stat(path).st_mode
    mode |= (mode & 0o444) >> 2    # copy R bits to X
    os.chmod(path, mode)

def mkss(file_path,file_type,template_dict):
    with open(file_path, 'x') as file:
        file.write(template_dict[file_type])
    make_executable(file_path)

def main():
    template_dict = {"sh": "#!/usr/bin/env bash\n",
                     "py": "#!/usr/bin/env python3\n"\
                     "import argparse\n\n"\
                     "def main():\n"\
                     "    parser = argparse.ArgumentParser()\n"\
                     "    parser.add_argument('example')\n"\
                     "    args = parser.parse_args()\n"\
                     "\nif __name__ == '__main__':\n    main()\n"}

    file_types = list(template_dict.keys())
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--type', default='sh', choices=file_types)
    parser.add_argument('file')
    args = parser.parse_args()
    mkss(args.file,args.type,template_dict)

if __name__ == "__main__":
    main()
