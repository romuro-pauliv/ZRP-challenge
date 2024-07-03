# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                           api/utils/json_reader.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# |--------------------------------------------------------------------------------------------------------------------|
import json

from datetime import datetime
from pathlib import PosixPath, Path
from typing import Any

from app.log.genlog import genlog
from app.config.config_vars import ConfigPaths
# |--------------------------------------------------------------------------------------------------------------------|

class JsonManager(object):
    """
    Manages JSON files including reading, writing backups, and updating contents.

    Attributes:
        path (PosixPath): The file path of the JSON file to manage.
        json (dict): The contents of the JSON file.
    """
    def __init__(self, filename: str) -> None:
        """
        Initializes the JsonManager with the given filename.

        Args:
            filename (str): The name of the JSON file (without extension) to manage.
        """
        self.path: PosixPath = Path(ConfigPaths.JSON_ROOT, f"{filename}.json")
        self.read()

    def read(self) -> None:
        """
        Reads the JSON file and loads its contents into the `json` attribute.
        Logs the read operation.
        """
        with open(self.path) as f:
            self.json: dict[str, Any] = json.load(f)
            genlog.log(True, self.path, True)
            f.close()
    
    def write_backup(self) -> None:
        """
        Writes a backup of the current JSON contents to a new file with a timestamped filename.
        Logs the backup operation.
        """
        backup_path: PosixPath = Path(ConfigPaths.JSON_ROOT, f"{str(datetime.now())}.json")
        with open(backup_path, "w") as f:
            json.dump(self.json, f, indent=4)
            genlog.log(True, f"write backup {backup_path}", True)
            f.close()
    
    def update(self, updated_data: dict[str, Any]) -> None:
        """
        Updates the JSON file with the provided data, writes it to the file, and then reloads the contents.
        Logs the update operation.

        Args:
            updated_data (dict): The new data to write to the JSON file.
        """
        with open(self.path, "w") as f:
            json.dump(updated_data, f, indent=4)
            genlog.log(True, f"write {self.path}", True)
            f.close()
        
        self.read()
    