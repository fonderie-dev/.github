from importlib.metadata import version

import fonderie_fixture


def test_version_matches_installed_metadata() -> None:
    assert fonderie_fixture.__version__ == version("fonderie-fixture")
