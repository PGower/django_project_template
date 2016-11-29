import os
import sys
import argparse
import shutil
import logging
import subprocess
import zipfile
import urllib
import zipfile
import platform
import shutil
# Expect that python2.7 and virtualenv are installed

logger = logging.getLogger(__name__)

GITHUB_URL = 'https://github.com/PGower/django_project_template'
PROJECT_ZIP = 'https://github.com/PGower/django_project_template/archive/master.zip'


class TemplateBootstrapper(object):
    def __init__(self, project_name=None, target_directory=None, venv_name=None):
        self.project_name = project_name
        self.target_directory = os.path.abspath(target_directory)
        self.venv_name = venv_name

        self.setup_tempdir()
        self.setup_target_directory()
        self.setup_virtualenv()
        # everything from here down should be in the venv
        self.setup_project()
        self.setup_sphinx()

    @property
    def venv_path(self):
        """Path for the virtual environment we are setting up in the project."""
        return os.path.join(self.target_directory, self.venv_name)

    @property
    def temp_path(self):
        """Temporary path where the project template will be downloaded."""
        return os.path.join(os.path.expanduser('~'), '.dj_bootstrap_tempdir/')

    @property
    def template_path(self):
        """Path to the template in the temp_path."""
        return os.path.join(self.temp_path, 'template/django_project_template-master/')

    def setup_tempdir(self):
        # Create a temp dir in the users home area and download the zip of the project template from github
        if os.path.exists(self.temp_path):
            # remove it so we can start again
            shutil.rmtree(self.temp_path)
        # create it
        os.mkdir(self.temp_path)
        urllib.urlretrieve(PROJECT_ZIP, os.path.join(self.temp_path, 'template.zip'))
        # unzip
        z = zipfile.ZipFile(os.path.join(self.temp_path, 'template.zip'))
        z.extractall(os.path.join(self.temp_path, 'template/'))

    def setup_target_directory(self):
        # Does the target directory exist?
        if not os.path.exists(self.target_directory):
            os.mkdir(self.target_directory)

    def setup_virtualenv(self):
        # Create the virtualenv
        o = subprocess.check_output(['virtualenv', self.venv_path])
        print o
        # Activate the virtualenv
        activate_this_file = os.path.join(self.venv_path, 'Scripts/activate_this.py')
        execfile(activate_this_file, dict(__file__=activate_this_file))

    def setup_project(self):
        try:
            o = subprocess.check_output(['pip', 'install', '-r', os.path.join(self.template_path, 'project_template/requirements.txt')])
        except subprocess.CalledProcessError as e:
            # most likely this is an error with installing a package in the requirements file, print the error and ignore.
            print str(e)

        dj_admin = 'django-admin' if not platform.system() == 'Windows' else 'django-admin.exe'

        o = subprocess.check_output([dj_admin, 'startproject', '--template',  os.path.join(self.template_path, 'project_template'), self.project_name, self.target_directory])

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
