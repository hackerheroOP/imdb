import sys
from subprocess import CalledProcessError, check_call

import setuptools


def runRebuildmo():
    """Call the function to rebuild the locales."""
    try:
        check_call([sys.executable, "rebuildmo.py"])
    except CalledProcessError as e:
        print('ERROR: unable to rebuild .mo files; caught exception %s' % e)


runRebuildmo()

setuptools.setup()
