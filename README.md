# YoutubePlaylistDL v0.0.xa dev branch
*"Python to sit on top of Python to sit on top of other Python, will download playlists from youtube in audio or video with numerous formats."*

Very much a work in progress, recently started migrating it over to use more modular format ie. not having everything in one file.

##Installing and running
1) Download the [latest release](https://github.com/Pytato/YoutubePlaylistDL/releases) of the program.
2) Don't use Python 2.
3) Install [pafy](http://np1.github.io/pafy/) using `pip install pafy`.
4) Install [yt-dl](https://github.com/rg3/youtube-dl/) using `pip install youtube-dl`.
5) Open the zip and run `run.py` to begin.

##Checklist
- [x] Modularise the code into separate areas
    - [ ] WIP - make sure logging works completely.
        - [ ] Find a way to suppress logging errors due to non-conforming characters in video names.
- [x] Give option to download single audio file.
- [ ] Allow video downloads.
- [ ] Add user config options.
- [ ] Fix the damned bug that has been plaguing low quality audio downloads.
    - [x] Fixed to the best of my knowledge.
- [ ] Get video downloads working.
- [ ] Implement GUI interface. 
- [ ] Try integrating the program online (will publish results).

*Will attempt to keep updated as the program gets updated.*