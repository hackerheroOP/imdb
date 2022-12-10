from pytest import fixture

import os

import imdb.locale

from importlib import reload


@fixture
def italian():
    """Set the language temporarily to Italian."""
    lang = os.environ["LANG"]
    os.environ["LANG"] = "it_IT.UTF-8"
    reload(imdb.locale)
    yield imdb.locale._
    os.environ["LANG"] = lang
    reload(imdb.locale)


def test_locale_should_work(italian):
    assert italian("art-director") == "Direttore artistico"
