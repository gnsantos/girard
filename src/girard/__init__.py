def _get_version() -> str:
    """
    Get package version.

    Returns
    -------
    version : str
    """
    from os.path import dirname, join
    with open(join(dirname(__file__), "resources", "VERSION")) as f:
        return f.read().strip()


__version__ = _get_version()
