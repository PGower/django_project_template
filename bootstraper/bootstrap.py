import os
import sys
import argparse
import shutil
import logging
# Expect that python2.7 and virtualenv are installed

logger = logging.getLogger(__name__)

class TemplateBootstrapper(object):
    def __init__(self, project_name=None, target_directory=None, venv_target=None):
        self.project_name = project_name
        self.target_directory = os.path.abspath(target_directory)
        self.venv_target = venv_target

        self.setup_virtualenv()
        self.setup_sphinx()

    def setup_virtualenv(self):
        print self.target_directory

    def setup_sphinx(self):
        pass

def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('project_name', help='Django project name')
    parser.add_argument('--target_directory', '-t', type=str, help='Target for the project', default='./')
    parser.add_argument('--venv_target', '-v', type=str, help='Virtualenv Target Directory', default='env')

    args = parser.parse_args(sys.argv[1:])
    kwargs = vars(args)

    t = TemplateBootstrapper(**kwargs)

if __name__ == '__main__':
    main()
