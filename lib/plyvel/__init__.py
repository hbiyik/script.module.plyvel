"""
Plyvel, a fast and feature-rich Python interface to LevelDB.
"""

# Only import the symbols that are part of the public API
import abi
from ._version import __version__

_plyvel = abi.load("script.module.plyvel", "_plyvel")
__leveldb_version__ = _plyvel.__leveldb_version__
DB = _plyvel.DB
repair_db = _plyvel.repair_db
destroy_db = _plyvel.destroy_db
Error = _plyvel.Error
IOError = _plyvel.IOError
CorruptionError = _plyvel.CorruptionError
IteratorInvalidError = _plyvel.IteratorInvalidError