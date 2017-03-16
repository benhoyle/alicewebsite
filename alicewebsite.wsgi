import os, sys

PROJECT_DIR = '/home/alicewebsite/www'
VIRTUAL_ENV_DIR = '/home/alicewebsite/.virtualenvs/alicewebsite'

activate_this = os.path.join(VIRTUAL_ENV_DIR, 'bin', 'activate_this.py')
execfile(activate_this, dict(__file__=activate_this))
sys.path.append(PROJECT_DIR)

from alicehoyle import app as application