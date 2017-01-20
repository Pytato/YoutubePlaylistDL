# License stuff

import logging

import pafy

from audio import AudioDL

core_logger = logging.getLogger("PlaylistDL.core")


def var_def():
    core_logger.debug("core.var_def() started.")

    download_url = str(input("\nEnter the URL of download (can be playlist URL): "))
    if "https://www.youtube.com/" not in download_url:
        core_logger.error("Incorrect URL entered, must be either video URL or playlist URL from Youtube.")
        return()

    is_playlist = False
    # Catch playlists, will be improved at some point to catch shortened URLs.
    if "playlist" in download_url:
        logging.info("Playlist URL recognised, verifying integrity.")
        try:
            playlist_to_dl = pafy.get_playlist(download_url)
            print("Playlist: '{}' containing {} videos in found.".format(playlist_to_dl["title"],
                                                                         len(playlist_to_dl["items"])))
            is_playlist = True
        except ValueError:
            core_logger.error("pafy.get_playlist failed. URL entered is not found on Youtube, check for mistakes.")
            print("Failed to find playlist, check the URL")
            return()

    if is_playlist is False:
        try:
            video = pafy.new(download_url)
        except ValueError:
            print("URL incorrect, try again.")
            return()

    download_quality = str(input("Quality of download (arbitrary High/Low): "))
    if download_quality != "High" and download_quality != "Low":
        print("Enter download quality correctly.")
        return()

    download_type = str(input("File-form to download from youtube (audio/video): "))
    if download_type.lower() == "audio":
        pref_audio_type = str(input("Preferred audio file (ogg/m4a/webm): "))
        audiodl = AudioDL()
        core_logger.debug("audioDL initialised.")
        if is_playlist is True:
            core_logger.debug("is_playlist = True")
            audiodl.audio_playlist_gather(set=playlist_to_dl, fformat=pref_audio_type,
                                          quality=download_quality)
        else:
            audiodl.audio_single_gather(video, fformat=pref_audio_type, quality=download_quality)
    # elif download_type.lower() == "video":
    #     dl_video(...)


def download_from_url(url_dict, folder_title):
    print("Soon")
