from datetime import datetime

class Log:
    """
    Simple logger
    """
    INFO = "\033[92mInfo\033[0m"
    WARNING = "\033[93mWarn\033[0m"
    ERROR = "\033[91mError\033[0m"

    @staticmethod
    def _get_time() -> str:
        return datetime.now().strftime("%H:%M:%S")

    @staticmethod
    def info(string: str) -> None:
        print(f"<{Log._get_time()}> [{Log.INFO}] {string}")


    @staticmethod
    def warn(string: str) -> None:
        print(f"<{Log._get_time()}> [{Log.WARNING}] {string}")


    @staticmethod
    def error(string: str) -> None:
        print(f"<{Log._get_time()}> [{Log.ERROR}] {string}")
        raise Exception(string)