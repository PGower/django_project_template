import os
import sys
import argparse
import shutil

# Expect that python2.7 and virtualenv are installed

class TemplateBootstrapper(object):
    def __init__(self, name=None, target=None):
        self.project_name = name
        self.target_directory = os.path.abspath(target)

        self.setup_virtualenv()
        self.setup_sphinx()

    def setup_virtualenv(self):
        print self.target_directory

    def setup_sphinx(self):
        pass

def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--name', type=str, help='Django project name', required=True)
    parser.add_argument('--target', type=str, help='Target for the project', required=True)

    args = parser.parse_args(sys.argv[1:])
    kwargs = vars(args)

    t = TemplateBootstrapper(**kwargs)

if __name__ == '__main__':
    main()
