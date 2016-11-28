import os
import sys
import argparse
import shutil
import logging
import subprocess
# Expect that python2.7 and virtualenv are installed

logger = logging.getLogger(__name__)

GITHUB_URL = 'https://github.com/PGower/django_project_template'


class TemplateBootstrapper(object):
    def __init__(self, project_name=None, target_directory=None, venv_name=None):
        self.project_name = project_name
        self.target_directory = os.path.abspath(target_directory)
        self.venv_name = venv_name
        self.project_path = os.path.join(self.target_directory, self.project_name)
        self.venv_path = os.path.join(self.project_path, self.venv_name)

        self.setup_target_directory()
        self.setup_virtualenv()
        self.setup_sphinx()

    def setup_tempdir(self):
        # Create a temp dir in the users home area and download the zip of the project template from github
        pass

    def setup_target_directory(self):
        # Does the target directory exist?
        if not os.path.exists(self.project_path):
            os.mkdir(self.project_path)

    def setup_virtualenv(self):
        # Create the virtualenv
        subprocess.check_output(['virtualenv', self.venv_path])
        # Activate the virtualenv
        activate_this_file = os.path.join(self.venv_path, 'Scripts/activate_this.py')
        execfile(activate_this_file, dict(__file__=activate_this_file))
        subprocess.check_output(['pip', 'install', 'django'])

    def setup

    def setup_sphinx(self):
        pass


def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('project_name', help='Django project name')
    parser.add_argument('--target_directory', '-t', type=str, help='Target for the project', default='./')
    parser.add_argument('--venv_name', '-v', type=str, help='Virtualenv Directory Name', default='env')

    args = parser.parse_args(sys.argv[1:])
    kwargs = vars(args)

    t = TemplateBootstrapper(**kwargs)

if __name__ == '__main__':
    main()
