# TTY youtube client

its finally here, the one thing literally NO ONE ASKED FOR!!

A way to run youtube videos in TTY

Dependencies:
* (pip) yt-search
* (system) mplayer
* (system) yt-dlp
* (system) fbdev2
* (system) pulseaudio

arch dependencies install: `# pacman -S pulseaudio xf86-video-fbdev yt-dlp && pip3 install youtube_search`

debian dependencies install: `# apt-get install pulseaudio xserver-xorg-video-fbdev && pip3 install --no-deps -U yt-dlp && pip3 install youtube_search`

if you use another distro I'm sure you can figure it out ;)

to run it either do ./youtube.py or python3 youtube.py
