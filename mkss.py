#!/usr/bin/env python3
from sys import argv, platform
import subprocess

def main():
    if len(argv) == 3:
        destfile_path=argv[-2]
        filetype=argv[-1]
    elif len(argv) == 2:
        destfile_path=argv[-1]
        filetype='sh'
    else:
        print('Invalid number of arguments')

    template_dict = {"sh": "#!/usr/bin/env bash",
                     "py": "#!/usr/bin/env python3\n\ndef main():\n    "\
                            "pass\n\nif __name__ == '__main__':\n    main()"}

    with open(destfile_path,'x') as destfile:
        destfile.write("{}\n".format(template_dict[filetype]))
        if platform.startswith('linux'):
            subprocess.run(['chmod','+x',destfile_path])

if __name__ == "__main__":
    main()
