import os
import sys
from importlib import import_module

import setuptools

REBUILDMO_DIR = os.path.join('imdb', 'locale')
REBUILDMO_NAME = 'rebuildmo'


def runRebuildmo():
    """Call the function to rebuild the locales."""
    cwd = os.getcwd()
    path = list(sys.path)
    languages = []
    try:
        scriptPath = os.path.dirname(__file__)
        modulePath = os.path.join(cwd, scriptPath, REBUILDMO_DIR)
        sys.path += [modulePath, '.', cwd]
        rebuildmo = import_module(os.path.join(REBUILDMO_DIR, REBUILDMO_NAME).replace(os.path.sep, '.'))
        os.chdir(modulePath)
        languages = rebuildmo.rebuildmo()
        print('Created locale for: %s.' % ' '.join(languages))
    except Exception as e:
        print('ERROR: unable to rebuild .mo files; caught exception %s' % e)
    sys.path = path
    os.chdir(cwd)
    return languages


runRebuildmo()

setuptools.setup()
