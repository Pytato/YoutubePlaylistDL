
import logging
import pafy
import os
import time
from urllib import request
from datetime import datetime


class VideoDL:
    def __init__(self):
        self.video_logger = logging.getLogger("PlaylistDL.core.video.VideoDL")
        self.video_logger.debug("Logging init complete, class init complete.")

    def playlist_gather(self, playlist, fformat, quality_pref):
        print("Soon")

    def single_gather(self, video, fformat, quality_pref):
        print("soon")
