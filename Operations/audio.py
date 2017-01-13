
import logging
import pafy


external_logger = logging.getLogger('YoutubeDL.core.audio')


class AudioDL:
    def __init__(self):
        self.audioDL_logger = logging.getLogger("YoutubeDL.core.audio.audioDL")
        self.audioDL_logger.debug("core.audio.audioDL initialised.")

    def audio_playlist_dl(self, set, fformat="", quality=""):
        self.audioDL_logger.debug("core.audio.audioDL.audio_playlist_dl() started.")
        self.audioDL_logger.info("Generating array of download streams in your specifications.")
        streams = []
        if quality == "High":
            for video in set["items"]:
                stream_a = video["pafy"].getbestaudio(preftype=fformat)
                streams.append(stream_a)
                self.audioDL_logger.info("Found audio of '{0}' in quality, {1} with extension, {2}. Added to list."
                                         .format(stream_a.title, stream_a.bitrate, stream_a.extension))
            self.audioDL_logger.info("List generation complete, beginning downloads (may take some time).")
        elif quality == "Low":
            stream_qualities_example_s = set["items"]["pafy"].audiostreams
            stream_qualities_example_txt = ""
            stream_qualities_example_a = []
            # Generates both the array to store streams and a string formatted for a user based input
            for item in stream_qualities_example_s:
                if fformat in item:
                    if stream_qualities_example_s.index(item) == (len(stream_qualities_example_s) - 2):
                        stream_qualities_example_txt = stream_qualities_example_txt + item + " and "
                    elif stream_qualities_example_s.index(item) == (len(stream_qualities_example_s) - 1):
                        stream_qualities_example_txt = stream_qualities_example_txt + item + "."
                    else:
                        stream_qualities_example_txt = stream_qualities_example_txt + item + ", "
                    stream_qualities_example_a.append(item)
            bitrate = ""
            while bitrate not in stream_qualities_example_a:
                bitrate = str(int("\n\nBitrate choices: {}\n\nChose a bitrate (you need to enter the entire name): "
                                  .format(stream_qualities_example_txt)))
            self.audioDL_logger.info("Bitrate accepted, will be downloading in "+bitrate)
            for video in set["items"]:
                stream_a = video["pafy"].audiostreams(preftype=fformat)
                streams.append(stream_a)
                self.audioDL_logger.info("Found audio of '{0}' in quality, {1} with extension, {2}. Added to list."
                                         .format(stream_a.title, stream_a.bitrate, stream_a.extension))
            self.audioDL_logger.info("List generation complete, beginning downloads (may take some time).")
        else:
            self.audioDL_logger.error("Neither 'High' or 'Low' quality selected.")


# def dl_audio(set, fformat="", quality="", playlist=False):
# core_logger.debug("core.dl_audio() started.")
# if playlist is True:
#     print("Generating array of download URLs.")
#     streams = []
#     if quality.capitalize() == "High":
#         for video in set["items"]:
#             streams.append(video["pafy"].getbestaudio(preftype=fformat))
#     else:
#         print("Option coming soon")
#         return()
#         # for video in set["items"]:
#         #     streams.append(video["pafy"].get)
#     print("Array generation complete, beginning download (this may take a while).")
# print("All downloads from this instance will be stored under the name of this playlist ({})."
#       .format(set["title"]))
# foldername = "./Downloads/{0} [{1}]".format(set["title"], datetime.strftime(datetime.today(),
#                                                                             format="%d-%m-%y_%H%M%S"))
# os.mkdir(foldername)
# for item in set["items"]:
#     s = item["pafy"].getbestaudio(preftype=fformat)
#     f = s.download(filepath=foldername+"/")
