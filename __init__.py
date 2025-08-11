import importlib.metadata

__version__ = importlib.metadata.version(__package__)

from . import edgepy as edgepy
from . import pycombat as pycombat
from . import utils as utils
from . import diffexp as diffexp
