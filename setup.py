import os.path

import setuptools

locale_dir = os.path.join("imdb", "locale")
setuptools.setup(locale_src=locale_dir, locale_dir=locale_dir)
