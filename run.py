# license stuff

import logging
import os
import time
from datetime import datetime

import core

# Setup
print("Starting PlaylistDL.\n\nChecking for missing paths.")
root_paths = ["./logs", "./Downloads"]
for route_p in root_paths:
    if os.path.exists(route_p) is False:
        os.mkdir(route_p)
        print("Regenerated the path, "+route_p+".")
time.sleep(0.15)
# Logging
# Generate main logger
main_logger = logging.getLogger('PlaylistDL')
main_logger.setLevel(logging.DEBUG)
# Generate a standard format (save line room, PEP8 and sanity)
log_formats = logging.Formatter("{} | [%(name)s] | [%(levelname)s] : %(message)s"\
                                .format(datetime.strftime(datetime.today(), format="[%d-%m-%y | %H:%M:%S]")))
# Set up the handler for stream
stream_h = logging.StreamHandler()
stream_h.setFormatter(log_formats)
# Attach it to the main logger
main_logger.addHandler(stream_h)
# Set up the handler for log files
file_h = logging.FileHandler(filename="./logs/{}.log".format(datetime.strftime(datetime.today(),
                                                                               format="%d-%m-%y_%H%M%S")))
file_h.setFormatter(log_formats)
main_logger.addHandler(file_h)
main_logger.info("Logging has been configured, if you want to change formatting you will have to alter the source.")
core.var_def()
