
import logging
import pafy
import os
import time
from urllib import request
from datetime import datetime

external_logger = logging.getLogger('PlaylistDL.core.audio')


class AudioDL:
    def __init__(self):
        self.audioDL_logger = logging.getLogger("PlaylistDL.core.audio.audioDL")
        self.audioDL_logger.debug("core.audio.audioDL initialised.")

    def audio_playlist_gather(self, set, fformat="mp3", quality=""):
        self.audioDL_logger.debug("core.audio.audioDL.audio_playlist_dl() started.")
        best_bitrates = {}
        time.sleep(0.2)
        if quality == "High":
            for video in set["items"]:
                dl_stream = video["pafy"].getbestaudio(preftype=fformat)
                if dl_stream is not None:
                    dl_url = dl_stream.url
                    best_bitrates[video["pafy"].title+"."+fformat] = dl_url
                    self.audioDL_logger.info("Found audio of '{0}' in quality, {1}. Added to list."
                                             .format(video["pafy"].title,
                                                     video["pafy"].getbestaudio(preftype=fformat).bitrate))
                else:
                    self.audioDL_logger.warning(video["pafy"].title+" does not have a stream in your chosen format, skipping.")
            self.audioDL_logger.info("List generation complete.")
            self.download_from_url(best_bitrates,set["title"])
        elif quality == "Low":
            # Asks for preferred bitrate
            choices = [96, 128, 160, 192, 256, 320]
            bitrate = 0
            while bitrate not in choices:
                bitrate = int(input("Bitrate choices: {}\n\nEnter desired bitrate (higher number is higher quality): "
                                    .format(choices)))
            self.audioDL_logger.info(
                "Bitrate accepted, generating array of audio streams that have a closest match to choice")
            for video in set["items"]:
                stream_qualities = {}
                # Iterate through the available audiostreams
                for stream in video["pafy"].audiostreams:
                    # If the stream is the right filetype, add the bitrate to the stream_qualitites array
                    if stream.extension == fformat:
                        # Generate a friendly bitrate number
                        s_bitrate = int(stream.bitrate.replace("k", ""))
                        # And give it the key value of its bitrate with a URL to download from attached.
                        stream_qualities[s_bitrate] = stream.url
                # Find the closest bitrate available in the dictionary and get the URL attached,
                # stick the URL in another array.
                closest_bitrate = min(stream_qualities, key=lambda x: abs(x-bitrate))
                best_bitrates[video["pafy"].title+"."+fformat] = stream_qualities[closest_bitrate]
                self.audioDL_logger.info("Found audio of '{0}' in quality, {1}k. Added to list."
                                         .format(video["pafy"].title, closest_bitrate))
            self.audioDL_logger.info("List generation complete.")
            self.download_from_url(best_bitrates, set["title"])
        else:
            self.audioDL_logger.error("Neither 'High' or 'Low' quality selected.")

    def audio_single_gather(self, audio_pafy, fformat, quality):
        self.audioDL_logger.debug("core.audio.audioDL.audio_single_gather() started.")
        # High quality downloads are the simplest to do
        if quality == "High":
            self.audioDL_logger.info("Finding highest quality audio file in your chosen format.")
            audio_pafy.getbestaudio(preftype=fformat)
        elif quality == "Low":
            choices = [96, 128, 160, 192, 256, 320]
            bitrate = 0
            while bitrate not in choices:
                bitrate = int(input("Bitrate choices: {}\n\nEnter desired bitrate (higher number is higher quality): "
                                    .format(choices)))
            self.audioDL_logger.info(
                "Bitrate accepted, finding closest quality stream to choice.")
            stream_qualities = {}
            best_bitrates = {}
            for stream in audio_pafy.audiostreams:
                if stream.extension == fformat:
                    stream_bitrate = int(stream.bitrate.replace("k", ""))
                    stream_qualities[stream_bitrate] = stream.url
            closest_bitrate = min(stream_qualities, key=lambda x: abs(x - bitrate))
            best_bitrates[audio_pafy.title + "." + fformat] = stream_qualities[closest_bitrate]
            self.audioDL_logger.info("Found audio of '{0}' in quality, {1}k. Added to list."
                                     .format(audio_pafy.title, closest_bitrate))
            self.download_from_url(best_bitrates, audio_pafy.title)

    def download_from_url(self, url_dict, pl_title):
        self.audioDL_logger.info("Downloading audio (may take some time).")
        download_folder_name = pl_title+" [{}]".format(datetime.strftime(datetime.today(),
                                                                         format="%d-%m-%y_%H%M%S"))
        os.mkdir("./Downloads/"+download_folder_name)
        for title, dl_url in url_dict.items():
            safe_characters = (' ', '.', '_')
            file_title = "".join(c for c in title if c.isalnum() or c in safe_characters).rstrip()
            print("Now downloading "+file_title+".")
            time.sleep(0.25)
            request.urlretrieve(dl_url, filename="./Downloads/"+download_folder_name+"/"+file_title)
            print("Finished downloading "+file_title+".")
        print("Finished downloading playlist: {} The downloaded files can be found in './Downloads/{}'."
              .format(pl_title, download_folder_name))
