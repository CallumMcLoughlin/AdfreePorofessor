import os.path
import json

from log import Log


def _read_config(filename: str) -> dict[str, str]:
    """
    Read configuration from json file
    :param filename: Path to file
    :return: Dictionary of deserialized json
    """
    if not os.path.exists(filename):
        Log.error(f"Configuration file (${filename}) not found")
        raise FileNotFoundError()

    return json.load(open(filename))

Config = _read_config("..\\config\\config.json")