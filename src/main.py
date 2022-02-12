import os
import shutil

import fileparser
from log import Log
from config import Config


def get_highest_folder_version(folder_path: str) -> str:
    """
    Get directory in folder path with highest value, i.e latest version
    :param folder_path: Path to directory with install version folders
    :return: Latest folder version
    """
    folder_path = os.path.expandvars(folder_path)
    folders = [name for name in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, name))]
    folders = sorted(folders, reverse = True)
    return folders[0]


def kill_overwolf() -> None:
    """
    Kill Overwolf program
    """
    Log.info(f"Stopping Overwolf...")
    program_name = Config["overwolfProgramName"]
    try:
        os.system(f'taskkill /f /im {program_name} > nul 2>&1')
    except Exception:
        Log.error("Failed to kill Overwolf")


def patch_overwolf() -> None:
    """
    Patch Overwolf file verification
    """
    Log.info("Patching Overwolf...")
    patchfile = Config["overwolfPatchFile"]
    folder_path = Config["overwolfInstallDir"]
    folder = os.path.join(folder_path, get_highest_folder_version(folder_path))
    shutil.copy2(patchfile, folder)


def patch_porofessor() -> None:
    """
    Patch Porofessor files to remove ads
    """
    Log.info("Patching Porofessor...")
    folder_path = Config["porofessorInstallDir"]
    folder = os.path.expandvars(os.path.join(folder_path, get_highest_folder_version(folder_path)))
    for folders in Config["porofessorParseFolders"]:
        fullpath = os.path.join(folder, os.path.join(folders))
        for file in os.listdir(fullpath):
            if file.endswith(".html"):
                fileparser.parse_remove_div_ids(fullpath, file, Config["porofessorAdIds"])


def main():
    kill_overwolf()
    patch_overwolf()
    patch_porofessor()
    Log.info("Done!")


if __name__ == "__main__":
    main()