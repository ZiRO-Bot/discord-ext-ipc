import collections

from discord.ext.ipc.client import Client
from discord.ext.ipc.server import Server
from discord.ext.ipc.errors import *


_VersionInfo = collections.namedtuple("_VersionInfo", "major minor micro release serial")

version = "2.1.3"
version_info = _VersionInfo(*version.split(".") + ["final", 0])
