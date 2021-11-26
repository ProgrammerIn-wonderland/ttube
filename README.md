# TTY youtube client

its finally here, the one thing literally NO ONE ASKED FOR!!

A way to run youtube videos in TTY

Dependencies:
* (pip) yt-search
* (system) mplayer
* (system) youtube-dl
* (system) fbdev2

arch dependencies install: `# pacman -S xf86-video-fbdev youtube-dl && pip install yt-search`

debian dependencies install: `# apt-get install xserver-xorg-video-fbdev youtube-dl && pip install yt-search`

if you use another distro I'm sure you can figure it out ;)

to run it either do ./youtube.py or python3 youtube.py