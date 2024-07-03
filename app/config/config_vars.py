# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                          api/config/config_vars.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
from app.config.config_files import configfiles

from pathlib import PosixPath, Path
# |--------------------------------------------------------------------------------------------------------------------|


class ConfigPaths(object):
    JSON_ROOT   : PosixPath = Path(configfiles.dot_ini['paths']['data']['json'])


class ConfigModel(object):
    GPT_MODEL           : str = configfiles.dot_ini['model']['API']['model_name']
    REQUEST_STOP_AFTER  : int = int(configfiles.dot_ini['model']['retry_request']['stop_after_attempt'])
    TOOL_CALLS_LOOP     : int = int(configfiles.dot_ini['model']['retry_request']['tool_calls_loop'])