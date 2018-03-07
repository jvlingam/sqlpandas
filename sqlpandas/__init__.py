import pkg_resources
from SQLpandas import SQLpandas

try:
    __version__ = pkg_resources.get_distribution(__name__).version
except:
    __version__ = '0.1'
