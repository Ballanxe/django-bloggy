import socket


if socket.gethostname() == "alberto-HP-Pavilion-dv7-Notebook-PC":

	from .base import *

else:

	from .production import *